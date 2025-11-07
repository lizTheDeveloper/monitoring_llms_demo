# Critical Thinking Framework for AI Alignment

Question your assumptions, identify blind spots, and make better decisions about monitoring.

## 1. Question Your Metrics

**Key Questions**:
- What assumptions are built in?
- What edge cases might be missed?
- Are you measuring what you think?
- What biases exist in criteria?

**Common Issues**:
- **LLM judge bias**: The evaluator itself may be biased
- **Arbitrary thresholds**: Why 0.7? What's special about that number?
- **Incomplete coverage**: Checking profanity but missing subtle harm

## 2. Consider Context

**Key Questions**:
- How does user/cultural context affect appropriateness?
- What's the cost of false positives vs false negatives?
- Should thresholds vary by domain/use case?

**Common Issues**:
- **Cultural differences**: Language acceptable in one culture, offensive in another
- **Domain variance**: Medical needs 0.95 faithfulness, creative writing 0.7
- **User intent**: Adversarial testing vs genuine queries

## 3. Look for Patterns

**Key Questions**:
- Random or systematic failures?
- Different outcomes by user group?
- Temporal degradation?
- Correlated failure modes?

**Common Issues**:
- **Systematic bias**: Certain demographics consistently score lower
- **Temporal degradation**: Slow increase in toxicity over time
- **Correlated failures**: Faithfulness failures predict relevance failures

## 4. Validate Your Validation

**Key Questions**:
- How do you know metrics are correct?
- Are automated metrics validated by humans?
- When do metrics need updating?

**Common Issues**:
- **Judge-human disagreement**: LLM judge vs human reviewers
- **Metric drift**: Calibrated on old data, applied to new scenarios
- **Missing failures**: Users report issues metrics don't catch

## 5. Think About Trade-offs

**Key Questions**:
- What are trade-offs between metrics?
- Cost of too strict vs too lenient?
- How to balance competing objectives?

**Common Trade-offs**:
- **Faithfulness vs helpfulness**: Too strict → overly conservative
- **Toxicity filtering**: Over-filtering → unhelpful responses
- **Fairness vs personalization**: Equal treatment vs customization

## Applying the Framework

### Review Schedule
- **Weekly**: Review metrics, look for patterns
- **Monthly**: Question assumptions, validate metrics  
- **Quarterly**: Deep dive on trade-offs and context

### Documentation (Per Metric)
- Assumptions built in
- Context where applicable
- Observed patterns
- Validation method
- Trade-offs with other metrics

### Red Flags
- Metrics never fail (too lenient)
- Metrics always fail (too strict)
- Systematic differences by user group
- Gradual degradation over time
- User reports metrics miss

---

## Related Resources

- See [ALIGNMENT_METRICS.md](ALIGNMENT_METRICS.md) for specific metrics
- See [PRODUCTION_MONITORING.md](PRODUCTION_MONITORING.md) for monitoring strategies
- See [BEST_PRACTICES.md](BEST_PRACTICES.md) for implementation guidance

