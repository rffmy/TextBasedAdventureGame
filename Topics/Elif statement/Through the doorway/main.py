a = int(input())
b = int(input())
c = int(input())
x = int(input())
y = int(input())

if a > x and b > y or a > y and b > x:
    print("The box cannot be carried")
elif a > x and c > y or a > y and c > x:
    print("The box cannot be carried")
elif b > x and c > y or b > y and c > x:
    print("The box cannot be carried")
else:
    print("The box can be carried")
