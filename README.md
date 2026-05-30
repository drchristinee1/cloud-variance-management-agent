# Cloud Variance Management Agent

Agentic FinOps governance workflow that turns cloud cost variance signals into owner-assigned Jira actions, SLA tracking, escalation, and savings validation.

![Cloud Variance Architecture](./images/Cloud%20Variance%20management%20architecture%20diagram.png)

## Problem

Traditional cloud optimization tools often stop at dashboards or recommendations.

This project demonstrates an agentic, workflow-native approach that transforms cloud cost signals into accountable engineering action..

Rather than stopping at visibility, the workflow connects detection, AI-assisted reasoning, ownership, and Jira-based execution to support accountable remediation and measurable outcomes.

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
