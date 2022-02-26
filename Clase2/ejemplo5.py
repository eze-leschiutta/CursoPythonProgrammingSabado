# Manejo de archivos

# Creacion y escritura de archivo

# Forma 1

# ~ archivo = open("prueba.txt","a") # append

# ~ archivo.write("Chau\n")

# ~ archivo.write("Adios\n")

# ~ archivo.close()


# Forma 2

# ~ lista=["Bye\n", "Hoy es sabado\n", "final de la carga\n"]
# ~ archivo = open("prueba2.txt","a")

# ~ archivo.writelines(lista)

# ~ archivo.close()



# Apertura y lectura de un archivo
archivo = open("prueba.txt","r") # read
saludos = archivo.read()
print(saludos)
print("----------------")

# Solo usar un metodo de lectura a la vez
#solo_una_linea = archivo.readline()
#print(solo_una_linea)

archivo.close()


#recorrer archivo
archivo = open("prueba2.txt","r") 
# ~ linea = archivo.readline()
# ~ while linea != "":
	# ~ print(linea)
	# ~ linea = archivo.readline()

# ~ contador = 1
# ~ for linea in archivo.readlines():
for contador, linea in enumerate(archivo, 1):
	print("{0}:{1}".format(contador,linea))
	contador+=1


archivo.close()
print("Fin del programa")


# Formato de texto

print("----formato de texto------------")


nombre = "Juan"
edad = 20

print(nombre + " tiene edad " + str(edad))
print(nombre, "tiene edad", edad)
#print(nombre, "tiene edad", edad, sep="-", end=".")
print(nombre, "tiene edad", edad, sep="-")
print("termino")



#PlaceHolder

print("{1} tiene {0} años".format(edad, nombre))


print(f"{nombre} tiene {edad} años")


