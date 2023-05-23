count = 0


def message():
    global count
    count += 1
    print("Hello World")
    if count == 10:
        return
    message()


message()
