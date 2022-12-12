# write your code here
months_per_year = 12
with open('salary.txt', 'r') as infile, \
        open('salary_year.txt', "w") as outfile:
    for line in infile.readlines():
        outfile.write(str(int(line) * months_per_year) + "\n")


