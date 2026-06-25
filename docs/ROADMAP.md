# ROADMAP.md

## Project: **idea‑flow**  
**Offline‑First Idea & Board Management App**

> **Goal** – Deliver a lightweight, offline‑first experience that lets teams capture, organize, and sync ideas across devices, while proving a clear, paid‑able need before expanding the feature set.

---

## 1. MVP – Must‑Have for Launch  
*(Must‑have items are marked with **⚡**)*

| # | Feature | Acceptance Criteria | MVP‑Critical |
|---|---------|---------------------|--------------|
| 1 | **Board CRUD** | Users can create, rename, delete boards locally. | ⚡ |
| 2 | **Idea CRUD** | Users can add, edit, delete ideas within a board. | ⚡ |
| 3 | **Offline Persistence** | All data stored in local SQLite (or equivalent) and survives app restarts. | ⚡ |
| 4 | **Sync Engine** | Detect network changes, push local changes to the server, pull remote changes, resolve conflicts (last‑write‑wins). | ⚡ |
| 5 | **Sync Status UI** | Visual indicator (e.g., banner) showing “Offline”, “Syncing…”, “Synced”. | ⚡ |
| 6 | **Unit & Integration Tests** | ≥80 % coverage for core logic, CI pipeline. | ⚡ |
| 7 | **Basic API Server** | REST endpoint `/boards`, `/ideas` with authentication stub. | ⚡ |
| 8 | **Documentation** | README, API spec, developer setup guide. | ⚡ |

> **Launch Target:** Q3 2026 (after internal validation and a closed beta with 30+ users).

---

## 2. v1 – Core Expansion (Q4 2026 – Q2 2027)

### Themes & Milestones

| Theme | Milestone | Key Features | Validation |
|-------|-----------|--------------|------------|
| **Collaboration** | v1.0 | • User accounts (JWT) <br>• Real‑time sync via WebSocket <br>• Board sharing with permissions | • A/B test on shared board adoption <br>• 5 % increase in daily active users |
| **Productivity** | v1.1 | • Tagging & categorization <br>• Search across boards <br>• Idea voting | • 10 % lift in idea completion rate |
| **UX Enhancements** | v1.2 | • Drag‑and‑drop reordering <br>• Offline‑first optimistic UI <br>• Dark mode | • 15 % reduction in support tickets |
| **Metrics & Analytics** | v1.3 | • Usage dashboards <br>• Export CSV/JSON | • 3 % increase in paid plan conversions |

> **Release Cadence:** 3‑month sprints, with quarterly reviews against validated KPIs.

---

## 3. v2 – AI & Enterprise (Q3 2027 – Q1 2028)

### Themes & Milestones

| Theme | Milestone | Key Features | Validation |
|-------|-----------|--------------|------------|
| **AI‑Powered Ideation** | v2.0 | • GPT‑style idea generation (via vLLM) <br>• Contextual prompts per board <br>• Idea summarization | • 20 % increase in idea volume <br>• Positive NPS on AI features |
| **Enterprise Integration** | v2.1 | • SSO (OAuth2) <br>• LDAP sync <br>• Audit logs | • 5 % enterprise sign‑ups |
| **Mobile & PWA** | v2.2 | • React‑Native / PWA build <br>• Push notifications for sync status | • 30 % mobile usage |
| **Performance & Scaling** | v2.3 | • IndexedDB + worker sync <br>• Serverless backend (AWS Lambda) <br>• Load‑testing | • 99.9 % uptime, <1 s sync latency |

> **Roadmap Note:** v2 will leverage the shared BRAIN (pgvector) for storing embeddings of ideas, enabling semantic search and recommendation.

---

## 4. Cross‑Cutting Initiatives

| Initiative | Description | Timeline |
|------------|-------------|----------|
| **CI/CD & Test Automation** | GitHub Actions + Poetry, automated linting, unit & integration tests | Continuous |
| **Security Hardening** | OWASP Top‑10 review, JWT best practices, data encryption at rest | Q4 2026 |
| **Documentation & SDK** | Public API docs (OpenAPI), Python SDK for external tools | Q1 2027 |
| **Community & Open‑Source** | Publish under MIT, encourage PRs, issue triage | Q2 2027 |

---

## 5. Success Metrics

| Metric | Target | Frequency |
|--------|--------|-----------|
| Daily Active Users (DAU) | 5 k | Monthly |
| Sync Success Rate | ≥99.5 % | Weekly |
| NPS | ≥70 | Quarterly |
| Revenue (Paid Plans) | $10 k/month | Monthly |

---

## 6. Risks & Mitigations
