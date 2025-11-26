
from sqlalchemy.orm import Session
from sqlalchemy import select
import bcrypt

from app.models import User
from app.schemas.user import UserCreate, UserUpdate



# ---------------------------------------------
#    UTILIDAD INTERNA: HASHING DE CONTRASEÑA
# ---------------------------------------------
def hash_password(password: str) -> str:
    """
    Recibe la contraseña en texto plano y devuelve un hash seguro con bcrypt.
    """
    salt = bcrypt.gensalt() # genera una sal segura automáticamente
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed.decode("utf-8") # se guarda en DB como str


# -------------------------------
#    Obtener usuario por email
# -------------------------------
def get_user_by_email(db: Session, email: str) -> User | None:
    return db.scalar(select(User).where(User.email == email))


# ----------------------------
#    Obtener usuario por ID
# ----------------------------
def get_user_by_id(db: Session, user_id: int) -> User | None:
    return db.scalar(select(User).where(User.id == user_id))


# --------------------------------
#    Obtener todos los usuarios
# --------------------------------
def get_all_users(db: Session) -> list[User]:
    return db.scalar(select(User)).all()


# -------------------------------------------
#    Crear usuario con contraseña hasheada
# -------------------------------------------
def create_user(db: Session, data: UserCreate) -> User:
    # 1) Comprobar email único
    if get_user_by_email(db, data.email):
        raise ValueError("El email ya está registrado, usuario duplicado.")
    
    # 2) Generar modelo con contraseña hasheada
    hashed_pwd = hash_password(data.password)
    new_user = User(
        name=data.name,
        email=data.email,
        hashed_password=hashed_pwd, # nunca guardar plaintext
        is_active=True,
        is_admin=False
    )

    # 3) Guardar en DB
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# ----------------------------------
#    Actualizar usuario (opcional)
# ----------------------------------
def update_user(db: Session, db_user: User, update: UserUpdate) -> User:
    update_data = update.dict(exclude_unset=True)

    # si incluye nueva contraseña -> hashearla también
    if "password" in update_data:
        update_data["hashed_password"] = hash_password(update_data.pop("password"))

    for key, value in update_data.items():
        setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)
    return db_user


# ---------------------------------
#    Eliminar usuario (opcional)
# ---------------------------------
def delete_user(db: Session, db_user: User) -> None:
    db.delete(db_user)
    db.commit()
