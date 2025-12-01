def find_largest_number(numbers):
    """
    Function to find the largest number in a list.
    :param numbers: List of numbers
    :return: The largest number in the list or None if the list is empty
    """
    if not numbers:
        raise ValueError("The input list cannot be empty.")
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    # Sample input
    numbers = [3, 5, 2, 9, 1]
    largest_number = find_largest_number(numbers)
    print(f'The largest number is: {largest_number}')