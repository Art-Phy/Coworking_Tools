
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.crud.user import (
    create_user,
    get_user_by_id,
    get_user_by_email,
    get_all_users,
    update_user
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


# ---------------------------
#    POST -> Crear usuario
# ---------------------------
@router.post("/", response_model=UserResponse, status_code=201)
def register_user(new_user: UserCreate, db: Session = Depends(get_db)):

    # email único
    if get_user_by_email(db, new_user.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El mail ya está registrado"
        )
    
    user = create_user(db, new_user)
    return user


# --------------------------------------
#    GET -> Listar todos los usuarios
# --------------------------------------
@router.get("/", response_model=list[UserResponse])
def list_users(db: Session = Depends(get_db)):
    return get_all_users(db)


# -----------------------------------
#    GET -> Obtener usuario por ID
# -----------------------------------
@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):

    user = get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail=f"El usuario con ID {user_id} no existe."
        )
    
    return user


# ------------------------------------------
#    PUT -> Actualizar usuario (opcional)
# ------------------------------------------
@router.put("/{user_id}", response_model=UserResponse)
def update_existing_user(user_id: int, update: UserUpdate, db: Session = Depends(get_db)):

    db_user = get_user_by_id(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    update = update_user(db, db_user, update)
    return update
