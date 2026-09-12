n = 10
fib = [0, 1]
for i in range(2, n):
    fib.append(fib[-1] + fib[-2])
print("First 10 Fibonacci numbers:", fib)