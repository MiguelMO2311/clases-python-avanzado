from cuenta_palabras import contar_texto

def test_smoke():
    texto = "Hola mundo\nPython 123\n"

    words, letters = contar_texto(texto)

    assert words == 4
    assert letters == 15  # corregido
