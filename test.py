def find_largest_number(numbers):
    """
    Returns the largest number from a list of numbers.

    Parameters:
    numbers (list): A list of numerical values.

    Returns:
    int or float: The largest number in the list. If the list is empty, returns None.
    """
    if not isinstance(numbers, list):
        raise ValueError('Input must be a list.')
    if not numbers:
        return None
    return max(numbers)


if __name__ == '__main__':
    example_numbers = [10, 20, 4, 45, 99]
    largest_number = find_largest_number(example_numbers)
    print(f'The largest number is: {largest_number}')