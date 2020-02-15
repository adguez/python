'''Bases de Datos '''
import sqlite3
conn = sqlite3.connect('example.db')

c = conn.cursor()

def create_table():
	c.execute(''' CREATE TABLE IF NOT EXISTS Tablas(nombre VARCHAR(50), registro DATETIME, errores INT)''')
	print("DB CREADA correctamente")

def data_entry():
	c.execute("INSERT INTO Tablas VALUES('Axel',datetime('now'),1)")
	conn.commit()
def lista_data():
	c.execute("SELECT * FROM Tablas")
	data = c.fetchall()
	for p in data:
		print("{} {} {}".format(p[0], p[1], p[2]))

#create_table()
#data_entry()
lista_data()

c.close()
conn.close()

