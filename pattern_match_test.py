from customer import Customer
from order_item import OrderItem
from order import Order


def main():
    # test customer validation
    for name, addr, ent in (
        ('one', 'two', True),
        ('one', 'two', 43),
        (3123, 'two', True),
        ('one', '', False),
        ('one', 'two', 'false'),
        ('', '', '')
    ):
        try:
            c = Customer(name=name, address=addr, enterprise=ent)
        except Exception as ex:
            print(ex)
    print("\n")
    for id, name, qty, price, backo in (
        (1, 'abc', 10, 13.40, False),
        (1, '', 0, 12, True),
        (1, 'abc', 1, 0, True),
        (1, 'abc', 1, 1, False),
        (1, 'abc', 2, 3., 'false')
    ):
        try:
            o = OrderItem(id, name, qty, price, backo)
        except Exception as ex:
            print(ex)


main()
