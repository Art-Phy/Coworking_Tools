
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.tool import ToolCreate, ToolUpdate, ToolResponse
from app.crud.tool import (
    get_tool_by_id,
    get_all_tools,
    create_tool,
    update_tool,
    delete_tool,
)

router = APIRouter(
    prefix="/tools",
    tags=["Tools"]
)


# ---------------------------------------
#    POST /tools/ -> Crear herramienta
# ---------------------------------------
@router.post("/", response_model=ToolResponse, status_code=status.HTTP_201_CREATED)
def create_new_tool(tool_data: ToolCreate, db: Session = Depends(get_db)):
    """
    Crea una nueva herramienta en el sistema.

    - Valida automáticamente el body gracias a ToolCreate.
    - Comprueba si ya existe una herramienta con ese nombre (opcional, por ahora no).
    - Devuelve la herramienta creada con su ID asignado.
    """
    new_tool = create_tool(db, tool_data)
    return new_tool


# ----------------------------------------
#    GET /tools/ -> Listar herramientas
# ----------------------------------------
@router.get("/{tool_id}", response_model=ToolResponse)
def get_tool(tool_id: int, db: Session = Depends(get_db)):
    """
    Obtiene una herramienta por su ID.
    Lanza error 401 si no existe.
    """
    tool = get_tool_by_id(db, tool_id)
    if not tool:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La herramienta con ID {tool_id} no existe."
        )
    return tool


# ----------------------------------------------------
#    PUT /tools/{tool_id} -> Actualizar herramienta
# ----------------------------------------------------
@router.put("/{tool_id}", response_model=ToolResponse)
def update_existing_tool(tool_id: int, update_data: ToolUpdate, db: Session = Depends(get_db)):
    """
    Actualiza los datos de una herramienta existente.
    Si la herramienta no existe -> 404.
    """
    db_tool = get_tool_by_id(db, tool_id)
    if not db_tool:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No existe una herramienta con ID {tool_id}."
        )
    
    updated_tool = update_tool(db, db_tool, update_data)
    return updated_tool


# -----------------------------------------------------
#    DELETE /tools/{tool_id} -> Eliminar herramienta
# -----------------------------------------------------
@router.delete("/{tool_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_tool(tool_id: int, db: Session = Depends(get_db)):
    """
    Elimina una herramienta de la base de datos.
    Si no existe -> 404.
    """
    db_tool = get_tool_by_id(db, tool_id)
    if not db_tool:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No existe una herramienta con ID {tool_id}."
        )
    
    delete_tool(db, db_tool)
    return None
