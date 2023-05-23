import json
filename = "students.json"


def read(student_id):
    with open(filename, "r") as fp:
        data = fp.read()
        data = json.loads(data)
        student = list(filter(lambda x: x['id'] == student_id, data))

        # student = [{id: 3, name}]
        if student:
            print(student[0])
        else:
            print("Invalid student id")
        choice = input("Wish to continue? (y/n) ")
        return True if choice.lower() == 'y' else False

