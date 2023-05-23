import os
import json
filename = "students.json"


def create():
    id = input("Enter student id ")
    name = input("Enter student name ")
    age = input("Enter student age")
    data = dict(id=id, name=name, age=age)
    if not os.path.exists(filename):
        with open(filename, "w") as fp:
            json_obj = json.dumps(data)
            fp.write(json_obj)
    else:
        pass

