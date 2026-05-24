import redis
import json
import time
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
def publicar(canal, tipo, payload):
    mensaje = {
        "tipo": tipo,
        "payload": payload,
        "timestamp": datetime.utcnow().isoformat(),
        "version": "1.0"
    }
    pub.publish(canal, json.dumps(mensaje))
    print(f"[PUBLICADO] Canal: {canal} | Tipo: {tipo}")
    print(f"  Datos: {payload}\n")

print("=== StudySync — Publicador iniciado ===\n")

# Canal 1: sesion creada
publicar(
    canal="study:sesion:creada",
    tipo="SESION_CREADA",
    payload={
        "sesion_id": 1,
        "materia": "Programación IV",
        "organizador": "Fernando Montero",
        "fecha": "2026-05-25",
        "hora": "19:00"
    }
)

time.sleep(2)

# Canal 2: usuario unido a grupo
publicar(
    canal="study:usuario:unido",
    tipo="USUARIO_UNIDO",
    payload={
        "usuario": "Ana Quispe",
        "grupo": "Grupo Prog IV",
        "sesion_id": 1
    }
)

time.sleep(2)

# Canal 1 de nuevo: otra sesion
publicar(
    canal="study:sesion:creada",
    tipo="SESION_CREADA",
    payload={
        "sesion_id": 2,
        "materia": "Base de Datos",
        "organizador": "Carlos Mamani",
        "fecha": "2026-05-26",
        "hora": "20:00"
    }
)

print("=== Todos los mensajes publicados ===")