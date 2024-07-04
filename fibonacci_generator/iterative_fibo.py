def fibonacci(n):
    fibonacci = [0, 1]
    for i in range(1, n):
        fibonacci.append((fibonacci[i] + fibonacci[i - 1]))
    return fibonacci[:n]


user_input = input("Enter the number sequence to generate the  series: ")

try:
    n = int(user_input)
    if n < 0:
        print("Please enter a non-negative integer.")
    else:
        print(fibonacci(n))
except:
    print("Invalid Input. Please enter an integer.")
