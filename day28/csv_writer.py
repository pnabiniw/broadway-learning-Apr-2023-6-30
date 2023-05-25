import csv
students = [
    {"name": "Jon", "age": 23, "id": 1},
    {"name": "Jane", "age": 25, "id": 2},
]

with open("new_data.csv", "w") as cw:
    csv_writer = csv.DictWriter(cw, fieldnames=students[0].keys(), delimiter="\t")
    csv_writer.writeheader()
    for student in students:
        csv_writer.writerow(student)
