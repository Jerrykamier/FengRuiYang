from fastapi import FastAPI

from app.api.health import router as health_router
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="高校科研 RAG 文献知识库 Demo 后端服务",
)


@app.get("/")
def root():
    return {
        "message": "University RAG Assistant API",
        "docs": "/docs",
        "health": "/api/health",
    }


app.include_router(health_router, prefix="/api")
