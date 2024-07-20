import psycopg2 as pg
conn = None
cur = None
try:

    with pg.connect(

        host="localhost",
        dbname="demo",
        user="postgres",
        password="postgresql",
        port=5432
    ) as conn:
        with conn.cursor() as cur:
            script = '''CREATE TABLE employee (
                id INT PRIMARY KEY,
                name VARCHAR(255),
                addres VARCHAR(255),
                emp_id INT
                )'''
            # cur.execute(script)
            insert_script = 'INSERT INTO employee (id ,name , addres , emp_id) VALUES (%s,%s,%s,%s)'
            insert_values = (2 , 'laxman', 'chomy', 22)
            
            table_data ='SELECT * FROM employee'
            data = cur.execute(table_data)
            print(cur.fetchall())
            print(data)
            conn.commit()
except Exception as error:
    print(error)

# finally:
#     if conn is not None:
#         conn.close()

#     if cur is not None:
#         cur.close()
