from pydantic import BaseModel, EmailStr

class UsuarioRegister(BaseModel):
    nombre: str
    email: EmailStr
    password: str
    carrera: str
    semestre: int

class UsuarioLogin(BaseModel):
    email: EmailStr
    password: str

class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    email: str
    carrera: str
    semestre: int

    class Config:
        from_attributes = True