import math

class Punto:
	def mover(self ,x ,y):
		self.x = x
		self.y = y
	def reiniciar(self):
		self.mover(0 ,0)
	def calcular_distancia(self ,otro_punto):
		return math.sqrt(
				(self.x - otro_punto.x)**2
				+ (self.y - otro_punto.y)**2
			)


punto = Punto()
punto.x = 3

print(punto.x)

##### DE momento marca una EXCEPCION DEBIDO A QUE EL ATRIBUTO NO EXISTE
print(punto.y)