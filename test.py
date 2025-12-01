def find_largest_number(numbers):
    if not numbers:
        raise ValueError("The list is empty. Please provide a list of numbers.")
    largest_number = numbers[0]  # Assume the first number is the largest initially
    for current_number in numbers:
        if current_number > largest_number:
            largest_number = current_number
    return largest_number

# Example usage
if __name__ == "__main__":
    try:
        print(find_largest_number([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))  # Output should be 9
    except ValueError as e:
        print(e)