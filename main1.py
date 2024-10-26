# main.py
from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/api/multiply")
def multiply(conductance: int, pump: str):
    # 예제: 단순한 계산 수행
    result = conductance * 2
    return {"result": result, "pump": pump}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
