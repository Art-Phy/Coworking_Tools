
### 🛠 Coworking Tools API — v1.0.0

Sistema profesional para gestión de herramientas compartidas en espacios coworking.  
Incluye **reservas en tiempo real**, validación anti-solapamiento, roles Admin/User y seguridad con **JWT**.

---

### 🚀 Tecnologías principales

| Tecnología | Uso |
|----------|------|
| FastAPI + Uvicorn | API backend |
| SQLAlchemy + Alembic | ORM + Migraciones |
| Pydantic v2 | Validación y respuestas |
| JWT + OAuth2 | Autenticación segura |
| Logging + RotatingLog | Monitorización |

---

### 📦 Instalación

```bash
git clone https://github.com/Art-Phy/Coworking_Tools.git
cd Coworking_Tools
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

▶ Ejecución del servidor

```bash
fastapi dev app/main.py --reload
```

Documentación disponible:

| URL | Uso |
|-----|-----|
| http://localhost:8000/docs | Swagger principal |
| http://localhost:8000/redoc | Documentación alternativa |
| http://localhost:8000/health | Healthcheck live |

---

### 🔐 Seguridad & Roles

| Tipo usuario | Puede |
|-------------|--------|
| **User** | Reservar, usar herramientas, gestionar sus reservas |
| **Admin** | Ver todo, modificar todo, borrar todo |

Token requerido:

```
Authorization: Bearer <TOKEN>
```

---

### Endpoints principales

| Módulo | Rutas |
|-------|--------|
| Users | `/users/`, `/users/{id}` |
| Tools | `/tools/`, `/tools/{id}` |
| Reservations | `/reservations/`, `/reservations/user/{id}` |
| Auth Login | `/auth/login` (Form Data) |

---

## 📄 Changelog completo
Disponible en `CHANGELOG.md`.

---

### 🏁 Estado final del proyecto

| Módulo | Estado |
|--------|--------|
| Usuarios | ✔ Completado |
| Herramientas | ✔ CRUD + Gestión |
| Reservas | ✔ Anti-solapamiento completo |
| JWT | ✔ Login + Tokens válidos |
| Permisos | ✔ Roles Admin & User |
| v1.0.0 Stable | 🔥 Lanzamiento oficial |

---

#### Autor  
**Arturo Sanma**  
📩 Contacto y portfolio en GitHub
