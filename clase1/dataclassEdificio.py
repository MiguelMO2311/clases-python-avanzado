from dataclasses import dataclass, field
from typing import List


def nombre_piso(piso: int, piso_alto: int) -> str:
    """
    Convierte un número de piso en su representación según las convenciones.
    """
    match piso:
        case _ if piso < 0:
            return f"S{abs(piso)}"   # Sótano
        case 0:
            return "B"               # Bajo
        case 1:
            return "E"               # Entreplanta
        case _ if piso == piso_alto:
            return "A"               # Azotea
        case _:
            return str(piso)         # Piso normal


@dataclass
class Edificio:
    piso_base: int
    piso_alto: int
    plantas: List[str] = field(init=False)  # se calcula en __post_init__

    def __post_init__(self):
        """
        Genera la lista de plantas usando la función auxiliar `nombre_piso`.
        """
        self.plantas = [
            nombre_piso(piso, self.piso_alto)
            for piso in range(self.piso_base, self.piso_alto + 1)
        ]


# Ejemplo de uso
if __name__ == "__main__":
    inst = Edificio(-2, 5)
    print(inst.plantas)

