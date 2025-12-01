def print_fibonacci(n):
    """
    Generate Fibonacci sequence up to the n-th term and print the output.

    Parameters:
    n : int
        The number of terms in the Fibonacci sequence to generate.
    """
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()  # For new line after the sequence

# Example usage
if __name__ == '__main__':
    print_fibonacci(10)