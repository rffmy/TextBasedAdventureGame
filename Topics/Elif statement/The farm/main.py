money = int(input())

sheep = money // 6769
cows = money // 3848
pigs = money // 1296
goats = money // 678
chickens = money // 23

if sheep >= 1:
    print(str(sheep) + " sheep")
elif cows >= 2:
    print(str(cows) + " cows")
elif cows == 1:
    print(str(cows) + " cow")
elif pigs >= 2:
    print(str(pigs) + " pigs")
elif pigs == 1:
    print(str(pigs) + " pig")
elif goats >= 2:
    print(str(goats) + " goats")
elif goats == 1:
    print(str(goats) + " goat")
elif chickens >= 2:
    print(str(chickens) + " chickens")
elif chickens == 1:
    print(str(chickens) + " chicken")
else:
    print("None")
