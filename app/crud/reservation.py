
from sqlalchemy.orm import Session
from sqlalchemy import select, and_

from app.models import Reservation
from app.schemas.reservation import ReservationCreate, ReservationUpdate



# ----------------------------
#    Obtener reserva por ID
# ----------------------------
def get_reservation_by_id(db: Session, reservation_id: int) -> Reservation | None:
    return db.scalars(select(Reservation).where(Reservation.id == reservation_id))



# ----------------------------------
#    Obtener reservas por usuario
# ----------------------------------
def get_reservation_by_user(db: Session, user_id: int) -> list[Reservation]:
    return db.scalars(select(Reservation).where(Reservation.user_id == user_id)).all()



# --------------------------------------
#    Obtener reservas por herramienta
# --------------------------------------
def get_reservation_by_tool(db: Session, tool_id: int) -> list[Reservation]:
    return db.scalars(select(Reservation).where(Reservation.tool_id == tool_id)).all()



# -------------------------------------------------------------------------
#                          Regla Anti-Solapamiento
#    Comprobar si existe otra reserva activa en el mismo rango de tiempo
# -------------------------------------------------------------------------
def reservation_conflicts(db: Session, data: ReservationCreate) -> bool:
    return db.scalar(
        select(Reservation).where(
            Reservation.tool_id == data.tool_id,
            Reservation.status == "active",
            and_(
                Reservation.start_time < data.end_time,
                Reservation.end_time > data.start_time
            )
        )
    ) is not None



# ------------------------------------
#    Crear Reserva (con validación)
# ------------------------------------
def create_reservation(db: Session, data: ReservationCreate) -> Reservation:

    # 1) Comprobar solapamiento
    if reservation_conflicts(db, data):
        raise ValueError("Ya existe una reserva activa en ese horario.")
    
    # 2) Crear reserva
    new_reservation = Reservation(
        user_id=data.user_id,
        tool_id=data.tool_id,
        start_time=data.start_time,
        end_time=data.end_time,
        status="active"
    )

    db.add(new_reservation)
    db.commit()
    db.refresh(new_reservation)
    return new_reservation



# --------------------------------------------
#    Actualizar reserva (revalida horarios)
# --------------------------------------------
def update_reservation(db: Session, db_reservation: Reservation, update: ReservationUpdate) -> Reservation:

    update_data = update.dict(exclude_unset=True)

    # Si se modifica horario -> revalidar solapamientos
    if "start_time" in update_data or "end_time" in update_data:
        temp_data = ReservationCreate(
            user_id=db_reservation.user_id,
            tool_id=db_reservation.tool_id,
            start_time=update_data.get("start_time", db_reservation.start_time),
            end_time=update_data.get("end_time", db_reservation.end_time),
        )
        if reservation_conflicts(db, temp_data):
            raise ValueError("La actualización genera solapamiento. Cambios no aplicados.")
        
    for key, value, in update_data.items():
        setattr(db_reservation, key, value)

    db.commit()
    db.refresh(db_reservation)
    return db_reservation



# ---------------------------------
#    Eliminar / Cancelar reserva
# ---------------------------------
def delete_reservation(db: Session, db_reservation: Reservation) -> None:
    db.delete(db_reservation)
    db.commit()
