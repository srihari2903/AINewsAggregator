from fastapi import FastAPI

app = FastAPI(title="AI News Aggregator")

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI News Aggregator! The system is up and running."}

if __name__ == "__main__":
    import uvicorn
    # Run the app on localhost:8000
    uvicorn.run(app, host="0.0.0.0", port=8000)
