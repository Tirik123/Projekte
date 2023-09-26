import mysql.connector

conn = mysql.connector.connect(host = 'localhost', 
                               username = 'sqluser', 
                               password = 'Barney314159C', 
                               database = 'warenkorbsystem')

my_cursor = conn.cursor()

my_cursor.execute("ALTER TABLE Warenkorb ADD COLUMN product_amount INT NOT NULL")

