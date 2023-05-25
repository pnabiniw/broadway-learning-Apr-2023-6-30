from day27.estd_connection import estd_connection
cursor = estd_connection()


def delete(student_id):
    sql = f"""
    DELETE FROM INFO WHERE ID='{student_id}'
    """
    cursor.execute(sql)
    print("Student deleted successfully !!")
    choice = input("Wish to continue? (y/n) ")
    return True if choice.lower() == 'y' else False
