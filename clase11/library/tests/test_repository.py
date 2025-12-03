from app.domain.models import Book

def test_repository_create_and_get(repo):
    book = repo.create("1984", "George Orwell")
    assert isinstance(book, Book)
    fetched = repo.get(book.id)
    assert fetched is not None
    assert fetched.title == "1984"

def test_repository_list(repo):
    repo.create("1984", "George Orwell")
    repo.create("Brave New World", "Aldous Huxley")
    items = repo.list()
    assert len(items) == 2

def test_repository_update(repo):
    b = repo.create("Temp", "Anon")
    updated = repo.update(b.id, "Temp V2", "Anon")
    assert updated is not None
    assert updated.title == "Temp V2"

def test_repository_delete(repo):
    b = repo.create("Temp", "Anon")
    ok = repo.delete(b.id)
    assert ok is True
    assert repo.get(b.id) is None
