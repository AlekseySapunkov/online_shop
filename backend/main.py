from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Разрешенные источники
    allow_credentials=True,
    allow_methods=["*"],  # Разрешенные методы (GET, POST, etc.)
    allow_headers=["*"],  # Разрешенные заголовки
)
@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}
@app.get("/products")
def read_products():
    return {"message": "Welcome to the API"}
