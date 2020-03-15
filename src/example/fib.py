"""Calculate the fibonacchi sequence."""


def fib(n: int) -> int:
    """Calculate nth value of the fibonacchi sequence."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
