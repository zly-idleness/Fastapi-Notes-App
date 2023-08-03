from src.routes import notes, users
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise import Tortoise

from src.database.register import register_tortoise
from src.database.config import TORTOISE_ORM

# enable schemas to read relationship between models
Tortoise.init_models(["src.database.models"], "models")

# notice the order of the imports and init_model

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)


app.include_router(users.router)
app.include_router(notes.router)


@app.get("/")
def home():
    return "Hello, World!"
