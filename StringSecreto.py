class StringSecreto:
	
	def __init__(self, string_plano, frase_pass):
		self.__string_plano = string_plano
		self.__frase_pass = frase_pass

	def decript(self, frase_pass):
		if self.__frase_pass == frase_pass:
			return self.__string_plano
		else:
			return 'Verifique su clave'

string_secreto = StringSecreto("Frase secrete","clave")

print(string_secreto.decript("clave"))
print(string_secreto.decript("clabe"))

#----> Saltar el sistema
print("HACKED: ",string_secreto._StringSecreto__string_plano)