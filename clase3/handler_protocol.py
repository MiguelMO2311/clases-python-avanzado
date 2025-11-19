from typing import Protocol, TypeVar

# Definimos tipos genéricos para entrada y salida
T_in = TypeVar("T_in")
T_out = TypeVar("T_out")

class EventHandler(Protocol[T_in, T_out]):
    def handle(self, event: T_in) -> T_out:
        ...
        
# Ejemplo de implementación: recibe un str y devuelve un int
class LengthHandler:
    def handle(self, event: str) -> int:
        return len(event)

# Otro ejemplo: recibe un número y devuelve un string
class NumberToStringHandler:
    def handle(self, event: int) -> str:
        return f"El numero es {event}"

# Función que usa el protocolo
def process_event(handler: EventHandler[T_in, T_out], event: T_in) -> T_out:
    return handler.handle(event)

# Ejemplos de uso
h1 = LengthHandler()
print(process_event(h1, "Hola mundo"))   # 10

h2 = NumberToStringHandler()
print(process_event(h2, 42))            
