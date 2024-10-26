from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from mkvactrannumpy import calculate_value

app = FastAPI()

# 입력값을 받기 위한 모델 정의
class InputData(BaseModel):
    a: float
    b: float
    c: float
    d: float

@app.post("/api/calculate")
def perform_calculation(data: InputData):
    try:
        result = calculate_value(data.a, data.b, data.c, data.d)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
