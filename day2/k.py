import keyword

print(keyword.iskeyword("def")); print(dir(keyword))

a = 1
if a == 1:
    print("Hello")    # Indentation matters in python

# print('I'm here')  # This gives an error
print('I\'m here')  # This is correct. Here \' is an escape sequence
