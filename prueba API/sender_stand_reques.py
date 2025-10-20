import requests
from configuracion import *
from data import *


def crear_usuario():
    return requests.post(BASE_URL + "/user", json=new_user_body)

def get_usuario_consulta(USERNAME):
    return requests.get(BASE_URL + "/user/" + USERNAME )

def update_usuario(USERNAME, update_user_body):
    return requests.put(BASE_URL + "/user/" + USERNAME, json=update_user_body)

def borrar_usuario(USERNAME):
    return requests.delete(BASE_URL + "/user/" + USERNAME)