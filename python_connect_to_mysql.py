import mysql.connector

conn = mysql.connector.connect(host = 'localhost', 
                               username = 'sqluser', 
                               password = 'Barney314159C', 
                               database = 'warenkorbsystem')

my_cursor = conn.cursor()

#my_cursor.execute("ALTER TABLE Warenkorb ADD COLUMN product_amount INT NOT NULL")

#my_cursor.execute('INSERT INTO Produkte (product_name, product_price) VALUES (%s, %s)', ("Aubergine", 2.99))

#conn.commit()

#my_cursor.execute('Select * From Produkte')

#my_cursor.execute("INSERT INTO produkte ")

'''for x in my_cursor:
    print(x)'''

#my_cursor.execute('INSERT INTO Produkte (product_name, product_price) VALUES (%s, %s)', ("Apfel", 1.99))

#conn.commit()

my_cursor.execute('Select * From Produkte')

for x in my_cursor:
    print(x)