import pytest
from functools import wraps
from io import StringIO
import sys

# Importamos el decorador y la función a probar
from decorador_login_retry import login, conexion_bd


def test_conexion_valida(capsys):
    # Caso válido: debe ejecutar la función y devolver None (porque conexion_bd no retorna nada)
    resultado = conexion_bd("Miguel", valido=True)
    captured = capsys.readouterr()

    # Verificamos que se imprimen los mensajes esperados
    assert "El rol del usuario es: admin" in captured.out
    assert "He entrado en mi función: conexion_bd" in captured.out
    assert "Intento #1 de login..." in captured.out
    assert "El usuario Miguel ha accedido a base de datos" in captured.out

    # La función no devuelve nada explícito → resultado es None
    assert resultado is None


def test_conexion_invalida(capsys):
    # Caso inválido: debe intentar 3 veces y luego denegar acceso
    resultado = conexion_bd("Maria", valido=False)
    captured = capsys.readouterr()

    # Verificamos que se imprimen los intentos y el mensaje de denegación
    assert "El rol del usuario es: admin" in captured.out
    assert "He entrado en mi función: conexion_bd" in captured.out
    assert "Intento #1 de login..." in captured.out
    assert "Intento #2 de login..." in captured.out
    assert "Intento #3 de login..." in captured.out
    assert "Credenciales inválidas." in captured.out
    assert "Acceso denegado tras 3 intentos." in captured.out

    # La función devuelve None porque no se logró validar
    assert resultado is None


def test_login_decorador_personalizado(capsys):
    # Creamos una función decorada con rol distinto y menos intentos
    @login("tester", max_retries=2)
    def dummy(*, valido):
        return "OK"

    # Caso válido
    resultado = dummy(valido=True)
    captured = capsys.readouterr()
    assert resultado == "OK"
    assert "El rol del usuario es: tester" in captured.out
    assert "Intento #1 de login..." in captured.out

    # Caso inválido
    resultado = dummy(valido=False)
    captured = capsys.readouterr()
    assert resultado is None
    assert "Acceso denegado tras 2 intentos." in captured.out
