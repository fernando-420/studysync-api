import redis
import json
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL")
sub = redis.Redis(
    host="master-stinkbug-135566.upstash.io",
    port=6379,
    password="gQAAAAAAAhGOAAIgcDJmOGNhZjExMjRiNmQ0NjJjOTBlNjkxNDQxYzZiZjQyNg",
    ssl=True,
    decode_responses=True
)
def manejar_sesion_creada(payload):
    print(f"  📚 Nueva sesión de estudio creada!")
    print(f"     Materia:     {payload['materia']}")
    print(f"     Organizador: {payload['organizador']}")
    print(f"     Fecha:       {payload['fecha']} a las {payload['hora']}")

def manejar_usuario_unido(payload):
    print(f"  👤 Usuario se unió a un grupo!")
    print(f"     Usuario: {payload['usuario']}")
    print(f"     Grupo:   {payload['grupo']}")
    print(f"     Sesión:  #{payload['sesion_id']}")

print("=== StudySync — Suscriptor iniciado ===")
print("=== Escuchando canales: study:* ===\n")

pubsub = sub.pubsub()
pubsub.psubscribe("study:*")

for mensaje in pubsub.listen():
    if mensaje["type"] == "pmessage":
        canal = mensaje["channel"]
        datos = json.loads(mensaje["data"])
        
        ahora = datetime.utcnow().strftime("%H:%M:%S")
        print(f"[{ahora}] MENSAJE RECIBIDO")
        print(f"  Canal:   {canal}")
        print(f"  Tipo:    {datos['tipo']}")
        print(f"  Version: {datos['version']}")

        if datos["tipo"] == "SESION_CREADA":
            manejar_sesion_creada(datos["payload"])
        elif datos["tipo"] == "USUARIO_UNIDO":
            manejar_usuario_unido(datos["payload"])

        print()