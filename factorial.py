def factorial(n):
    """
    Calculate the factorial of a non-negative integer.

    Parameters:
    n (int): A non-negative integer for which to calculate the factorial.

    Returns:
    int: The factorial of the input integer.

    Raises:
    ValueError: If n is a negative integer.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    return _factorial_helper(n)


def _factorial_helper(n):
    """
    Recursive helper function to calculate factorial.
    """
    if n == 0:
        return 1
    return n * _factorial_helper(n - 1)


# Example usage:
# print(factorial(5))  # Output: 120

