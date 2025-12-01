def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.

    Parameters:
    n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of the integer n.

    Raises:
    ValueError: If n is a negative integer or not an integer.
    """
    if not isinstance(n, int):
        raise ValueError('Input must be a non-negative integer.')
    if n < 0:
        raise ValueError('Input must be a non-negative integer.')

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def test_factorial():
    """
    Unit tests for the factorial function.
    """
    import unittest

    class TestFactorial(unittest.TestCase):
        def test_factorial_of_zero(self):
            self.assertEqual(factorial(0), 1)

        def test_factorial_of_positive_integer(self):
            self.assertEqual(factorial(5), 120)

        def test_factorial_negative_integer(self):
            with self.assertRaises(ValueError) as context:
                factorial(-1)
            self.assertEqual(str(context.exception), 'Input must be a non-negative integer.')

        def test_factorial_non_integer(self):
            with self.assertRaises(ValueError) as context:
                factorial(3.5)
            self.assertEqual(str(context.exception), 'Input must be a non-negative integer.')

    unittest.main()


