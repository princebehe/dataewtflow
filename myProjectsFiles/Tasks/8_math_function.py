def calculate(a, b):
    total_sum = a + b
    difference = a - b
    product = a * b
    return total_sum, difference, product

s, d, p = calculate(10, 5)
print(f"Sum: {s}, Difference: {d}, Product: {p}")