import sys

# Constants for input validation messages
INVALID_INPUT_MSG = "Input must be a list of numbers."
EMPTY_LIST_MSG = "The list cannot be empty."

def find_max(numbers):
    if not isinstance(numbers, list):
        raise ValueError(INVALID_INPUT_MSG)
    if not numbers:
        raise ValueError(EMPTY_LIST_MSG)
    # Using max for simplicity and efficiency
    return max(numbers)

if __name__ == '__main__':
    try:
        numbers = [int(x) for x in sys.argv[1:]]  # example input via command line
        maximum = find_max(numbers)
        print(f'The maximum number is: {maximum}')  # Output the maximum
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f'An unexpected error occurred: {e}')  

