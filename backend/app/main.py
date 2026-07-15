from fastapi import FastAPI

app = FastAPI(
    title="AuditPilot API",
    description="Open-source ISO 27001 readiness assistant.",
    version="0.1.0",
)


@app.get("/", tags=["Health"])
def root() -> dict[str, str]:
    return {
        "status": "healthy",
        "project": "AuditPilot",
        "version": "0.1.0",
    }


@app.get("/health", tags=["Health"])
def health_check() -> dict[str, str]:
    return {"status": "healthy"}