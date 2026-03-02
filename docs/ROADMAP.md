# TrustPlane — Roadmap

## In progress

- [ ] Blog post (Swedish) — publish on base76.se
- [ ] Landing page — base76.se/trustplane

---

## Planned

### DigitalOcean Marketplace listing
**Priority:** High
**Effort:** 1–2 days

List TrustPlane as a 1-Click App on DigitalOcean Marketplace.

**Steps:**
1. Wrap `docker-compose.yml` in a cloud-init script (auto-start on boot)
2. Build Ubuntu 24.04 LTS base image with Packer
3. Run DO cleanup + validation scripts (`cleanup.sh`, `img_check.sh`)
4. Submit via Vendor Portal
5. Optional: provision managed PostgreSQL automatically via DO DBaaS

**References:**
- https://github.com/digitalocean/marketplace-partners
- https://marketplace.digitalocean.com/vendors/guidelines-resources

---

### Hosting partner integrations

| Provider | Type | Status | Notes |
|---|---|---|---|
| Hetzner | Self-hosted deployment guide | Planned | Marketplace closed — publish guide instead |
| UpCloud | Self-hosted deployment guide | Planned | Finnish, good EU profile |
| Berget.ai | Provider adapter (`berget.py`) | Planned | Swedish inference, GLM + Llama, OpenAI-compatible API |
| Infomaniak | Self-hosted deployment guide | Backlog | Swiss data residency |
| OVHcloud | Self-hosted deployment guide | Backlog | HDS certified (healthcare) |

---

### Provider adapters

| Provider | Status | Notes |
|---|---|---|
| Berget.ai | Planned | OpenAI-compatible, add when API opens |
| Z.ai (GLM) | Planned | Applied to startup program 2026-03-03 |

---

### Core engine

- [ ] Dynamic Ue/Ua extraction from token log-probabilities
- [ ] Domain-specific prior calibration API
- [ ] Merkle-tree audit trail attestation (cryptographic append-only)

---

## Completed

- [x] TrustPlane gateway (FastAPI, trust scoring, policy enforcement)
- [x] Multi-tenant PostgreSQL isolation
- [x] Pluggable provider system (Ollama, OpenAI, Anthropic, Groq, Cerebras)
- [x] RBAC (admin / operator / auditor / viewer)
- [x] Webhooks with retry logic
- [x] Audit export (CSV + EU AI Act Article 13 PDF)
- [x] Rate limiting (Redis token bucket)
- [x] MCP server for Claude Code
- [x] Docker Compose self-hosted bundle
- [x] README, Whitepaper, Architecture docs
- [x] Three scenario guides (healthcare, legal, public sector)
- [x] EU AI Act compliance guide
- [x] Hero image in README
- [x] GitHub repo live: base76-research-lab/TrustPlane
