#### String formatting with % #####

# %s is for string
# %d is for integer
# %f is for float values

message = "Hello from %s. I'm learning %s" % ("Broadway", "Python")
print(message)
m = "Hello I'm %d years old" % (25)
print(m)


# format() method in string

m = "Hello I'm {}".format("John Doe")
print(m)

m = "I'm {age} years old".format(age=45)
print(m)

# We can also include positions in the placeholder
m = "I have {1}, {0} and {2}".format("pen", "pencil", "book")
print(m)   # This gives => I have pencil, pen and book

# If we don't mention the position then the values are taken in order
m = "I have {}, {}, {}".format("pen", "pencil", "book")
print(m)  # Result => I have pen, pencil, book


# m = "I have {}, {}, and {}".format("pen", "pencil")   # This gives error because one of
# the placeholders can't fill the value

m = "I have {1} and {2}".format("pen", "pencil", "book")  # But this doesn't raise error
print(m)

# This also raises error
# m = "I have {0}, {} and {}".format("pen", "pencil",  "book")

m = "I have {item1}, {item2} and {item3}".format(item1="pen", item2="pencil", item3="book")
print(m)

# Position of keyword arguments doesn't matter
m = "I have {item1}, {item2} and {item3}".format(item2="pen", item1="pencil", item3="book")
print(m)

# But positional argument can't be given after a keyword argument in any python functions
# m = "I have {item1}, {item2} and {item3}".format(item1="pen", "pencil", item3="book")
# This raises error


# F-strings
item1 = "pen"
item2 = "pencil"
item3 = "book"

m = f"I have {item1}, {item2} and {item3}"
print(m)

# We can directly write string inside the placeholder
m = f"I have {'pen'}, {'pencil'} and {'book'}"
print(m)

# F-strings are also valid for triple quoted string
m = f"""
I have {item1} and {item2}
"""
print(m)
