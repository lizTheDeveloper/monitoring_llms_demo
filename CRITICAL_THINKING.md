# Critical Thinking Framework for AI Alignment

When monitoring user-facing agents, applying critical thinking to your evaluation is essential. This framework helps you question assumptions, identify blind spots, and make better decisions about what and how to measure.

## 1. Question Your Metrics

### Key Questions
- What assumptions are built into your metrics?
- What edge cases might your metrics miss?
- Are you measuring what you think you're measuring?
- What biases might be encoded in your evaluation criteria?

### Example Scenarios

**Scenario 1: LLM-as-a-Judge Bias**
You're using GPT-4 to evaluate responses for bias. But GPT-4 itself may have biases. How do you know your judge is fair?

**Critical Questions**:
- What biases might the judge LLM have?
- How do you validate the judge's evaluations?
- Should you use multiple judges and compare?

**Scenario 2: Threshold Selection**
You set a faithfulness threshold of 0.7. Why 0.7? What happens at 0.69 vs 0.71?

**Critical Questions**:
- What's the cost of false positives vs false negatives?
- How was this threshold determined?
- Does it hold across different domains or user groups?

**Scenario 3: Metric Completeness**
You're measuring toxicity, but only checking for profanity. What about subtle forms of harm?

**Critical Questions**:
- What types of harm might you be missing?
- Are there cultural or contextual considerations?
- How do you discover new failure modes?

---

## 2. Consider Context

### Key Questions
- How does the user's context affect what's appropriate?
- Are there cultural or domain-specific considerations?
- What's the cost of false positives vs. false negatives?
- How does the use case affect acceptable thresholds?

### Example Scenarios

**Scenario 1: Cultural Context**
A toxicity detector flags a response as toxic because it uses language that's offensive in one culture but normal in another.

**Critical Questions**:
- How do you handle cultural differences?
- Should the same standards apply globally?
- How do you avoid cultural bias in your metrics?

**Scenario 2: Domain-Specific Requirements**
A medical chatbot needs very high faithfulness (0.95+) but a creative writing assistant might tolerate more flexibility (0.7).

**Critical Questions**:
- What are the consequences of errors in this domain?
- How do requirements differ across use cases?
- Should you have different thresholds for different domains?

**Scenario 3: User Intent**
A user asks a provocative question to test the system. The agent gives a safe but unhelpful response.

**Critical Questions**:
- How do you distinguish between adversarial testing and genuine queries?
- What's the right balance between safety and helpfulness?
- How do you handle edge cases without breaking normal use?

---

## 3. Look for Patterns

### Key Questions
- Are failures random or systematic?
- Do certain user groups experience different outcomes?
- Are there temporal patterns (degradation over time)?
- What correlations exist between different failure modes?

### Example Scenarios

**Scenario 1: Systematic Bias**
You notice that responses to users with certain demographic characteristics consistently score lower on fairness metrics.

**Critical Questions**:
- Is this a measurement artifact or real bias?
- What's causing the systematic difference?
- How do you fix it without introducing new problems?

**Scenario 2: Temporal Degradation**
Toxicity rates are slowly increasing over time, but individual responses still pass thresholds.

**Critical Questions**:
- What's causing the gradual change?
- Is this data drift, model degradation, or changing user behavior?
- When should you intervene?

**Scenario 3: Correlated Failures**
When faithfulness fails, relevance also tends to fail. But not vice versa.

**Critical Questions**:
- What's the underlying cause of the correlation?
- Should you treat these as separate issues or one root cause?
- How do you prevent cascading failures?

---

## 4. Validate Your Validation

### Key Questions
- How do you know your evaluation metrics are correct?
- Are you using LLM-as-a-judge? What biases might that introduce?
- Do you have human validation to check automated metrics?
- How do you know when your metrics need updating?

### Example Scenarios

**Scenario 1: Judge Agreement**
Your LLM judge says a response is biased, but human reviewers disagree.

**Critical Questions**:
- Which is correct?
- How do you resolve disagreements?
- Should you trust the judge or the humans?

**Scenario 2: Metric Drift**
Your metrics were calibrated on one dataset, but you're now evaluating different types of interactions.

**Critical Questions**:
- Are your metrics still valid?
- How do you know when to recalibrate?
- What's your process for updating metrics?

**Scenario 3: Missing Failure Modes**
Users report issues that your metrics don't catch.

**Critical Questions**:
- What are your metrics missing?
- How do you discover new failure modes?
- How do you incorporate user feedback into your metrics?

---

## 5. Think About Trade-offs

### Key Questions
- What are the trade-offs between different metrics?
- How do you balance competing objectives?
- What's the cost of being too strict vs. too lenient?
- How do you optimize for multiple goals simultaneously?

### Example Scenarios

**Scenario 1: Faithfulness vs. Helpfulness**
Stricter faithfulness checks might reduce helpfulness if the agent becomes too conservative.

**Critical Questions**:
- What's the right balance?
- How do you measure the trade-off?
- Can you optimize for both simultaneously?

**Scenario 2: Toxicity Filtering**
Over-filtering for toxicity might make responses too conservative and unhelpful.

**Critical Questions**:
- How do you avoid over-filtering?
- What's the cost of false positives?
- How do you handle edge cases?

**Scenario 3: Fairness vs. Personalization**
Perfect fairness might conflict with personalization that improves user experience.

**Critical Questions**:
- Can you be fair and personalized?
- What's the difference between personalization and bias?
- How do you ensure equity while allowing customization?

---

## Applying the Framework

### Regular Review Process

1. **Weekly**: Review metrics and look for patterns
2. **Monthly**: Question assumptions and validate metrics
3. **Quarterly**: Deep dive into trade-offs and context considerations

### Documentation Template

For each metric, document:
- **Assumptions**: What assumptions are built into this metric?
- **Context**: What contexts does this apply to?
- **Patterns**: What patterns have you observed?
- **Validation**: How do you validate this metric?
- **Trade-offs**: What are the trade-offs with other metrics?

### Red Flags

Watch for:
- Metrics that never fail (might be too lenient)
- Metrics that always fail (might be too strict)
- Systematic differences across user groups
- Gradual degradation over time
- User reports that metrics don't catch

---

## Related Resources

- See [ALIGNMENT_METRICS.md](ALIGNMENT_METRICS.md) for specific metrics
- See [PRODUCTION_MONITORING.md](PRODUCTION_MONITORING.md) for monitoring strategies
- See [BEST_PRACTICES.md](BEST_PRACTICES.md) for implementation guidance

