"""
Use filter() function and lambda to filter the tuples from the list whose elements
sum is greater than 10

"""

data = [(1, 2, 3), (15, 5), (8, 1, 1), (20, 21), (10, 20, 30)]


def greater_than_10(data):
    return sum(data) > 10


result = list(filter(lambda x: sum(x) > 10, data))
print(result)
