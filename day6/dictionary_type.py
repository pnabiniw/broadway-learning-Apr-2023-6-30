## Accessing dictionary values

student = {"name": "Jon", "age": 23, "department": "CS"}

print(student["name"])  # This gives Jon
print(student["age"])   # This gives 23
# print(student["id"])    # This raises KeyError

# We can also use get() method in dictionary to access the value
print(student.get("name"))  # This also gives Jon

# But if the key is not present in the dictionary then it gives None
print(student.get("id"))  # This gives None as id key is not present in the dictionary

# We can also give a default value to the get() method
print(student.get("id"))  # This gives value 3 for the id key

# But if we give default value to the key already present in the dictionary,
# it ignores the default value
print(student.get("name", "Jane"))  # It gives Jon and the value Jane is ignored




#### Adding and Updating dictionary values

# if the key id is not present in the dictionary then it adds the key and assign the value 4
student["id"] = 4
print(student)

# If the key id is already present in the dictionary then it updates the value in the id,
# in this case 5
student["id"] = 5   # id 4 is updated to 5
student["name"] = "Jane"  # name in the dictionary Jon is updated to Jane


# We can also use update() method to update the existing dictionary
further_info = {"email": "jane@gmail.com", "address": "Kalanki"}

# This gives {"name": "Jane", "age": 23, "department": "CS", "id": 5,
# "email": "jane@gmail.com", "address": "Kalanki"}
student.update(further_info)
print(student)


# Removing items from the dictionary

# pop() method takes key as a parameter. It removes the provided key-value pair from the dictionary
# and returns the value
a = student.pop("address")  # this pops out the address from the dictionary and value is
# assigned to the 'a' variable
print(student)
print(a)


# If we try to pop out the key not present in the dictionary then it raises KeyError
# student.pop("height")  # This raises error because "height" key is not present in the dictionary

# But we can assign a default value
height = student.pop("height", 5.9)   # This gives 5.9 in the height variable
print(height)


data = student.popitem()   # This pops out the last key-value pair from the dictionary and returns
# a (key, value) tuple

print(data)  # result will be ("address", "Kalanki")

# student.clear()  # clears out the entire dictionary elements
# del student  # deletes the student dictionary object


# Restrictions in dictionary Keys

# 1. Dictionary keys must be immutable
# 2. Tuples can be used as the dictionary key until it has no any mutable values
# 3. If a key is repeated then the last assigned key is considered.

a = {(1, 2): 1}   # This is valid
a = {(1, [1, 2]): 2}  # This is invalid
