import sys

n = int(input())

if n < 1 or n > 100:
    # Consider using sys.exit()
    # exit(1)
    sys.exit()

factorial = 1

while n > 0:
    factorial *= n
    n -= 1

print(factorial)
