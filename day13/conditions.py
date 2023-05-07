# In if...elif...else ladder, if one of the conditions is satisfied then the next blocks
# are not executed. In contrast, in normal if...if..if..else blocks, every conditions
# are checked and every satisfied blocks are executed.

# All the logical and relational operations can be used in conditions check.
# We can directly use truthy or Falsy values without logical or relational operations.
a = 2

if a:
    print("It is non-empty")


if a == 1:
    print("It is 1")

elif a == 2:
    print("It is 2")

elif a == 2:
    print('It is 2 again')

else:
    print("Nothing")


# Ternary if...else
print("It is non empty") if a else print("It's empty")


# Nested if

message = "Hello World"
if message:
    if message == "Hello":
        print(f"Hi it's {message}")
    else:
        print(message)
else:
    print("Empty String !!")


n = int(input("Enter any number "))
