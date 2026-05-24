from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from src.routes.usuarios import router as usuarios_router

app = FastAPI(
    title="StudySync API",
    description="API REST para la plataforma StudySync — gestión de usuarios",
    version="1.0.0",
)

app.include_router(usuarios_router, prefix="/api")

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": "Error interno del servidor", "detalle": str(exc)},
    )

@app.get("/")
def root():
    return {"mensaje": "Bienvenido a StudySync API", "docs": "/docs"}