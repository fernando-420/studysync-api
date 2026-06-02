from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.database.connection import get_db
from src.models.db_models import Usuario
from src.schemas.usuarios import UsuarioRegister, UsuarioLogin, UsuarioResponse
from src.auth.jwt_handler import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Autenticación"])

@router.post("/register", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED, description="Registra un nuevo usuario estudiante")
def register(usuario_in: UsuarioRegister, db: Session = Depends(get_db)):
    # Control de duplicados
    existe = db.query(Usuario).filter(Usuario.email == usuario_in.email).first()
    if existe:
        raise HTTPException(status_code=400, detail="El email ya está registrado")
    
    nuevo_usuario = Usuario(
        nombre=usuario_in.nombre,
        email=usuario_in.email,
        password=hash_password(usuario_in.password), # Guardamos el Hash seguro
        carrera=usuario_in.carrera,
        semestre=usuario_in.semestre
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

@router.post("/login", description="Inicia sesión y obtiene un token JWT")
def login(usuario_in: UsuarioLogin, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.email == usuario_in.email).first()
    if not usuario or not verify_password(usuario_in.password, usuario.password):
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    
    token = create_access_token(data={"sub": usuario.email, "id": usuario.id})
    return {"access_token": token, "token_type": "bearer"}