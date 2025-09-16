# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict, Any
import random
from datetime import datetime

app = FastAPI(title="Car Health Monitoring API")

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Store historical data - initialize as empty list
historical_data: List[Dict[str, Any]] = []

@app.get("/")
async def root():
    return {"message": "Car Health Monitoring API"}

@app.get("/car/status")
async def get_car_status():
    """Endpoint to get simulated car status data"""
    try:
        # Generate random car data
        data = {
            "speed": random.randint(0, 120),
            "fuel": random.randint(0, 100),
            "engineTemp": random.randint(70, 120),
            "tirePressure": {
                "frontLeft": round(random.uniform(30.0, 36.0), 1),
                "frontRight": round(random.uniform(30.0, 36.0), 1),
                "rearLeft": round(random.uniform(30.0, 36.0), 1),
                "rearRight": round(random.uniform(30.0, 36.0), 1)
            },
            "batteryVoltage": round(random.uniform(11.8, 14.2), 1),
            "rpm": random.randint(600, 4000),
            "timestamp": datetime.now().isoformat()
        }
        
        # Update historical data (keep last 10 readings)
        historical_data.append(data)
        if len(historical_data) > 10:
            historical_data.pop(0)  # Remove the oldest item
        
        return data
    except Exception as e:
        # Return error message if something goes wrong
        return {"error": str(e)}

@app.get("/car/history")
async def get_car_history():
    """Endpoint to get historical car data"""
    return historical_data

if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 8000))  # Railway provides PORT
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=False)

    