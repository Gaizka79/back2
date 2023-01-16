from  fastapi import APIRouter

router = APIRouter(prefix="/list",
                  tags=["listado"])

lista = ["Esta", "es", "una", "lista", "nueva"]

@router.get("/")
def listado():
    return lista