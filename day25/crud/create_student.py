import os
import json
filename = "students.json"


def create():
    id = input("Enter student id ")
    name = input("Enter student name ")
    age = input("Enter student age ")
    student = dict(id=id, name=name, age=age)
    if not os.path.exists(filename):
        with open(filename, "w") as fp:
            json_obj = json.dumps([student], indent=2)
            fp.write(json_obj)
    else:
        with open(filename, "r+") as fp:
            data = fp.read()
            data = json.loads(data)
            data.append(student)
            fp.seek(0)
            fp.write(json.dumps(data, indent=2))
    print("Student added successfully")
    choice = input("Wish to continue? (y/n) ")
    return True if choice.lower() == 'y' else False
