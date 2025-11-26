from functools import wraps

def mostrar_nombre(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f" Estoy decorando la función: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@mostrar_nombre
def sumar(a, b):
    return a + b

@mostrar_nombre
def multiplicar(a, b):
    return a * b

if __name__ == "__main__":
   
#   Ejmeplo de uso 
    print(sumar(3, 4))
    print(multiplicar(5, 6))
