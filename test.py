def find_largest_number(numbers):
    if not numbers:
        raise ValueError("The input list cannot be empty.")
    return max(numbers)

# Unit tests

def test_find_largest_number():
    assert find_largest_number([1, 2, 3]) == 3
    assert find_largest_number([-1, -2, -3]) == -1
    assert find_largest_number([5]) == 5
    try:
        find_largest_number([])
    except ValueError as e:
        assert str(e) == "The input list cannot be empty."

# Run the tests

test_find_largest_number()