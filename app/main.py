
from fastapi import FastAPI

# Routers
from app.api.routers.health import router as health_router
from app.api.routers.tools import router as tools_router
from app.api.routers.users import router as users_router
from app.api.routers.reservations import router as reservations_router
from app.api.routers.auth import router as auth_router

# Logging
from app.core.logging_config import init_logging


# ========================================================
#                   APLICACIÓN PRINCIPAL
# ========================================================
app = FastAPI(
    title="Coworking Tools API",
    description="Sistema completo de gestión de herramientas compartidas en espacios coworking. ✔ Users + ✔ Tools + ✔ Reservations + 🔐 JWT + 🛂 Roles admin.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)



# ========================================================
#                        STARTUP
# ========================================================
@app.on_event("startup")
def startup_event():
    """Se ejecuta automáticamente al iniciar el servidor."""
    init_logging()     # <<< Logging profesional activado
    print("\n🚀 API iniciada correctamente con LOGGING habilitado\n")


# ========================================================
#                       ROUTERS
# ========================================================
app.include_router(health_router)
app.include_router(tools_router)
app.include_router(users_router)
app.include_router(reservations_router)
app.include_router(auth_router)


# ========================================================
#                      ENDPOINTS BASE
# ========================================================
@app.get("/health")
def health_check():
    """Para comprobar que la API está viva."""
    return {"status": "ok"}


@app.get("/")
def root():
    """Pantalla de presentación de la API."""
    return {
        "message": "Bienvenido a la Shared Tools Reservation API",
        "docs_url": "/docs",
        "health_url": "/health",
        "version": "1.0.0",
    }
