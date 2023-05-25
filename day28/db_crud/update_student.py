from day27.estd_connection import estd_connection
cursor = estd_connection()


def update(student_id, to_change, changed_value):
    sql = f"""
    UPDATE INFO SET {to_change}='{changed_value}' WHERE ID='{student_id}'
    """
    cursor.execute(sql)
    print("Student updated successfully !!")
    choice = input("Wish to continue? (y/n) ")
    return True if choice.lower() == 'y' else False
