"""
1. How to swap two variables in python without using a third variable?
2. What will be the output of following code?
"""

a = 1
b = 2
a, b = b, a   # Tuple packing / unpacking

names = ["Jon", "Jane", "Eren", "Ragnar", "Arya"]
print(list(enumerate(names)))

# a = [(0, "John"), (1, "Jane"), (2, "Eren")]

for index, value in enumerate(names):
    print(index)
    print(value)
