from fastapi import FastAPI

app = FastAPI(
    title="Football Analytics API",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "status": "healthy",
        "service": "football-analytics"
    }