# Graph pilot comparison

AI-assisted development set; graph and expected anchors co-designed. Not held-out, not independent correctness evaluation.

Answer correctness remains unscored. Controls measure routing/filtering, not general negative-answer accuracy. Single-run latency includes cache/model warm-up.

```json
{
  "baseline": {
    "cases": 2,
    "errors": 0,
    "anchors_found": 5,
    "anchors_expected": 7,
    "model_usable_anchors_found": 5,
    "all_anchor_cases": 1,
    "positive_cases": 2,
    "control_passed": 0,
    "control_cases": 0,
    "model_fallbacks": 0,
    "required_gaps_disclosed": 0,
    "required_gap_cases": 0,
    "median_seconds": 24.06,
    "positive_median_seconds": 24.06,
    "response_status_counts": {
      "draft": 2
    }
  },
  "graph": {
    "cases": 2,
    "errors": 0,
    "anchors_found": 7,
    "anchors_expected": 7,
    "model_usable_anchors_found": 7,
    "all_anchor_cases": 2,
    "positive_cases": 2,
    "control_passed": 0,
    "control_cases": 0,
    "model_fallbacks": 0,
    "required_gaps_disclosed": 0,
    "required_gap_cases": 0,
    "median_seconds": 20.78,
    "positive_median_seconds": 20.78,
    "response_status_counts": {
      "draft": 1,
      "incomplete": 1
    }
  }
}
```
