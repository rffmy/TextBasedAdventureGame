score = int(input())
max_score = int(input())

pct = score / max_score

grades = {"B": 0.9, "C": 0.8, "D": 0.7, "F": 0.6}

if pct < grades["F"]:
    print("F")
elif pct < grades["D"]:
    print("D")
elif pct < grades["C"]:
    print("C")
elif pct < grades["B"]:
    print("B")
else:
    print("A")
