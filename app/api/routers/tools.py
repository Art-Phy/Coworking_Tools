from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.roles import require_admin
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


# ----------------------------------------------------
#    POST /tools/ -> Crear herramienta (ADMIN ONLY)
# ----------------------------------------------------
@router.post("/", response_model=ToolResponse, status_code=status.HTTP_201_CREATED)
def create_new_tool(
    tool_data: ToolCreate,
    db: Session = Depends(get_db),
    current_user = Depends(require_admin)
):
    """
    Crea una nueva herramienta.

    Roles:
    - Solo usuarios con permiso admin pueden acceder.
    """
    new_tool = create_tool(db, tool_data)
    return new_tool



# --------------------------------------------------
#    GET /tools/ -> Listar todas las herramientas
# --------------------------------------------------
@router.get("/", response_model=list[ToolResponse])
def list_tools(db: Session = Depends(get_db)):
    """
    Devuelve una lista con todas las herramientas registradas.
    Accesible para cualquier usuario (no requiere admin por ahora).
    """
    return get_all_tools(db)



# ----------------------------------------------------
#    GET /tools/{id} -> Obtener herramienta (Todos)
# ----------------------------------------------------
@router.get("/{tool_id}", response_model=ToolResponse)
def get_tool(tool_id: int, db: Session = Depends(get_db)):
    """
    Obtiene una herramienta por ID.
    Disponible para cualquier usuario autenticado o no (por ahora).
    """
    tool = get_tool_by_id(db, tool_id)
    if not tool:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La herramienta con ID {tool_id} no existe."
        )
    return tool


# --------------------------------------------------------
#    PUT /tools/{id} -> Editar herramienta (ADMIN ONLY)
# --------------------------------------------------------
@router.put("/{tool_id}", response_model=ToolResponse)
def update_existing_tool(
    tool_id: int,
    update_data: ToolUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(require_admin)
):
    """
    Actualiza los datos de una herramienta.
    Solo administradores pueden modificar.
    """
    db_tool = get_tool_by_id(db, tool_id)
    if not db_tool:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No existe una herramienta con ID {tool_id}."
        )
    return update_tool(db, db_tool, update_data)


# -------------------------------------------------------------
#    DELETE /tools/{id} -> Eliminar herramienta (ADMIN ONLY)
# -------------------------------------------------------------
@router.delete("/{tool_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_tool(
    tool_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(require_admin)
):
    """
    Elimina una herramienta.
    Solo administradores pueden borrar.
    """
    db_tool = get_tool_by_id(db, tool_id)
    if not db_tool:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No existe una herramienta con ID {tool_id}."
        )
    delete_tool(db, db_tool)
    return None

