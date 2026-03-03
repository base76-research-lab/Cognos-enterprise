# TrustPlane — Incident Register
**EU AI Act Article 73 | QUALITY_MANAGEMENT.md §9**

This directory contains the incident register for TrustPlane.
Each incident is documented in a separate file named `YYYY-MM-DD-<slug>.md`.

---

## Incident Classification

| Class | Definition | Response SLA |
|-------|-----------|-------------|
| **Critical** | Audit log failure, data breach, systematic incorrect decisions, personal data exposure | 24h containment · 48h tenant notification · 15d IMY report if rights impact |
| **Major** | Single-tenant report failure, provider routing failure, prolonged downtime | 72h resolution |
| **Minor** | Documentation gap, non-material config error, cosmetic bug | Next release cycle |

## Reporting Obligation (Art. 73)

If an incident involves:
- Serious risk to health, safety, or fundamental rights of natural persons, **or**
- Personal data exposure

→ Report to **IMY** (Integritetsskyddsmyndigheten, Sweden) within **15 days** of detection.
IMY contact: https://www.imy.se/en/about-us/contact-us/

## Incident File Template

See `TEMPLATE.md` in this directory.

## Log

| ID | Date | Class | Status | Summary |
|----|------|-------|--------|---------|
| — | — | — | — | No incidents recorded |
