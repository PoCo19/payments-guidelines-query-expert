# Graph pilot comparison

AI-assisted development set; graph and expected anchors co-designed. Not held-out, not independent correctness evaluation.

Answer correctness remains unscored. Controls measure routing/filtering, not general negative-answer accuracy. Single-run latency includes cache/model warm-up.

```json
{
  "baseline": {
    "cases": 8,
    "errors": 0,
    "anchors_found": 20,
    "anchors_expected": 22,
    "all_anchor_cases": 7,
    "positive_cases": 8,
    "control_passed": 0,
    "control_cases": 0,
    "model_fallbacks": 0,
    "required_gaps_disclosed": 0,
    "required_gap_cases": 0,
    "median_seconds": 21.52,
    "positive_median_seconds": 21.52,
    "response_status_counts": {
      "draft": 6,
      "incomplete": 2
    }
  },
  "graph": {
    "cases": 8,
    "errors": 0,
    "anchors_found": 22,
    "anchors_expected": 22,
    "all_anchor_cases": 8,
    "positive_cases": 8,
    "control_passed": 0,
    "control_cases": 0,
    "model_fallbacks": 0,
    "required_gaps_disclosed": 0,
    "required_gap_cases": 0,
    "median_seconds": 19.736,
    "positive_median_seconds": 19.736,
    "response_status_counts": {
      "draft": 6,
      "incomplete": 2
    }
  }
}
```
