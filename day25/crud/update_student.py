import json
filename = "students.json"


def update(student_id, to_change, changed_data):
    with open(filename, "r+") as fp:
        data = fp.read()
        data = json.loads(data)
        # data = json.load(fp)
        student = list(filter(lambda x: x['id'] == student_id, data))
        if student:
            index = data.index(student[0])
            data[index][to_change] = changed_data
            fp.seek(0)

            # json.dump(data, fp, indent=2)
            fp.write(json.dumps(data, indent=2))
            print("Info updated successfully !")
        else:
            print("Invalid student id")
    choice = input("Wish to continue? (y/n) ")
    return True if choice.lower() == 'y' else False
