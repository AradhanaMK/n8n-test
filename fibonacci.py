def fibonacci(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
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

if __name__ == "__main__":
    print_fibonacci(10)


def test_fibonacci():
    assert fibonacci(0) == []
    assert fibonacci(1) == [0]
    assert fibonacci(2) == [0, 1]
    assert fibonacci(5) == [0, 1, 1, 2, 3]
    assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    try:
        fibonacci(-1)
    except ValueError:
        pass  # Expected behavior
    try:
        fibonacci(3.5)
    except ValueError:
        pass  # Expected behavior


test_fibonacci()
