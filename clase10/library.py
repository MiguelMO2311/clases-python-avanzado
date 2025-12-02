from dataclasses import dataclass, asdict
from typing import List, Optional, Protocol
import json, os

DATA_FILE = "books.json"

# --- Modelo con dataclass ---
@dataclass
class Book:
    # Representa un libro con id, título y autor
    id: int
    title: str
    author: str

# --- Interfaz de repositorio (contrato) ---
class BookRepositoryInterface(Protocol):
    # Define las operaciones básicas que debe tener cualquier repositorio de libros
    def list(self) -> List[Book]: ...
    def get(self, book_id: int) -> Optional[Book]: ...
    def create(self, title: str, author: str) -> Book: ...
    def update(self, book_id: int, title: str, author: str) -> Optional[Book]: ...
    def delete(self, book_id: int) -> bool: ...

# --- Implementación concreta con JSON ---
class JsonBookRepository(BookRepositoryInterface):
    def __init__(self, path: str = DATA_FILE):
        # Inicializa el archivo JSON si no existe
        self.path = path
        if not os.path.exists(self.path):
            with open(self.path, "w", encoding="utf-8") as json_file:
                json.dump({"seq": 0, "items": []}, json_file)

    def _load(self):
        # Carga datos desde el archivo JSON
        with open(self.path, "r", encoding="utf-8") as json_file:
            return json.load(json_file)

    def _save(self, data):
        # Guarda datos en el archivo JSON
        with open(self.path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=2, ensure_ascii=False)

    def list(self) -> List[Book]:
        # Devuelve todos los libros como objetos Book
        data = self._load()
        return [Book(**item) for item in data["items"]]

    def get(self, book_id: int) -> Optional[Book]:
        # Busca un libro por su ID
        data = self._load()
        for item in data["items"]:
            if item["id"] == book_id:
                return Book(**item)
        return None

    def create(self, title: str, author: str) -> Book:
        # Crea un nuevo libro y lo guarda
        data = self._load()
        data["seq"] += 1
        book = Book(id=data["seq"], title=title, author=author)
        data["items"].append(asdict(book))
        self._save(data)
        return book

    def update(self, book_id: int, title: str, author: str) -> Optional[Book]:
        # Actualiza título y autor de un libro existente
        data = self._load()
        for i, item in enumerate(data["items"]):
            if item["id"] == book_id:
                item["title"] = title
                item["author"] = author
                data["items"][i] = item
                self._save(data)
                return Book(**item)
        return None

    def delete(self, book_id: int) -> bool:
        # Elimina un libro por su ID
        data = self._load()
        before_count = len(data["items"])
        data["items"] = [item for item in data["items"] if item["id"] != book_id]
        self._save(data)
        return len(data["items"]) < before_count

# --- Fábrica de repositorios ---
class RepositoryFactory:
    # Devuelve la implementación de repositorio según el tipo
    @staticmethod
    def get_book_repository(kind="json") -> BookRepositoryInterface:
        if kind == "json":
            return JsonBookRepository()
        raise ValueError("Tipo de repositorio no soportado")

# --- Servicio con reglas de negocio ---
class LibraryService:
    def __init__(self, book_repo: BookRepositoryInterface):
        # Recibe un repositorio y lo usa para aplicar reglas de negocio
        self.book_repo = book_repo

    def add_book(self, title: str, author: str) -> Book:
        # Añade un libro nuevo
        return self.book_repo.create(title, author)

    def show_books(self) -> List[Book]:
        # Devuelve todos los libros
        return self.book_repo.list()

    def edit_book(self, book_id: int, title: str, author: str) -> Optional[Book]:
        # Edita un libro existente
        return self.book_repo.update(book_id, title, author)

    def remove_book(self, book_id: int) -> bool:
        # Elimina un libro por ID
        return self.book_repo.delete(book_id)

# --- Ejemplo de uso ---
if __name__ == "__main__":
    # Se obtiene el repositorio desde la fábrica
    repo = RepositoryFactory.get_book_repository("json")
    service = LibraryService(repo)

    # Crear libro
    book1 = service.add_book("1984", "George Orwell")
    print("Creado:", book1)

    # Listar libros
    for book in service.show_books():
        print("Listado:", book)

    # Actualizar libro
    updated = service.edit_book(book1.id, "1984 (Edición revisada)", "George Orwell")
    print("Actualizado:", updated)
    
       # Listar libros
    for book in service.show_books():
        print("Listado:", book)

    # Eliminar libro
    deleted = service.remove_book(book1.id)
    print("Eliminado:", deleted)
    
    # Listar libros
    for book in service.show_books():
        print("Listado:", book)
        