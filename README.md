# 🛡️ AuditPiloPull Shark achievement test 1.

> **Open-source AI-powered compliance platform for ISO/IEC 27001 readiness, evidence management, and security governance.**

AuditPilot helps organisations prepare for security audits by validating risk registers, analysing supporting documentation, identifying compliance gaps, and generating actionable remediation recommendations.

By combining deterministic validation with AI-assisted analysis, AuditPilot transforms audit preparation from a stressful annual exercise into a continuous, evidence-driven compliance workflow.

---

## 🚧 Project Status

**Current Version:** `v0.3.0-alpha`

### Phase Progress

- ✅ Phase 1 – Backend Foundation
- ✅ Phase 2 – Validation Engine
- ✅ Phase 3 – Evidence Intelligence Pipeline
- ✅ Phase 4 – Compliance Framework Engine
- ⏳ Phase 5 – CAPA and Ticket Generation
- ⏳ Phase 6 – AI Compliance Copilot
- ⏳ Phase 7 – Dashboard and Reporting

---

## ✨ Current Features

### Backend

- ✅ FastAPI backend
- ✅ Interactive Swagger API documentation
- ✅ RESTful API architecture
- ✅ CSV and XLSX processing
- ✅ PDF, DOCX and TXT parsing
- ✅ Modular service structure

### Risk Register Validation

AuditPilot currently detects:

- ✅ Duplicate Risk IDs
- ✅ Empty Risk IDs
- ✅ Duplicate rows
- ✅ Empty rows
- ✅ Missing required columns
- ✅ Missing owners
- ✅ Missing titles
- ✅ Missing descriptions
- ✅ Missing treatment plans
- ✅ Missing review dates
- ✅ Invalid review dates
- ✅ Past-due review dates
- ✅ Invalid likelihood values
- ✅ Invalid impact values

### Validation Engine

- ✅ Modular validation engine
- ✅ Validation rule interface
- ✅ Rule registry
- ✅ Rule runner
- ✅ Severity model
- ✅ Validation result model
- ✅ Audit-readiness scoring
- ✅ Type-safe findings

### Evidence Manager

- ✅ Multi-format evidence upload
- ✅ PDF text extraction
- ✅ DOCX text extraction
- ✅ TXT parsing
- ✅ CSV parsing
- ✅ XLSX parsing
- ✅ SHA-256 checksum generation
- ✅ UUID-based evidence identifiers
- ✅ Evidence repository
- ✅ List evidence
- ✅ Retrieve evidence by ID
- ✅ Delete evidence

### Document Classification

AuditPilot can automatically classify uploaded documents as:

- ✅ Policy
- ✅ Procedure
- ✅ Risk Register
- ✅ Asset Register
- ✅ Incident Register
- ✅ Audit Report
- ✅ Training Record
- ✅ Unknown

### Metadata Extraction

AuditPilot extracts:

- ✅ File size
- ✅ MIME type
- ✅ Upload timestamp
- ✅ SHA-256 checksum
- ✅ Page count
- ✅ Word count
- ✅ Character count
- ✅ Author metadata
- ✅ Document creation date
- ✅ Document modification date

### Evidence Status Engine

AuditPilot currently detects:

- ✅ Draft documents
- ✅ Missing approval information
- ✅ Missing version information
- ✅ Invalid documents
- ✅ Documents requiring human review
- ✅ Sufficient evidence

### Evidence Insights

- ✅ Evidence summary endpoint
- ✅ Total evidence count
- ✅ Sufficient evidence count
- ✅ Human-review-required count
- ✅ Invalid evidence count
- ✅ Document-type breakdown
- ✅ Common evidence issues

---

## 🧪 Quality

- ✅ 49 automated tests
- ✅ Pytest test suite
- ✅ Ruff linting
- ✅ MyPy static type checking
- ✅ Type-safe models and services
- ✅ Feature-branch development
- ✅ Pull-request workflow
- ✅ Conventional commit messages

Current quality status:

```text
49 tests passing
MyPy clean
Ruff clean
```

---

## 🏗️ Architecture

```text
AuditPilot
│
├── backend
│   ├── app
│   │   ├── api
│   │   ├── core
│   │   ├── routes
│   │   │   ├── upload.py
│   │   │   └── evidence.py
│   │   │
│   │   ├── services
│   │   │   ├── document_parser.py
│   │   │   ├── document_classifier.py
│   │   │   ├── metadata_extractor.py
│   │   │   ├── evidence_models.py
│   │   │   ├── evidence_repository.py
│   │   │   ├── evidence_service.py
│   │   │   ├── evidence_status_engine.py
│   │   │   └── evidence_summary.py
│   │   │
│   │   ├── validators
│   │   │   ├── engine.py
│   │   │   ├── registry.py
│   │   │   ├── runner.py
│   │   │   ├── severity.py
│   │   │   ├── models.py
│   │   │   └── rules
│   │   │
│   │   └── main.py
│   │
│   ├── tests
│   ├── pyproject.toml
│   └── uv.lock
│
├── frontend
├── docs
├── examples
└── README.md
```

---

## 🔄 Core Workflow

```text
Upload Evidence
      ↓
File Validation
      ↓
Document Parsing
      ↓
Automatic Classification
      ↓
Metadata Extraction
      ↓
Evidence Status Evaluation
      ↓
Evidence Repository
      ↓
Evidence Summary
      ↓
Framework Mapping
      ↓
Gap Analysis
      ↓
CAPA and Ticket Generation
```

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/anirudhnshandilya/auditpilot.git
cd auditpilot/backend
```

### Install dependencies

```bash
uv sync
```

### Run the API

```bash
uv run uvicorn app.main:app --reload
```

Open the Swagger interface:

```text
http://127.0.0.1:8000/docs
```

---

## 📡 Current API Endpoints

### Health

```text
GET /
GET /health
```

### Risk Register

```text
POST /upload/risk-register
```

### Evidence Manager

```text
POST   /evidence/upload
GET    /evidence
GET    /evidence/summary
GET    /evidence/{document_id}
DELETE /evidence/{document_id}
```

---

## 🧪 Testing

Run the full test suite:

```bash
uv run pytest
```

Run type checking:

```bash
uv run mypy app
```

Run linting:

```bash
uv run ruff check .
```

Run the complete quality gate:

```bash
uv run pytest
uv run mypy app
uv run ruff check .
```

---

## 🛠️ Technology Stack

### Backend

- Python 3.12
- FastAPI
- Pandas
- PyMuPDF
- python-docx
- OpenPyXL
- Pydantic
- Uvicorn

### Testing and Quality

- Pytest
- MyPy
- Ruff
- pandas-stubs

### Planned

- PostgreSQL
- SQLAlchemy
- Alembic
- Redis
- React
- TypeScript
- Docker
- GitHub Actions
- OpenAI-compatible LLM providers
- Local LLM support
- Vector search
- RAG

---

## 📌 Roadmap

### ✅ Phase 1 — Backend Foundation

- FastAPI backend
- Health endpoints
- Swagger documentation
- Project structure
- Dependency management
- Initial automated testing

### ✅ Phase 2 — Validation Engine

- Risk Register upload
- CSV/XLSX processing
- Validation rule interface
- Rule registry
- Rule runner
- Severity model
- Risk Register validation rules
- Audit-readiness scoring
- Automated validation tests

### ✅ Phase 3 — Evidence Intelligence Pipeline

#### Part A — Evidence Upload Foundation

- PDF upload
- DOCX upload
- TXT upload
- CSV upload
- XLSX upload
- Document parser
- Evidence service

#### Part B — Evidence Repository

- UUID-based identifiers
- Store evidence
- List evidence
- Retrieve evidence
- Delete evidence

#### Part C — Document Classification

- Automatic document classification
- Policy detection
- Procedure detection
- Risk Register detection
- Asset Register detection
- Incident Register detection
- Audit Report detection
- Training Record detection

#### Part D — Metadata Extraction

- Page count
- Word count
- Character count
- Author
- Creation date
- Modification date
- Checksum

#### Part E — Evidence Status Engine

- Draft detection
- Approval detection
- Version detection
- Human-review status
- Sufficient evidence status

#### Part F — Evidence Insights

- Evidence summary
- Document-type distribution
- Evidence-status distribution
- Common issue detection

### ✅ Phase 4 — Compliance Framework Engine

Planned support:

- ISO/IEC 27001
- ISO/IEC 27002
- ISO/IEC 42001
- NIST Cybersecurity Framework
- CIS Controls
- SOC 2
- CSA CCM
- DORA
- NIS2

Planned capabilities:

- Framework plugin architecture
- Control libraries
- Evidence-to-control mapping
- Control coverage analysis
- Compliance gap detection
- Framework scoring
- Cross-framework mapping

### ⏳ Phase 5 — CAPA and Ticket Engine

- Corrective action generation
- Preventive action generation
- Root-cause tracking
- Priority assignment
- Due-date recommendations
- Required-evidence recommendations
- GitHub Issues integration
- Jira integration
- Azure DevOps integration
- ServiceNow integration

### ⏳ Phase 6 — AI Compliance Copilot

- Policy analysis
- Evidence extraction
- Control mapping
- Gap explanations
- CAPA recommendations
- Audit Q&A
- Executive summaries
- RAG-based evidence search
- Local and hosted LLM support
- Prompt-injection safeguards

### ⏳ Phase 7 — Dashboard and Reporting

- React dashboard
- Framework readiness scores
- Evidence coverage
- Findings by severity
- Open CAPAs
- Overdue actions
- Risk distribution
- Executive summaries
- PDF reports
- DOCX reports
- XLSX reports

---

## 🌟 Vision

AuditPilot aims to become an open-source compliance operating system for:

- Security compliance
- Risk management
- Evidence management
- Audit readiness
- Remediation tracking
- AI governance
- Continuous compliance

The long-term workflow is:

```text
Gap detected
      ↓
Explain why it matters
      ↓
Map to framework controls
      ↓
Generate CAPA
      ↓
Create remediation ticket
      ↓
Recommend required evidence
      ↓
Track until closure
```

Most compliance tools stop at identifying a gap.

AuditPilot aims to support the full remediation lifecycle.

---

## 👥 Maintainers

| Name | Role | Focus |
|---|---|---|
| **Anirudh Shandilya** | Project Lead and Cybersecurity Engineer | Security, GRC, backend architecture and open-source management |
| **Suryakiran Suresh** | AI and Data Science Contributor | Machine learning, NLP, AI models and analytics |

---

## 🤝 Contributing

Contributions are welcome.

To contribute:

1. Fork the repository.
2. Create a feature branch.

```bash
git checkout -b feature/my-feature
```

3. Commit your changes.

```bash
git commit -m "feat: add new capability"
```

4. Push your branch.

```bash
git push origin feature/my-feature
```

5. Open a pull request.

Please read `CONTRIBUTING.md` before submitting changes.

Areas where contributors can help:

- FastAPI
- React
- AI and NLP
- ISO/IEC 27001
- ISO/IEC 42001
- NIST CSF
- SOC 2
- Cloud security
- DevOps
- Testing
- Documentation

---

## 🔐 Security

Please report security vulnerabilities according to the guidance in `SECURITY.md`.

Do not disclose vulnerabilities through public GitHub issues.

---

## 📄 License

AuditPilot is licensed under the **Apache License 2.0**.

---

## ⭐ Support the Project

If you find AuditPilot useful:

- ⭐ Star the repository
- 🍴 Fork the project
- 🛠️ Contribute improvements
- 🐛 Report issues
- 💬 Share feedback

Your support helps AuditPilot reach more security professionals, GRC practitioners, engineers, auditors and open-source contributors.
