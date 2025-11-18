import pytest
from json_utils import procesar_json, todo_mayusculas, buscar_error

def test_todo_mayusculas():
    datos = {"mensaje": "hola mundo", "estado": "error"}
    resultado = procesar_json(datos, todo_mayusculas)
    assert resultado["mensaje"] == "HOLA MUNDO"
    assert resultado["estado"] == "ERROR"

def test_buscar_error():
    datos = {"mensaje": "hola mundo", "estado": "ERROR crítico"}
    resultado = procesar_json(datos, buscar_error)
    assert "ERROR crítico" in resultado
