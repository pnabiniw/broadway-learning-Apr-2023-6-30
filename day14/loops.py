# Looping in list

vowels = ["a", "e", "i", "o", "u"]
for vowel in vowels:
    print(vowel)

nums = [1, 2, 3, 4]
new_nums = []
for num in nums:
    value = num * 2
    new_nums.append(value)
print(new_nums)


# Looping in Tuple
a = (1, 2, 3, 4)
for i in a:
    print(i)

# Looping in String
message = "Hello World"
for i in message:
    print(i)

# Looping in Set
vowels = {"a", "e", "i", "o", "u"}
for vowel in vowels:
    print(vowel)


# Looping in Dictionary
student = {"name": "Jon", "age": 45, "department": "CS"}

for key in student:
    print(key)


values = student.values()
for value in values:
    print(value)


keys = student.keys()
for key in student:
    print(key)

for item in student.items():
    print(item)


for key, value in student.items():
    print(key)
    print(value)


# Range function in python
# Range returns an iterator which can be iterated through

first_ten_natural_numbers = range(1, 11)
for num in first_ten_natural_numbers:
    print(num)

for num in range(5):   # It gives 0, 1, 2, 3, 4
    print(num)

for num in range(0, 10, 2):
    print(num)    # It gives 0, 2, 4, 6, 8

for reversed_num in range(10, 1, -1):
    print(reversed_num)

for reversed_num in range(10, 1, -2):
    print(reversed_num)


# If we don't want the loop value inside the loop then we can use underscore
for _ in range(5):
    print("Hello World")  # This prints "Hello World" 5 times

