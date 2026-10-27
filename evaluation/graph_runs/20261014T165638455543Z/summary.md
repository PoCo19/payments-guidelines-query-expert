# Graph pilot comparison

AI-assisted development set; graph and expected anchors co-designed. Not held-out, not independent correctness evaluation.

Answer correctness remains unscored. Controls measure routing/filtering, not general negative-answer accuracy. Single-run latency includes cache/model warm-up.

```json
{
  "baseline": {
    "cases": 40,
    "errors": 0,
    "anchors_found": 60,
    "anchors_expected": 78,
    "model_usable_anchors_found": 59,
    "all_anchor_cases": 13,
    "positive_cases": 28,
    "control_passed": 12,
    "control_cases": 12,
    "model_fallbacks": 34,
    "required_gaps_disclosed": 0,
    "required_gap_cases": 2,
    "median_seconds": 2.08,
    "positive_median_seconds": 2.086,
    "response_status_counts": {
      "abstained": 3,
      "clarification_needed": 2,
      "model_unavailable": 34,
      "source_excerpts": 1
    }
  },
  "graph": {
    "cases": 40,
    "errors": 0,
    "anchors_found": 78,
    "anchors_expected": 78,
    "model_usable_anchors_found": 77,
    "all_anchor_cases": 28,
    "positive_cases": 28,
    "control_passed": 12,
    "control_cases": 12,
    "model_fallbacks": 34,
    "required_gaps_disclosed": 2,
    "required_gap_cases": 2,
    "median_seconds": 2.085,
    "positive_median_seconds": 2.091,
    "response_status_counts": {
      "abstained": 3,
      "clarification_needed": 2,
      "model_unavailable": 34,
      "source_excerpts": 1
    }
  }
}
```
