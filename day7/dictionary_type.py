### Dictionary Methods

student = {"name": "Jane", "age": 45, "dept": ["CS", "Civil"]}
# student.clear()  # This clears the dictionary
s = student.copy()  # This is shallow copy

# This returns a dictionary {1: "Hello World", 2: "Hello World", 3: "Hello World"}
print(s.fromkeys([1, 2, 3], "Hello World"))


# If second parameter i.e. value not provided then None is considered
# {1: None, 2: None, 3: None}
print(s.fromkeys([1, 2, 3]))

print(student.items())  # it returns list-like object of tuples containing (key, value) pair
# [("name", "Jane"), ("age", 45), ("dept",  ["CS", "Civil"])]

print(student.keys())  # it returns list-like object of dictionary keys ["name", "age", "dept"]
print(student.values())  # it returns list-like object of dictionary values ["Jane", 45, ["CS", "Civil"]]

student.setdefault("name", "Jon")   # name key with value Jane is already present in the
# dictionary, so default value Jon is not considered

student.setdefault("id", 1)  # id key is not present in the dictionary. So, it is added in the
# dictionary with its default value 1


# Task 1 => Area of a circle
radius = int(input('Enter a radius of a circle '))
area = (22 / 7) * radius ** 2
print("Area of the circle is ", area)

# Task 2 => Frequency of the input number
a = [5, 2, 3, 5, 3, 2, 3, 3, 1, 4]
value = int(input("Enter the number "))
count = a.count(value)
print(f"Frequency of {value} is", count)
