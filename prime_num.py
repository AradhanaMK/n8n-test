def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_range_input():
    while True:
        try:
            range_start = int(input("Enter the start of the range: "))
            range_end = int(input("Enter the end of the range: "))
            if range_start <= range_end:
                return range_start, range_end
            else:
                print("Start must be less than or equal to end.")
        except ValueError:
            print("Please enter valid integers.")


def print_prime_numbers(range_start, range_end):
    prime_numbers = [num for num in range(range_start, range_end + 1) if is_prime(num)]
    print(f"Prime numbers between {range_start} and {range_end}: {prime_numbers}")


def main():
    range_start, range_end = get_range_input()
    print_prime_numbers(range_start, range_end)


if __name__ == '__main__':
    main()