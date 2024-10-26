from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS 설정: GitHub Pages에서의 요청 허용
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://sugook.github.io"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# /api/calculate 엔드포인트 정의
@app.post("/api/calculate")
def calculate(a: int, b: int, c: int, d: int):
    try:
        result = (a + b) * (c - d)  # 예제 계산
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
