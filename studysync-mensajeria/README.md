# StudySync Mensajería — Redis Pub/Sub

Sistema de notificaciones en tiempo real usando Redis Pub/Sub con Upstash.

## Canales implementados

| Canal | Evento | Descripción |
|-------|--------|-------------|
| `study:sesion:creada` | SESION_CREADA | Notifica cuando se crea una sesión |
| `study:usuario:unido` | USUARIO_UNIDO | Notifica cuando alguien se une a un grupo |

## Estructura del mensaje

```json
{
  "tipo": "SESION_CREADA",
  "payload": { ... },
  "timestamp": "2026-05-25T21:45:07",
  "version": "1.0"
}
```

## Cómo ejecutar

Terminal 1 — Suscriptor (arrancar primero):
```bash
python subscriber.py
```

Terminal 2 — Publicador:
```bash
python publisher.py
```