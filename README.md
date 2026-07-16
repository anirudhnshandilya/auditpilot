# 🛡️ AuditPilot

> **Open-source AI-powered compliance platform for ISO/IEC 27001 readiness, evidence management, and security governance.**

AuditPilot helps organisations prepare for security audits by validating risk registers, analysing supporting documentation, identifying compliance gaps, and generating actionable remediation recommendations.

By combining deterministic validation with AI-assisted analysis, AuditPilot transforms audit preparation from a stressful annual exercise into a continuous, self-correcting compliance workflow.

---

# 🚧 Project Status

**Current Version:** `v0.2.0-alpha`

### Phase Progress

- ✅ Phase 1 – Backend Foundation
- ✅ Phase 2 – Validation Engine
- 🚧 Phase 3 – Evidence Manager
- ⏳ Phase 4 – AI Copilot
- ⏳ Phase 5 – Framework Packs

---

# ✨ Current Features

## Backend

- ✅ FastAPI backend
- ✅ Interactive Swagger API
- ✅ RESTful upload endpoint
- ✅ CSV/XLSX parsing

---

## Validation Engine

- ✅ Modular Validation Engine
- ✅ Rule Registry
- ✅ Rule Runner
- ✅ Severity Model
- ✅ Audit Readiness Scoring
- ✅ Validation Result Model

---

## Risk Register Validation

Currently supports validation for:

- ✅ Duplicate Risk IDs
- ✅ Empty Risk IDs
- ✅ Duplicate Rows
- ✅ Empty Rows
- ✅ Missing Required Columns
- ✅ Missing Owner
- ✅ Missing Title
- ✅ Missing Description
- ✅ Missing Treatment Plan
- ✅ Missing Review Date
- ✅ Invalid Review Date
- ✅ Past Due Review Date
- ✅ Invalid Likelihood
- ✅ Invalid Impact

---

## Quality

- ✅ 20 Automated Tests
- ✅ Ruff Linting
- ✅ MyPy Static Type Checking
- ✅ Type-safe Validation Models

---

# 🚀 Coming Soon

## Phase 3

- 🚧 Evidence Manager
- 🚧 PDF Parser
- 🚧 DOCX Parser
- 🚧 Evidence Metadata
- 🚧 Document Classification
- 🚧 Evidence Status Tracking

## Phase 4

- ⏳ ISO 27001 Evidence Mapping
- ⏳ AI Policy Review
- ⏳ CAPA Recommendation Engine
- ⏳ Executive Audit Reports

## Phase 5

- ⏳ React Dashboard
- ⏳ User Authentication
- ⏳ Multi-Framework Support
- ⏳ Continuous Compliance Monitoring

---

# 🏗️ Architecture

```
AuditPilot
│
├── backend
│   ├── app
│   │   ├── routes
│   │   ├── services
│   │   ├── validators
│   │   │   ├── engine.py
│   │   │   ├── registry.py
│   │   │   ├── runner.py
│   │   │   ├── severity.py
│   │   │   └── rules
│   │   └── main.py
│   │
│   ├── tests
│   └── pyproject.toml
│
├── frontend        (Coming Soon)
├── docs
├── examples
└── README.md
```

---

# 🚀 Getting Started

## Clone

```bash
git clone https://github.com/anirudhnshandilya/auditpilot.git

cd auditpilot/backend
```

---

## Install

```bash
uv sync
```

---

## Run

```bash
uv run uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

# 🧪 Testing

Run the complete quality suite:

```bash
uv run pytest

uv run ruff check .

uv run mypy app
```

Current Status

```
✅ 20 Passing Tests

✅ Ruff Clean

✅ MyPy Clean
```

---

# 🛠️ Technology Stack

## Backend

- Python 3.12
- FastAPI
- Pandas
- PyMuPDF
- python-docx

## Testing

- Pytest
- MyPy
- Ruff

## Planned

- React
- PostgreSQL
- OpenAI API
- Docker
- GitHub Actions

---

# 📌 Roadmap

## ✅ Phase 1 — Backend Foundation

- FastAPI Backend
- Health API
- Swagger Documentation
- Project Structure

---

## ✅ Phase 2 — Validation Engine

- Upload API
- Rule Engine
- Rule Registry
- Rule Runner
- Risk Register Validation
- Severity Model
- Audit Readiness Score
- Automated Testing

---

## 🚧 Phase 3 — Evidence Manager

- PDF Upload
- DOCX Upload
- Document Parsing
- Evidence Metadata
- Evidence Classification
- Evidence Status Engine

---

## ⏳ Phase 4 — AI Compliance

- ISO 27001 Mapping
- Policy Analysis
- CAPA Recommendations
- AI Evidence Review

---

## ⏳ Phase 5 — Platform

- Dashboard
- Authentication
- Multi-Framework Support
- Executive Reports
- Continuous Compliance

---

# 👥 Maintainers

| Name | Role | Focus |
|------|------|------|
| **Anirudh Shandilya** | Cybersecurity Engineer | Security, GRC, Backend Architecture |
| **Suryakiran Suresh** | AI & Data Science | Machine Learning, NLP, AI Models |

---

# 🤝 Contributing

Contributions are welcome!

To contribute:

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature/my-feature
```

3. Commit your changes

```bash
git commit -m "feat: add amazing feature"
```

4. Push

```bash
git push origin feature/my-feature
```

5. Open a Pull Request

Please read **CONTRIBUTING.md** before submitting changes.

---

# 📄 License

Licensed under the **Apache License 2.0**.

---

# 🌟 Vision

AuditPilot aims to become an open-source compliance platform supporting multiple governance and security frameworks, including:

- ISO/IEC 27001
- ISO/IEC 27002
- ISO/IEC 42001
- NIST CSF
- CIS Controls
- SOC 2
- CSA CCM
- DORA
- NIS2

Through modular validation engines, AI-assisted evidence analysis, and continuous compliance workflows, AuditPilot seeks to make audit readiness faster, more transparent, and accessible to organisations of all sizes.

---

# ⭐ Support the Project

If you find AuditPilot useful:

- ⭐ Star the repository
- 🍴 Fork the project
- 🛠️ Contribute improvements
- 🐛 Report issues
- 💬 Share feedback

Your support helps grow the project and the open-source security community.
