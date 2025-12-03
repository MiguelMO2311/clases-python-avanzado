import os
import tempfile
import shutil
import pytest
from pathlib import Path

from app.repository.json_repo import JsonBookRepository
from app.services.book_service import BookService

@pytest.fixture
def temp_data_dir():
    # Crea un directorio temporal aislado para cada sesión de test
    tmp_dir = Path(tempfile.mkdtemp(prefix="library_data_"))
    yield tmp_dir
    shutil.rmtree(tmp_dir, ignore_errors=True)

@pytest.fixture
def repo(temp_data_dir):
    # Inicializa el repositorio apuntando al dir temporal
    return JsonBookRepository(data_path=temp_data_dir)

@pytest.fixture
def service(repo):
    return BookService(repo)
