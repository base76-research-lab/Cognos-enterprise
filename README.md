# CognOS Enterprise

**Your LLM doesn't know when to stop. Now it does.**

CognOS Enterprise is a trust-scoring gateway that sits between your application and any LLM — measuring epistemic uncertainty on every request, blocking what shouldn't pass, and giving you a full audit trail for every decision it makes.

Built for teams that can't afford to guess.

---

## The problem

You're running AI in production. Somewhere between "it works in the demo" and "it's live for 10,000 users", something will go wrong. A model will hallucinate a medical dosage. A legal assistant will cite a case that doesn't exist. A customer-facing bot will say something it shouldn't.

You won't know until after.

---

## The solution

Every request through CognOS is scored before it reaches your users:

```
C = p × (1 − Ue − Ua)
```

Where `Ue` is epistemic uncertainty (what the model doesn't know) and `Ua` is aleatoric uncertainty (what nobody can know). When the score drops below your threshold, the request is escalated — or blocked entirely.

Four outcomes. No surprises.

| Score | Decision | What happens |
|---|---|---|
| High confidence | `PASS` | Request goes through |
| Borderline | `REFINE` | Warning headers attached |
| Low confidence | `ESCALATE` | Webhook fired, human notified |
| Unacceptable | `BLOCK` | Request rejected, trace saved |

Every decision is logged. Every log is exportable. Every export is EU AI Act compliant.

---

## Features

### Trust scoring on every request
Drop-in replacement for your existing LLM calls. Same API shape, same models — with epistemic headers on every response.

```
X-Cognos-Trust-Score: 0.8731
X-Cognos-Decision: PASS
X-Cognos-Trace-Id: tr_a3f91c2d44b1
X-Cognos-Policy: enterprise_v1
```

### Plug in any LLM
One gateway. Every provider.

```yaml
provider: ollama          # Local, private, free
provider: openai          # GPT-4o, o1, o3
provider: anthropic       # Claude 3.5, Claude 4
provider: groq            # llama3, mixtral at 500+ tok/s
provider: cerebras        # Fastest inference on earth
```

Switch providers without changing your application code. Configure fallback providers for zero-downtime failover.

### Multi-tenant isolation
Every tenant gets their own PostgreSQL schema. No data bleeds between customers. Ever.

```
tenant_acme.traces
tenant_globocorp.traces
tenant_startupxyz.traces
```

### Webhooks on ESCALATE and BLOCK
Your systems know the moment something goes wrong — before your users do.

```json
{
  "trace_id": "tr_a3f91c2d44b1",
  "decision": "ESCALATE",
  "trust_score": 0.31,
  "tenant_id": "acme",
  "timestamp": "2026-03-02T14:22:11Z"
}
```

### EU AI Act compliance, built in
Article 13 transparency reports generated automatically. Export to PDF or CSV on demand.

```bash
curl -H "X-API-Key: your-key" \
  "https://your-gateway/v1/audit/export?format=pdf" \
  -o eu_ai_act_report.pdf
```

### Self-hosted or SaaS
Run it on your own infrastructure with Docker Compose, or use our hosted version. Your data never has to leave your environment.

---

## Quickstart

```bash
# Clone
git clone https://github.com/base76-research-lab/Cognos-enterprise.git
cd Cognos-enterprise

# Configure
cp .env.example .env
# Set COGNOS_PROVIDER, COGNOS_MODEL, your API key

# Start
docker-compose up

# Test
curl -X POST http://localhost:8788/v1/chat/completions \
  -H "X-API-Key: test-key" \
  -H "X-Cognos-Tenant: demo" \
  -H "Content-Type: application/json" \
  -d '{"model":"ollama/llama3.2:1b","messages":[{"role":"user","content":"Hello"}]}'
```

That's it. Your LLM now has a conscience.

---

## Architecture

```
Your App
   │
   ▼
CognOS Enterprise Gateway   ←── trust scoring, RBAC, rate limiting
   │                             tenant isolation, webhooks, audit
   ├── Ollama (local)
   ├── OpenAI
   ├── Anthropic
   ├── Groq
   └── Cerebras
```

The gateway is stateless. PostgreSQL holds the audit trail. Redis handles rate limiting. The dashboard gives you visibility into all of it.

---

## Free vs Enterprise

| Feature | Free | Enterprise |
|---|---|---|
| Trust scoring (PASS/REFINE/ESCALATE/BLOCK) | ✓ | ✓ |
| All LLM providers | ✓ | ✓ |
| Trace history + CSV export | ✓ | ✓ |
| Webhooks | 1 endpoint / 100 events/day | Unlimited |
| Tenants | 1 | Unlimited |
| Rate limit | 100 req/day | Configurable |
| PDF audit reports (EU AI Act) | ✗ | ✓ |
| Fallback providers | ✗ | ✓ |
| Custom RBAC roles | ✗ | ✓ |
| Session memory | ✗ | ✓ |
| Token compression | ✗ | ✓ |
| SLA + support | ✗ | ✓ |

Start free. Upgrade when you need it.

---

## Compliance

CognOS Enterprise is designed for teams operating under **EU AI Act** requirements for high-risk AI systems (Annex III).

- **Article 9** — Continuous risk management via epistemic scoring on every inference
- **Article 12** — Complete record-keeping with trace IDs, timestamps, and decision logs
- **Article 13** — Automated transparency reports (PDF) covering all attestations
- **Article 14** — Human oversight via webhook escalation before consequences occur

Full guide: [docs/EU_AI_ACT.md](docs/EU_AI_ACT.md)

---

## Built on open source

CognOS Enterprise is built on top of **[cognos-proof-engine](https://github.com/base76-research-lab/cognos-proof-engine)** — the open-source trust-scoring core. The proof engine handles the math. The enterprise layer handles everything else.

Related projects:
- [cognos-session-memory](https://github.com/base76-research-lab/cognos-session-memory) — Verified context injection via epistemic trust scoring
- [token-compressor](https://github.com/base76-research-lab/token-compressor) — Context compression for long-running sessions
- [cognos-risk-dashboard](https://github.com/base76-research-lab/cognos-risk-dashboard) — Visual trust monitoring (included in this repo)

---

## Research

The trust-scoring model is grounded in **Field-Node-Cockpit (FNC)** theory — a framework for observable, coherent, and ethically bounded autonomous AI systems, developed at [Base76 Research Lab](https://base76.se).

Published: [Applied AI Philosophy](https://github.com/Applied-Ai-Philosophy)

---

## License

Enterprise edition — contact [bjorn@base76.se](mailto:bjorn@base76.se) for licensing.

OSS core: [cognos-proof-engine](https://github.com/base76-research-lab/cognos-proof-engine) (MIT)

---

*Built by [Base76 Research Lab](https://base76.se), Sjöbo, Sweden.*
