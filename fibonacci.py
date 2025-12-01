def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


def print_fibonacci(n):
    fib_sequence = fibonacci(n)
    for num in fib_sequence:
        print(num)
    print()  # Print a newline after the sequence

# Further modularity could be achieved by allowing fibonacci to be used as a generator if needed.

# To ensure code stability, automated tests should be added for the fibonacci function.
# Example test: assert fibonacci(5) == [0, 1, 1, 2, 3]