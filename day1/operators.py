# Arithmetic operators
a = 5
b = 3
# Addition
c = a + b
print(c)

# Subtraction
c = a - b
print(c)

# Multiplication
c = a * b
print(c)

# Division
c = a / b
print(c)

# Modulus Operator
c = a % 2  # It gives remainder of the division
print(c)

# Exponent Operator
c = a ** 2   # Use ** instead of ^ to raise the power of
print(c)

# Floor Division
c = a // 2  # It removes the decimal value of the result
print(c)



######### Comparision Operators #################

# Equals To
print(a == b)

# Not equals to
print(a != b)

# Greater than
print(a > b)

# Less than
print(a < b)

# Greater than or equals to
print(a >= b)

# Less than or equals to
print(a <= b)


# Logical Operators
# and , or and not are the logical operators in python
a = True
b = False
# And Operator
print(a and b)

# Or operator
print(a or b)

# Not operator
print(not a)


# Identity Operator
print(a is b)  # We can check id of the object using builtin id function; id(a)
print(a is not b)


# Membership Operator
a = [1, 2, 3]
print(2 in a)  # This gives True result
print(2 not in a)  # This gives False result


# Assignment operator
a = 2  # This the most basic assignment operator

a = a + 1  # This gives a as 3
# This can also be done as
a += 1

# And the same goes for other arithmetical operators
a -= 1
a *= 1  # and so on


# Precedence and Associativity
print(3*5//5)  # Associativity is left to right
print(3**2**4)  # Associativity is right to left
