# Graph pilot comparison

AI-assisted development set; graph and expected anchors co-designed. Not held-out, not independent correctness evaluation.

Answer correctness remains unscored. Controls measure routing/filtering, not general negative-answer accuracy. Single-run latency includes cache/model warm-up.

```json
{
  "baseline": {
    "cases": 6,
    "errors": 0,
    "anchors_found": 15,
    "anchors_expected": 19,
    "all_anchor_cases": 3,
    "positive_cases": 6,
    "control_passed": 0,
    "control_cases": 0,
    "model_fallbacks": 0,
    "median_seconds": 27.837,
    "positive_median_seconds": 27.837,
    "response_status_counts": {
      "draft": 5,
      "incomplete": 1
    }
  },
  "graph": {
    "cases": 6,
    "errors": 0,
    "anchors_found": 19,
    "anchors_expected": 19,
    "all_anchor_cases": 6,
    "positive_cases": 6,
    "control_passed": 0,
    "control_cases": 0,
    "model_fallbacks": 0,
    "median_seconds": 22.404,
    "positive_median_seconds": 22.404,
    "response_status_counts": {
      "draft": 4,
      "incomplete": 2
    }
  }
}
```
