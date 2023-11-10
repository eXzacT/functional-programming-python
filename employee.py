import csv
from itertools import count as itertools_count
from dataclasses import dataclass
from tramp import tramp


@dataclass
class Employee:
    id: int
    name: str
    manager: object


with open("baby-names.csv") as names:
    reader = csv.reader(names)

    def read_name():
        try:
            return next(reader)[1]
        except StopIteration:
            return None
    _ = read_name()  # Skip first row

    # First employee won't have a manager
    emps = Employee(1, read_name(), None)
    # Increment i infinitely until break
    for i in itertools_count(2):
        nxt_name = read_name()
        # If get_name() returns None it means we reached EOF
        if nxt_name == None:
            break
        # Other employees have previous employee as manager
        emps = Employee(i, nxt_name, emps)


def nth_over(e, over=0, curr=None):
    if e is None or over == 0:
        yield e if e else curr
    else:
        yield nth_over(e.manager, over - 1, e)


print(tramp(nth_over, emps, 2).name)
