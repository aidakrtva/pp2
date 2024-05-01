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
            phone VARCHAR(11) PRIMARY KEY
); 
""")

conn.commit()

#creating contacts
cur.execute("""INSERT INTO PhoneBook (name, phone) VALUES
            ('aida', '87768082005'),
            ('ayim', '87761231233'),
            ('azamat', '87012847143'),
            ('anuar', '87053489922');
""")

conn.commit()

#get contact
cur.execute('SELECT name, phone FROM PhoneBook')
print (cur.fetchall())

#changing azamats phone 
cur.execute("""UPDATE PhoneBook
            SET phone = '87777777777'
            WHERE name = 'azamat';
""")

conn.commit()

#deleting names 
cur.execute("""DELETE FROM PhoneBook
            WHERE name = 'azamat';
""")

conn.commit()