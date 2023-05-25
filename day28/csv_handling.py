# CSV =>(Comma Separated Values) Way of storing data in comma separated form

import csv
from utils import insert_into_table
filename = "students.csv"

# with open(filename, "r") as cr:
#     csv_reader = csv.reader(cr)  # It returns an iterator object
#     next(csv_reader)  # Skipping the first line (column names)
#     for each_line in csv_reader:
#         print(each_line[1])


with open(filename, "r") as cr:
    csv_reader = csv.DictReader(cr)  # We can also add delimiter="," here
    for each_line in csv_reader:
        # print(each_line['age'])
        insert_into_table(each_line)
print("CSV has been loaded to table !!")
