# True and False are the boolean data types.
# All the relational, logical, identity and membership operations
# returns boolean data type

a = 5
b = 4

# Relational operations
print(a == b)
print(a > b)

# Logical operations
print(bool(a) and bool(b))  # This gives True
b = 0
print(bool(a) and bool(b))  # This gives False
print(a or b)

# Identity operations
print(a is b)
print(a is not b)

# Membership operations
print(2 in [1, 2, 3])
print(4 not in [1, 2, 3])


# Boolean class is the subclass of the integer class so True => 1
# and False => 0

print(True + 1)  # This gives 2 because True means 1
print(False * 70)  # This gives 0


# Concept of Truthy and Falsy
# Any non-empty list, string, tuple, set, dictionary is a truthy value.
# In contrast, all the empty list, string, tuple, set, dictionary is a
# Falsy value including 0 for integer

print(bool(1))  # True
print(bool(0))  # False

print(bool([1, 2]))  # True because it non-empty list
print(bool([]))  # False

print(bool(None))  # It gives False
print(bool(True))  # It gives True
print(bool(False))  # It gives False
