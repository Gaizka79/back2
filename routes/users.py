from fastapi import APIRouter
#from db.client import db_client

router = APIRouter(prefix="/users",
                   tags=["Users"])

user_list = [{
    "Nombre", "Gaizka",
    "Apellidos", "Arrondo Arce"
    },
    {"Nombre", "Adele",
    "Apellidos", "Arrondo Agiriano"
    }]

@router.get("/")
async def users():
    return user_list