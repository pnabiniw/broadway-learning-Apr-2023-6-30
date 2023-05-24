from estd_connection import estd_connection

cursor = estd_connection()

sql = """
DELETE FROM STUDENT WHERE ID='1'
"""

cursor.execute(sql)
print("Student Deleted !!")
