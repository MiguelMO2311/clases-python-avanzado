from typing import Optional
from app.domain.models import User
from app.repository.interfaces import UserRepositoryInterface

class UserService:
    def __init__(self, repo: UserRepositoryInterface):
        self.repo = repo

    def register_user(self, username: str, password: str) -> User:
        if not username.strip() or not password.strip():
            raise ValueError("Usuario y contraseña no pueden estar vacíos")
        return self.repo.register(username, password)

    def login_user(self, username: str, password: str) -> Optional[User]:
        return self.repo.login(username, password)
