def find_largest_number(numbers):
    """
    Find the largest number in a list.

    Parameters:
    numbers (list): A list of numbers.

    Returns:
    int or None: The largest number in the list, or None if the list is empty.
    """
    if not numbers:
        return None

    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

# Example usage:
if __name__ == '__main__':
    num_list = [3, 5, 1, 2, 4]
    print(f'The largest number is: {find_largest_number(num_list)}')

