from src.models.usuario import UsuarioCreate, UsuarioUpdate
from typing import List

_usuarios = [
    {"id": 1, "nombre": "Ana Quispe", "email": "ana@upds.edu.bo", "carrera": "Ingeniería de Sistemas", "semestre": 5},
    {"id": 2, "nombre": "Carlos Mamani", "email": "carlos@upds.edu.bo", "carrera": "Ingeniería de Sistemas", "semestre": 3},
]
_siguiente_id = 3


def obtener_todos():
    return _usuarios


def obtener_por_id(usuario_id: int):
    return next((u for u in _usuarios if u["id"] == usuario_id), None)


def crear(datos: UsuarioCreate):
    global _siguiente_id
    nuevo = {"id": _siguiente_id, **datos.model_dump()}
    _usuarios.append(nuevo)
    _siguiente_id += 1
    return nuevo


def actualizar(usuario_id: int, datos: UsuarioUpdate):
    usuario = obtener_por_id(usuario_id)
    if not usuario:
        return None
    cambios = datos.model_dump(exclude_unset=True)
    usuario.update(cambios)
    return usuario


def eliminar(usuario_id: int):
    global _usuarios
    original = len(_usuarios)
    _usuarios = [u for u in _usuarios if u["id"] != usuario_id]
    return len(_usuarios) < original