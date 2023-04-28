# Set is an unordered data-type in python
# Set is mutable but it's values must be immutable
# We create set using curly braces for e.g. {1, 2, 3, "Hello"}
# To create an empty set we use set() built-in function
# Note: {}  => This is an empty dictionary and not an empty set

s = {1, 2, 3}  # Non-empty set
s = set()  # This is an empty set
# a = {[1, 2, 3], 3}  # This is invalid because it has an mutable type list


# Adding and Removing set items
s.add(4)  # this adds 4 in the set at arbitrary position
s.update([5, 6, 7])  # this adds 5, 6 and 7 in the set at random position
