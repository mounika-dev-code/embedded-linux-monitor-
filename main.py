from fastapi import FastAPI
from fastapi.responses import JSONResponse
import subprocess
import json

app = FastAPI()

# Root route
@app.get("/")
def root():
    return {"message": "FastAPI server is running!"}

# Health check route
@app.get("/health")
def health():
    return {"status": "ok"}

# Metrics route with error handling
@app.get("/metrics")
def metrics():
    try:
        # Run the external agent
        result = subprocess.check_output(["../agent/health_agent"], stderr=subprocess.STDOUT)
        
        # Decode bytes to string
        result_str = result.decode("utf-8")
        
        # Parse JSON output
        data = json.loads(result_str)
        return data

    except subprocess.CalledProcessError as e:
        # Subprocess failed
        return JSONResponse(
            status_code=500,
            content={"error": "Subprocess failed", "details": e.output.decode("utf-8")}
        )

    except FileNotFoundError:
        # Agent executable not found
        return JSONResponse(
            status_code=500,
            content={"error": "Agent executable not found at '../agent/health_agent'"}
        )

    except json.JSONDecodeError:
        # Invalid JSON output
        return JSONResponse(
            status_code=500,
            content={"error": "Invalid JSON output from agent", "raw_output": result_str}
        )
