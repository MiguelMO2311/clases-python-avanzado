from decimal import Decimal
import pytest
from main import Item


def test_item_creation(laptop):
    """Verifica creación básica de Item"""
    assert laptop.id == "item-001"
    assert laptop.name == "Laptop"
    assert laptop.price == Decimal("999.99")
    assert laptop.quantity == 1


def test_cart_add_item(cart, laptop):
    """Verifica añadir item al carrito"""
    cart.add_item(laptop)
    items = cart.get_items()
    assert len(items) == 1
    assert items[0].id == "item-001"


def test_cart_total_calculation(cart, laptop, mouse):
    """Verifica cálculo del total"""
    cart.add_item(laptop)
    cart.add_item(mouse)
    expected_total = Decimal("999.99") + Decimal("29.99")
    assert cart.get_total() == expected_total


def test_cart_duplicate_item_increments_quantity(cart, laptop):
    """Verifica que añadir item duplicado incrementa cantidad"""
    cart.add_item(laptop)
    cart.add_item(Item(id="item-001", name="Laptop", price=Decimal("999.99"), quantity=1))
    items = cart.get_items()
    assert len(items) == 1
    assert items[0].quantity == 2


def test_eventbus_notifies_subscriber(event_bus, cart, laptop):
    """Verifica que se notifica a suscriptores"""
    events_received = []
    def listener(event_name, data):
        events_received.append((event_name, data))
    event_bus.subscribe(listener)
    cart.add_item(laptop)
    assert len(events_received) == 1
    assert events_received[0][0] == "item_added"
    assert events_received[0][1]["item"].id == "item-001"


def test_multiple_subscribers(event_bus, cart, laptop):
    """Verifica que múltiples suscriptores reciben eventos"""
    received_1 = []
    received_2 = []
    def listener1(event_name, data):
        received_1.append(event_name)
    def listener2(event_name, data):
        received_2.append(event_name)
    event_bus.subscribe(listener1)
    event_bus.subscribe(listener2)
    cart.add_item(laptop)
    assert len(received_1) == 1
    assert len(received_2) == 1


def test_event_data_contains_cart_info(event_bus, cart, laptop):
    """Verifica que los eventos contienen información del carrito"""
    received_data = {}
    def listener(event_name, data):
        received_data.update(data)
    event_bus.subscribe(listener)
    cart.add_item(laptop)
    assert received_data["cart_id"] == "cart-001"
    assert received_data["total"] == Decimal("999.99")
    assert received_data["item"].name == "Laptop"


def test_end_to_end(event_bus, cart, laptop, mouse):
    """Prueba integral: creación de items, añadir al carrito, calcular total y notificar eventos"""
    events_received = []
    def listener(event_name, data):
        events_received.append((event_name, data))
    event_bus.subscribe(listener)
    cart.add_item(laptop)
    cart.add_item(mouse)
    items = cart.get_items()
    assert len(items) == 2
    assert cart.get_total() == Decimal("1029.98")
    assert len(events_received) == 2
    for _, data in events_received:
        assert data["cart_id"] == "cart-001"
        assert "item" in data
        assert "total" in data
