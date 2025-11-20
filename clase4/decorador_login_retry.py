# from functools import wraps

# def login(role: str, max_retries: int = 3) -> callable:
#     def decorador(funcion: callable) -> callable:
#         @wraps(funcion)
#         def wrapper(*args, **kwargs) -> any:
#             print(f"El rol del usuario es: {role}")
#             print(f"He entrado en mi función: {funcion.__name__}")

#             intentos = 0
#             while intentos < max_retries:
#                 intentos += 1
#                 print(f"Intento #{intentos} de login...")

#                 if kwargs.get("valido", False):
#                     return funcion(*args, **kwargs)
#                 else:
#                     print("Credenciales inválidas.")

#             print(f"Acceso denegado tras {max_retries} intentos.")
#             return None
#         return wrapper
#     return decorador


########### Version con TypeVars ##############

import logging
from functools import wraps

# Configuración básica del logger
logging.basicConfig(level=logging.INFO)

class LoginError(Exception):
    """Excepción personalizada para fallos de login."""

def login(role: str, max_retries: int = 3):
    def decorador(funcion):
        @wraps(funcion)
        def wrapper(*args, **kwargs):
            logging.info("El rol del usuario es: %s", role)
            logging.info("He entrado en mi función: %s", funcion.__name__)

            intentos = 0
            while intentos < max_retries:
                intentos += 1
                logging.info("Intento #%s de login...", intentos)

                if kwargs.get("valido", False):
                    return funcion(*args, **kwargs)
                else:
                    logging.warning("Credenciales inválidas.")

            logging.error("Acceso denegado tras %s intentos.", max_retries)
            # Aquí lanzamos una excepción para que quede constancia en traceback
            raise LoginError(f"Acceso denegado tras {max_retries} intentos.")
        return wrapper
    return decorador



# Ejemplo de uso

@login("admin", max_retries=3)
def conexion_bd(usuario: str, *, valido: bool):
    if valido:
        print(f"El usuario {usuario} ha accedido a base de datos")

# Caso válido
conexion_bd("Miguel", valido=True)

print("-" * 40)

# Caso inválido
conexion_bd("Maria", valido=False)


