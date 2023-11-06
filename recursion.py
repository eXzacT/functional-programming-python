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
            c = a + b
            a = b
            b = c
        return b


def fibonacci_recursive(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def sum_recursive(n: int) -> int:
    if n == 0:
        return n
    return n + sum_recursive(n - 1)


def sum_recursive_tail(n: int, accumulator: int = 0) -> int:
    if n == 0:
        return accumulator
    return sum_recursive_tail(n - 1, accumulator + n)
