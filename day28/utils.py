from day27.estd_connection import estd_connection
cursor = estd_connection()


def insert_into_table(info):
    sql = f"""
    INSERT INTO INFO(ID, NAME, EMAIL, AGE) 
    VALUES ('{info["id"]}', '{info["name"]}', '{info["email"]}', '{info["age"]}')
    """
    cursor.execute(sql)
    print("Data Inserted !!")
