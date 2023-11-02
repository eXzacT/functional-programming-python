from collections import deque
from itertools import islice


def consume(iterator, n=None):
    "Advance the iterator n-steps ahead. If n is none, consume entirely."
    # Use functions that consume iterators at C speed.
    if n is None:
        # feed the entire iterator into a zero-length deque
        deque(iterator, maxlen=0)
    else:
        # advance to the empty slice starting at position n
        next(islice(iterator, n, n), None)


class Order:
    # class attribute
    orders = []

    # instance attributes
    order_id = 0
    shipping_address = ''
    expedited = False
    shipped = False
    customer = None

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
        # By wrapping filter with list we make it evaluate instantly, otherwise it will stay lazy (02/11/2023)
        return filter(predicate, iter)

    @staticmethod
    def map(func, iter):
        # Same comment as above (02/11/2023)
        return map(func, iter)

    @staticmethod
    def get_filtered_info(predicate, func, iter):
        return Order.map(func, Order.filter(predicate, iter))

    @staticmethod
    def get_filtered_info_lc(predicate, func, iter):
        return [func(x) for x in iter if predicate(x)]

    @staticmethod
    def get_order_by_id(order_id, orders):
        return Order.filter(lambda order: order.order_id == order_id, orders)

    @staticmethod
    def get_order_by_id_lc(orderid, orders):
        return [x for x in orders if x.orderid == orderid]

    @staticmethod
    def set_order_expedited(order_id, orders):
        for order in Order.get_order_by_id(order_id, orders):
            order.expedited = True

    @staticmethod
    def set_expedited(order):
        order.expedited = True

    @staticmethod
    def set_order_expedited_f(order_id, orders):
        # If we don't wrap this with consume nothing changes because both map and filter are lazy iters (02/11/2023)
        consume(Order.map(Order.set_expedited,
                          Order.filter(lambda order: order.order_id == order_id, orders)))

    @staticmethod
    def get_expedited_orders_customer_names(orders):
        return Order.get_filtered_info(
            Order.test_expedited,
            Order.get_customer_name,
            orders
        )

    @staticmethod
    def get_expedited_orders_customer_names_lambda(orders):
        return Order.get_filtered_info(
            lambda order: order.expedited,
            lambda order: order.customer.name,
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
    def get_expedited_orders_customer_addresses_lambda(orders):
        return Order.get_filtered_info(
            lambda order: order.expedited,
            lambda order: order.customer.address,
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
    def get_expedited_orders_shipping_addresses_lambda(orders):
        return Order.get_filtered_info(
            lambda order: order.expedited,
            lambda order: order.shipping_address,
            orders
        )

    @staticmethod
    def get_not_expedited_orders_customer_names(orders):
        return Order.get_filtered_info(
            lambda order: not order.expedited,
            lambda order: order.customer.name,
            orders
        )

    @staticmethod
    def get_not_expedited_orders_customer_addresses(orders):
        return Order.get_filtered_info(
            lambda order: not order.expedited,
            lambda order: order.customer.address,
            orders
        )

    @staticmethod
    def get_not_expedited_orders_shipping_addresses(orders):
        return Order.get_filtered_info(
            lambda order: not order.expedited,
            lambda order: order.shipping_address,
            orders
        )
