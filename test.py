numbers = [10, 25, 3, 99, 56, 78]

largest = numbers[0]   # assume first number is largest

for num in numbers:
    if num > largest:
        largest = num

print("Largest number:", largest)
