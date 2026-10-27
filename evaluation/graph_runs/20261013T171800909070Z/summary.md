# Graph pilot comparison

AI-assisted development set; graph and expected anchors co-designed. Not held-out, not independent correctness evaluation.

Answer correctness remains unscored. Controls measure routing/filtering, not general negative-answer accuracy. Single-run latency includes cache/model warm-up.

```json
{
  "baseline": {
    "cases": 20,
    "errors": 0,
    "anchors_found": 33,
    "anchors_expected": 39,
    "all_anchor_cases": 7,
    "positive_cases": 12,
    "control_passed": 8,
    "control_cases": 8,
    "model_fallbacks": 0,
    "median_seconds": 1.772,
    "response_status_counts": {
      "abstained": 1,
      "clarification_needed": 1,
      "source_excerpts": 18
    }
  },
  "graph": {
    "cases": 20,
    "errors": 0,
    "anchors_found": 39,
    "anchors_expected": 39,
    "all_anchor_cases": 12,
    "positive_cases": 12,
    "control_passed": 8,
    "control_cases": 8,
    "model_fallbacks": 0,
    "median_seconds": 1.811,
    "response_status_counts": {
      "abstained": 1,
      "clarification_needed": 1,
      "source_excerpts": 18
    }
  }
}
```
