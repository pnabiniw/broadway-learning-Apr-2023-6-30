from estd_connection import estd_connection

cursor = estd_connection()
id = input("Enter student id ")
name = input("Enter name ")
age = input("Enter age ")

sql = f"""
INSERT INTO STUDENT(ID, NAME, AGE) VALUES ('{id}', '{name}', {age})
"""

cursor.execute(sql)
print("Student Added Successfully !!")
