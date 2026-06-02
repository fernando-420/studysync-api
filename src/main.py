from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware  # ¡NUEVO!: Para la seguridad CORS
from src.routes.usuarios import router as usuarios_router
from src.routes.auth import router as auth_router  # ¡NUEVO!: Importamos las rutas de registro/login

app = FastAPI(
    title="StudySync API",
    description="API REST segura con JWT y documentación profesional integrada — StudySync",
    version="1.0.0",
)

# =================================================================
# MEDIDA DE SEGURIDAD ADICIONAL: Configuración de CORS
# =================================================================
# Define qué dominios externos pueden consumir tu API. 
# Evitamos usar "*" en allow_origins para cumplir con estándares de producción.
origins = [
    "http://localhost:3000",        # Tu entorno de desarrollo local (Frontend)
    "http://127.0.0.1:3000",
    # "https://tu-app-frontend.render.com" <-- Descomenta y pon tu URL real de frontend si tienes una
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, PUT, DELETE)
    allow_headers=["*"],  # Permite todas las cabeceras (incluyendo Authorization para el Token)
)

# =================================================================
# REGISTRO DE ROUTERS (Rutas de la API)
# =================================================================
# 1. Rutas públicas de autenticación (/auth/register y /auth/login)
app.include_router(auth_router) 

# 2. Rutas de negocio (/api/usuarios) protegidas con JWT
app.include_router(usuarios_router, prefix="/api")


# =================================================================
# MANEJADOR GLOBAL DE EXCEPCIONES
# =================================================================
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": "Error interno del servidor", "detalle": str(exc)},
    )

# =================================================================
# RUTA INICIAL (Root)
# =================================================================
@app.get("/")
def root():
    return {
        "mensaje": "Bienvenido a la versión segura de StudySync API",
        "version": "1.0.0",
        "docs": "/docs",
        "endpoints": {
            "autenticacion": ["/auth/register", "/auth/login"],
            "privados": "/api/usuarios"
        }
    }