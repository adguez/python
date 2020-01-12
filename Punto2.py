import math

class Punto:
	def __init__(self ,x=0 ,y=0):
		self.mover(x ,y)
	def mover(self ,x ,y):
		self.x = x
		self.y = y
	def reiniciar(self):
		self.mover(0 ,0)
	def getUbicacion(self):
		print("POX X: ",self.x ,"POS Y: ",self.y)
	def calcular_distancia(self ,otro_punto):
		return math.sqrt(
				(self.x - otro_punto.x)**2
				+ (self.y - otro_punto.y)**2
			)


punto = Punto()
punto.getUbicacion()

punto1 = Punto(5)
punto1.getUbicacion()