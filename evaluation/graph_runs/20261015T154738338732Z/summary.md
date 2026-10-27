# Graph pilot comparison

AI-assisted development set; graph and expected anchors co-designed. Not held-out, not independent correctness evaluation.

Answer correctness remains unscored. Controls measure routing/filtering, not general negative-answer accuracy. Single-run latency includes cache/model warm-up.

```json
{
  "baseline": {
    "cases": 3,
    "errors": 0,
    "anchors_found": 9,
    "anchors_expected": 11,
    "model_usable_anchors_found": 9,
    "all_anchor_cases": 2,
    "positive_cases": 3,
    "control_passed": 0,
    "control_cases": 0,
    "model_fallbacks": 0,
    "required_gaps_disclosed": 0,
    "required_gap_cases": 0,
    "median_seconds": 19.721,
    "positive_median_seconds": 19.721,
    "response_status_counts": {
      "draft": 3
    }
  },
  "graph": {
    "cases": 3,
    "errors": 0,
    "anchors_found": 11,
    "anchors_expected": 11,
    "model_usable_anchors_found": 11,
    "all_anchor_cases": 3,
    "positive_cases": 3,
    "control_passed": 0,
    "control_cases": 0,
    "model_fallbacks": 0,
    "required_gaps_disclosed": 0,
    "required_gap_cases": 0,
    "median_seconds": 16.694,
    "positive_median_seconds": 16.694,
    "response_status_counts": {
      "draft": 3
    }
  }
}
```
