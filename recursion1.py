
def add(a, b):
    if b == 0:
        return a
    return add(a + 1, b - 1)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = add(num1, num2)

print("Sum:", result)
