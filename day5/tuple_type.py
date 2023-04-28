#### Tuple Packing and Unpacking

a = 1, 2, 3   # Note there is no small bracket but this still creates a tuple and
# called  tuple packing

# The elements in the RHS are assigned to each variables in the LHS. This is called tuple
# unpacking
a, b, c = 1, 2, "Hello World"
print(a, b, c)


# we can swap the variables in python without the third temporary variable using tuple
# unpacking
a = 1
b = 2
a, b = b, a   # b,a is unpacked to variables a, b


# Tuple Slicing

a = (1, 2, 3, 4, 5, 6, 7)
print(a[:])  # This gives all the elements in the tuple

print(a[::2])   # This traverse through all the elements in the tuple but returns the
# elements on the jump of one  => (1, 3, 5, 7)


# Negative step slicing

a = (0, 1, 3, 4, 5, 6, 7)
print(a[-1: -6: -1])   # This gives (6, 5, 4, 3)

print(a[::-1])  # This reverses the tuple (7, 6, 5, 4, 3, 2, 1)


# Tuple Operations #

a = (1, 2, 3)
b = (4, 5, 6)
print(a + b)  # This gives a third tuple a + b

print(a * 3)  # This gives (1, 2, 3, 1, 2, 3, 1, 2 ,3)

print(1 in a)  # Membership check; this gives True
print(5 in a)  # This gives False
print(4 not in b)  # This gives False


### There are only two methods in tuple data type, count() and index()

a = (1, 2, 3, 1, 2, 2, 3, 3, 3, 4, 1)
c = a.count(1)   # This returns the count of the element provided as the parameter
print(c)

i = a.index(2)  # This gives 1 as the first index of 2 is 1
print(i)
i = a.index(1, 1, 4)  # This gives 3 as it searches 1 in range 1 to 4
print(i)



#### Built-in functions  #####

a = (1, 2, 3, 4)
print(sum(a))  # This returns the sum of all the elements inside the sequence, here, tuple

print(max(a))  # This gives 4
print(min(a))   # This gives 1


print(sorted(a))   # This sorts the elements in the tuple (1, 2, 3, 4)
c = list(reversed(a))  # This reverses the tuple
print(c)


