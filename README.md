# Cloud Variance Management Agent

Agentic FinOps governance workflow that turns cloud cost variance signals into owner-assigned Jira actions, SLA tracking, escalation, and savings validation.

## Problem

Traditional cloud optimization tools often stop at dashboards or recommendations.

This project explores a workflow-native approach where cloud cost signals become accountable engineering action.

## Workflow

```text
Cloud Cost Signal
        ↓
Variance Detection
        ↓
AI Reasoning
        ↓
Priority Assignment
        ↓
Owner Identification
        ↓
Jira Ticket Draft
        ↓
Workflow Execution
        ↓
SLA + Validation
```

## Agentic Workflow Components

### Detection Layer
- Variance threshold detection
- Cloud spend anomaly identification

### AI Reasoning Layer
- Likely driver inference
- Priority scoring
- Recommended remediation path

### Governance Layer
- Owner assignment
- Jira artifact generation
- Accountability workflow

## Repository Structure

```text
sample-data/
src/
templates/
jira_tickets/
```

## Example Agent Output

Example:

Service: AWSLambda  
Variance: 180%  
Likely Driver: Recursive invocation or sudden traffic increase  
Priority: P1 Critical  
Action: Open Jira and request response within SLA.

## Vision

Optimization is not only about identifying waste.

It is about turning signals into accountable action and measurable outcomes.
