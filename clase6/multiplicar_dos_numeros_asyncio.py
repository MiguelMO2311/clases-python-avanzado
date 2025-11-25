import asyncio
from typing import TypeVar, Tuple

T = TypeVar("T", int, float)

async def multiplicar(a: T, b: T) -> Tuple[T, T, T]:
    """
    Multiplica dos números de tipo T y devuelve una tupla (a, b, resultado).
    """
    return a, b, a * b

async def main(pares: list[Tuple[T, T]]):
    """
    Recibe una lista de pares y lanza tareas asíncronas para multiplicarlos.
    """
    # Crear tareas automáticamente
    tareas = [asyncio.create_task(multiplicar(a, b)) for a, b in pares]

    # Esperar a todas las tareas y recoger resultados
    resultados = await asyncio.gather(*tareas)

    # Mostrar resultados
    for a, b, resultado in resultados:
        print(f"{a} x {b} = {resultado}")

if __name__ == "__main__":
    # Aquí decides qué pares pasarle a main()
    pares = [(3, 4), (5, 6), (7, 8), (9, 10)]
    asyncio.run(main(pares))
