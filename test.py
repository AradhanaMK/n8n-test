# find_largest_number function
# This function takes a list of numbers and returns the largest number in the list.
# Example usage:
# largest = find_largest_number([1, 2, 3, 4, 5])
# print(largest)

def find_largest_number(numbers):
    """
    Find the largest number in a list.
    
    Args:
        numbers (list): A list of numeric values.
    
    Returns:
        int or float: The largest number in the list.
    """
    return max(numbers)


# Automated unit tests
import unittest

class TestFindLargestNumber(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(find_largest_number([1, 2, 3, 4, 5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(find_largest_number([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(find_largest_number([-1, 0, 1]), 1)


if __name__ == '__main__':
    unittest.main()

