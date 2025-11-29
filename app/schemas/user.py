
from pydantic import BaseModel, EmailStr, Field
from typing import Optional


# ----------------------------------------
#      SCHEMAS DE USUARIO (Pydantic)
# ----------------------------------------
# Mantenemos seguridad:
# - Nunca devolvemos contraseñas
# - Password sólo se recibe en UserCreate
# -----------------------------------------

# Base común que comparten los schemas
class UserBase(BaseModel):
    name: str = Field(..., example="Arturo Sanma")
    email: EmailStr = Field(..., example="usuario@example.com")


# ---------------------------------------------------------------------
#    Crear usuario (incluye contraseña en texto plano, sólo entrada)
# ---------------------------------------------------------------------
class UserCreate(UserBase):
    password: str = Field(
        ...,
        min_length=6,
        example="contraseña123",
        description="Contraseña del usuario. Se guardará hasheada."
    )


# --------------------------------------------------
#    Respuesta al cliente (NO incluye contraseña)
# --------------------------------------------------
class UserResponse(UserBase):
    id: int
    is_active: bool
    is_admin: bool

    class Config:
        from_attributes = True


# -----------------------------------------------------------------
#    Esquema de actualización (por si se quiere editar usuarios)
# -----------------------------------------------------------------
class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
