# enumerate() function

vowels = ["a", "e", "i", "o", "u"]

for i in range(len(vowels)):
    print("index", i)
    print("value", vowels[i])

# The above loop can be obtained easily from this code
for index, value in enumerate(vowels):
    print("index", index)
    print("value", value)


# enumerate() function takes start argument, where we can give the start count.
for count, value in enumerate(vowels, start=1):
    print("count", count)  # 1, 2, 3, 4, 5
    print("value", value)
