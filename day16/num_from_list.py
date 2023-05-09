a = [4, 2, 3, 1, 2, 5]  # 42224
# new_str = ''
# for i in a:
#     new_str += f'{i}'
#
# print(int(new_str))

num = a[0]
for index in range(len(a)):
    try:
        num = num * 10 + a[index+1]
    except IndexError:
        break
print(num)
