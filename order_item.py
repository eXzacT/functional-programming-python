from dataclasses import dataclass


@dataclass(frozen=True)
class OrderItem:
    item_id: int
    name: str
    quantity: int
    price: int
    backordered: bool

    def __post_init__(self):
        match (self.item_id, self.name, self.quantity, self.price, self.backordered):
            case (int(i), str(), int(q), int(p), bool()):
                pass
            case (i, str(), int(), int(), bool()):
                raise ValueError(f'Id {i} is not an integer')
            case (int(), n, int(), int(), bool()):
                raise ValueError(f'Name {n} is not a string')
            case (int(), str(), q, int(), bool()):
                raise ValueError(f'Quantity {q} is not an integer')
            case (int(), str(), int(), p, bool()):
                raise ValueError(f'Price {p} is not an integer')
            case (int(), str(), int(), int(), b):
                raise ValueError(f'Backordered {b} is not a boolean')
            case _:
                raise ValueError('Unable to parse arguments')

    @property
    def total_price(self):
        return self.quantity * self.price
