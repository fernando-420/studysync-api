from fastapi import APIRouter, HTTPException
from src.models.usuario import UsuarioCreate, UsuarioUpdate
from src.controllers import usuarios_controller as ctrl

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


@router.get("", status_code=200)
def listar_usuarios():
    usuarios = ctrl.obtener_todos()
    return {"total": len(usuarios), "usuarios": usuarios}


@router.get("/{usuario_id}", status_code=200)
def obtener_usuario(usuario_id: int):
    usuario = ctrl.obtener_por_id(usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail=f"Usuario con id {usuario_id} no encontrado")
    return usuario


@router.post("", status_code=201)
def crear_usuario(datos: UsuarioCreate):
    nuevo = ctrl.crear(datos)
    return {"mensaje": "Usuario creado exitosamente", "usuario": nuevo}


@router.put("/{usuario_id}", status_code=200)
def actualizar_usuario(usuario_id: int, datos: UsuarioUpdate):
    actualizado = ctrl.actualizar(usuario_id, datos)
    if not actualizado:
        raise HTTPException(status_code=404, detail=f"Usuario con id {usuario_id} no encontrado")
    return {"mensaje": "Usuario actualizado exitosamente", "usuario": actualizado}


@router.delete("/{usuario_id}", status_code=200)
def eliminar_usuario(usuario_id: int):
    eliminado = ctrl.eliminar(usuario_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail=f"Usuario con id {usuario_id} no encontrado")
    return {"mensaje": f"Usuario con id {usuario_id} eliminado exitosamente"}