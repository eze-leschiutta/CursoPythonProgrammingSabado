
# Bucles iterativos
# for
# while

lista = [10,20,30,40]
lista_cargada = []

for elemento in lista:
	print(elemento)


# range(desde, hasta, incremento)
# ~ range(0,10,1) -> {0,1,2,3,4,5,6,7,8,9}
# ~ range(0,10,2) -> {0,2,4,6,8}
# ~ range(5,10,1) -> {5,6,7,8,9}
# ~ range(5,-1,-1) -> {5,4,3,2,1,0}

# ~ range(10)

print("---------------------")

for posicion in range(0,4,1):
	print(lista[posicion])
	
	

print("----------contador-----------")
for contador in range(0,10,1):
	contador = contador + 1
	print(contador)

print("----------cargar lista-----------")

for contador in range(10,60,10):
	lista_cargada.append(contador)
	print(lista_cargada)
	
	
# matrices: es un tipo de lista, donde los elementos son lista


print("----------matriz-----------")

matriz = [[1,2,3,4],[3,"a", True],[45,6,77,90]]
print(type(matriz))

print(matriz[2][2])

matriz[1].append(66)

print(matriz)

print("----------iteracion de matriz-----------")

m = [[4,5,6,7],[10,11,12,13]] 

# filas : posicion de la matriz anidada
# columanas: posicion del elemento en la matriz que se esta iterando



for fila in m:
	for columna in fila:
		print(columna)

print("----------iteracion de matriz forma 2-----------")

for fila in range(0,2,1):
	for columna in range(0,3,1):
		print(m[fila][columna])







