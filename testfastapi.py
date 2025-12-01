from typing import List, Union

class NumberAnalyzer:
    """
    A class to analyze a list of numbers.
    """

    def __init__(self, numbers: List[Union[int, float]]) -> None:
        self.numbers = numbers
        self.validate_numbers()

    def validate_numbers(self) -> None:
        """
        Validates the numbers list to ensure it contains only numeric values.
        Raises EmptyListError if the list is empty and raises NonNumericValueError for non-numeric values.
        """
        if not self.numbers:
            raise EmptyListError("The list is empty.")
        for number in self.numbers:
            if not isinstance(number, (int, float)):
                raise NonNumericValueError(f"Non-numeric value found: {number}")

    def find_maximum(self) -> Union[int, float]:
        """
        Returns the maximum value from the list of numbers.
        """
        return max(self.numbers)

class EmptyListError(Exception):
    pass

class NonNumericValueError(Exception):
    pass

# Example usage:
# analyzer = NumberAnalyzer([1, 2, 3, 4, 5])
# print(analyzer.find_maximum())  # Output: 5
