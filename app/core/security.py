
from datetime import datetime, timedelta
from jose import jwt, JWTError
from typing import Optional

from app.core.config import settings


# ---------------------------------
#    CONFIGURACIÓN DEL TOKEN JWT
# ---------------------------------
SECRET_KEY = "SUSTITUIR_POR_VARIABLE_ENV" 
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 



# ---------------------------
#    Crear TOKEN de acceso
# ---------------------------
def create_access_token(data: dict, expires_delta: Optional[int] = None) -> str:
    """
    Genera un JWT firmado con expiración automática.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(
        minutes=expires_delta or ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode["exp"] = expire

    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt



# -----------------------------------
#    Verificar y decodificar TOKEN
# -----------------------------------
def verify_token(token: str) -> dict:
    """
    Valida la firma del token y devuelve su contenido o lanza error.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    
    except JWTError:
        raise ValueError("Token inválido o expirado")
