# Exception Handling

x = int(input("Enter first number : "))
y = int(input("Enter second number : "))

try:
    z = x/y
    print("Division Result : ", z)
except ZeroDivisionError:
    print("Invalid attempt to divide")
