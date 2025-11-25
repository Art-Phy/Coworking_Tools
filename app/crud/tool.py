
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models import Tool
from app.schemas.tool import ToolCreate, ToolUpdate



# -------------------------------------------------------------------------
#                  CRUD TOOL - Capa de acceso a datos
# -------------------------------------------------------------------------
# Este archivo contiene funciones responsables de interactuar con la BD.
# - No maneja request/response (eso es del router)
# - No maneja validaciones de negocio (eso es del service si lo hubiera)
# - Solo hace operaciones CRUD con SQLAlchemy (acceso directo a la DB)
# -------------------------------------------------------------------------


def get_tool_by_id(db: Session, tool_id: int) -> Tool | None:
    """
    Obtiene una herramienta por su ID.
    Devuelve None si no existe.
    """
    return db.scalar(select(Tool).where(Tool.id == tool_id))


def get_all_tools(db: Session) -> list[Tool]:
    """
    Obtiene todas las herramientas registradas en la base de datos.
    """
    return db.scalar(select(Tool)).all()


def create_tool(db: Session, tool_data: ToolCreate) -> Tool:
    """
    Crea una nueva herramienta en la base de datos
    """
    new_tool = Tool(**tool_data.dict())
    db.add(new_tool)
    db.commit()
    db.refresh(new_tool) # Recarga la DB (incluye el ID generado)
    return new_tool


def update_tool(db: Session, db_tool: Tool, update_data: ToolUpdate) -> Tool:
    """
    Actualiza una herramienta existente.
    Recibe el modelo Tool existente y los datos a actualizar.
    """
    # Sólo actualizamos campos que vienen en el ToolUpdate (no nulos)
    update_dict = update_data.dict(exclude_unset=True)
    for key, value in update_dict.items():
        setattr(db_tool, key, value)

    db.commit()
    db.refresh(db_tool)
    return db_tool


def delete_tool(db: Session, db_tool: Tool) -> None:
    """
    Elimina una herramienta de la base de datos.
    """
    db.delete(db_tool)
    db.commit()
