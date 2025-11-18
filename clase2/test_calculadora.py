import pytest
from calculadora import Calculadora

@pytest.fixture
def calc():
    # Se crea una nueva calculadora para cada test
    return Calculadora()

def test_inicializacion(calc):
    assert calc.valor == 0

def test_sumar(calc):
    assert calc.sumar(5) == 5
    assert calc.sumar(3) == 8

def test_reset(calc):
    calc.sumar(10)
    calc.reset()
    assert calc.valor == 0
