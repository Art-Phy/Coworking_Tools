
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.security import verify_token
from app.crud.user import get_user_by_id
from app.core.database import get_db


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")



# -------------------------------------------
#    Obtener usuario autenticado desde JWT
# -------------------------------------------
def get_current_user(
        token: str = Depends(oauth2_scheme),
        db: Session = Depends(get_db)
):
    try:
        payload = verify_token(token)
        user_id = int(payload.get("sub"))

    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    user = get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="Usuario no existe")
    
    return user
