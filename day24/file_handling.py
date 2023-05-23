# File modes in python
# r = read
# w = write
# a = append
# x = exclusive write


# write mode
# try:
#     fp = open("file.txt", "w")
#     fp.write("Hello from file")
# except:
#     pass
# finally:
#     fp.close()
#
#
# # read mode
# try:
#     fp = open("file.txt", "r")
#     data = fp.read()
#     print(type(data))   # Result => string
#     print(data)
# except:
#     pass
# finally:
#     fp.close()
#
# # append mode
# try:
#     fp = open("file.txt", "a")
#     fp.write("\nPython is awesome !")
# except:
#     pass
# finally:
#     fp.close()

# try:
#     fp = open("file.txt", "x")
#     fp.write("File does not exist")
# except:
#     pass
# finally:
#     fp.close()


# Context Managers
# Read mode
# with open("file.txt", "r") as fp:
#     data = fp.read()
#     print(data)
#
#
# with open("file.txt", "w") as fp:
#     fp.write("Hello from file")
#
# with open("file.txt", "a") as fp:
#     fp.write("\nPython is awesome !")


with open("file.txt", "r+") as fp:
    data = fp.read()
    print(data)
    fp.write("New Line added")


with open("file.txt", "w+") as fp:
    fp.write("Hello World")
    data = fp.read()
    print(data)


with open("file.txt", "a+") as fp:
    fp.write("\nPython is high level language")
    print(fp.read())
