from fastapi import FastAPI
from app.services.scheduler import SchedulerService
from contextlib import asynccontextmanager

# Use lifespan events to start/stop the scheduler
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    scheduler = SchedulerService()
    scheduler.start()
    yield
    # Shutdown (optional cleanup)

app = FastAPI(title="AI News Aggregator", lifespan=lifespan)

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI News Aggregator! The system is up and running."}

if __name__ == "__main__":
    import uvicorn
    # Run the app on localhost:8000
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

