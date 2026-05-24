from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_listar_usuarios():
    response = client.get("/api/usuarios")
    assert response.status_code == 200
    assert "usuarios" in response.json()


def test_crear_usuario():
    response = client.post("/api/usuarios", json={
        "nombre": "Test Usuario",
        "email": "test_pytest@upds.edu.bo",
        "carrera": "Ingeniería de Sistemas",
        "semestre": 1
    })
    assert response.status_code == 201
    assert response.json()["usuario"]["nombre"] == "Test Usuario"


def test_usuario_no_encontrado():
    response = client.get("/api/usuarios/99999")
    assert response.status_code == 404


def test_crear_usuario_campos_vacios():
    response = client.post("/api/usuarios", json={
        "nombre": "",
        "email": "test@upds.edu.bo",
        "carrera": "Ingeniería de Sistemas",
        "semestre": 1
    })
    assert response.status_code == 400


def test_eliminar_usuario_inexistente():
    response = client.delete("/api/usuarios/99999")
    assert response.status_code == 404