class EmptyListError(Exception):
    """
    Exception raised when the input list is empty.
    """
    def __init__(self, message="The input list cannot be empty."):
        super().__init__(message)

class NonNumericValueError(Exception):
    """
    Exception raised when a non-numeric value is encountered.
    """
    def __init__(self, value, message="All elements must be numeric."):
        self.value = value
        super().__init__(f'{message} Invalid value: {value}')

from typing import List, Union

class NumberAnalyzer:
    def __init__(self, numbers: List[Union[int, float]]):
        self.numbers = numbers

    def validate_numbers(self) -> None:
        self.check_empty_list()
        self.check_non_numeric_values()

    def check_empty_list(self) -> None:
        if not self.numbers:
            raise EmptyListError()

    def check_non_numeric_values(self) -> None:
        for value in self.numbers:
            if not isinstance(value, (int, float)):
                raise NonNumericValueError(value)

    def find_maximum(self) -> Union[int, float]:
        self.validate_numbers()
        return max(self.numbers)

    """
    Example Usage:
    na = NumberAnalyzer([1, 2, 3])
    max_value = na.find_maximum()  # Should return 3
    
    # Test Cases:
    # Valid case:
    # na = NumberAnalyzer([1, 2, 3])
    # assert na.find_maximum() == 3
    # Invalid case – Empty List:
    # na = NumberAnalyzer([])
    # try:
    #     na.find_maximum()
    # except EmptyListError as e:
    #     print(e)  # Should print: The input list cannot be empty.
    # Invalid case – Non-numeric Value:
    # na = NumberAnalyzer([1, 'a', 3])
    # try:
    #     na.find_maximum()
    # except NonNumericValueError as e:
    #     print(e)  # Should print: All elements must be numeric. Invalid value: a
    """