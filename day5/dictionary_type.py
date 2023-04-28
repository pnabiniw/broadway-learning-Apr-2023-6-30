### Dictionaries are the key-value pairs built inside the curly-braces separated by commas.
# We can also use a dict() function to create a dictionary

a = {}  # This is an empty dictionary
a = dict()  # This also creates an empty dictionary
student = {"name": "Jon", "age": 24}  # creating dictionary with curly braces
print(student)
student = dict(name="Jon", age=34)   # creating dictionary with dict() function
print(student)


### Accessing dictionary values
# Dictionary values can be accessed using big brackets [] or using get() method

 # This returns None
print(student["name"])  # Getting value using brackets
print(student.get("name"))  # Getting value using get() method

print(student["id"])  # This raises KeyError because 'id' key is not present in the dictionary
print(student.get('id'))
