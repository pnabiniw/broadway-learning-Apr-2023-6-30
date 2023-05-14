import time

def decorate_me(func):
    def inner_func():
        print("I have been decorated")
        return func()
    return inner_func
#
#
# @decorate_me
# def ordinary():
#     return "ordinary"


# ordinary = decorate_me(ordinary)
# print(ordinary())


def change_to_upper(func):
    def inner_func():
        value = func()
        return value.upper()
    return inner_func


def execution_time(func):
    def inner_func():
        start = time.time()
        a = func()
        end = time.time()
        print(f"Execution time is {end-start}")
        return a
    return inner_func


def login_required(func):
    def inner_func(*args, **kwargs):
        pw = input("Enter the password ")
        if pw == '123':
            return func(*args, **kwargs)
        else:
            return "Invalid Password"
    return inner_func


# def message(m, a, b):
#     print(a)
#     print(m)
#     print(b)
#     return "done"
#
#
# message = login_required(message)
# print(message(1, 2, 3))
#
#
# def decorate_m(func):
#     def inner_func(*args, **kwargs):
#         return func(*args, **kwargs)
#     return inner_func
