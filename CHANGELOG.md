
## 📘 Changelog
Todas las novedades, cambios y mejoras del proyecto **Coworking Tools API** se documentan aquí.

Este archivo sigue el formato recomendado por [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/)  
y la numeración de versiones basada en [Semantic Versioning](https://semver.org/lang/es/).

---

### [v0.1.0] - 2025-xx-xx
#### 🚀 Añadido
- Creación de la estructura profesional del proyecto con FastAPI.
- Configuración inicial de SQLAlchemy (engine, sesión y declarative base).
- Archivo `config.py` con `Settings` usando `pydantic-settings`.
- Inclusión de `.env` y `.gitignore` adaptado.
- Enrutador modular inicial (`/health/`) para comprobación de estado.
- Configuración del servidor de desarrollo moderno mediante `fastapi dev`.


---

### [Sin publicar]
#### 🚧 En progreso
- Modelos principales (`User`, `Tool`, `Reservation`).
- Configuración inicial de Alembic para migraciones.
- Preparación para la versión **v0.2.0**.

---

### ⭐ Notas
- Este proyecto sigue GitFlow:  
`main` → versiones estables  
`develop` → trabajo integrado  
`feature/...` → desarrollo modular  
- Cada release estable estará asociada a un tag (`vX.Y.Z`).
