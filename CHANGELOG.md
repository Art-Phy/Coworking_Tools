
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

### [v0.2.0] - 2025-xx-xx
#### 🚀 Añadido
- Creación de los modelos principales del dominio usando SQLAlchemy:
  - `User`
  - `Tool`
  - `Reservation`
- Configuración completa y profesional de Alembic:
  - Integración con `settings.DATABASE_URL`
  - Importación automática de metadatos
  - Modo `online` y `offline`
  - Compatible con SQLite en desarrollo
- Generación de la migración inicial:
  - `users`
  - `tools`
  - `reservations`
- Creación de la base mediante `alembic upgrade head`

---

### [v0.3.0] - 2025-xx-xx
#### 🚀 Añadido
- Schemas Pydantic para Tools:
  - `ToolBase`, `ToolCreate`, `ToolUpdate`, `ToolResponse`
- CRUD completo de herramientas usando SQLAlchemy 2.0:
  - `get_tool_by_id`
  - `get_all_tools`
  - `create_tool`
  - `update_tool`
  - `delete_tool`
- Router REST para herramientas:
  - `POST /tools/`
  - `GET /tools/`
  - `GET /tools/{id}`
  - `PUT /tools/{id}`
  - `DELETE /tools/{id}`
- Integración del router de Tools en `main.py`.
- Documentación automática en OpenAPI.

### 🛠 Mejorado
- Validación y manejo de errores con `HTTPException`.
- Actualización parcial de modelos usando `exclude_unset=True`.

### 🧪 Probado
- Endpoints probados correctamente con Thunder Client.
- Casos normales: creación, consulta, actualización y borrado.

---

### ⭐ Notas
- Este proyecto sigue GitFlow:  
`main` → versiones estables  
`develop` → trabajo integrado  
`feature/...` → desarrollo modular  
- Cada release estable estará asociada a un tag (`vX.Y.Z`).
