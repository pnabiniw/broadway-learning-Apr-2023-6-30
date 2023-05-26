"""
1. What are the methods to get keys, values and key-value pair in dictionary?
2. How to loop in key-value pair?

"""

d = {1: 1, 2: 2}
d.values()
d.keys()
d.items()

for key, value in d.items():
    print(key)
    print(value)
