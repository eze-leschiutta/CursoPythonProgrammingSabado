#Excepciones

# Tecnicas
# Negocio

# otros lenguajes
# try / catch / finally

#Python
# try: esta parte se ejecuta si esta todo ok
# except: se jecuta el codigo que se dispara x la excepcion
# finally: se ejecuta siempre haya excepcion o no


# ~ try:
	# ~ int("tres")
# ~ except ValueError:
	# ~ print("El valor debe ser numerico")


# ~ try:
	# ~ int("A")
# ~ except TypeError:
	# ~ print("tipo de dato incorrecto")
# ~ except ValueError:
	# ~ print("El valor debe ser numerico")

# ~ try:
	# ~ int("A")
# ~ except (TypeError, ValueError):
	# ~ print("tipo de dato incorrecto o El valor debe ser numerico")
	
# ~ lista = [1,2,3,4]
# ~ try:
	# ~ print(lista[6])
# ~ except IndexError:
	# ~ print("Indice fuera de rango")
	

d = {"Juan":3, "Eva":5}
# ~ try:
	# ~ print(d["Pepe"])
# ~ except KeyError:
	# ~ print("Error de clave")
	
	
# ~ try:
	# ~ print(d["Pepe"])
# ~ except Exception:
	# ~ print("Ocurrio un error")
	
	
# try / except / else / finally



# ~ while(True):
	# ~ try:
		# ~ n = float(input("Introduce un numero: "))
		# ~ m = 4
		# ~ print("{}/{} = {}".format(n,m,n/m))
	# ~ except Exception:
		# ~ print("Ha ocurrido un error, introduce bien el numero")	
	# ~ else:
		# ~ print("Todo funcion ok")
		# ~ break
	# ~ finally:
		# ~ print("Fin de la iteracion")
		
		

num1 = 3
num2 = 0
#print(num1/num2)
#print(c)

try:
	c = "123"
	raise NameError("Nombre invalido")
except NameError:
	print("Error")

	
