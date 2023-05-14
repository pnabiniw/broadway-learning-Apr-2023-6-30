from day18.decorators import change_to_upper, execution_time, \
    login_required


@change_to_upper
def print_message():
    return "hello world"


# print_message = change_to_upper(print_message)
result = print_message()
print(result)


@change_to_upper
def another_message():
    return "Python is awesome"

print(another_message())


@execution_time
def time_estimation():
    for i in range(1000000000):
        pass
    return "done"

# print(time_estimation())


@login_required
def message(m):
    return m


print(message("Python is Awesome"))

