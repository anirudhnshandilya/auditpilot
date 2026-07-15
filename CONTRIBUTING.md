# Contributing to AuditPilot

First off, thank you for considering contributing to AuditPilot! 🎉

AuditPilot is an open-source project focused on helping organisations improve their security compliance and audit readiness. Contributions of all sizes are welcome.

---

## Ways to Contribute

- Report bugs
- Suggest new features
- Improve documentation
- Improve validation logic
- Add support for additional compliance frameworks
- Improve tests and CI/CD
- Refactor code

---

## Development Setup

Clone the repository:

```bash
git clone https://github.com/anirudhnshandilya/auditpilot.git
cd auditpilot/backend
```

Install dependencies:

```bash
uv sync
```

Run the application:

```bash
uv run uvicorn app.main:app --reload
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## Running Tests

```bash
uv run pytest
uv run ruff check .
uv run mypy app
```

---

## Development Workflow

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature/my-feature
```

3. Make your changes

4. Commit using meaningful commit messages

```bash
git commit -m "Add risk register validation"
```

5. Push your branch

6. Open a Pull Request

---

## Code Standards

- Follow PEP 8
- Keep functions small and focused
- Write tests for new functionality
- Use type hints where possible
- Update documentation when required

---

## Questions?

Open a GitHub Issue if you'd like to discuss an idea before implementing it.

Thank you for helping improve AuditPilot.
