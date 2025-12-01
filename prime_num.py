from typing import List


def generate_prime_numbers(n: int) -> List[int]:
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


def get_input_range() -> tuple:
    while True:
        try:
            start = int(input("Enter the start of the range: "))
            end = int(input("Enter the end of the range: "))
            if start < 0 or end < 0:
                print("Please enter non-negative integers.")
                continue
            if start > end:
                print("Start must be less than or equal to end.")
                continue
            return start, end
        except ValueError:
            print("Invalid input. Please enter valid integers.")


def display_primes(primes: List[int]) -> None:
    if primes:
        print("Prime numbers:", primes)
    else:
        print("No prime numbers found in this range.")


def main() -> None:
    start, end = get_input_range()
    prime_numbers = generate_prime_numbers(end)
    display_primes([num for num in prime_numbers if num >= start])


if __name__ == '__main__':
    main()