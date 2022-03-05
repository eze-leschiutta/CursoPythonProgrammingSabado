# Paradigma de objetos

# ~ class MiClase:
	# ~ def __init__(self):
		# ~ print("has creado una instancia de MiClase")
		
# ~ mi_objeto = MiClase()


# ~ class Ejemplo:
	# ~ __atributo_privado = "soy un aributo privado, innancalzable desde afuera"
	
	# ~ def __metodo_privado(self):
		# ~ print("Soy un metodo privado")
		
	# ~ def atributo_publico(self):
		# ~ return self.__atributo_privado
		
	# ~ def metodo_publico(self):
		# ~ return self.__metodo_privado()
		
	
# ~ e = Ejemplo()

# ~ print(e.atributo_publico())
# ~ e.metodo_publico()


class Pelicula:
	def __init__(self, titulo, duracion, lanzamiento):
		self.titulo = titulo
		self.duracion = duracion
		self.lanzamiento = lanzamiento
		
	def __str__(self):
		return '{} ({})'.format(self.titulo, self.lanzamiento)
		

class Catalogo:
	peliculas = []
	
	def __init__(self, peliculas=[]):
		self.peliculas = peliculas
		
	def agregar(self, p):
		self.peliculas.append(p)
	
	def mostrar(self):
		for p in self.peliculas:
			print(p)
			
			
p = Pelicula("El padrino", 175, 1972)

c = Catalogo([p])

c.mostrar()

c.agregar(Pelicula("El padrino 2", 200, 1975))

c.mostrar()	
		
		
		
		
		
		
		
