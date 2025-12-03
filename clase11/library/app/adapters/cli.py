import argparse
from app.repository.json_repo import JsonBookRepository
from app.repository.user_repo import JsonUserRepository
from app.services.book_service import BookService
from app.services.user_service import UserService

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="CLI Biblioteca - CRUD de libros y gestión de usuarios")
    subparsers = parser.add_subparsers(dest="command")

    # --- Libros ---
    create_p = subparsers.add_parser("create", help="Crear libro")
    create_p.add_argument("title", help="Título del libro")
    create_p.add_argument("author", help="Autor del libro")

    subparsers.add_parser("list", help="Listar libros")

    get_p = subparsers.add_parser("get", help="Obtener libro por ID")
    get_p.add_argument("id", type=int)

    update_p = subparsers.add_parser("update", help="Actualizar libro por ID")
    update_p.add_argument("id", type=int)
    update_p.add_argument("title")
    update_p.add_argument("author")

    delete_p = subparsers.add_parser("delete", help="Eliminar libro por ID")
    delete_p.add_argument("id", type=int)

    # --- Usuarios ---
    register_p = subparsers.add_parser("register", help="Registrar usuario")
    register_p.add_argument("username")
    register_p.add_argument("password")

    login_p = subparsers.add_parser("login", help="Login usuario")
    login_p.add_argument("username")
    login_p.add_argument("password")

    return parser

def main():
    parser = build_parser()
    args = parser.parse_args()

    # Servicios
    book_repo = JsonBookRepository()
    book_service = BookService(book_repo)

    user_repo = JsonUserRepository()
    user_service = UserService(user_repo)

    # --- Libros ---
    if args.command == "create":
        book = book_service.add_book(args.title, args.author)
        print(f"Creado: {book}")
    elif args.command == "list":
        for book in book_service.list_books():
            print(book)
    elif args.command == "get":
        book = book_service.get_book(args.id)
        print(book if book else "No encontrado")
    elif args.command == "update":
        updated = book_service.edit_book(args.id, args.title, args.author)
        print(f"Actualizado: {updated}" if updated else "No encontrado")
    elif args.command == "delete":
        deleted = book_service.remove_book(args.id)
        print("Eliminado" if deleted else "No encontrado")

    # --- Usuarios ---
    elif args.command == "register":
        user = user_service.register_user(args.username, args.password)
        print("Usuario registrado:", user)
    elif args.command == "login":
        user = user_service.login_user(args.username, args.password)
        print("Login exitoso:", user if user else "Credenciales inválidas")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
