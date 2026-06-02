from sqlalchemy.orm import Session
from src.models.db_models import Usuario
# CAMBIO AQUÍ: Importamos UsuarioRegister con el alias UsuarioCreate para no romper tu código de abajo
from src.models.usuario import UsuarioRegister as UsuarioCreate, UsuarioUpdate
import redis
import json
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL")
pub = redis.Redis(
    host="master-stinkbug-135566.upstash.io",
    port=6379,
    password="gQAAAAAAAhGOAAIgcDJmOGNhZjExMjRiNmQ0NjJjOTBlNjkxNDQxYzZiZjQyNg",
    ssl=True,
    decode_responses=True
)


def publicar_evento(canal, tipo, payload):
    mensaje = {
        "tipo": tipo,
        "payload": payload,
        "timestamp": datetime.utcnow().isoformat(),
        "version": "1.0"
    }
    pub.publish(canal, json.dumps(mensaje))


def obtener_todos(db: Session):
    return db.query(Usuario).all()


def obtener_por_id(usuario_id: int, db: Session):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()


def crear(datos: UsuarioCreate, db: Session):
    nuevo = Usuario(
        nombre=datos.nombre,
        email=datos.email,
        carrera=datos.carrera,
        semestre=datos.semestre
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    publicar_evento(
        canal="study:usuario:creado",
        tipo="USUARIO_CREADO",
        payload={
            "id": nuevo.id,
            "nombre": nuevo.nombre,
            "email": nuevo.email,
            "carrera": nuevo.carrera,
            "semestre": nuevo.semestre
        }
    )
    return nuevo


def actualizar(usuario_id: int, datos: UsuarioUpdate, db: Session):
    usuario = obtener_por_id(usuario_id, db)
    if not usuario:
        return None
    cambios = datos.model_dump(exclude_unset=True)
    for campo, valor in cambios.items():
        setattr(usuario, campo, valor)
    db.commit()
    db.refresh(usuario)
    return usuario


def eliminar(usuario_id: int, db: Session):
    usuario = obtener_por_id(usuario_id, db)
    if not usuario:
        return False
    db.delete(usuario)
    db.commit()
    return True