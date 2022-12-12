# put your python code here
a = float(input())
b = float(input())
op = input()

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/" or op == "mod" or op == "div":
    if b == 0:
        print("Division by 0!")
    else:
        if op == "/":
            print(a / b)
        elif op == "mod":
            print(a % b)
        elif op == "div":
            print (a // b)
elif op == "pow":
    print (a ** b)




