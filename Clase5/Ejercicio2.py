import requests

alumnos = (
	("Pedro", 10),
	("Eva", 12),
	("Maria", 11)
)

# EJEMPLO POST

# ~ for nombre, curso in alumnos:
	# ~ r = requests.post("https://5cfdb2b8ca949b00148d38ba.mockapi.io/student", json =  {"name":nombre, "courses":curso})
	# ~ print("codigo de estado respuesta:",r.status_code)
	# ~ respuesta = r.json()
	# ~ print("contenido de la respuesta:", respuesta)
	
	

# EJEMPLO GET

# ~ r = requests.get("https://5cfdb2b8ca949b00148d38ba.mockapi.io/student")

# ~ if r.status_code == 200:
	# ~ respuesta = r.json()
	# ~ for alumno in respuesta:
		# ~ print("ID_Alumno:", alumno["id"])
		# ~ print("Nombre:", alumno["name"])
		# ~ print("Cursos:", alumno["courses"])
		# ~ print("-----------------")
# ~ else:
	# ~ print("ocurrio un error")
	

# EJEMPLO GET x ID

r = requests.get("https://5cfdb2b8ca949b00148d38ba.mockapi.io/student/3")
print("codigo de estado respuesta:",r.status_code)
if r.status_code == 200:
	respuesta = r.json()
	print("Estudiante Nro 3:", respuesta)
	print("-----------------")
	print("ID_Alumno:", respuesta["id"])
	print("Nombre:", respuesta["name"])
	print("Cursos:", respuesta["courses"])


# EJEMPLO PUT -> ACTUALIZAR UN ESTUDIANTE

# ~ datos={"courses": 30}

# ~ r = requests.put("https://5cfdb2b8ca949b00148d38ba.mockapi.io/student/3", json =  datos)
# ~ print("codigo de estado respuesta:",r.status_code)
# ~ respuesta = r.json()
# ~ print("contenido de la respuesta:", respuesta)


# EJEMPLO DELETE -> ELIMINAR UN ESTUDIANTE
# ~ r = requests.delete("https://5cfdb2b8ca949b00148d38ba.mockapi.io/student/3")
# ~ print("codigo de estado respuesta:",r.status_code)
# ~ respuesta = r.json()
# ~ print("contenido de la respuesta:", respuesta)
