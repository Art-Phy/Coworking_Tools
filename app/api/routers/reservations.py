
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.reservation import (
    ReservationCreate, ReservationResponse, ReservationUpdate
)
from app.crud.reservation import (
    create_reservation,
    get_reservation_by_id,
    get_reservation_by_user,
    get_reservation_by_tool,
    update_reservation,
    delete_reservation
)


router = APIRouter(
    prefix="/reservations",
    tags=["Reservations"]
)


# ---------------------------------------------------
#    POST -> Crear reserva (con anti-solapamiento)
# ---------------------------------------------------
@router.post("/", response_model=ReservationResponse, status_code=201)
def new_reservation(data: ReservationCreate, db: Session = Depends(get_db)):
    
    try:
        reservation = create_reservation(db, data)
        return reservation
        
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, # conflicto de reserva
            detail=str(e)
        )



# ----------------------------------------
#    # GET -> Listar todas las reservas
# ----------------------------------------
@router.get("/", response_model=list[ReservationResponse])
def list_resercations(db: Session = Depends(get_db)):
    from sqlalchemy import select
    from app.models import Reservation
    return db.scalars(select(Reservation)).all()



# ---------------------------
#    GET -> Obtener por ID
# ---------------------------
@router.get("/{reservation_id}", response_model=ReservationResponse)
def get_reservation(reservation_id: int, db: Session = Depends(get_db)):

    reservation = get_reservation_by_id(db, reservation_id)

    if not reservation:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")
    
    return reservation



# ---------------------------------
#    GET -> Reservas por usuario
# ---------------------------------
@router.get("/user/{user_id}", response_model=list[ReservationResponse])
def reservations_by_user(user_id: int, db: Session = Depends(get_db)):
    return get_reservation_by_user(db, user_id)



# -------------------------------------
#    GET -> Reservas por herramienta
# -------------------------------------
@router.get("/tool/{tool_id}", response_model=list[ReservationResponse])
def reservations_by_tool(tool_id: int, db: Session = Depends(get_db)):
    return get_reservation_by_tool(db, tool_id)



# ----------------------------------------------
#    PUT -> Editar reserva (con revalidación)
# ----------------------------------------------
@router.put("/{reservation_id}", response_model=ReservationResponse)
def edit_reservation(reservation_id: int, update: ReservationUpdate, db: Session = Depends(get_db)):

    reservation = get_reservation_by_id(db, reservation_id)

    if not reservation:
        raise HTTPException(status_code=404, detail="Reserva no existe")
    
    try:
        updated = update_reservation(db, reservation, update)
        return update
    
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(e)
        )



# -----------------------------------------
#    DELETE -> Cancelar/eliminar reserva
# -----------------------------------------
@router.delete("/{reservation_id}", status_code=204)
def remove_reservation(reservation_id: int, db: Session = Depends(get_db)):

    reservation = get_reservation_by_id(db, reservation_id)

    if not reservation:
        raise HTTPException(status_code=404, detail="No existe esa reserva")
    
    delete_reservation(db, reservation)
    return None
