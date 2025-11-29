
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import bcrypt

from app.core.database import get_db
from app.core.security import create_access_token
from app.crud.user import get_user_by_email
from app.schemas.user import UserResponse


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)



# ----------------------------
#    LOGIN -> Generar TOKEN
# ----------------------------
from fastapi import Form

@router.post("/login")
def login(
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):

    # 1. Buscar usuario por email
    user= get_user_by_email(db, email)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no existe")
    
    # 2. Verificar contraseña con bcrypt
    if not bcrypt.checkpw(password.encode("utf-8"), user.hashed_password.encode("utf-8")):
        raise HTTPException(status_code=401, detail="Contraseña incorrecta")
    
    # 3. Generar JWT con `sub = user.id``
    token = create_access_token({"sub": str(user.id)})

    # 4. Respuesta profesional
    return{
        "access_token": token,
        "token_type":"bearer",
        "user": UserResponse.from_orm(user)
    }
