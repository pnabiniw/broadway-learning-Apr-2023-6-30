# Built-in functions for strings


a = 'Hello Broadway'
print(len(a))
print(bool(a))


# We can also use slice() built-in function
value = a[slice(2, 8)]
print(value)   # This is same as a[2:8]

print(type(a))   # This gives type of 'a' i.e. string



# String Methods

a = "Hello World. I'm learning Python"
print(a.capitalize())  # This capitalizes first letter of the first word in a sentence
print(a.title())  # This capitalizes first letter of every word in a sentence
print(a.upper())  # This capitalizes all the letters in a sentence
print(a.lower())  # This makes all the letter in a sentence in small/lower case


result = a.split()  # This splits the string with space and returns a list
# => ["Hello", "World.", "I'm", "learning", "Python"]
print(result)


# join() is a string method that joins the elements of a list by the string which
# calls the join()
messages = ["Hello", "World"]
" ".join(messages)  # "Hello World"
"+".join(messages)  # "Hello+World"

a = "Hello World. I'm learning Python"
a.find("World")  # This searches 'World' in the string and returns the index where
# it finds the 'World'. In this case 6

a.find('o')  # This gives 4 as 'o' first occurs in 4th position
a.find('o', 5)  # This searches 'o' from the 5th index. Thus, it returns 6


a.replace("Hello", "hello")  # This replaces "Hello" in the string with "hello" and
# returns a new string


