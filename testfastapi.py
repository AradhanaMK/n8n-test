class NumberAnalyzer:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_max(self):
        """
        Returns the maximum number from the list of numbers.
        If the list is empty, returns None.
        """
        if not self.numbers:
            return None
        return max(self.numbers)

    def find_min(self):
        """
        Returns the minimum number from the list of numbers.
        If the list is empty, returns None.
        """
        if not self.numbers:
            return None
        return min(self.numbers)

    def find_average(self) -> float:
        """
        Returns the average of the list of numbers.
        If the list is empty, returns 0.0.
        
        :return: float
        """
        if not self.numbers:
            return 0.0
        return sum(self.numbers) / len(self.numbers)

    def analyze(self) -> dict:
        """
        Analyzes the list of numbers and returns a summary with max, min, and average.
        
        :return: dict containing the max, min, and average values.
        """
        return {
            'max': self.find_max(),
            'min': self.find_min(),
            'average': self.find_average()
        }

# Example Usage:
# numbers = [1, 2, 3, 4, 5]
# analyzer = NumberAnalyzer(numbers)
# print(analyzer.analyze())  # Should output: {'max': 5, 'min': 1, 'average': 3.0}

# Note: Example usage should be moved to a separate test file.