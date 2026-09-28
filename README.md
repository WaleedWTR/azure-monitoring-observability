# Azure Monitoring & Observability

A portfolio observability project combining Azure Monitor / Log Analytics concepts, SLI/SLO design, KQL and synthetic service-health analytics.

> **Portfolio note:** Metrics and alerts in this repository use synthetic service data and generic infrastructure.

## What this project demonstrates

- Log Analytics infrastructure
- Azure Monitor action-group design
- KQL operational queries
- SLI/SLO calculation
- error-rate and latency analysis
- alert design
- monitoring-as-code
- operational runbooks

## Architecture

```text
Applications / Azure Resources
          |
          v
   Platform Telemetry
          |
          v
   Log Analytics Workspace
      /            \
     /              \
    KQL           Alerting
     |               |
     v               v
Dashboards       Action Group
     \               /
      \             /
       Operational Response
```

## Run the synthetic SLO analysis

```bash
python scripts/slo_report.py
```

## Skills demonstrated

**Azure Monitor · Log Analytics · KQL · Observability · SLI/SLO · Bicep · Alerting · Service Operations**
