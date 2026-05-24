from pydantic import BaseModel
from typing import Optional


class UsuarioCreate(BaseModel):
    nombre: str
    email: str
    carrera: str
    semestre: int


class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = None
    email: Optional[str] = None
    carrera: Optional[str] = None
    semestre: Optional[int] = None


class Usuario(BaseModel):
    id: int
    nombre: str
    email: str
    carrera: str
    semestre: int