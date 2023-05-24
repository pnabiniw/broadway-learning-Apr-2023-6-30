from estd_connection import estd_connection

cursor = estd_connection()

sql = """
SELECT * FROM STUDENT WHERE ID='1'
"""

cursor.execute(sql)
result = cursor.fetchone()
print(result)
