
from pydantic import BaseModel, Field
from typing import Optional


# ------------------------------------------------------------------------
#                       SCHEMAS PARA LA ENTIDAD TOOL
# ------------------------------------------------------------------------
# En FastAPI, los Schemas representan cómo entran y salen los datos.
# - ToolBase   → Propiedades comunes
# - ToolCreate → Datos necesarios para crear una herramienta
# - ToolUpdate → Datos para actualizar parcialmente
# - ToolResponse → Datos que devolvemos al cliente
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
# Base común: contiene los campos compartidos entre create/update/response
#-------------------------------------------------------------------------
class ToolBase(BaseModel):
    name: str = Field(..., example="Taladro inalámbrico")
    description: Optional[str] = Field(None, example="Taladro de 18V con batería")
    status: Optional[str] = Field(
        default="available",
        example="maintenance",
        description="Estado de la herramienta: available, maintenance o broken",
    )
    requires_training: Optional[bool] = Field(
        default=False,
        example=True,
        description="Indica si requiere capacitación previa para usarla",
    )



# -----------------------------------------------
#    Esquema para crear una herramienta (POST)
# -----------------------------------------------
class ToolCreate(ToolBase):
    """Datos requeridos para crear una herramienta."""
    pass



# ---------------------------------------------------------------------------
#             Esquema para actualizar una herramienta (PUT/PATCH)
#  Todos los campoos son opcionales para permitir actualizaciones parciales
# ---------------------------------------------------------------------------
class ToolUpdate(BaseModel):
    name: Optional[str] = Field(None)
    description: Optional[str] = Field(None)
    status: Optional[str] = Field(None)
    requires_training: Optional[bool] = Field(None)



# ---------------------------------------------------------------------------
#               Esquemas para respuestas enviadas al cliente
#  Incluye el campo 'id' y configura orm_model=True para usar datos del ORM
# ---------------------------------------------------------------------------
class ToolResponse(ToolBase):
    id: int

    class Config:
        orm_mode = True
