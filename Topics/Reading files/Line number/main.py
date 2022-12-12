# read sample.txt and print the number of lines

# Below produces a lot of style warnings, so had to refactor
# https://wemake-python-stylegui.de/en/latest/pages/usage/violations/refactoring.html#wemake_python_styleguide.violations.refactoring.ImplicitSumViolation
# n = 0
# file = open("sample.txt", "r")
# for _ in file:
#    n += 1
# file.close()

# This works fine and accepted without warnings
# with open("sample.txt", "r") as f:
#    n = len(f.readlines())
#    print(n)

# https://www.programiz.com/python-programming/generator
with open('sample.txt', 'r') as file_in:
    print(sum(1 for _ in file_in))

