import json, os
from dataclasses import asdict
from typing import Optional
from app.domain.models import User
from app.repository.interfaces import UserRepositoryInterface
from app.config import load_settings

class JsonUserRepository(UserRepositoryInterface):
    def __init__(self, filename="users.json"):
        settings = load_settings()
        self.file_path = settings.data_dir / filename
        if not self.file_path.exists():
            self._save({"seq": 0, "items": []})

    def _load(self):
        with open(self.file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _save(self, data):
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def register(self, username: str, password: str) -> User:
        data = self._load()
        for item in data["items"]:
            if item["username"] == username:
                raise ValueError("Usuario ya existe")
        data["seq"] += 1
        user = User(id=data["seq"], username=username, password=password)
        data["items"].append(asdict(user))
        self._save(data)
        return user

    def login(self, username: str, password: str) -> Optional[User]:
        data = self._load()
        for item in data["items"]:
            if item["username"] == username and item["password"] == password:
                return User(**item)
        return None
