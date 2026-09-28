# Alert Design

## Alert on symptoms where possible

Useful alerts should help answer:

- is the user experience degraded?
- is a critical dependency failing?
- is action required now?

## Avoid alert noise

Every alert should have:

- owner
- severity
- threshold rationale
- runbook
- expected response
- suppression/deduplication strategy
- review date

## Example alert hierarchy

**Critical**
- sustained service unavailability
- severe error-rate increase
- complete loss of critical dependency

**Warning**
- deteriorating latency
- growing errors
- telemetry gaps
- capacity approaching an operational threshold

## Operational principle

An alert that repeatedly fires without action is a monitoring defect.
