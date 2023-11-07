import sys
import types


def fibonacci_iterative(n: int) -> int:
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for _ in range(2, n+1):
            a, b = b, a+b
        return b


def fibonacci_recursive(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def fibonacci_recursive_tail(n: int, curr=0, nxt=1) -> int:
    if n == 0:
        return curr
    else:
        return fibonacci_recursive_tail(n-1, nxt, curr+nxt)


def fibonacci_recursive_tail_tramp(n: int, curr=0, nxt=1) -> int:
    if n == 0:
        yield curr
    else:
        yield fibonacci_recursive_tail_tramp(n-1, nxt, curr+nxt)


def calculate_sum(n: int) -> int:
    return n*(n+1)/2


def sum_recursive(n: int) -> int:
    if n == 0:
        return n
    return n+sum_recursive(n-1)


def sum_recursive_tail(n: int, accumulator: int = 0) -> int:
    if n == 0:
        return accumulator
    return sum_recursive_tail(n-1, accumulator+n)


def tramp(gen, *args, **kwargs):
    g = gen(*args, **kwargs)
    while isinstance(g, types.GeneratorType):
        g = next(g)
    return g


print([fibonacci_recursive_tail(i) for i in range(10)])
print([tramp(fibonacci_recursive_tail_tramp, i) for i in range(10)])
print([fibonacci_recursive(i) for i in range(10)])

sys.set_int_max_str_digits(20899)
# print(tramp(fibonacci_recursive_tail_tramp, 100_000))
