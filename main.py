from fastapi import FastAPI
from routes import listado, users

app = FastAPI()

@app.get("/")
async def hello():
    return {"message": "Kaixo World"}

@app.get("/kaixo")
async def kaixo():
    return {"message": "Kaixo munduari"}

app.include_router(listado.router)
app.include_router(users.router)