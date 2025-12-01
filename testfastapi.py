from typing import List

class NumberAnalyzer:
    def __init__(self, numbers: List[float]):
        self.numbers = numbers

    def analyze(self):
        ":return: A dictionary containing the max, min, and average of the numbers"
        return {
            'max': self.find_max(),
            'min': self.find_min(),
            'average': self.find_average(),
        }

    def find_max(self) -> float:
        """
        :return: The maximum number from the list.
        :raises ValueError: If the list is empty.
        """
        if not self.numbers:
            raise ValueError('Cannot find max of an empty list.')
        return max(self.numbers)

    def find_min(self) -> float:
        """
        :return: The minimum number from the list.
        :raises ValueError: If the list is empty.
        """
        if not self.numbers:
            raise ValueError('Cannot find min of an empty list.')
        return min(self.numbers)

    def find_average(self) -> float:
        """
        :return: The average of the numbers. If the list is empty, returns 0.
        """
        return sum(self.numbers) / len(self.numbers) if self.numbers else 0.0

# Example usage (to be moved to a separate test file)
# if __name__ == '__main__':
#     analyzer = NumberAnalyzer([1.5, 2.5, 3.0])
#     results = analyzer.analyze()
#     print(results)  # Output should show max, min, and average