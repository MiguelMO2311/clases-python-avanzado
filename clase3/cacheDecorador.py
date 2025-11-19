from functools import wraps

# Decorador @avisar

def avisar(funcion: callable) -> callable:
    
    @wraps(funcion)
    def wrapper(*args, **kwargs):
        print(f"[Aviso] He entrado en la función: {funcion.__name__}")
        resultado = funcion(*args, **kwargs)
        return resultado
    return wrapper

# Decorador @cache

def cache(funcion: callable) -> callable:
    """
    Decorador que guarda en una caché los resultados de la función.
    Si se llama con los mismos argumentos, devuelve el resultado guardado.
    """
    memoria = {}  # closure: guarda input -> output

    @wraps(funcion)
    def wrapper(*args, **kwargs):
        clave = (args, tuple(sorted(kwargs.items())))
        if clave in memoria:
            print(f"[Cache] Recuperado resultado de {funcion.__name__}{args}{kwargs}")
            return memoria[clave]

        resultado = funcion(*args, **kwargs)
        memoria[clave] = resultado
        print(f"[Cache] Guardado resultado de {funcion.__name__}{args}{kwargs}")
        return resultado

    return wrapper

# Ejemplos de uso

@avisar
def sumar(a: int, b: int) -> int:
    return a + b

@avisar
def multiplicar(a: int, b: int) -> int:
    return a * b

@cache
def potencia(base: int, exponente: int) -> int:
    print("Ejecutando cálculo de potencia...")
    return base ** exponente


if __name__ == "__main__":
    # Ejemplo con @avisar
    print(sumar(2, 3))
    print(sumar(10, 5))
    print(multiplicar(4, 6))

    print("-" * 40)

    # Ejemplo con @cache
    print(potencia(2, 3))   # Calcula y guarda
    print(potencia(2, 2))   # Recupera de cache
    print(potencia(3, 2))   # Calcula y guarda
    print(potencia(3, 5))   # Recupera de cache
