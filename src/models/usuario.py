from pydantic import BaseModel, EmailStr

# Lo que se envía para registrarse (POST /auth/register)
class UsuarioRegister(BaseModel):
    nombre: str
    email: EmailStr
    password: str
    carrera: str
    semestre: int

# Lo que se envía para iniciar sesión (POST /auth/login)
class UsuarioLogin(BaseModel):
    email: EmailStr
    password: str

# Lo que responde la API (Ocultando la contraseña por seguridad)
class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    email: str
    carrera: str
    semestre: int

    class Config:
        from_attributes = True


class Usuario(BaseModel):
    id: int
    nombre: str
    email: str
    carrera: str
    semestre: int
    # Nuevo esquema para cuando se actualicen datos (PUT /usuarios/{id})
# Ponemos los campos opcionales (con None) o requeridos según prefieras
class UsuarioUpdate(BaseModel):
    nombre: str | None = None
    carrera: str | None = None
    semestre: int | None = None