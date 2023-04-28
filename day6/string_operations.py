a = "Hello"
b = "World"
print(a + b)  # + operator is used for string concatenation.
# Result is HelloWorld

print(a * 3)  # * is used as a broadcast operator. Result is "HelloHelloHello"
print("H" in a)  # This returns True
print("W" not in b)  # This returns False


# Accessing the string elements
# String elements can be accessed with indexing and slicing just like in the List and Tuples.
# But item assignment in any particular index is not possible in the string as it is immutable.

# a[1] = "Z"   # This is not possible in string.
