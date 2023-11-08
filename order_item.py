from dataclasses import dataclass


@dataclass(frozen=True)
class OrderItem:
    item_id: int
    name: str
    quantity: int
    price: int
    backordered: bool

    @property
    def total_price(self):
        return self.quantity * self.price
