# Escribir un programa que cree un diccionario simulando un carrito de compra.
# El programa debe preguntar el articulo y su precio y añadir el par al diccionario hasta que el usuario decide terminar.
# Despues se debe mostrar por pantalla la lista de compras y el costo total.
# Ejemplo
"""
	Lista de Compras
	Articulo1		Precio1
	Articulo2		Precio2
	......
	......
	Total			Precio Total
"""

carrito = {}
more = 'S'

#while carrito[item] != 'Camisa':
while more == 'S':
	item = input("Introduce un articulo: ")
	precio = float(input("Introduce el precio del item " + item + " :"))
	carrito[item] = precio
	more = input("Quiere añadir otro articulo al carrito (S / N) ?")
	
costoTotal = 0

print("Lista de Compras")

for item, precio in carrito.items():
	print(item, '\t', precio)
	costoTotal += precio
	
print('Total', '\t', costoTotal)
