def fibonacci():
    a = 0
    b = 1
    for i in range(7):
        yield b
        a, b = b, a + b


obj = fibonacci()

print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
