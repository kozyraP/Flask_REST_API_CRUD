import sqlite3
import os.path

if os.path.exists('company.db'):
    print("DB already exists")
else:
    f = open("company.db", "w")
    f.close()
    print("DB created")

conn = sqlite3.connect('company.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS employee (
              birth_day timestamp,
              email varchar(255) not null,
              name varchar(50) not null,
              phone_number varchar(255))
;''')

conn.commit()

c.execute('''INSERT INTO 
                    employee (name,birth_day,email,phone_number) 
            VALUES 
                    ('Pawel Kozyra','1991-01-20','someemail@mail.net','123-123'),
                    ('Harry Potter','1981-01-20','hp@mail.net','12343-123')
        ;''')

conn.commit()

conn.close()
