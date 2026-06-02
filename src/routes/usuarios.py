from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.models.usuario import UsuarioCreate, UsuarioUpdate
from src.controllers import usuarios_controller as ctrl
from src.database.connection import get_db
# ¡NUEVO!: Importamos el validador del token JWT
from src.auth.jwt_handler import get_current_user 

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


@router.get("", status_code=200, description="Listar usuarios (Requiere autenticación JWT)")
def listar_usuarios(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    """
    Ruta protegida. Si no envían el token Bearer válido, 
    FastAPI responderá automáticamente un error 401.
    """
    usuarios = ctrl.obtener_todos(db)
    return {"total": len(usuarios), "usuarios": usuarios}


@router.get("/{usuario_id}", status_code=200, description="Obtener un usuario por ID (Requiere autenticación JWT)")
def obtener_usuario(usuario_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    usuario = ctrl.obtener_por_id(usuario_id, db)
    if not usuario:
        raise HTTPException(status_code=404, detail=f"Usuario con id {usuario_id} no encontrado")
    return usuario


@router.post("", status_code=201, description="Crear usuario administrador (Requiere autenticación JWT)")
def crear_usuario(datos: UsuarioCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    if not datos.nombre or not datos.email or not datos.carrera:
        raise HTTPException(status_code=400, detail="Faltan campos obligatorios: nombre, email, carrera")
    nuevo = ctrl.crear(datos, db)
    return {"mensaje": "Usuario creado exitosamente", "usuario": nuevo}


@router.put("/{usuario_id}", status_code=200, description="Actualizar un usuario (Requiere autenticación JWT)")
def actualizar_usuario(usuario_id: int, datos: UsuarioUpdate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    actualizado = ctrl.actualizar(usuario_id, datos, db)
    if not actualizado:
        raise HTTPException(status_code=404, detail=f"Usuario con id {usuario_id} no encontrado")
    return {"mensaje": "Usuario actualizado exitosamente", "usuario": actualizado}


@router.delete("/{usuario_id}", status_code=200, description="Eliminar un usuario (Requiere autenticación JWT)")
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    eliminado = ctrl.eliminar(usuario_id, db)
    if not eliminado:
        raise HTTPException(status_code=404, detail=f"Usuario con id {usuario_id} no encontrado")
    return {"mensaje": f"Usuario con id {usuario_id} eliminado exitosamente"}