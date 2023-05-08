# Iterators are those objects which can be iterated through
# Iterables are those objects which can be converted to iterator object

a = [1, 2, 3, 4]
iter_a = iter(a)

print(next(iter_a))
print(next(iter_a))
print(next(iter_a))
print(next(iter_a))
# print(next(iter_a))   # At last it raises StopIteration exception

b = [4, 5, 6, 7]
iter_b = iter(b)
# for loop in python is just a syntatic sugar for while loop
while True:
    print("Here")
    try:
        print(next(iter_b))
    except StopIteration:
        break
