# while

contador = 1

while contador <= 10:
	print(contador)
	contador = contador + 1
	

#break : sale del bucle de manera completa


print("----------break-----------")
contador = 1
while contador <= 10:
	print(contador)
	contador = contador + 1
	if contador == 5:
		break
		
		
# continue: sale de la iteracion pero no del bucle

print("----------continue-----------")
contador = 1
while contador <= 10:	
	if contador == 5:
		continue
	print(contador)
	contador = contador + 1
