
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="API Security Testing Tool",
    description="A tool for testing authorized APIs for common security weaknesses.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type", "Authorization"],
)


@app.get("/")
async def home():
    return {
        "message": "API Security Testing Tool backend is running!",
        "version": "0.1.0",
    }


@app.get("/api/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "api-security-testing-tool",
    }
