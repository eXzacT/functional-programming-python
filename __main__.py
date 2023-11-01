# from order import Order
from order_with_lambdas import Order
from customer import Customer


def main():
    cust1 = Customer()
    cust1.name = 'Heart of Gold'
    cust1.address = 'The Milky Way Galaxy'
    cust1.enterprise = False
    cust2 = Customer()
    cust2.name = 'Milliways Restaurant'
    cust2.address = 'Magrathea'
    cust2.enterprise = True
    cust3 = Customer()
    cust3.name = 'Pero Dijetlic'
    cust3.address = 'MK10'
    cust3.enterprise = True

    ord1 = Order()
    ord1.customer = cust1
    ord1.expedited = False
    ord1.shipping_address = 'Infinitely Improbable'

    ord2 = (Order())
    ord2.customer = cust2
    ord2.expedited = True
    ord2.shipping_address = 'Magrathea'

    ord3 = (Order())
    ord3.customer = cust3
    ord3.expedited = True
    ord3.shipping_address = 'MK10'

    Order.orders = [ord1, ord2, ord3]
    print(Order.get_expedited_orders_customer_names())
    print(Order.get_expedited_orders_customer_addresses())
    print(Order.get_expedited_orders_shipping_addresses())


main()
