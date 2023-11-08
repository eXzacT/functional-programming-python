from collections import deque, namedtuple
from order_item import OrderItem
from dataclasses import dataclass, field
from customer import Customer
from functools import lru_cache


def consume(iter):
    deque(iter, maxlen=0)


def action_if(func, predicate, iter):
    consume(func(i) for i in iter if predicate(i))


def get_updated_tuple(predicate, func, iter):
    return tuple(func(i) if predicate(i) else i for i in iter)


@dataclass(frozen=True)
class Order:
    # Class attribute
    orders: tuple = field(init=False)

    # Instance attributes
    order_id: int
    shipping_address: str
    expedited: bool
    shipped: bool
    customer: Customer
    order_items: tuple[OrderItem, ...]

    @staticmethod
    def test_expedited(order):
        return order.expedited

    @staticmethod
    def test_not_expedited(order):
        return not order.expedited

    @staticmethod
    def get_customer_name(order):
        return order.customer.name

    @staticmethod
    def get_customer_address(order):
        return order.customer.address

    @staticmethod
    def get_shipping_address(order):
        return order.shipping_address

    @staticmethod
    def get_filtered_info(predicate, func, orders):
        return map(func, filter(predicate, orders))

    @property
    @lru_cache(maxsize=1)
    def total_price(self):
        return sum(i.total_price for i in self.order_items)

    @staticmethod
    def get_order_details(orders):
        d = namedtuple(
            'OrderDetails', 'order_id, customer, expedited, item_id, item, total_price, backordered')
        return (d(o.order_id, o.customer, o.expedited, i.item_id, i.name, i.price * i.quantity, i.backordered)
                for o in orders for i in o.order_items)

    @staticmethod
    def get_order_by_id(order_id, orders):
        return filter(lambda o: o.order_id == order_id, orders)

    @staticmethod
    def notify_backordered(orders, msg):
        for order in orders:
            for item in order.order_items:
                if item.backordered:
                    order.customer.notify(order.customer, msg)

    @staticmethod
    def notify_backordered(orders, msg):
        Order.map(lambda order: order.customer.notify(order.customer, msg),
                  Order.filter(lambda order: Order.filter(
                      lambda item: item.backordered, order.order_items),
            orders)
        )

    @staticmethod
    def notify_backordered(orders, msg):
        Order.get_filtered_info(
            lambda order: any(item.backordered for item in order.order_items),
            lambda order: order.customer.notify(order.customer, msg),
            orders
        )

    @staticmethod
    def notify_backordered(orders, msg):
        action_if(
            lambda o: o.customer.notify(o.customer, msg),
            lambda o: any(i.backordered for i in o.order_items),
            orders
        )

    @staticmethod
    def mark_backordered(orders, order_id, item_id):
        return get_updated_tuple(
            lambda o: o.order_id == order_id,
            lambda o:
                Order(o.order_id, o.shipping_address, o.expedited, o.shipped, o.customer,
                      get_updated_tuple(
                          lambda i: i.item_id == item_id,
                          lambda i: OrderItem(
                              i.item_id, i.name, i.quantity, i.price, True),
                          o.order_items
                      )),
            orders)

    @staticmethod
    def mark_backordered_items(items, item_id):
        return get_updated_tuple(
            lambda i: i.item_id == item_id,
            lambda i: OrderItem(
                i.item_id, i.name, i.quantity, i.price, True
            ),
            items
        )

    @staticmethod
    def count_expedited_orders_with_backordered_items(orders):
        return [o for o in orders if o.expedited and
                any(i.backordered for i in o.order_items)]

    @staticmethod
    def count_expedited_orders_with_backordered_items_comp(orders):
        return sum(1 for o in orders if o.expedited and
                   any(i.backordered for i in o.order_items))

    @staticmethod
    def count_expedited_orders_with_backordered_items_rec(orders, count=0):
        if len(orders) == 0:
            return 0
        o = orders[0]
        count += 1 if o.expedited and any(
            i.backordered for i in o.order_items) else 0
        return count+Order.count_expedited_orders_with_backordered_items_rec(
            orders[1:])

    @staticmethod
    def count_expedited_orders_with_backordered_items_tail(orders, accumulator=0):
        if len(orders) == 0:
            return accumulator
        o = orders[0]
        add = 1 if o.expedited and any(
            i.backordered for i in o.order_items) else 0
        return Order.count_expedited_orders_with_backordered_items_rec(
            orders[1:], accumulator+add)

    @staticmethod
    def count_expedited_orders_with_backordered_items_gen(orders, accumulator=0):
        if len(orders) == 0:
            yield accumulator
        o = orders[0]
        add = 1 if any(
            i.backordered for i in o.order_items if o.expedited) else 0
        yield Order.count_expedited_orders_with_backordered_items_gen(
            orders[1:], accumulator+add
        )

    @staticmethod
    def set_order_expedited(orderid, orders):
        for order in Order.get_order_by_id(orderid, orders):
            order.expedited = True

    @staticmethod
    def get_expedited_orders_customer_names(orders):
        return Order.get_filtered_info(
            Order.test_expedited,
            Order.get_customer_name,
            orders
        )

    @staticmethod
    def get_expedited_orders_customer_addresses(orders):
        return Order.get_filtered_info(
            Order.test_expedited,
            Order.get_customer_address,
            orders
        )

    @staticmethod
    def get_expedited_orders_shipping_addresses(orders):
        return Order.get_filtered_info(
            Order.test_expedited,
            Order.get_shipping_address,
            orders
        )

    @staticmethod
    def get_not_expedited_orders_customer_names(orders):
        return Order.get_filtered_info(
            Order.test_not_expedited,
            Order.get_customer_name,
            orders
        )

    @staticmethod
    def get_not_expedited_orders_customer_addresses(orders):
        return Order.get_filtered_info(
            Order.test_not_expedited,
            Order.get_customer_address,
            orders
        )

    @staticmethod
    def get_not_expedited_orders_shipping_addresses(orders):
        return Order.get_filtered_info(
            Order.test_not_expedited,
            Order.get_shipping_address,
            orders
        )
