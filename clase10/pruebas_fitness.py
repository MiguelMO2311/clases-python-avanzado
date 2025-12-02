def dividir(n1, n2):
    return n1 / n2

def sumar(n1, n2):
    return n1 + n2



from time import time

def fitness_rendimiento(funcion):
    inicio = time()
    for _ in range(10_000_000):
        funcion(1, 1)
    duracion = time() - inicio
    return 1/duracion

def fitness_precision(funcion):
    pruebas = [
        (1, 2, 3),
        (-1, 0, -1),
        (10, -4, 6),
        (3456789, 876543, 4333332)
    ]
    aciertos = 0
    for n1, n2, resultado in pruebas:
        if funcion(n1, n2) == resultado:
            aciertos += 1
    return aciertos / len(pruebas)

from pytest import mark
@mark.parametrize("n1, n2, resultado", [
        (1, 2, 3),
        (-1, 0, -1),
        (10, -4, 6),
        (3456789, 876543, 4333332)
    ])
def test_sumar(n1, n2, resultado):
    assert sumar(n1, n2) == resultado

print(fitness_precision(sumar))