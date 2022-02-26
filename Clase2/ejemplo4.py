# Diccionario

alumno = {"nombre":"Juan", "cursos": 3, "materias": ["Python", "Java", "C#"]}

print(type(alumno))

print(alumno["nombre"])

alumno["curso-actual"] = "Python"

alumno["cursos"] = 5

print(alumno)


for clave in alumno:
	print(clave, alumno[clave])


