##################  Numbers ##################################
# To check the type of data we use type() built-in function
# For example

a = 2e3
print(type(a))   # 'a' is a float type

print(3e6432674332)  # this gives infinity (inf)

b = 3 + 4j   # b is a complex datatype
print(b)


#### Mutable and Immutable check

a = [1, 2, 3, 4]
a[2] = 5  # expected result [1, 2, 5, 4]
print(a)


b = (1, 2, 3, 4)
b[2] = 5
print(b)


######### List Datatype ###########

a = [1, 2.3, "Hello Broadway"]  # This is a list

# List supports indexing
print(a[0])  # It gives the data of first index
print(a[1])  # It gives the data of second index and so on

print(len(a))  # It gives the length of the list i.e. total elements in that list


print(a[-1])   # List supports negative indexing. So -1 gives the data from the last.

a[1] = "Hello World"   # This sets the value to index 1 of the list
a[-1] = 56
print(a)
