#  You can experiment here, it won’t be checked
import time

out2 = open('file2.txt', 'w')

for i in range(3):
    print(i, file=out2, flush=True)
    # the numbers are immediately written to the file
    time.sleep(5)

out2.close()
