from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)


@router.get("/")
def health_check():
    """
    Devuelve un estado básico de la API.
    Este endpoint se usa comúnmente en despliegues para monitoreo.
    """
    return {"status": "ok"}
