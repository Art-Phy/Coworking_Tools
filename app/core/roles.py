
from fastapi import Depends, HTTPException, status
from app.core.auth import get_current_user



def require_admin(current_user = Depends(get_current_user)):
    """
    Verifica si el usuario autenticado es admin.
    Si no lo es -> responde con un 403.
    """
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tienes permisos para realizar esta acción."
        )
    return current_user
