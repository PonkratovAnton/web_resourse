from random import randrange, randint

from app.database import cursor, conn

name_resource_type = ['Самосвал', 'Эскалатор', 'Билаз', 'Трактор']

cursor.execute('''CREATE TABLE IF NOT EXISTS resource_type (
                  id SERIAL PRIMARY KEY,
                  name VARCHAR(255) NOT NULL,
                  max_speed INT)''')

cursor.execute(""" CREATE TABLE IF NOT EXISTS resource (
                   id SERIAL PRIMARY KEY,
                   type_id INT REFERENCES resource_type(id),
                   name VARCHAR(255) NOT NULL,
                   current_speed DECIMAL)""")

for _ in range(4):
    cursor.execute(
        "INSERT INTO resource_type (name, max_speed) VALUES (%s, %s)",
        (name_resource_type[_], randrange(40, 80, 10))
    )

for _ in range(100):
    cursor.execute(
        "INSERT INTO resource (type_id, name, current_speed) "
        "VALUES (%s, %s, %s)",
        (randrange(1, 5, 1), f"{chr(randint(0x0410, 0x044F))}{randrange(100, 200, 1)}", randrange(40, 100, 10))
    )

conn.commit()
conn.close()
