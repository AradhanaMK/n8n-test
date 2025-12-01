def get_non_negative_integer_range():
    while True:
        try:
            start = int(input("Enter the start of the range (non-negative integer): "))
            if start < 0:
                print("Please enter a non-negative integer.")
                continue
            end = int(input("Enter the end of the range (non-negative integer): "))
            if end < 0:
                print("Please enter a non-negative integer.")
                continue
            return start, end
        except ValueError:
            print("Invalid input. Please enter a non-negative integer, for example, '5' instead of 'five'.")


def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def generate_prime_numbers(start: int, end: int):
    prime_numbers = []
    for num in range(start, end + 1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers


def display_primes(prime_numbers):
    for prime in prime_numbers:
        print(prime)


def main():
    start, end = get_non_negative_integer_range()
    prime_numbers = generate_prime_numbers(start, end)
    display_primes(filter(lambda num: num >= start, prime_numbers))


if __name__ == '__main__':
    main()