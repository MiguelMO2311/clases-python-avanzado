import json
from pathlib import Path
from typing import List, Optional
from dataclasses import asdict

from app.domain.models import Book
from app.repository.interfaces import BookRepositoryInterface
from app.config import load_settings

class JsonBookRepository(BookRepositoryInterface):
    """
    Repositorio de libros en un archivo JSON.
    Estructura del JSON:
      {
        "seq": <int>,
        "items": [ { "id": int, "title": str, "author": str }, ... ]
      }
    """
    def __init__(self, data_path: Path | None = None):
        settings = load_settings()
        base_dir = data_path if data_path else settings.data_dir
        self.file_path = base_dir / settings.data_file
        self.encoding = settings.encoding
        self.indent = settings.json_indent
        self.ensure_ascii = settings.ensure_ascii

        # Inicializa el archivo si no existe
        if not self.file_path.exists():
            self._save({"seq": 0, "items": []})

    def _load(self) -> dict:
        with self.file_path.open("r", encoding=self.encoding) as f:
            return json.load(f)

    def _save(self, data: dict) -> None:
        with self.file_path.open("w", encoding=self.encoding) as f:
            json.dump(data, f, indent=self.indent, ensure_ascii=self.ensure_ascii)

    def list(self) -> List[Book]:
        data = self._load()
        return [Book(**item) for item in data.get("items", [])]

    def get(self, book_id: int) -> Optional[Book]:
        data = self._load()
        for item in data.get("items", []):
            if item["id"] == book_id:
                return Book(**item)
        return None

    def create(self, title: str, author: str) -> Book:
        data = self._load()
        data["seq"] = int(data.get("seq", 0)) + 1
        book = Book(id=data["seq"], title=title, author=author)
        data.setdefault("items", []).append(asdict(book))
        self._save(data)
        return book

    def update(self, book_id: int, title: str, author: str) -> Optional[Book]:
        data = self._load()
        items = data.get("items", [])
        for i, item in enumerate(items):
            if item["id"] == book_id:
                item["title"] = title
                item["author"] = author
                items[i] = item
                self._save(data)
                return Book(**item)
        return None

    def delete(self, book_id: int) -> bool:
        data = self._load()
        before = len(data.get("items", []))
        data["items"] = [item for item in data.get("items", []) if item["id"] != book_id]
        self._save(data)
        return len(data["items"]) < before
