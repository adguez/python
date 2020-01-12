import datetime

#  Almacena todas las ID's disponibles
ultima_id = 0

class Nota:
	"""Representa una nota en el cuaderno. Se compara con un String en las busquedas y las etiquetas para cada nota"""
	def __init__(self, memo, tags=''):
		"""Inicializa una nota con un memo y opcional tags separado por comas. Automaticamente configura la fecha de creacion de la nota y una unica ID"""
		self.memo = memo
		self.tags = tags
		self.creation_date = datetime.date.today()
		global ultima_id
		ultima_id += 1
		self.id = ultima_id

	def match(self, filter):
		'''DEtermina si esta nota concuerda con el filtro de texto. Devuelve True si concuerda. Busqueda es case sensitive  compara tanto con text como con tags'''
		return filter in self.memo or filter in self.tags


class Cuaderno:
	'''Reresenta una coleccion de noas que pueden ser etiquetadas, modificadas, y se pueden buscar'''
	def __init__(self):
		'''Iicializa el cuaderno con un lista vacia'''
		self.notas = []

	def nueva_nota(self, memo, tags=''):
		'''Crea una nueva nota y la aniade a la lista'''
		self.notas.append(Nota(memo, tags))
	def modificar_memo(self, nota_id, memo):
		'''Busca la nota con el ID indicado y cambia su memo al valor indicado'''
		#for nota in self.notas:
		#	if nota.id == nota_id:
		#		nota.memo = memo
		#		break
		self._encontrar_nota(nota_id).tags = tags
	def modificar_tags(self, nota_id, tags):
		'''Busca la nota con el ID indicado y cambia su memo al valor indicado'''
		#for nota in self.notas:
		#	if nota.id == nota_id:
		#		nota.tags = tags
		#		break
		self._encontrar_nota(nota_id).memo = memo
	def search(self, filter):
		'''Busca las notas que concuerden con el filtro string dado'''
		return [nota for nota in self.notas if nota.match(filter)]
	def _encontrar_nota(self, nota_id):
		'''Localiza la nota con la ID indicada'''
		for nota in self.notas:
			if nota.id == nota_id:
				return nota.id
		retun None