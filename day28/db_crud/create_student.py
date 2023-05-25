from day27.estd_connection import estd_connection
cursor = estd_connection()


def create():
    id = input("Enter student id ")
    name = input("Enter student name ")
    email = input("Enter student email ")
    age = input("Enter student age ")

    sql = f"""
    INSERT INTO INFO(ID, NAME, EMAIL, AGE) VALUES ('{id}', '{name}', '{email}', {age})
    """
    cursor.execute(sql)
    print("Student added successfully !")
    choice = input("Wish to continue? (y/n) ")
    return True if choice.lower() == 'y' else False
