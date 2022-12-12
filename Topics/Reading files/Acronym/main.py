# read test.txt
with open("test.txt", 'r') as test_file:
    for line in test_file:
        print(line[:1])
