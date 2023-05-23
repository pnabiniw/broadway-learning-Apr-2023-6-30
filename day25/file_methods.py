# with open("info.txt", "w") as fp:
#     fp.write("Hello World\nLearning Python")


# read
# readline
# readlines
with open("info.txt", "r") as fp:
    data = fp.read()
    print(data)

    fp.seek(0)
    data = fp.read(5)
    print(data)

    fp.seek(13)
    data = fp.readline()   # readline reads the text from the cursor position to the next-line character
    print(data)

    fp.seek(0)
    data = fp.readlines()  # readlines reads the file and returns each line data in the list
    print(data)
    print(fp.tell())


with open("info.txt", "a") as fp:
    data = ["\nLearning File methods\n", "Append Mode"]
    fp.writelines(data)
