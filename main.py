from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import listado, users, users_db

app = FastAPI()

# Middleware
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def hello():
    return {"message": "Kaixo World"}

@app.get("/kaixo")
async def kaixo():
    return {"message": "Kaixo munduari"}

app.include_router(listado.router)
app.include_router(users_db.router)
app.include_router(users.router)