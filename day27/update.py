from estd_connection import estd_connection

cursor = estd_connection()

sql = """
UPDATE STUDENT SET NAME='JANE' WHERE ID='1'
"""

cursor.execute(sql)
print("Student Updated Successfully !")
