# squares = {1: 1, 3: 9, 5: 25, 6: 36}

key_to_delete = int(input())

if key_to_delete in squares:
    print(squares[key_to_delete])
    del squares[key_to_delete]
else:
    print("There is no such key")

print(squares)
