# TrustPlane — Licensing Offer
**Base76 Research Lab · Björn Wikström · Sjöbo, Sweden**
**Contact:** björn@base76.se · https://github.com/base76-research-lab/TrustPlane

---

## What This Is

TrustPlane is a production-ready reference implementation of the **CognOS epistemic trust-scoring framework** — a method for making AI decision-making observable, auditable, and compliant with the EU AI Act (Regulation 2024/1689).

It is not sold as a managed service. It is offered as a **licensable method and codebase** — for organisations and consultancies that need to build EU AI Act compliance infrastructure and want a proven foundation rather than starting from scratch.

---

## The Problem It Solves

**EU AI Act obligations apply from August 2026.** High-risk AI system providers must demonstrate:

- A documented risk management system (Art. 9)
- Technical documentation per Annex IV (Art. 11)
- Automatic logging and 6-month retention (Art. 12)
- Transparency to deployers (Art. 13)
- Human oversight with audit trail (Art. 14)
- A quality management system (Art. 17)
- Serious incident reporting process (Art. 73)

Most organisations have none of this. TrustPlane implements all of it.

---

## What the Method Provides

The core of TrustPlane is the **CognOS trust formula**:

```
C = p · (1 − Ue − Ua)
```

Where:
- `p` = base confidence of the model output
- `Ue` = epistemic uncertainty (model operating outside knowledge domain)
- `Ua` = aleatoric uncertainty (irreducible input noise)

This formula, combined with six signal dimensions (epistemic uncertainty, aleatoric uncertainty, model divergence, citation density, contradiction, out-of-distribution detection), produces a **deterministic, auditable trust score** for every AI decision.

The method is grounded in the **FNC (Field-Node-Cockpit) framework** — published research on observable autonomous AI systems by Base76 Research Lab.

---

## What a Licensee Receives

| Component | Description |
|-----------|-------------|
| Full source code | FastAPI gateway, PostgreSQL multi-tenant store, compliance report engine |
| EU AI Act documentation | Technical documentation (Annex IV), QMS (Art. 17), incident register (Art. 73) |
| Compliance report engine | Deterministic risk-area analysis mapped to Articles 9, 12, 13, 14 — no LLM required |
| Human oversight API | Override endpoint with mandatory audit trail per Art. 14 |
| Retention enforcement | Automatic 6-month minimum per Art. 12 |
| Decision mandate layer | Structured epistemic audit trail for organisational decisions |
| UI dashboard | Next.js compliance officer and tenant admin interface |
| Deployment support | Docker-compose, configuration documentation |
| Architecture consultation | 4 hours with Björn Wikström on adaptation to licensee context |

---

## What the Licensor Retains

- Intellectual property and authorship of the CognOS/FNC method
- Right to publish the method as research
- Credit in any derivative product ("Powered by CognOS · Base76 Research Lab")
- Option to list licensee as reference case (with consent)

---

## Licensing Models

### A — Single Organisation License
For an organisation deploying TrustPlane internally for their own AI systems.

- One-time license fee: **negotiable, typically 80–150k SEK**
- Includes: full codebase, documentation, 4h consultation
- Ongoing: optional annual support agreement

### B — Reseller / Consultancy License
For a consultancy or RegTech firm deploying TrustPlane for multiple clients under their own brand.

- License fee + royalty per deployment: **negotiable**
- White-label permitted with credit retained
- Includes: full codebase, documentation, 8h consultation + train-the-trainer

### C — Research / Pilot Partnership
For organisations wanting to co-develop or validate the method in a specific domain (healthcare, finance, public sector).

- Co-funded model: licensee contributes domain expertise and pilot environment
- Suitable for Vinnova / EU Horizon co-applications
- Output: shared research publication + production-ready implementation

---

## Why Now

The EU AI Act's August 2026 deadline is 5 months away. Building compliance infrastructure from scratch takes 6–12 months for most organisations. TrustPlane is deployable in days.

The alternative — waiting for a commercial SaaS vendor — means dependency on a third-party for your compliance audit trail. TrustPlane gives you the infrastructure you own and control.

---

## Next Step

A 30-minute call to understand your context and whether TrustPlane is a fit.

**björn@base76.se**
