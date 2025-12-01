class EmptyListError(Exception):
    pass

class NonNumericValueError(Exception):
    def __init__(self, value):
        super().__init__(f"Non-numeric value encountered: {value} (expected a numeric value)")

class NumberAnalyzer:
    def __init__(self, numbers):
        self.numbers = numbers

    def check_empty_list(self) -> None:
        if not self.numbers:
            raise EmptyListError("The list of numbers cannot be empty.")

    def check_non_numeric_values(self) -> None:
        for value in self.numbers:
            if not isinstance(value, (int, float)):
                raise NonNumericValueError(value)

    def analyze(self) -> dict:
        self.check_empty_list()
        self.check_non_numeric_values()
        return {
            "count": len(self.numbers),
            "sum": sum(self.numbers),
            "average": sum(self.numbers) / len(self.numbers)
        }

# Example usage:
# analyzer = NumberAnalyzer([1, 2, 3])
# print(analyzer.analyze())

