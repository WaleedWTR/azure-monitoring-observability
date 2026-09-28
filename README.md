# Azure Monitoring & Observability

![Observability validation](https://github.com/WaleedWTR/azure-monitoring-observability/actions/workflows/validate.yml/badge.svg)

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

## Key documentation

- [SLI / SLO design](docs/sli-slo.md)
- [Alert design](docs/alert-design.md)
- [Operational KQL](kql/operational-hunting.kql)
- [Synthetic service metrics](data/synthetic_service_metrics.csv)
- [Technical references](docs/references.md)

## Skills demonstrated

**Azure Monitor · Log Analytics · KQL · Observability · SLI/SLO · Bicep · Alerting · Service Operations**
