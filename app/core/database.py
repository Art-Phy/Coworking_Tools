
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# Motor de conexión. Para SQLite se usa connect_args.
engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in settings.DATABASE_URL else {}
)

# Sesión de la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base que heredan todos los modelos
Base = declarative_base()


def get_db():
    """
    Dependencia FastAPI paara obtener una sesión de base de datos.
    Cada petición obtiene una sesión nuevas que se cierra al terminar.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
