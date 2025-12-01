def get_input_range():
    while True:
        try:
            start = int(input('Enter the start of the range (positive integer): '))
            end = int(input('Enter the end of the range (positive integer): '))
            if start < 0 or end < 0:
                print('Please enter positive integers for the range.')
                continue
            return start, end
        except ValueError:
            print('Invalid input. Please enter valid integers for the range.')


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def print_prime_numbers(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes


if __name__ == '__main__':
    start, end = get_input_range()
    prime_numbers = print_prime_numbers(start, end)
    print(f'Prime numbers between {start} and {end}: {prime_numbers}')

