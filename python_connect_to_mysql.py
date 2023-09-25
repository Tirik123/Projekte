import mysql.connector

conn = mysql.connector.connect(host = 'localhost', username = 'sqluser', password = 'Barney314159C', database = 'warenkorbsystem')
my_cursor = conn.cursor()

conn.commit()
conn.close()

print('Connection succesfully created!')