from dataclasses import dataclass

@dataclass
class Book:
    id: int
    title: str
    author: str
@dataclass
class User:
    id: int
    username: str
    password: str 
