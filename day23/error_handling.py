# In python (or any languages) there are three types of errors
# 1. Syntatic error
# 2. Logical error
# 3. Exceptions / Runtime error


# try:
#     num = int(input("Enter a number"))
# except ValueError:
#     print("Please enter a number not characters")
# except ZeroDivisionError:
#     print("Don't divide by zero")
# else:
#     print(num)
# finally:
#     print("Finally executed")


# try:
#     num1 = float(input("Enter a number "))
#     num2 = float(input("Enter another number "))
# except ValueError:
#     print("Please enter a valid number ")
# else:
#     print("The sum of two numbers is", num1 + num2)
#
#
# try:
#     num1 = int(input("Enter a number "))
#     num2 = int(input("Enter another number "))
#     div = num1 / num2
#     print(div)
# except  (ValueError, ZeroDivisionError):
#     print("Character or zero in denominator detected ")


student = {"name": "Jane", "age": 45, "department": "Mathematics"}
key = input("Enter the info you want to access ")
try:
    print(f"The value of {key} is ", student[key])
except KeyError:
    print("Invalid key for the dictionary ")
