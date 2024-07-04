def fibonacci():
    a = 0
    b = 1
    for i in range(7):
        yield b
        a, b = b, a + b


user_input = input("Enter the number sequence to generate the  series: ")

try:
    n = int(user_input)
    if n < 0:
        print("Please enter a non-negative integer.")
    else:
        print(fibonacci(n))
except:
    print("Invalid Input. Please enter an integer.")
