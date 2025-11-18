from dataclasses import dataclass, field
from collections import deque
from typing import Any

@dataclass
class Cola:
    _cola: deque = field(default_factory=deque)

    def añadir_tarea(self, tarea: Any) -> None:
        """Añade una tarea al final de la cola."""
        self._cola.append(tarea)

    def siguiente_tarea(self) -> Any:
        """Devuelve y elimina la siguiente tarea en la cola."""
        if self._cola:
            return self._cola.popleft()
        return None

    def tareas_pendientes(self) -> int:
        """Devuelve el número de tareas pendientes."""
        return len(self._cola)

    def __str__(self) -> str:
        """Representación legible de la cola."""
        return f"Cola(pendientes={len(self._cola)})"
    
# Ejemplo de uso
    
if __name__ == "__main__":
    cola = Cola()

    cola.añadir_tarea("procesar_imagen")
    cola.añadir_tarea("backup")
    cola.añadir_tarea("exportar_pdf")

    print(cola)  # Cola(pendientes=3)

    print(cola.siguiente_tarea())  # procesar_imagen
    print(cola.siguiente_tarea())  # backup

    print(cola)  # Cola(pendientes=1)


