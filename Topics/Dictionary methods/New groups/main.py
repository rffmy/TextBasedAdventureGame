# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

# your code here
n = int(input())

count_in_groups = dict.fromkeys(groups)

i = 1

for group in groups:
    if i > n:
        break
    count_in_group = int(input())
    count_in_groups[group] = count_in_group
    i = i + 1

print(count_in_groups)
