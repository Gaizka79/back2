from fastapi import APIRouter, HTTPException, status
from typing import List
from db.models.user import User
from db.schemas.user import user_schema, users_schema

from db.client import db_client


router = APIRouter(prefix="/usersdb",
                   tags=["UsersDB"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado!"}})

users_list = []

@router.get("/", response_model=List[User])
async def users():
    return users_schema(db_client.user.find())