# import pytest
# from dictionaryClass import Diccionario

# # Fixture: diccionario vacío
# @pytest.fixture
# def dic_vacio():
#     return Diccionario()

# # Fixture: diccionario con datos iniciales
# @pytest.fixture
# def dic_con_datos():
#     d = Diccionario()
#     d.agregar("nombre", "Miguel")
#     d.agregar("edad", 35)
#     return d

# def test_agregar_y_obtener(dic_vacio):
#     dic_vacio.agregar("nombre", "Miguel")
#     dic_vacio.agregar("edad", 50)
#     assert dic_vacio.obtener("nombre") == "Miguel"
#     assert dic_vacio.obtener("edad") == 50

# def test_sustituir_valor(dic_con_datos):
#     dic_con_datos.agregar("edad", 51)   # sustituye
#     assert dic_con_datos.obtener("edad") == 51

# def test_eliminar(dic_con_datos):
#     dic_con_datos.eliminar("nombre")
#     with pytest.raises(KeyError):
#         dic_con_datos.obtener("nombre")

# def test_update_diccionarios(dic_con_datos):
#     d2 = Diccionario()
#     d2.agregar("edad", 40)   # sobrescribe
#     d2.agregar("ciudad", "Madrid")

#     dic_con_datos.update(d2)   # usar update en lugar de unir
#     assert dic_con_datos.obtener("edad") == 40
#     assert dic_con_datos.obtener("ciudad") == "Madrid"
#     assert dic_con_datos.obtener("nombre") == "Miguel"

# def test_pertenencia(dic_con_datos):
#     assert ("nombre" in dic_con_datos) is True   # usar in en lugar de contiene
#     assert ("ciudad" in dic_con_datos) is False

# def test_claves_valores_items(dic_con_datos):
#     assert dic_con_datos.keys() == ["nombre", "edad"]
#     assert dic_con_datos.values() == ["Miguel", 35]
#     assert dic_con_datos.items() == [("nombre", "Miguel"), ("edad", 35)]

# def test_len_y_clear(dic_con_datos):
#     assert len(dic_con_datos) == 2   # usar len en lugar de tamaño
#     dic_con_datos.clear()            # usar clear en lugar de limpiar
#     assert len(dic_con_datos) == 0
#     assert dic_con_datos.keys() == []
#     assert dic_con_datos.values() == []

# version test del Profe
import pytest
from dictionaryClass import Diccionario

class DicAdapter:
    """
    Adapter para exponer una API:
      - set / get(default) / delete -> True/False
      - contains / length / clear
      - keys / values / items
      - str(...) que imprime con repr de clave y valor
    Internamente usa Diccionario.
    """
    def __init__(self):
        self._d = Diccionario()

    # API de escritura/lectura
    def set(self, key, value):
        self._d.agregar(key, value)

    def get(self, key, default=None):
        try:
            return self._d.obtener(key)
        except KeyError:
            return default

    def delete(self, key):
        try:
            self._d.eliminar(key)
            return True
        except KeyError:
            return False

    # API de consulta/estado
    def contains(self, key):
        return (key in self._d)  # usa __contains__ definido en tu clase

    def length(self):
        return len(self._d)

    def clear(self):
        self._d.clear()

    # Vistas
    def keys(self):
        return self._d.keys()

    def values(self):
        return self._d.values()

    def items(self):
        return self._d.items()

    # Representación como dict usando repr en clave y valor
    def __str__(self):
        pares = [f"{repr(k)}: {repr(v)}" for k, v in self._d.items()]
        return "{" + ", ".join(pares) + "}"


@pytest.fixture
def dic():
    # Usamos el adapter para mantener tu clase intacta
    return DicAdapter()


def test_basico_set_and_get(dic):
    dic.set("a", 1)
    dic.set("b", 2)
    assert dic.get("a") == 1
    assert dic.get("b") == 2


def test_set_sobreescribe(dic):
    dic.set("k", "first")
    dic.set("k", "second")
    assert dic.get("k") == "second"
    assert dic.length() == 1


def test_get_con_missing(dic):
    assert dic.get("noexiste") is None
    guardia = object()
    assert dic.get("noexiste", guardia) is guardia


def test_delete(dic):
    dic.set("x", 10)
    assert dic.delete("x") is True
    assert dic.get("x") is None
    assert dic.delete("x") is False


def test_avanzado_contains_length_clear(dic):
    assert dic.contains("z") is False
    dic.set("z", 99)
    assert dic.contains("z") is True
    assert dic.length() == 1
    dic.clear()
    assert dic.length() == 0
    assert dic.contains("z") is False


def test_llaves_en_orden(dic):
    pares = [("uno", 1), ("dos", 2), ("tres", 3)]
    for key, value in pares:
        dic.set(key, value)
    assert dic.keys() == ["uno", "dos", "tres"]
    assert dic.values() == [1, 2, 3]
    assert dic.items() == pares


def test_items_independientes(dic):
    dic.set("a", [1, 2])
    items = dic.items()
    assert isinstance(items, list)
    assert isinstance(items[0], tuple)
    assert items[0][0] == "a"
    assert items[0][1] == [1, 2]


def test_imprime_como_dict(dic):
    dic.set("a", 1)
    dic.set("b", "test")
    expected = "{" + f"{repr('a')}: {repr(1)}, {repr('b')}: {repr('test')}" + "}"
    assert str(dic) == expected


@pytest.mark.parametrize(
    "key, value",
    [
        ("str", "texto"),
        (123, 456),
        (("tupla",), ("valor",)),
    ],
)
def test_duck_typing(dic, key, value):
    dic.set(key, value)
    assert dic.get(key) == value
    assert dic.contains(key) is True
    assert dic.length() == 1


def test_secuencia_operaciones(dic):
    dic.set("a", 1)
    dic.set("b", 2)
    dic.set("c", 3)
    assert dic.length() == 3
    dic.delete("b")
    assert dic.length() == 2
    assert dic.keys() == ["a", "c"]
    dic.set("a", 10)
    assert dic.get("a") == 10
