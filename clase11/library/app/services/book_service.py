from typing import List, Optional
from app.domain.models import Book
from app.repository.interfaces import BookRepositoryInterface

class BookService:
    """
    Capa de negocio para operaciones de libros.
    Encapsula reglas (por ejemplo, validaciones básicas).
    """
    def __init__(self, repo: BookRepositoryInterface):
        self.repo = repo

    def add_book(self, title: str, author: str) -> Book:
        # Validaciones simples de negocio
        if not title.strip():
            raise ValueError("El título no puede estar vacío")
        if not author.strip():
            raise ValueError("El autor no puede estar vacío")
        return self.repo.create(title, author)

    def list_books(self) -> List[Book]:
        return self.repo.list()

    def get_book(self, book_id: int) -> Optional[Book]:
        return self.repo.get(book_id)

    def edit_book(self, book_id: int, title: str, author: str) -> Optional[Book]:
        if not title.strip():
            raise ValueError("El título no puede estar vacío")
        if not author.strip():
            raise ValueError("El autor no puede estar vacío")
        return self.repo.update(book_id, title, author)

    def remove_book(self, book_id: int) -> bool:
        return self.repo.delete(book_id)
