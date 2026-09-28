# SLI / SLO Design

## Service Level Indicators

Example indicators used in this lab:

- **Availability:** proportion of observation intervals where the service is available
- **Error rate:** failed requests divided by total requests
- **Latency:** request latency observed over time

## Example objectives

A production service might define objectives such as:

- monthly availability >= agreed target
- error rate below an agreed threshold
- percentile latency within a user-experience target

The exact numbers should come from service criticality and user needs, not arbitrary industry defaults.

## Error budgets

An SLO creates an error budget: the amount of unreliability the service can tolerate while still meeting the objective.

Error budgets can help balance:

- reliability work
- feature delivery
- change risk
- operational improvement
