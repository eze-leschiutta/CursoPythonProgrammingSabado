
# ~ print()
# ~ input()
# ~ int()
# ~ float()


# Funciones

# ~ def nombre_funcion(parametro):
	# ~ sentencias
	
	
def imprimir_mensaje(parametro = "chau"):
	cadena = "Se llamo a la funcion"
	return cadena + " - " + str(parametro)
	
	
def elDobleValor(numero):
	c = numero * 2 
	#c += n
	return c
	
def suma(n1, n2=10):
	return n1 + n2
	

print("inicio del programa")
n = 10

mensaje = imprimir_mensaje(5)
print(mensaje)


result = elDobleValor(n)

variable2 = result * 4

print(elDobleValor(n))
print(result)

mensaje2 = imprimir_mensaje()
print(mensaje2)

variable_sumar = suma(12)
print("la suma es:", variable_sumar)
print("fin del programa")
