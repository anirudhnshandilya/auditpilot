# 🛡️ AuditPilot

> Open-source AI-powered ISO/IEC 27001 readiness assistant for security and GRC teams.

AuditPilot helps organisations prepare for security audits by validating risk registers, asset registers, and supporting documentation. It combines deterministic validation with AI-assisted analysis to identify gaps, improve evidence quality, and generate actionable remediation recommendations. By automating the tedious process of manual evidence verification, AuditPilot transforms audit preparation from a stressful annual scramble into a continuous, self-correcting workflow

> 🚧 **Status:** Early development (v0.1.0-alpha)

---

## ✨ Features

### Current
- ✅ FastAPI backend
- ✅ Interactive Swagger API documentation
- ✅ Upload Risk Register (CSV/XLSX)
- ✅ File parsing with Pandas
- ✅ Automated testing with Pytest
- ✅ Linting with Ruff
- ✅ Type checking with MyPy

### Coming Soon
- 🔄 Risk Register validation engine
- 🔄 Asset Register upload
- 🔄 CAPA recommendation generator
- 🔄 ISO 27001 evidence mapping
- 🔄 AI-powered policy analysis
- 🔄 Executive audit readiness reports
- 🔄 React dashboard

---

## 🏗️ Project Architecture

```
AuditPilot
│
├── backend          # FastAPI API
├── frontend         # React UI (coming soon)
├── docs             # Architecture & roadmap
├── examples         # Sample datasets
└── tests            # Automated tests
```

---

## 🚀 Getting Started

### Clone

```bash
git clone https://github.com/anirudhnshandilya/auditpilot.git
cd auditpilot/backend
```

### Install

```bash
uv sync
```

### Run

```bash
uv run uvicorn app.main:app --reload
```

Visit:

```
http://127.0.0.1:8000/docs
```

---

## 📌 Roadmap

### v0.1
- [x] FastAPI backend
- [x] Health endpoints
- [x] Risk Register upload
- [ ] Upload validation
- [ ] CSV/XLSX parser

### v0.2
- [ ] Validation engine
- [ ] Asset Register support
- [ ] Findings report

### v0.3
- [ ] CAPA recommendations
- [ ] Dashboard
- [ ] Authentication

### v0.4
- [ ] AI-powered evidence extraction
- [ ] ISO 27001 control mapping
- [ ] Audit readiness scoring

---

## 🧪 Testing

```bash
uv run pytest
uv run ruff check .
uv run mypy app
```

---

## 🤝 Contributing

Contributions are welcome!

If you'd like to improve AuditPilot:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

Please read the `CONTRIBUTING.md` before submitting a PR.

---

## 📄 License

Licensed under the Apache 2.0 License.

---

## ⭐ Support the Project

If you find AuditPilot useful, consider giving it a ⭐ on GitHub. It helps the project reach more security professionals and encourages further development.
