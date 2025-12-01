# fibonacci.py


def fibonacci(n):
    """Generate Fibonacci sequence up to the nth term."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


def print_fibonacci(n):
    """Print the Fibonacci sequence up to the nth term."""
    fib_sequence = fibonacci(n)
    print("Fibonacci sequence:")
    for num in fib_sequence:
        print(num)


# Note: Consider implementing automated tests to verify the functionality of the fibonacci function.

