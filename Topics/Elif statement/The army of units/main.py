i = int(input())
if i < 1:
    print("no army")
elif i < 10:
    print("few")    
elif i < 50:
    print("pack")
elif i < 500:
    print("horde")
elif i < 1000:
    print("swarm")
else:
    print("legion")
