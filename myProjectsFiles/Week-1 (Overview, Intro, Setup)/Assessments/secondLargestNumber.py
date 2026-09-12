nums = [10, 20, 4, 45, 99]
unique_nums = sorted(list(set(nums)))
second_largest = unique_nums[-2] if len(unique_nums) >= 2 else None
print(second_largest)