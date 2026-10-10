"""Request-local timing, model budgets and progress. No shared mutable engine state."""
import contextvars
import functools
import time

CURRENT = contextvars.ContextVar('answer_run', default=None)
PROGRESS = contextvars.ContextVar('answer_progress', default=None)
LABELS = {'retrieval':'Finding and ranking evidence', 'generation':'Drafting the answer',
          'claim_support':'Checking claim support', 'coverage':'Reviewing scope and omissions',
          'embedding':'Encoding the question', 'model_metadata':'Checking the embedding model'}


class Run:
    def __init__(self, config):
        self.started=time.monotonic(); self.config=config; self.calls=[]; self.stages=[]
        self.limit=float(config.get('answer_timeout_seconds',120)); self.stage='retrieval'
        self.stage_started=self.started; self.claim_started=None
        self.progress=PROGRESS.get()

    def remaining(self):
        return self.limit-(time.monotonic()-self.started)

    def set_stage(self, name):
        now=time.monotonic()
        if name!=self.stage:
            self.stages.append(dict(stage=self.stage,seconds=round(now-self.stage_started,3)))
            self.stage=name;self.stage_started=now
        if self.progress:self.progress(LABELS.get(name,name))

    def timeout(self, stage):
        limits={'embedding':20,'model_metadata':10,'generation':60,'claim_support':12,'coverage':15}
        remaining=self.remaining()
        if stage=='claim_support':
            if self.claim_started is None:self.claim_started=time.monotonic()
            remaining=min(remaining,float(self.config.get('claim_review_budget_seconds',35))-(time.monotonic()-self.claim_started))
        value=min(remaining,float(self.config.get(stage+'_timeout_seconds',limits[stage])))
        if value<=0:raise TimeoutError('Answer review time budget exhausted')
        return value

    def report(self):
        return dict(total_seconds=round(time.monotonic()-self.started,3),budget_seconds=self.limit,
                    stages=self.stages+[dict(stage=self.stage,seconds=round(time.monotonic()-self.stage_started,3))],
                    model_calls=self.calls)


def stage(name):
    run=CURRENT.get()
    if run:run.set_stage(name)


def call_stage(endpoint,payload):
    if endpoint=='/api/embed':return 'embedding'
    properties=payload.get('format',{}).get('properties',{})
    if 'findings' in properties:return 'coverage'
    if 'status' in properties:return 'claim_support'
    return 'generation'


def tracked_answer(fn):
    @functools.wraps(fn)
    def wrapped(self,payload):
        run=Run(self.config); token=CURRENT.set(run);run.set_stage('retrieval')
        try:
            try:
                result=fn(self,payload)
            except (OSError,TimeoutError) as exc:
                # Recover source access without another neural/model request.
                run.set_stage('retrieval')
                result=fn(self,dict(payload,mode='evidence',method='bm25',rerank=False))
                result.update(mode=payload.get('mode','evidence'),abstained=True,
                              answer='The local model was unavailable or exceeded its time budget. Keyword source excerpts are shown; no AI answer is asserted.',
                              model_failure=type(exc).__name__)
                result['warnings'].append('Model processing stopped. Retry a narrower question or inspect the source excerpts.')
            result['timing']=run.report();result['elapsed_ms']=round(result['timing']['total_seconds']*1000)
            return result
        finally:CURRENT.reset(token)
    return wrapped
