def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_prime_numbers(start: int, end: int) -> list[int]:
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes


def get_input_range():
    while True:
        try:
            start = int(input('Enter the start of the range (positive integer): '))
            end = int(input('Enter the end of the range (positive integer): '))
            if start < 0 or end < 0:
                raise ValueError('Input must be a positive integer.')
            if start > end:
                raise ValueError('Start must be less than or equal to end.')
            return start, end
        except ValueError as e:
            print(e)


def display_prime_numbers(prime_numbers: list[int]) -> None:
    if not prime_numbers:
        print('No prime numbers found in the specified range.')
    else:
        print('Prime numbers in the specified range:', prime_numbers)


if __name__ == '__main__':
    start, end = get_input_range()
    prime_numbers = generate_prime_numbers(start, end)
    display_prime_numbers(prime_numbers)