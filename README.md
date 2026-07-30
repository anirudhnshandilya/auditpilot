<div align="center">

# 🛡️ AuditPilot

### Open-source security compliance, evidence intelligence and audit-readiness platform

**Validate risk registers. Analyse evidence. Map ISO/IEC 27001 controls. Detect gaps. Generate remediation actions.**

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Tests](https://img.shields.io/badge/tests-82%20passing-brightgreen)](#-engineering-quality)
[![MyPy](https://img.shields.io/badge/MyPy-clean-blue)](#-engineering-quality)
[![Ruff](https://img.shields.io/badge/Ruff-clean-purple)](#-engineering-quality)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md)
[![Project Status](https://img.shields.io/badge/status-active%20development-orange)](#-project-status)

[Getting Started](#-getting-started) •
[Features](#-what-auditpilot-does) •
[API](#-api-endpoints) •
[Architecture](#-architecture) •
[Roadmap](#-roadmap) •
[Contributing](#-contributing)

</div>

---

## Why AuditPilot?

Preparing for an ISO/IEC 27001 audit is still heavily manual.

Security and GRC teams often spend days or weeks:

- chasing evidence across multiple systems;
- validating inconsistent spreadsheets;
- checking whether policies are approved and current;
- mapping documents to framework controls;
- identifying missing evidence;
- maintaining corrective-action trackers;
- producing readiness summaries for management.

AuditPilot brings these activities into one extensible, open-source workflow.

```text
Risk Registers
      ↓
Validation Engine
      ↓
Evidence Upload
      ↓
Document Intelligence
      ↓
ISO/IEC 27001 Mapping
      ↓
Coverage Analysis
      ↓
Gap Detection
      ↓
Compliance Scoring
      ↓
CAPA Generation
      ↓
Remediation Tracking
```

> AuditPilot is designed to help organisations move from  
> **“Are we compliant?”**  
> to  
> **“We know exactly where we stand and what to fix next.”**

---

## ✨ What AuditPilot Does

### 🧾 Validates compliance registers

Upload a CSV or XLSX risk register and detect:

- duplicate or missing Risk IDs;
- missing owners, titles and descriptions;
- missing treatment plans;
- invalid likelihood and impact values;
- missing, invalid or overdue review dates;
- duplicate and empty rows;
- missing required columns.

### 📄 Processes audit evidence

Upload:

- PDF
- DOCX
- TXT
- CSV
- XLSX

AuditPilot parses the content, generates a SHA-256 checksum and stores structured evidence metadata.

### 🧠 Understands documents

AuditPilot can automatically:

- classify document types;
- extract metadata;
- detect drafts;
- detect missing approval information;
- detect missing version information;
- identify documents requiring human review;
- assess whether evidence appears sufficient.

### 🗺️ Maps evidence to ISO/IEC 27001 controls

Uploaded evidence can be mapped to controls using:

- control-specific keywords;
- matched-keyword tracking;
- deterministic confidence scores;
- a typed control library.

### 📊 Measures framework coverage

AuditPilot calculates:

- total controls;
- covered controls;
- uncovered controls;
- framework coverage percentage;
- covered and uncovered control IDs.

### 🚨 Detects compliance gaps

For uncovered controls, AuditPilot returns:

- control ID;
- control title;
- expected evidence;
- gap severity;
- remediation recommendation.

### ✅ Generates remediation actions

Detected compliance gaps can be converted into CAPA-style actions containing:

- control reference;
- remediation recommendation;
- expected evidence;
- priority;
- action status.

---

## 🎯 Example Output

### Evidence-to-control mapping

```json
{
  "filename": "information-security-policy.pdf",
  "document_type": "Policy",
  "evidence_status": "Sufficient",
  "control_mappings": [
    {
      "control_id": "A.5.1",
      "confidence": 1.0,
      "matched_keywords": [
        "information security policy",
        "approved by",
        "policy review",
        "version"
      ]
    }
  ]
}
```

### ISO/IEC 27001 coverage

```json
{
  "total_controls": 2,
  "covered_controls": 1,
  "uncovered_controls": 1,
  "coverage_percentage": 50.0,
  "covered_control_ids": [
    "A.5.1"
  ],
  "uncovered_control_ids": [
    "A.5.2"
  ]
}
```

### Compliance gap

```json
{
  "control_id": "A.5.2",
  "control_title": "Information security roles and responsibilities",
  "expected_evidence": [
    "Roles and responsibilities matrix",
    "Job descriptions",
    "RACI matrix"
  ],
  "severity": "Medium",
  "recommendation": "Provide evidence for A.5.2 (Information security roles and responsibilities)."
}
```

### Remediation action

```json
{
  "control_id": "A.5.2",
  "control_title": "Information security roles and responsibilities",
  "priority": "Medium",
  "recommendation": "Provide evidence for A.5.2 (Information security roles and responsibilities).",
  "expected_evidence": [
    "Roles and responsibilities matrix",
    "Job descriptions",
    "RACI matrix"
  ],
  "status": "Open"
}
```

---

## 🚧 Project Status

AuditPilot is under active development.

```text
Phase 1  Backend Foundation                 ✅ Complete
Phase 2  Validation Engine                  ✅ Complete
Phase 3  Evidence Intelligence Pipeline     ✅ Complete
Phase 4  Compliance Framework Engine        ✅ Complete
Phase 5  CAPA and Remediation Engine         🚧 In progress
Phase 6  AI Compliance Copilot               ⏳ Planned
Phase 7  Dashboard and Reporting             ⏳ Planned
```

The current implementation is suitable for development, experimentation and open-source collaboration. It is not yet intended to replace professional legal, certification or audit advice.

---

## 🔥 Current Highlights

| Capability | Status |
|---|---:|
| FastAPI backend | ✅ |
| Risk Register validation | ✅ |
| Multi-format evidence upload | ✅ |
| PDF and DOCX text extraction | ✅ |
| Evidence repository | ✅ |
| Automatic document classification | ✅ |
| Metadata extraction | ✅ |
| Evidence-quality analysis | ✅ |
| ISO/IEC 27001 control library | ✅ |
| Evidence-to-control mapping | ✅ |
| Framework coverage analysis | ✅ |
| Compliance gap detection | ✅ |
| Compliance scoring | ✅ |
| CAPA generation | ✅ |
| Framework registry | ✅ |
| Persistent database storage | 🚧 |
| React dashboard | ⏳ |
| AI Compliance Copilot | ⏳ |

---

## 🏗️ Architecture

```text
                            AuditPilot
                                │
              ┌─────────────────┴─────────────────┐
              │                                   │
       Register Validation                 Evidence Intelligence
              │                                   │
      Validation Engine                    Document Parser
              │                                   │
        Rule Registry                    Document Classifier
              │                                   │
          Rule Runner                    Metadata Extractor
              │                                   │
           Findings                   Evidence Status Engine
              │                                   │
              └─────────────────┬─────────────────┘
                                │
                       Framework Registry
                                │
                    ISO/IEC 27001 Controls
                                │
                       Control Mapping
                                │
                       Coverage Analysis
                                │
                        Gap Detection
                                │
                     Compliance Scoring
                                │
                       CAPA Generation
                                │
                     Remediation Workflow
                                │
                  AI Copilot and Dashboard
```

### Repository structure

```text
AuditPilot
│
├── backend
│   ├── app
│   │   ├── api
│   │   ├── core
│   │   │
│   │   ├── frameworks
│   │   │   ├── models.py
│   │   │   ├── registry.py
│   │   │   ├── service.py
│   │   │   ├── iso27001.py
│   │   │   ├── mapping.py
│   │   │   ├── mapper.py
│   │   │   ├── coverage.py
│   │   │   ├── coverage_service.py
│   │   │   ├── gaps.py
│   │   │   ├── gap_service.py
│   │   │   ├── scoring.py
│   │   │   └── scoring_service.py
│   │   │
│   │   ├── remediation
│   │   │   ├── models.py
│   │   │   └── service.py
│   │   │
│   │   ├── routes
│   │   │   ├── upload.py
│   │   │   ├── evidence.py
│   │   │   ├── frameworks.py
│   │   │   └── remediation.py
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
├── docs
├── examples
├── frontend
├── CONTRIBUTING.md
├── SECURITY.md
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.12+
- [`uv`](https://docs.astral.sh/uv/)

### Clone the repository

```bash
git clone https://github.com/anirudhnshandilya/auditpilot.git
cd auditpilot/backend
```

### Install dependencies

```bash
uv sync
```

### Start the API

```bash
uv run uvicorn app.main:app --reload
```

Open the interactive Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

Alternative API documentation:

```text
http://127.0.0.1:8000/redoc
```

---

## 📡 API Endpoints

### Health

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Project health information |
| `GET` | `/health` | Health check |

### Risk Register

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/upload/risk-register` | Upload and validate a CSV/XLSX risk register |

### Evidence

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/evidence/upload` | Upload and process evidence |
| `GET` | `/evidence` | List uploaded evidence |
| `GET` | `/evidence/summary` | Return evidence-level insights |
| `GET` | `/evidence/{document_id}` | Retrieve evidence metadata |
| `DELETE` | `/evidence/{document_id}` | Delete evidence |

### Frameworks

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/frameworks/iso27001` | List ISO/IEC 27001 controls |
| `GET` | `/frameworks/iso27001/{control_id}` | Retrieve one control |
| `GET` | `/frameworks/iso27001/coverage` | Calculate control coverage |
| `GET` | `/frameworks/iso27001/gaps` | Detect compliance gaps |
| `GET` | `/frameworks/iso27001/score` | Calculate compliance score |

### Remediation

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/remediation/actions` | Generate remediation actions from current gaps |

---

## 🧠 Document Intelligence

AuditPilot currently classifies documents as:

- Policy
- Procedure
- Risk Register
- Asset Register
- Incident Register
- Audit Report
- Training Record
- Unknown

Extracted metadata includes:

- filename;
- MIME type;
- size;
- upload timestamp;
- SHA-256 checksum;
- page count;
- word count;
- character count;
- author;
- document creation date;
- document modification date.

Evidence-quality checks currently include:

- draft detection;
- approval detection;
- version detection;
- invalid-document detection;
- human-review recommendations;
- sufficient-evidence classification.

---

## 🧾 Risk Register Rules

<details>
<summary><strong>View implemented validation rules</strong></summary>

- Duplicate Risk ID
- Empty Risk ID
- Duplicate rows
- Empty rows
- Missing required columns
- Missing owner
- Missing title
- Missing description
- Missing treatment plan
- Missing review date
- Invalid review date
- Past-due review date
- Invalid likelihood
- Invalid impact

</details>

---

## 🧪 Engineering Quality

AuditPilot is developed with automated quality gates.

```text
✅ 82 automated tests passing
✅ MyPy static type checking clean
✅ Ruff linting clean
✅ Typed domain models
✅ Modular service architecture
✅ Feature-branch workflow
✅ Pull-request reviews
✅ Conventional commit messages
```

Run the full test suite:

```bash
uv run pytest
```

Run static type checking:

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
- Uvicorn
- Pandas
- OpenPyXL
- PyMuPDF
- python-docx

### Testing and quality

- Pytest
- MyPy
- Ruff
- pandas-stubs

### Planned platform components

- PostgreSQL
- SQLAlchemy
- Alembic
- Redis
- React
- TypeScript
- Docker
- GitHub Actions
- Background workers
- OpenAI-compatible LLM providers
- Local LLM support
- Vector search
- Retrieval-augmented generation

---

## 🗺️ Roadmap

### ✅ Phase 1 — Backend Foundation

- FastAPI backend
- Health endpoints
- Swagger/OpenAPI
- Initial project structure
- Dependency management
- Automated testing foundation

### ✅ Phase 2 — Validation Engine

- Risk Register upload
- CSV/XLSX parsing
- Validation rule interface
- Rule registry
- Rule runner
- Severity model
- Audit-readiness results
- Risk Register rule pack

### ✅ Phase 3 — Evidence Intelligence Pipeline

- Multi-format evidence upload
- Document parsing
- Evidence repository
- UUID identifiers
- Automatic classification
- Metadata extraction
- Evidence status evaluation
- Evidence insights and summaries

### ✅ Phase 4 — Compliance Framework Engine

- Typed control model
- ISO/IEC 27001 control library
- Framework registry
- Control retrieval API
- Evidence-to-control mapping
- Confidence scoring
- Coverage analysis
- Gap detection
- Compliance scoring

### 🚧 Phase 5 — CAPA and Remediation Engine

- [x] Remediation action models
- [x] CAPA generation from compliance gaps
- [x] Priority assignment
- [x] Required-evidence recommendations
- [x] Remediation API
- [ ] Action ownership
- [ ] Due dates and SLA rules
- [ ] Action lifecycle management
- [ ] Remediation history
- [ ] Closure evidence
- [ ] Executive remediation summary
- [ ] Persistent action storage
- [ ] GitHub Issues integration
- [ ] Jira integration
- [ ] Azure DevOps integration
- [ ] ServiceNow integration

### ⏳ Phase 6 — AI Compliance Copilot

- Policy review
- Evidence analysis
- Control-mapping assistance
- Gap explanations
- CAPA recommendations
- Audit Q&A
- Executive summaries
- RAG-based evidence search
- Local and hosted LLM support
- Prompt-injection safeguards
- Human approval workflows

### ⏳ Phase 7 — Dashboard and Reporting

- React and TypeScript frontend
- Framework-readiness dashboard
- Evidence-coverage visualisation
- Findings by severity
- Risk heatmaps
- Open and overdue CAPAs
- Executive summaries
- PDF reports
- DOCX reports
- XLSX reports
- Authentication
- Role-based access control
- Multi-tenant support
- Continuous compliance monitoring

### Future framework support

The framework registry is being designed to support:

- ISO/IEC 27001
- ISO/IEC 27002
- ISO/IEC 42001
- NIST Cybersecurity Framework
- CIS Controls
- SOC 2
- CSA CCM
- DORA
- NIS2

---

## 🌟 Long-Term Vision

AuditPilot aims to become an open-source compliance operating system for:

- security compliance;
- governance, risk and compliance;
- evidence management;
- audit readiness;
- remediation tracking;
- AI governance;
- continuous compliance.

The target end-to-end workflow is:

```text
Gap detected
      ↓
Explain why it matters
      ↓
Map to framework controls
      ↓
Generate corrective action
      ↓
Assign owner and due date
      ↓
Create remediation ticket
      ↓
Recommend closure evidence
      ↓
Track until completion
      ↓
Recalculate readiness
```

Most compliance tools stop after identifying a gap.

AuditPilot aims to support the entire remediation lifecycle.

---

## 👥 Maintainers

| Name | Role | Focus |
|---|---|---|
| **Anirudh N Shandilya** | Project Co-Lead and Cybersecurity Engineer | Security, GRC, backend architecture and open-source project management |
| **Suryakiran Suresh** | Project Co-Lead and AI and Data Science Contributor | Machine learning, NLP, analytics and AI model development |

---

## 🤝 Contributing

Contributions are welcome from:

- cybersecurity engineers;
- GRC professionals;
- auditors;
- FastAPI developers;
- React and TypeScript developers;
- AI and NLP engineers;
- DevOps engineers;
- technical writers;
- ISO/IEC 27001 and ISO/IEC 42001 specialists.

### Contribution workflow

1. Fork the repository.
2. Create a feature branch.

```bash
git checkout -b feature/my-feature
```

3. Make and test your changes.

```bash
uv run pytest
uv run mypy app
uv run ruff check .
```

4. Commit using a conventional commit message.

```bash
git commit -m "feat: add new capability"
```

5. Push your branch.

```bash
git push origin feature/my-feature
```

6. Open a pull request.

Please review [`CONTRIBUTING.md`](CONTRIBUTING.md) before submitting changes.

---

## 💡 Ways to Contribute

You can help by:

- adding framework controls;
- improving evidence classification;
- proposing validation rules;
- improving documentation;
- writing tests;
- reviewing API design;
- creating dashboard components;
- designing integrations;
- reporting bugs;
- suggesting real-world GRC workflows.

---

## 🔐 Security

Please report security vulnerabilities using the process described in [`SECURITY.md`](SECURITY.md).

Do not disclose vulnerabilities through public GitHub issues.

---

## 📄 Licence

AuditPilot is licensed under the [Apache License 2.0](LICENSE).

---

## ⭐ Help Build Open-Source Compliance Automation

AuditPilot is being built in the open.

If the project is useful or interesting to you:

- ⭐ **Star the repository**
- 🐛 Report bugs
- 💡 Suggest features
- 🛠️ Submit pull requests
- 🤝 Share it with security and GRC teams

Every star, issue and contribution helps make security-compliance automation more accessible.

<div align="center">

### Built for security teams, auditors, engineers and the open-source community.

**[⭐ Star AuditPilot](https://github.com/anirudhnshandilya/auditpilot)**

</div>
