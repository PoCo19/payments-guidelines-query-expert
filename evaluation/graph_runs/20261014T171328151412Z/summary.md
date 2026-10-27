# Graph pilot comparison

AI-assisted development set; graph and expected anchors co-designed. Not held-out, not independent correctness evaluation.

Answer correctness remains unscored. Controls measure routing/filtering, not general negative-answer accuracy. Single-run latency includes cache/model warm-up.

```json
{
  "baseline": {
    "cases": 40,
    "errors": 0,
    "anchors_found": 69,
    "anchors_expected": 78,
    "model_usable_anchors_found": 69,
    "all_anchor_cases": 21,
    "positive_cases": 28,
    "control_passed": 12,
    "control_cases": 12,
    "model_fallbacks": 0,
    "required_gaps_disclosed": 0,
    "required_gap_cases": 2,
    "median_seconds": 1.446,
    "positive_median_seconds": 1.629,
    "response_status_counts": {
      "abstained": 3,
      "clarification_needed": 2,
      "source_excerpts": 35
    }
  },
  "graph": {
    "cases": 40,
    "errors": 0,
    "anchors_found": 78,
    "anchors_expected": 78,
    "model_usable_anchors_found": 78,
    "all_anchor_cases": 28,
    "positive_cases": 28,
    "control_passed": 12,
    "control_cases": 12,
    "model_fallbacks": 0,
    "required_gaps_disclosed": 2,
    "required_gap_cases": 2,
    "median_seconds": 1.422,
    "positive_median_seconds": 1.563,
    "response_status_counts": {
      "abstained": 3,
      "clarification_needed": 2,
      "source_excerpts": 35
    }
  }
}
```
