import pytest
from closure_mayorEdad import validador_mayoria_edad

# Fixture: crea un validador con edad mínima 18
@pytest.fixture
def validador_18():
    return validador_mayoria_edad(18)

# Test: comprobar que funciona con distintos valores
@pytest.mark.parametrize("edad, esperado", [
    (17, False),   # menor de edad
    (18, True),    # justo en el límite
    (25, True),    # claramente mayor
])
def test_validador_mayoria_edad(validador_18, edad, esperado):
    assert validador_18(edad) == esperado

# Test: otro closure con edad mínima distinta
def test_validador_21():
    validador_21 = validador_mayoria_edad(21)
    assert validador_21(20) is False
    assert validador_21(21) is True
    assert validador_21(30) is True
