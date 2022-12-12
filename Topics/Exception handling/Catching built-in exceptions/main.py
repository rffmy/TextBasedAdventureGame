a = int(input())
b = int(input())

try:
    c = a / b
except ZeroDivisionError:
    print("The Error!")
else:
    print(c)