# FastAPI app entrypoint
from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Whatnot Automation MVP",
    description="AI-powered operations platform for inventory, research, finance, and order flows",
    version="0.1.0",
)

app.include_router(router)


@app.get("/health")
async def health() -> dict:
    return {"status": "ok", "service": "whatnot-automation-agent"}
