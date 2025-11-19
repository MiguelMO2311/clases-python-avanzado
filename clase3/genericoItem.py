from typing import TypeVar

T = TypeVar("T")

def get_size(item: T) -> int:
    return len(item)

# Ejemplos
print(get_size("Hola"))       # 4
print(get_size([1, 2, 3]))    # 3
print(get_size({1, 2, 3, 4})) # 4
