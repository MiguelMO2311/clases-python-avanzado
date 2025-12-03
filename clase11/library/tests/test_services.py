import pytest
from app.domain.models import Book

def test_service_add_and_list(service):
    b = service.add_book("Clean Code", "Robert C. Martin")
    assert isinstance(b, Book)
    items = service.list_books()
    assert len(items) == 1
    assert items[0].title == "Clean Code"

def test_service_validations(service):
    with pytest.raises(ValueError):
        service.add_book("", "Autor")
    with pytest.raises(ValueError):
        service.add_book("Titulo", "")

def test_service_edit_and_get(service):
    b = service.add_book("Old", "Anon")
    edited = service.edit_book(b.id, "New", "Anon")
    assert edited is not None
    assert edited.title == "New"
    fetched = service.get_book(b.id)
    assert fetched is not None
    assert fetched.title == "New"

def test_service_remove(service):
    b = service.add_book("Delete Me", "Anon")
    ok = service.remove_book(b.id)
    assert ok is True
    assert service.get_book(b.id) is None
