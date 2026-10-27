# Graph pilot comparison

AI-assisted development set; graph and expected anchors co-designed. Not held-out, not independent correctness evaluation.

Answer correctness remains unscored. Controls measure routing/filtering, not general negative-answer accuracy. Single-run latency includes cache/model warm-up.

```json
{
  "baseline": {
    "cases": 1,
    "errors": 0,
    "anchors_found": 2,
    "anchors_expected": 4,
    "model_usable_anchors_found": 2,
    "all_anchor_cases": 0,
    "positive_cases": 1,
    "control_passed": 0,
    "control_cases": 0,
    "model_fallbacks": 0,
    "required_gaps_disclosed": 0,
    "required_gap_cases": 0,
    "median_seconds": 15.79,
    "positive_median_seconds": 15.79,
    "response_status_counts": {
      "draft": 1
    }
  },
  "graph": {
    "cases": 1,
    "errors": 0,
    "anchors_found": 4,
    "anchors_expected": 4,
    "model_usable_anchors_found": 4,
    "all_anchor_cases": 1,
    "positive_cases": 1,
    "control_passed": 0,
    "control_cases": 0,
    "model_fallbacks": 0,
    "required_gaps_disclosed": 0,
    "required_gap_cases": 0,
    "median_seconds": 16.209,
    "positive_median_seconds": 16.209,
    "response_status_counts": {
      "draft": 1
    }
  }
}
```
