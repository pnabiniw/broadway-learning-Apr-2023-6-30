s = {
    "name": "Jon",
    "email": "jon@gmail.com",
    "address": "KTM"
}

### all() built-in function. This function takes iterable (sequence) as a
# parameter and returns True if all the elements of the sequence are truthy. In case of dictionary
# it checks the key of the dictionary

print(all(s))  # It gives True as all the keys of the dictionary (name, email, address) are truthy
print(all([]))  # This is an exception in the all() function because it returns True

a = {"": 1}  # This is a valid dictionary. An empty string is a key with value 1
print(all(a))  # This returns False because the dictionary has a Falsy key


# any() built-in functiona also takes iterable (sequence) as a parameter. But it returns True
# if at least one of the elements is Truthy
b = {0: "Hello", 1: "World"}
print(any(b))  # This returns True because one of the keys (i.e. 1) is Truthy

# But if all the keys are Falsy then it returns False
b = {"": "Hello", 0: "World"}
print(any(b))  # This returns False


student = {"name": "Jon", "age": 23}
print(sorted(student))  # It sorts the keys of the dictionary in alphabetical order.
# It returns ["age", "name]
