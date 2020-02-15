'''
Programa que genera tres tabla de multiplicar del 2 al 10
'''
from random import randint
from datetime import datetime
import sqlite3

def guardar_resultado(nombre, errores, total):
	conn = sqlite3.connect('example.db')
	cur = conn.cursor()
	query = "INSERT INTO Tablas VALUES(?,datetime('now'),?)"
	cur.execute(query,[nombre, errores])
	conn.commit()
	cur.close()
	conn.close()

def tablas():
	limite = 3
	contador = 0
	errores = 0

	nombre = raw_input("Ingresa tu nombre: ")

	tiempo_inicio = datetime.now()
	'''while contador < limite:
		tabla = randint(2,10)
		print("La tabla generada es: {}".format(tabla))
		aciertos = 0
		while aciertos < 10:
			factor = randint(1,10)
			try:
				respuesta = int(raw_input("{} x {} = ".format(tabla, factor)))
				if respuesta == (factor*tabla):
					aciertos += 1
				else:
					errores += 1
			except ValueError:
				print (" Ingrese solo numeros ")
		contador += 1
	'''
	tiempo_fin = datetime.now()

	total = tiempo_fin - tiempo_inicio

	print("\n\n\t+----------------------------------------+")
	print("\t|                                        |")
	print("\t| Felicidades!!! Has concluido tu prueba |")
	print("\t|                                        |")
	print("\t+----------------------------------------+")
	print("Duracion: {}".format(total))
	print("Errores: {}".format(errores))

	guardar_resultado(nombre, errores, total)

tablas()