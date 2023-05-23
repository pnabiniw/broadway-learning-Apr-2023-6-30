from create_student import create
from read_student import read
from update_student import update
from delete_student import delete


def inquiry():
    selection = input("Enter your choice C/R/U/D ")
    selection = selection.lower()
    if selection == "c":
        create()
    elif selection == "r":
        read()
    elif selection == "u":
        update()
    elif selection == "d":
        delete()
    else:
        print("Invalid Choice")


if __name__ == "__main__":
    inquiry()
