# Feature Launch Orchestrator V1 — validation record

Validated locally on **3 October 2026**. This records developer checks, not a guarantee of zero defects or independent business/domain certification.

## Automated checks

**143 Python tests passed**: the existing 103 tests plus 40 launch tests. The existing JavaScript answer-rendering tests passed, and the new UI passed JavaScript syntax checking.

Launch coverage includes the complete workflow; exact quote/reference validation; role responsibility checks; stale revision rejection; required approvals; task evidence and prerequisite gates; dependency-cycle rollback; source/control/partner change propagation; version archives; questions and explicit claim checks; duplicate jobs; failed/interrupted/superseded generation; prevention of a late result overwriting a review; at-most-once job application; persistent state; exact source-span reconstruction; output/input budget failures; actual HTTP routes; origin/host rejection; static path allowlisting and content security policy.

Run the Python suite with:

```powershell
.\run.cmd test
```

Saved result: [tests.txt](../output/launch-validation/tests.txt).

## Real model checks

The installed **qwen3.5:9b** completed all five workflows against isolated synthetic evidence through Ollama, with a 16,384-token context and 4,096-token output budget.

| Workflow | Result | Observed time |
|---|---|---:|
| Feature fact extraction | Passed structure, reference and quotation checks | 8.39 s |
| Customer Success draft | Passed; missing SLA commitments remained questions | 16.27 s |
| Marketing draft | Passed | 28.09 s |
| BD draft | Passed; partner test evidence and ownership remained questions | 13.86 s |
| Risk draft | Passed; implementation/testing evidence remained questions | 15.05 s |

These are one run's wall-clock observations on this computer, not a performance benchmark. Model loading, other processes, prompt size and changed configuration affect timings.

The first live attempts exposed paraphrased quotations in extraction and team output. Exact-quote validation correctly rejected those outputs. The implementation was changed so the model selects allowed passage IDs and Python copies the original quotation. The full five-workflow run then passed. Two regression tests cover this reconstruction directly.

The actual drafts were inspected. They preserved the fictional-pilot framing and exposed missing information. They also labelled much factual-looking prose as proposals and some content is generic. Passing these checks demonstrates a working generation contract, not that every draft is complete, correctly classified or ready for business use. Independent subject-matter review and a larger held-out evaluation remain future work. The live test's synthetic approval/disposition steps are explicitly labelled automated test steps; team drafts are not presented as human-approved launch decisions.

Report and outputs: [live-report.json](../output/launch-validation/live-report.json), [live-launch-pack.md](../output/launch-validation/live-launch-pack.md).

To repeat the opt-in live check:

```powershell
.\.venv\Scripts\python.exe -B -X utf8 evaluation\live_launch.py
```

Each run uses a separate timestamped database under `output/launch-validation/`. It never changes `data/launches/launches.sqlite3`.

## Browser journey

The built-in browser tool could not start because of the environment's Windows sandbox-helper failure. Validation used installed Playwright with headless Microsoft Edge instead. The test starts an isolated application server on port 8767, performs actual UI actions and shuts that server down afterwards.

Verified: create simulated pilot → approve facts → generate and approve four **template** deliverables → complete tasks in prerequisite order → record launch decision → download and inspect Markdown export → change a control → verify Risk staleness and Risk/BD task reopening → search the real UPI collection → import a passage with provenance. The 390-pixel layout had no horizontal overflow. No browser JavaScript errors occurred.

AI generation was tested through the real Python/Ollama path separately; the full browser journey uses the deterministic template mode so workflow regressions are repeatable. Manual extraction editing, every possible draft combination, independent multi-user access and production deployment are not claimed as comprehensively validated.

Report: [browser-report.json](../output/launch-validation/browser-report.json). Test source: `evaluation/browser_launch.cjs`; it uses the bundled Node Playwright package and installed Edge on this Windows system. It does not install a browser or modify the user's existing browser profile.

![Team deliverable screen](../output/launch-validation/02-risk-deliverable.png)

![Readiness after a control change](../output/launch-validation/04-change-impact.png)

## Boundaries to carry forward

The remaining work for an operational deployment includes authenticated roles, real organisational approvals/integrations, an independently authored domain evaluation, access-controlled internal sources, backup/restore drills and load/security review. Those are outside this local capstone V1. See the [technical guide](LAUNCH_ORCHESTRATOR_V1.md) for the current implementation boundaries and recovery procedures.
