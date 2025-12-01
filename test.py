def find_largest_number(numbers):
    """
    Find the largest number in a list.

    Parameters:
    numbers (list): A list of numerical values.

    Returns:
    int or float: The largest number in the list.
    Raises:
    ValueError: If the list is empty.
    """
    if not numbers:
        raise ValueError("The input list cannot be empty.")
    return max(numbers)

# Example usage:
# largest = find_largest_number([1, 2, 3, 4])
# print(largest)

# Automated unit tests:
import unittest

class TestFindLargestNumber(unittest.TestCase):
    def test_largest_number(self):
        self.assertEqual(find_largest_number([1, 2, 3, 4]), 4)
        self.assertEqual(find_largest_number([-1, -2, -3]), -1)
        self.assertEqual(find_largest_number([10, 20, 30]), 30)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            find_largest_number([])

if __name__ == '__main__':
    unittest.main()