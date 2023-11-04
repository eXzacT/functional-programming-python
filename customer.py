from dataclasses import dataclass


@dataclass(frozen=True)
class Customer:
    name: str
    address: str
    enterprise: bool

    @staticmethod
    def notify(customer, msg):
        print(f'Sending {msg} to {customer.name} at {customer.address}')
