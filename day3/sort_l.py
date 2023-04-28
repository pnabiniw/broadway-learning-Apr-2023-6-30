l1 = [(2, 3), (1, 1), (4, 2), (5, 5), (2, 4)]


def second_num(data):
    return data[1]


print("Before sorting => ", l1)

l1.sort(key=second_num)
print("After sorting => ", l1)
