from collections import deque
from order_item import OrderItem
from dataclasses import dataclass, field
from customer import Customer


def consume(iter):
    deque(iter, maxlen=0)


def action_if(func, predicate, iter):
    consume(func(i) for i in iter if predicate(i))


def get_updated_tuple(predicate, func, iter):
    return tuple(func(i) if predicate(i) else i for i in iter)


def get_filtered_info(predicate, func, iter):
    return tuple(func(i) for i in iter if predicate(i))


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
    def filter(predicate, iter):
        return tuple(filter(predicate, iter))

    @staticmethod
    def map(func, iter):
        return tuple(map(func, iter))

    @staticmethod
    def get_order_by_id(order_id, orders):
        return tuple(filter(lambda order: order.order_id == order_id, orders))

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
    def set_order_expedited(order_id, orders):
        for order in Order.get_order_by_id(order_id, orders):
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
