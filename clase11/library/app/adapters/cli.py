import argparse
from app.repository.json_repo import JsonBookRepository
from app.services.book_service import BookService

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="CLI Biblioteca - CRUD de libros")
    subparsers = parser.add_subparsers(dest="command")

    # Crear
    create_p = subparsers.add_parser("create", help="Crear libro")
    create_p.add_argument("title", help="Título del libro")
    create_p.add_argument("author", help="Autor del libro")

    # Listar
    subparsers.add_parser("list", help="Listar libros")

    # Obtener
    get_p = subparsers.add_parser("get", help="Obtener libro por ID")
    get_p.add_argument("id", type=int)

    # Editar
    update_p = subparsers.add_parser("update", help="Actualizar libro por ID")
    update_p.add_argument("id", type=int)
    update_p.add_argument("title")
    update_p.add_argument("author")

    # Eliminar
    delete_p = subparsers.add_parser("delete", help="Eliminar libro por ID")
    delete_p.add_argument("id", type=int)

    return parser

def main():
    parser = build_parser()
    args = parser.parse_args()
    repo = JsonBookRepository()
    service = BookService(repo)

    if args.command == "create":
        book = service.add_book(args.title, args.author)
        print(f"Creado: {book}")
    elif args.command == "list":
        for book in service.list_books():
            print(book)
    elif args.command == "get":
        book = service.get_book(args.id)
        print(book if book else "No encontrado")
    elif args.command == "update":
        updated = service.edit_book(args.id, args.title, args.author)
        print(f"Actualizado: {updated}" if updated else "No encontrado")
    elif args.command == "delete":
        deleted = service.remove_book(args.id)
        print("Eliminado" if deleted else "No encontrado")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
