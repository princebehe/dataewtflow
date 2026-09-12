numbers = [12, 45, 2, 89, 23, 56]
largest = numbers[0]
for n in numbers:
    if n > largest:
        largest = n
print(f"The largest number is {largest}.")