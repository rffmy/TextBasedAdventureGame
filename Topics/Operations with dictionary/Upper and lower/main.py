# the list with words from string
# please, do not modify it
some_iterable = input().split()

# use dictionary comprehension to create a new dictionary
upper_and_lower = {word.upper(): word.lower() for word in some_iterable}
print(upper_and_lower)