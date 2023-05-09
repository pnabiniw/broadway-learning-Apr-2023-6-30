# check whether a number is palindrome or not

# a = 123
# str_a = str(a)
# rev = str_a[::-1]
# print("Palindrome") if str_a == rev else print("Not Palindrome")

a = 121
rev = 0
b = a
while a != 0:
    remainder = a % 10
    rev = rev * 10 + remainder  # 321
    a = a // 10

print("Palindrome") if rev == b else print("Not Palindrome")
