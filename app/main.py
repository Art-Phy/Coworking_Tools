
from fastapi import FastAPI
from app.api.routers.health import router as health_router
from app.api.routers.tools import router as tools_router
from app.api.routers.users import router as users_router
from app.api.routers.reservations import router as reservations_router


# fastapi dev app/main.py --reload  

app = FastAPI(
    title="Coworking Tools API",
    description="API para gestionar usuarios, herramientas y reservas.",
    version="0.3.0", # Informativa a nivel de documentación FastAPI
)


# Incluir routers
app.include_router(health_router)
app.include_router(tools_router)
app.include_router(users_router)
app.include_router(reservations_router)


@app.get("/health")
def health_check():
    """
    Endpoint sencillo para comprobar que la API está viva.

    En producción, este tipo de endpoint suele usarse por sistemas de monitorización
    o balanceadores de carga para verificar que el servicio está funcionando.
    """
    return {"status": "ok"}

@app.get("/")
def root():
    """
    Endpoint raíz de bienvenida.

    Este endpoint no es estrictamente necesario, pero es útil mientras desarrollamos
    para ver rápidamente que la API responde yu para mostrar una pequeña descripción.
    """
    return{
        "message": "Bienvenido a la Shared Tools Reservation API",
        "docs_url": "/docs",
        "health_url": "/health",
    }
