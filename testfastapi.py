from typing import List

class NumberList:
    def __init__(self, numbers: List[float]):
        self.numbers = numbers

    def find_maximum_in_list(self) -> float:
        """Finds the maximum number in the list.

        Raises:
            ValueError: If the list is empty or contains non-numeric values.

        Returns:
            float: The largest number in the list.
        """
        if not self.numbers:
            raise ValueError("The list is empty. Please provide a list with numbers.")

        largest = self.numbers[0]
        for number in self.numbers:
            if not isinstance(number, (int, float)):
                raise ValueError("All items in the list must be numbers.")
            if number > largest:
                largest = number

        return largest

# Example usage
if __name__ == '__main__':
    num_list = NumberList([2, 3, 1, 5, 4])
    print(num_list.find_maximum_in_list())  # Should output 5