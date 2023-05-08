# break statement breaks the loop without completing the loop

a = [1, 3, 5, 2, 7]
for value in a:
    if value % 2 == 0:
        break
    print(value)


counter = 0
while True:
    print(counter)
    counter += 1
    if counter == 5:
        break


class A:
    pass   # Code is added here in future


def addition(a, b):
    pass   # Code is added here in future


if 3 > 5:
    pass



# else statement in python loops

nums = [1, 2, 3, 4]

for i in nums:
    print(i)
else:
    print("Loop Completed")


counter = 0
while counter < 5:
    print(counter)
    counter += 1
else:
    print("While loop completed")
