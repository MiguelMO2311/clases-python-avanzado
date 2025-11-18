import pytest
from usuario import Usuario
from hypothesis import given, strategies as st

# Fixture: usuario base para reutilizar en varios tests
@pytest.fixture
def usuario_base():
    return Usuario("Miguel", 50)

# Marks: inicialización
@pytest.mark.inicializacion
def test_inicializacion(usuario_base):
    assert usuario_base.nombre == "Miguel"
    assert usuario_base.edad == 50

# Parametrize: comprobar es_adulto con distintos valores
@pytest.mark.parametrizar
@pytest.mark.parametrize("edad, esperado", [
    (0, False),
    (17, False),
    (18, True),
    (25, True),
])
def test_es_adulto(edad, esperado):
    usuario_prueba = Usuario("Test", edad)
    assert usuario_prueba.es_adulto() == esperado

# Excepciones: prever errores en inicialización y actualización
@pytest.mark.errores
def test_nombre_vacio():
    with pytest.raises(ValueError):
        Usuario("", 20)

@pytest.mark.errores
def test_edad_negativa():
    with pytest.raises(ValueError):
        Usuario("Test", -1)

@pytest.mark.errores
def test_actualizar_nombre_vacio(usuario_base):
    with pytest.raises(ValueError):
        usuario_base.actualizar_nombre("")

# Hypothesis: invariantes generales

# Invariante: edad nunca negativa
@given(
    nombre=st.text(min_size=1).filter(lambda n: n.strip() != ""),
    edad=st.integers(min_value=0, max_value=120)
)
def test_invariante_edad_no_negativa(nombre, edad):
    usuario_generado = Usuario(nombre, edad)
    assert usuario_generado.edad >= 0

# Invariante: consistencia de es_adulto
@given(nombre=st.text(min_size=1), edad=st.integers(min_value=0, max_value=120))
def test_invariante_es_adulto_consistente(nombre, edad):
    usuario_generado = Usuario(nombre, edad)
    assert usuario_generado.es_adulto() == (usuario_generado.edad >= 18)

# Hypothesis: nombres vacíos o inválidos deben fallar
@given(
    nombre=st.text(min_size=1).filter(lambda n: n.strip() != ""), 
    edad=st.integers(min_value=0, max_value=120)
)
def test_invariante_es_adulto_consistente(nombre, edad):
    usuario_generado = Usuario(nombre, edad)
    assert usuario_generado.es_adulto() == (usuario_generado.edad >= 18)
