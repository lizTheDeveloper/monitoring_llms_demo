# Monitoring Task-Executing Agents

Agents that perform work (code generation, automation, tool usage) require specialized monitoring.

## What Are Task-Executing Agents?

Unlike conversational agents, these:
- Perform actions (not just provide information)
- Use tools and APIs
- Modify systems (code, files, databases)
- Have real-world consequences

**Examples**: Code generation tools, DevOps agents, ETL pipelines, workflow automation

## Critical Risks

- Security vulnerabilities
- Data breaches  
- System failures
- Compliance violations
- Financial losses

## Key Metrics

### 1. Task Completion Accuracy
**What**: Agent successfully completed intended task  
**Measure**: GoalAccuracyMetric (DeepEval/RAGAs), verify outcomes  
**Red flags**: Non-compiling code, incomplete deployments, partial processing

### 2. Code Quality and Safety ⚠️
**What**: Code is secure and follows best practices  
**Measure**: Static analysis (Bandit, Semgrep), custom security metrics  
**Red flags**: Hardcoded secrets, SQL injection, missing validation, insecure endpoints

### 3. Tool Usage Correctness
**What**: Correct use of tools and APIs  
**Measure**: ToolCallAccuracy (RAGAs), verify patterns, monitor logs  
**Red flags**: Wrong parameters, destructive operations, exceeding limits

### 4. Security and Compliance ⚠️
**What**: Actions comply with security policies  
**Measure**: Policy checks, access control verification, audit logging  
**Monitor**: Unauthorized access, data exposure, non-compliant configs

### 5. Resource Usage
**What**: Efficient resource use within budget  
**Measure**: Track costs, efficiency per task, quota usage

### 6. Error Handling
**What**: Graceful error handling and recovery  
**Measure**: Error rates, recovery success, state consistency

## Monitoring Strategy

### Three-Layer Approach
1. **Pre-Execution**: Task validation, permission checks, resource limits, policy compliance
2. **Real-Time**: Progress tracking, resource monitoring, error detection, anomaly detection
3. **Post-Execution**: Result verification, security scanning, compliance audit, cost analysis

## Code Generation Monitoring

**Key Metrics**:
- **Correctness**: Compilation rate, test pass rate, runtime errors
- **Security** ⚠️: Vulnerability detection, secret exposure, dependency issues
- **Quality**: Complexity, test coverage, documentation

**Example**:
```python
from deepeval.metrics import GEval

security_metric = GEval(
    name="Code Security",
    criteria="Check for SQL injection, XSS, hardcoded secrets. Return 0 if vulnerable.",
    threshold=0.95
)
```

## Best Practices

1. **Start with high-risk tasks** - Monitor critical operations first
2. **Multiple validation layers** - Pre, during, and post-execution
3. **Approval workflows** - Human approval for high-risk actions
4. **Audit logs** - Complete records of all actions
5. **Regular security audits** - Periodic reviews
6. **Test in isolation** - Safe environments before production
7. **Resource limits** - Prevent runaway usage
8. **Cost monitoring** - Track and control spending

## Related Resources

- See [ENTERPRISE_MONITORING.md](ENTERPRISE_MONITORING.md) for organizational monitoring strategies
- See [ALIGNMENT_METRICS.md](ALIGNMENT_METRICS.md) for general alignment metrics
- See [BEST_PRACTICES.md](BEST_PRACTICES.md) for implementation guidance

