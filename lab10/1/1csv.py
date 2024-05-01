import psycopg2

conn = psycopg2.connect(
    host = 'localhost', 
    dbname = 'suppliers', 
    user = 'postgres', 
    password = '808'
    )

cur = conn.cursor()

#deleting table 
cur.execute('DROP TABLE PhoneBook;')

conn.commit()

#creating table
cur.execute("""CREATE TABLE PhoneBook (
            name VARCHAR(255),
            phone VARCHAR(20) PRIMARY KEY
); 
""")

conn.commit()

import csv

filename = 'phonebook.csv'

with open (filename, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader :
            name, phone = row 


            #creating table 
            cur.execute(f"""INSERT INTO PhoneBook (name, phone) VALUES
                        ('{name}', '{phone}');
            """)

conn.commit()

