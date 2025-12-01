def find_largest_number(numbers):
    """
    Returns the largest number from a list of numbers.
    Raises ValueError if the input is not a list or if it contains non-numeric values.
    """
    if numbers is None:
        raise ValueError("Input cannot be None.")
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list.")
    if len(numbers) == 0:
        raise ValueError("List cannot be empty.")

    for number in numbers:
        if not isinstance(number, (int, float)):
            raise ValueError(f"Invalid value: {number}. All elements must be numbers.")

    return max(numbers)

# Edge case tests
try:
    print(find_largest_number([1, 2, 3]))  # Should return 3
    print(find_largest_number(None))  # Should raise an error
    print(find_largest_number([1, 'a', 3]))  # Should raise an error
    print(find_largest_number([]))  # Should raise an error
except ValueError as ve:
    print(ve)

# Code ends here
