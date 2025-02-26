factorial = lambda n: 1 if n == 0 or n == 1 else n * factorial(n - 1)

num = int(input("Enter a number: "))
print("Factorial:", factorial(num))
