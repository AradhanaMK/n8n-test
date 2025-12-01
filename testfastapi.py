class NumberAnalyzer:
    def __init__(self, numbers: list[float]) -> None:
        self.numbers = numbers

    def validate_numbers(self) -> None:
        if not all(isinstance(num, (int, float)) for num in self.numbers):
            raise TypeError("All items in the list must be numbers.")

    def analyze(self) -> dict:
        self.validate_numbers()
        total = sum(self.numbers)
        count = len(self.numbers)

        return {
            'count': count,
            'sum': total,
            'average': total / count if count > 0 else 0
        }

    def find_max(self) -> float:
        self.validate_numbers()
        return max(self.numbers)

    def find_min(self) -> float:
        self.validate_numbers()
        return min(self.numbers)

# Example usage:
# analyzer = NumberAnalyzer([1, 2, 3, 4])
# result = analyzer.analyze()
# print(result)