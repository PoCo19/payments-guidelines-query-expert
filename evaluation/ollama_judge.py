"""Native Ollama adapter for RAGAS collections, with explicit context limits."""
import asyncio
import json
import time
import httpx
from ragas.llms.base import InstructorBaseRagasLLM


class OllamaJudge(InstructorBaseRagasLLM):
    def __init__(self, endpoint, model, log_path, timeout=300, context_length=16384, max_tokens=4096):
        self.endpoint = endpoint
        self.model = model
        self.log_path = log_path
        self.context_length = context_length
        self.max_tokens = max_tokens
        self.client = httpx.AsyncClient(timeout=timeout, trust_env=False)
        self.current = {}

    def generate(self, prompt, response_model):
        return asyncio.run(self.agenerate(prompt, response_model))

    async def agenerate(self, prompt, response_model):
        payload = dict(model=self.model, prompt=prompt, stream=False, think=False,
                       format=response_model.model_json_schema(),
                       options=dict(temperature=0, num_ctx=self.context_length, num_predict=self.max_tokens))
        record = dict(**self.current, request=payload)
        start = time.monotonic()
        try:
            response = await self.client.post(self.endpoint + '/api/generate', json=payload)
            response.raise_for_status()
            data = response.json()
            record['response'] = data
            if data.get('done_reason') == 'length':
                raise ValueError('Judge output reached its token limit; score withheld.')
            if data.get('prompt_eval_count', 0) >= self.context_length:
                raise ValueError('Judge prompt reached its context limit; score withheld.')
            parsed = response_model.model_validate_json(data['response'])
            record['status'] = 'ok'
            return parsed
        except BaseException as exc:
            record.update(status='error', error=f'{type(exc).__name__}: {exc}')
            raise
        finally:
            record['seconds'] = round(time.monotonic() - start, 3)
            with self.log_path.open('a', encoding='utf-8') as f:
                f.write(json.dumps(record, ensure_ascii=False) + '\n')

    async def close(self):
        await self.client.aclose()
