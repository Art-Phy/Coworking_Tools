
from datetime import datetime
from pydantic import BaseModel, Field, validator
from typing import Optional


# -------------------------------------------
#    BASE de Reservation -> Campos comunes
# -------------------------------------------
class ReservationBase(BaseModel):
    user_id: int = Field(..., example=1, description="ID del usuario que reserva")
    tool_id: int = Field(..., example=3, description="ID de la herramienta reservada")
    start_time: datetime = Field(..., example="2025-05-02T10:00:00")
    end_time: datetime = Field(..., example="2025-05-02T12:00:00")

    # Validación Pydantic -> start_time deber ser < end_time
    @validator("end_time")
    def validate_dates(cls, end, values):
        start = values.get("start_time")
        if start and end <= start:
            raise ValueError("end_time debe ser posterior a start_time")
        return end
    


# --------------------------------
#    Schema para CREAR reservas
# --------------------------------
class ReservationCreate(ReservationBase):
    pass



# --------------------------------------------
#    Schema para RESPUESTA (response_model)
#           - Incluye ID + estado
# --------------------------------------------
class ReservationResponse(ReservationBase):
    id: int
    status: str = Field(default="active", description="active | cancelled")

    class Config:
        orm_mode = True



# -----------------------------------------------
#           Schema para ACTUALIZACIÓN
#    (cambiar herramienta, horario o cancelar)
# -----------------------------------------------
class ReservationUpdate(BaseModel):
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    status: Optional[str] = Field(None, example="cancelled")

    @validator("end_time")
    def validate_update_dates(cls, end, values):
        start = values.get("start_time")
        if start and end and end <= start:
            raise ValueError("end_time debe ser posterior a start_time")
        return end
