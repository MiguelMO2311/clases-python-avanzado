# main.py
from decimal import Decimal
from typing import List, Dict, Callable


class Item:
    """Representa un producto dentro del carrito"""
    def __init__(self, id: str, name: str, price: Decimal, quantity: int = 1):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Item(id={self.id}, name={self.name}, price={self.price}, quantity={self.quantity})"


class EventBus:
    """Sistema de eventos simple para notificar cambios"""
    def __init__(self):
        self._subscribers: List[Callable[[str, Dict], None]] = []

    def subscribe(self, listener: Callable[[str, Dict], None]) -> None:
        """Añade un suscriptor que recibirá eventos"""
        self._subscribers.append(listener)

    def publish(self, event_name: str, data: Dict) -> None:
        """Notifica a todos los suscriptores"""
        for listener in self._subscribers:
            listener(event_name, data)


class Cart:
    """Carrito de compras conectado a un EventBus"""
    def __init__(self, cart_id: str, event_bus: EventBus):
        self.cart_id = cart_id
        self._items: Dict[str, Item] = {}
        self._event_bus = event_bus

    def add_item(self, item: Item) -> None:
        """Añade un item al carrito. Si ya existe, incrementa cantidad."""
        if item.id in self._items:
            self._items[item.id].quantity += item.quantity
        else:
            # Guardamos una copia del item para evitar referencias externas
            self._items[item.id] = Item(
                id=item.id,
                name=item.name,
                price=item.price,
                quantity=item.quantity
            )

        # Publicar evento
        self._event_bus.publish("item_added", {
            "cart_id": self.cart_id,
            "item": self._items[item.id],
            "total": self.get_total()
        })

    def get_items(self) -> List[Item]:
        """Devuelve la lista de items en el carrito"""
        return list(self._items.values())

    def get_total(self) -> Decimal:
        """Calcula el total del carrito"""
        return sum(item.price * item.quantity for item in self._items.values())

    def __repr__(self):
        return f"Cart(cart_id={self.cart_id}, items={self._items})"
