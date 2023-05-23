import json
filename = "students.json"


def delete(student_id):
    with open(filename, "r+") as fp:
        data = fp.read()
        data = json.loads(data)
        student = list(filter(lambda x: x['id'] == student_id, data))
        if student:
            data.remove(student[0])
            fp.seek(0)
            fp.truncate()
            json_obj = json.dumps(data, indent=2)
            fp.write(json_obj)
            # json.dump(data, fp, indent=2)
            print("Student deleted successfully !!")
        else:
            print("Invalid student id")
    choice = input("Wish to continue? (y/n) ")
    return True if choice.lower() == 'y' else False
