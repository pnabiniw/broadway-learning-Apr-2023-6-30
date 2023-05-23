"""
JSON => JavaScript Object Notation
{
    "name": "Jane",
    "age": 45,
    "id": 1
} (Valid JSON)

[{"name": "Jane", "id": 2}, {"name": "Harry", "id": 3}]  => (Valid JSON)

{'name': 'Jon', 'id': 3}  (Invalid JSON because quotes cannot be single quotes in JSON.
It must be double quotes

"""
import json

students = [{'name': 'Jon', 'id': 1},
            {'name': 'Jane', 'id': 3},
            {'name': 'Harry', 'id': 2}]

with open("students.json", 'w') as fp:
    json_object = json.dumps(students, indent=2)
    fp.write(json_object)


with open("students.json", "r") as fp:
    data = fp.read()
    print(data)   # This gives a string data
    data = json.loads(data)
    print(data)   # This gives list data
    print(type(data))
    print(data[0]["name"])
