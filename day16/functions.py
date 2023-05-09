def addition(a, b):   # a and b are arguments
    """

    :param a: any number
    :param b: any number
    :return: sum of a and b
    """
    return a + b


result1 = addition(3, 4)   # 3 and 4 are parameters
result2 = addition(5, 7)
print(result1)
print(result2)


def addition(a, b):
    print(a + b)


addition(2, 3)



# Types of Arguments in function
# Positional Arguments
# Keyword Arguments
# Arbitrary Arguments


# a, b, and c are positional arguments in this function. It means they are compulsory
# arguments
def addition(a, b, c):
    return a + b + c


result = addition(1, 2, 3)


# Here b is a keyword / default argument
def addition(a, b=2):
    return a + b

result = addition(1)
print(result)


def addition(a, b=2):
    return a + b


result = addition(1, 5)
print(result)


def addition(a, b=5):
    return a + b

result = addition(1, 5)
print(result)

