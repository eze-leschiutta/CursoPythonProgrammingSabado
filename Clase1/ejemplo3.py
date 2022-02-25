# ejercicio: dado un numero ingresado por el usuario
# mostrar por pantalla el nombre del mes correspondiente
# si es un valor no valido, mostrar el mensaje " no existe el mes con ese valor ingresado"



numero = int(input("ingrese numero del 1 al 12: "))

if numero==1:
 print("el mes es enero")
elif numero==2:
    print("el mes es febrero")
else:
    print("el numero no corresponde a un mes")
    
    
    
numero = int(input('numero:'))
if numero >= 1 and numero <= 12:
	if numero == 1:
		print('enero')
	elif numero == 2:
		print('febrero')
	elif numero == 3:
		print('marzo')
	elif numero == 4:
		print('abril')
	elif numero == 5:
		print('mayo')
	elif numero == 6:
		print('junio')
	elif numero == 7:
		print('julio')
	elif numero == 8:
		print('agosto')
	elif numero == 9:
		print('septiembre')
	elif numero == 10:
		print('octubre')
	elif numero == 11:
		print('noviembre')
	elif numero == 12:
		print('diciembre')
else:
	print('no existe el mes con ese valor ingresado')
