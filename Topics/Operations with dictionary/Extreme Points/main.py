# import json
# import sys

# The following line creates a dictionary from the input. Do not modify it, please
test_dict = json.loads(input())
# {"a": 43, "b": 1233, "c": 8}

# https://docs.python.org/3.9/library/functions.html#min
# https://stackoverflow.com/questions/39496096/understanding-dictionary-get-in-python
print("min: %s" % min(test_dict.keys(), key=test_dict.get,
                      default="Empty json!"))
print("max: %s" % max(test_dict.keys(), key=test_dict.get,
                      default="Empty json!"))

# ---- explicit for loop to find min and max -----
# max_v = -sys.maxsize - 1
# min_v = sys.maxsize
#
# Work with the 'test_dict'
# for (k, v) in test_dict.items():
#    if v > max_v:
#        max_v = v
#        max_k = k
#    if v < min_v:
#        min_v = v
#        min_k = k
#
# print("min: %s" % min_k)
# print("max: %s" % max_k)
