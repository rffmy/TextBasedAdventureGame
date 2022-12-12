# read sums.txt
file = open('sums.txt', 'r')

for line in file:
    x, y = line.split()
    print(int(x) + int(y))

file.close()
