
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session


from app.core.auth import get_current_user
from app.core.auth import get_current_user
from app.core.database import get_db
from app.models import Reservation



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



def  require_owner_or_admin(reservation_id: int, current_user = Depends(get_current_user), db: Session = Depends(get_db)):
    """
    Permisos avanzados para reservas:

     - Un ADMIN puede modificar/cancelar cualquier reserva
     - Un usuario normal sólo puede manipular reservas que le pertenecen.
    """

    # Si es admin -> acceso directo permitido
    if current_user.is_admin:
        return True
    
    # Si no es adminm, buscamos la reserva
    reservation = db.get(Reservation, reservation_id)

    if not reservation:
        raise HTTPException(status_code=404, detail="La reserva no existe")
    
    # Si la reserva no pertenece al usuario -> acceso denegado
    if reservation.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acceso denegado. Sólo puedes gestionar tus propias reservas."
        )
    
    return True
