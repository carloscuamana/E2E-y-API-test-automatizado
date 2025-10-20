
from sender_stand_reques import *


def test_crear_usuario():
    response = crear_usuario()
    assert response.status_code == 200
    print(response)
def test_buscar_usuario():
    response = get_usuario_consulta (USERNAME)
    assert response.status_code == 200
    assert response.json().get("firstName") == "name"
    print(response)
def test_update_usuario():
    response = update_usuario(USERNAME, update_user_body)
    assert response.status_code == 200
    print(response)
def test_buscar_usuario_actualizado():
    response = get_usuario_consulta (USERNAME)
    assert response.status_code == 200
    assert response.json().get("firstName") == "nombre"
    print(response)
def test_eliminar_usuario():
    response = borrar_usuario(USERNAME)
    assert response.status_code == 200
    print(response)
