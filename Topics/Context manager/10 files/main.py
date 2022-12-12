# write your code here
max_count = 11
for i in range(1, max_count):
    # filename = 'file' + str(i) + '.txt'
    # https://hyperskill.org/learn/step/6037
    # Formatted string literals
    filename = f'file{i}.txt'
    with open(filename, 'w') as f:
        f.write(str(i))
