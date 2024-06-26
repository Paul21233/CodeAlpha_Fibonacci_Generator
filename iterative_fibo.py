def fibonacci(n):
    fibonacci = [0, 1]
    for i in range(1, n):
        fibonacci.append((fibonacci[i] + fibonacci[i - 1]))
    return fibonacci[:n]


print(fibonacci(8))
