from dataclasses import dataclass


@dataclass(frozen=True)
class Customer:
    name: str
    address: str
    enterprise: bool

    def __post_init__(self):
        match (self.name, self.address, self.enterprise):
            case (str(), str(), bool()):
                pass
            case (n, str(), bool()):
                raise ValueError(f'Name {n} is not a string')
            case (str(), a, bool()):
                raise ValueError(f'Address {a} is not a string')
            case (str(), str(), e):
                raise ValueError(f'Enterprise flag {e} is not a boolean')
            case _:
                raise ValueError('Unable to parse arguments')

    @staticmethod
    def notify(customer, msg):
        print(f'Sending {msg} to {customer.name} at {customer.address}')
