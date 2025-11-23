
from fastapi import FastAPI

# primera instancia de FastAPI
app = FastAPI(
    title="Shared Tools Reservation API",
    description="API para gestionar la reserva de herramientas compartidas en un makerspace.",
    version="0.1.0", # Informativa a nivel de documentación FastAPI
)


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
