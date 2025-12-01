def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.
    
    Parameters:
        n (int): A non-negative integer whose factorial is to be calculated.
    
    Returns:
        int: The factorial of the number n.
    
    Raises:
        ValueError: If n is a negative integer.
    """
    if not isinstance(n, int):
        raise ValueError("Input must be a non-negative integer.")
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def test_factorial():
    """
    Unit tests for the factorial function.
    """
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800
    try:
        factorial(-1)
    except ValueError:
        pass  # Expected behavior
    else:
        raise AssertionError("Factorial of negative number should raise ValueError")
    try:
        factorial(5.5)
    except ValueError:
        pass  # Expected behavior
    else:
        raise AssertionError("Factorial of non-integer should raise ValueError")

# Uncomment the following line to run tests if this file is executed directly
# test_factorial()