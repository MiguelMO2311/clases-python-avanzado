from dataclasses import dataclass

@dataclass
class Book:
    id: int
    title: str
    author: str

# Si en el futuro añades usuarios, se podría definir:
# @dataclass
# class User:
#     id: int
#     username: str
#     password_hash: str  # Nota: nunca almacenar contraseñas planas
