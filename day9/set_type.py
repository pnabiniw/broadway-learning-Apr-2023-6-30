# Methods in set

s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s.remove(9)
print(s)   # It removes 9 from the given set

s.discard(2)  # It removes 2 from the given set
print(s)

# The difference between remove and discard, if any key not present in
# the set is provided to the discard() then it returns None but the
# remove() method raises KeyError

value = s.pop()  # It randomly pops out the element from the set and return that element
print(value)
print(s)

s.clear()  # This clears the set


s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

s = s1.union(s2)   # This gives union of s1 and s2
print(s)  # Result {1, 2, 3, 4, 5, 6, 7, 8}

s = s1.intersection(s2)  # It gives intersections
print(s)  # Result => {4, 5}

s = s1.difference(s2)   # It gives s1 - s2
print(s)  # Result => {1, 2, 3}

print(s1.isdisjoint(s2))  # This gives False because they have common value {4, 5}

s = s1.symmetric_difference(s2)  # This is equivalent to complement of A intersection B
print(s)  # Result => {1, 2, 3, 6, 7, 8}

s1.symmetric_difference_update(s2)
print(s1)
# This updates the existing set s1 with new values of symmetric difference. It doesn't
# return anything but updates the set which calls it, here s1.

s1 = {1, 2, 3, 4, 5, 6, 7}
s2 = {2, 3, 4}
print(s2.issubset(s1))   # This gives True
print(s2.issuperset(s1))  # This gives False
print(s1.issuperset(s2))  # This gives True


# We can use bitwise operators for union, intersection, difference and symmetric
# difference in set

s = s1 | s2  # This is union operation
print(s)

s = s1 & s2  # This is intersection operation
print(s)

s = s1 - s2  # This is difference operation
print(s)

s = s1 ^ s2  # This gives symmetric difference
print(s)

