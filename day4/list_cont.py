a = [(4, 12, 5), (6, 1), (11, 12), (6, 7, 8)]


def get_last_num(item):
    return item[-1]


a.sort(key=get_last_num)
print(a)


# Reversing List

a = ['mango', 'banana', 'grapes', 'apple']
a.reverse()
print("Reversed => ", a)


# Shallow Copy and Deep Copy ##########

a = [[1, 2, 3], [4, 5]]
b = a

# This gives True. Here both a and b refer to the same list object. b is
# not a copy of a.
print(a is b)


b = a.copy()   # b is a shallow copy of a
# But in shallow copy, the mutable elements inside the list still refers
# to the same object. Thus, to completely copy the list, we need to deepcopy
b[0][1] = 5
print(a)
print(b)  # Here change occurs in both a and b because of shallow copy

from copy import deepcopy
b = deepcopy(a)
b[0][1] = 2
print(a)
print(b)  # Here change occurs only in b but not in a because of deepcopy
