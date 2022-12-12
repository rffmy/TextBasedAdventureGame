# put your python code here
a = int(input())
b = int(input())

nums = []

for i in range(a, b + 1):
    if i % 3 == 0:
        nums.append(i)

avg = sum(nums) / len(nums)
print(avg)
