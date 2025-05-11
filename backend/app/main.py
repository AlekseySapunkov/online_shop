from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.createDB import engine, Base, AsyncSessionLocal
from app.models.user import User
from app.models.products import Product
from app.schemas.user import UserResponse
from sqlalchemy import select

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Разрешенные источники
    allow_credentials=True,
    allow_methods=["*"],  # Разрешенные методы (GET, POST, etc.)
    allow_headers=["*"],  # Разрешенные заголовки
)
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.on_event("startup")
async def on_startup():
    await create_tables()

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}
@app.get("/products")
def read_products():
    return {"message": "Welcome to the API"}
@app.get("/users", response_model = list[UserResponse])
async def get_users():
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(User))
        users_list = result.scalars().all()
        return users_list
