# StudySync API — Gestión de Usuarios

API REST construida con Python + FastAPI para la plataforma StudySync.

## Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/api/usuarios` | Listar todos los usuarios |
| GET | `/api/usuarios/{id}` | Obtener usuario por ID |
| POST | `/api/usuarios` | Crear un nuevo usuario |
| PUT | `/api/usuarios/{id}` | Actualizar usuario |
| DELETE | `/api/usuarios/{id}` | Eliminar usuario |

## Instalación local

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn src.main:app --reload
```

## URL de producción

🔗 https://studysync-api-Fernando.onrender.com

## Arquitectura — Actividad 3
Cliente (Thunder Client)
↓ HTTP
API REST (FastAPI)
↓              ↓
Supabase DB    Redis Pub/Sub
(persiste)     (notifica)
↓
Suscriptor
### Por qué Redis además de la BD
Supabase guarda los datos de forma permanente pero no notifica a otros servicios.
Redis Pub/Sub permite que eventos como "usuario creado" lleguen en tiempo real
a cualquier suscriptor sin que la API sepa quién está escuchando.