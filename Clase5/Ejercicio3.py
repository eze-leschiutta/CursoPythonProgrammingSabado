import requests

nombre = input("Nombre: ")
email = input("Email:" )
texto = input("Texto: ")

datos = {
   "name":nombre,
   "email":email,
   "message":texto
}

r = requests.post("http://localhost:8880/form", data =  datos)
if r.status_code == 200:
	contenido = r.content.decode("utf-8")
	if contenido.find("Mensaje enviado") > -1:
		print("Formulario enviado correctamente")
	else:
		print("Complete todos los datos del formuario")
else:
	print("Error en la conexion al formulario")
	
# ~ if "Mensaje enviado" in contenido:
	# ~ print("Formulario enviado correctamente")
# ~ else:
    # ~ print("Complete todos los datos del formuario")
