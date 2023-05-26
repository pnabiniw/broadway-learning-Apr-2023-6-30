message = ["Hello", "world", "python", "is", "high", "level", "language"]
print(message[5])  # => level
print(message[0:5]) # => "Hello", "world", "python", "is", "high"
print(message[0:5:2])  # => Hello, python, high
print(message[2:5])  # => python, is high
print(message[5:2])  # => []
print(message[-5:-1]) # "python", "is", "high", "level"
print(message[-5:-1:-1])  # []
print(message[-1:-5:-1])  # language level high is
print(message[::-1])  # language, level, high, is, python, world, Hello
