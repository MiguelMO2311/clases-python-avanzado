import pytest
from decimal import Decimal

# Importa las clases desde tu archivo principal
from main import EventBus, Cart, Item


@pytest.fixture
def event_bus():
    """EventBus limpio para cada test"""
    return EventBus()


@pytest.fixture
def cart(event_bus):
    """Carrito conectado al EventBus"""
    return Cart(cart_id="cart-001", event_bus=event_bus)


@pytest.fixture
def laptop():
    """Item de ejemplo: Laptop"""
    return Item(
        id="item-001",
        name="Laptop",
        price=Decimal("999.99"),
        quantity=1
    )


@pytest.fixture
def mouse():
    """Item de ejemplo: Mouse"""
    return Item(
        id="item-002",
        name="Mouse",
        price=Decimal("29.99"),
        quantity=1
    )

# Pytest no carga automáticamente cualquier archivo que tengas en tu proyecto.

# Si defines tus fixtures en un archivo llamado fixtures.py, pytest lo trata como un módulo normal,
# no como un archivo especial de configuración.

# Eso significa que para usarlos en los tests, tendrías que importarlos manualmente (from fixtures import ...).

# Al hacer esa importación directa, lo que llega a tus tests no es el objeto del fixture, sino 
# la función que lo define (FixtureFunctionDefinition). Por eso te daba el error de "no tiene atributo id".