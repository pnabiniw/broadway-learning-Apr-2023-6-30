# Lambda / Anonymous functions

def addition(a, b):
    return a + b


addition(5, 6)

add = lambda a, b: a + b
print(add(2, 3))

# import os
# def clear():
#     os.system('cls')
#
# clear()

# clear = lambda : os.system('cls')
# clear()


a = [(2, 5), (1, 3), (7, 2)]

a.sort(key=lambda data: data[1])
print(a)

# d = {"Ram": 45, "Shyam": 50}
# name = input("Enter the user name ")
# age = lambda name: d[name]
# print(age(name))


# Map function
b = []
for i in a:
    b.append(i * 2)

a = [1, 2, 3, 4, 5]
changed_a = [i * 2 for i in a]  # List comprehension
print(changed_a)


def get_multiple_of_two(data):
    return data * 2


# Map function takes two arguments, function and an iterable
result = map(get_multiple_of_two, a)
print(list(result))

result = map(lambda data: data * 2, a)
print(list(result))

# Filter function

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [i for i in a if i % 2 == 0]  # List comprehension

result = filter(lambda value: value % 2 == 0, a)
print(list(result))

students = [{
    "name": "Jon",
    "age": 23
},
    {
        "name": "Jane",
        "age": 65
    },
    {
        "name": "Arya",
        "age": 19
    }, {
        "name": "Ben",
        "age": 45
    }
]
result = filter(lambda data: data['age'] <= 20, students)
print(list(result))


# Reduce function
from functools import reduce

a = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, a)
print(result)

