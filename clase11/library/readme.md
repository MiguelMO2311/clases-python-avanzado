# Software Biblioteca

Proyecto de gestión de biblioteca con arquitectura en capas (dominio, repositorio, servicios, adaptadores) y CLI para operaciones CRUD de libros y usuarios.

---

Características
  CRUD de libros (crear, listar, obtener, actualizar, eliminar).
  Gestión de usuarios (registro y login).
  Persistencia en archivo JSON configurable.
  Configuración externa mediante `.env` y `config.ini`.
  Tests unitarios con `pytest`.

---

Estructura del proyecto
plaintext
software_biblioteca/
├── .env
├── config.ini
├── app/
│   ├── config.py
│   ├── domain/
│   │   └── models.py
│   ├── repository/
│   │   ├── interfaces.py
│   │   └── json_repo.py
│   ├── services/
│   │   └── book_service.py
│   └── adapters/
│       └── cli.py
├── data/
│   └── database.json
└── tests/
    ├── conftest.py
    ├── test_repository.py
    └── test_services.py

---
Instalación

Clona el repositorio y entra en la carpeta del proyecto:

git clone <https://github.com/usuario/software_biblioteca.git>
cd software_biblioteca

Instala las dependencias necesarias:

pip install -r requirements.txt

---
Uso:

Ejecutar CLI

Desde la raíz del proyecto:

python -m app.adapters.cli create "1984" "George Orwell"
python -m app.adapters.cli list
python -m app.adapters.cli get 1
python -m app.adapters.cli update 1 "1984 (Edición revisada)" "George Orwell"
python -m app.adapters.cli delete 1

---
Tests:

Instala pytest si no lo tienes:

pip install pytest

Ejecuta los tests:

pytest -q

Para más detalle:

pytest -v

---
Configuración:

El proyecto utiliza configuración externa en .env y config.ini.

Ejemplo de .env:

DATA_DIR=./data
DATA_FILE=database.json
APP_ENV=development

Esto permite cambiar directorios y archivo de datos sin modificar el código.

---
Diseño aplicado:

Arquitectura en capas: dominio, repositorio, servicios, adaptadores.

Patrones: Repository, separación de configuración, CLI como adapter.

Principios SOLID: SRP en cada módulo; bajo acoplamiento mediante interfaces; configuración externa para portabilidad.

Configuración centralizada: .env y config.ini permiten cambiar ruta y formato sin tocar código.

Testabilidad: el repositorio acepta data_path, lo que facilita aislar entornos de prueba.

---
Licencia:

Este proyecto se distribuye bajo la licencia MMO.
