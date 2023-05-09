# def addition(*args):
#     return sum(args)
#
#
# result = addition(1, 2, 3, 4)
# print(result)


def addition(**kwargs):
    values = kwargs.values()
    return sum(values)


result = addition(a=1, b=1, c=2)
print(result)


def summ(a, b, c, d, e=10, f=4, *args, **kwargs):
    print(a, b, c, d)
    print(e, f)
    print(args)
    print(kwargs)


print(summ(1, 2, 3, 4, 5, 6, 7, 8, 9, p=10, q=11))
