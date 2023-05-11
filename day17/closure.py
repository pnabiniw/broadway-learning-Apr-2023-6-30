# Closures can the higher order functions in Python
# Criteria for closures are:
# 1. Closure function must define another nested function
# 2. The parameters passed inside the closure function must be used inside the
#    nested
# 3. Closure must return the nested function


def decorate_me(func):
    def inner_func():
        print("Im a decorated function")
        return func()
    return inner_func


def message():
    return "Hello World"


def addition():
    print("Im adding")



# result = decorate_me(message)
print(message())

# print(addition(1, 2, 3))
