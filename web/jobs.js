"use strict";
const LocalJob = {
  async run(path, payload, progress, started) {
    const created=await api(path,payload);
    if(started) started(created.id);
    for (;;) {
      const job=await api('/api/jobs?id='+encodeURIComponent(created.id));
      progress?.(job.stage,job.elapsed_seconds);
      if(job.status==='completed')return job.result;
      if(job.status==='failed')throw new Error(job.error || 'The operation failed.');
      await new Promise(resolve=>setTimeout(resolve,750));
    }
  }
};
