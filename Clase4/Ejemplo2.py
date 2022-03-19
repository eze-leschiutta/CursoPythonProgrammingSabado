import sqlite3

# creacion de objeto de BD

# ~ conn = sqlite3.connect("databaseCurso2.sqlite")
# ~ cursor = conn.cursor()
# ~ cursor.execute("CREATE TABLE personas (id NUMERIC, nombre TEXT, edad NUMERIC)")
# ~ conn.commit()
# ~ conn.close()

# insertar datos


# ~ personas = ((1, "Pablo", 30), (2, "Eva", 25), (3, "Pedro", 40))
# ~ conn = sqlite3.connect("databaseCurso2.sqlite")
# ~ cursor = conn.cursor()
# ~ for id, nombre, edad in personas:
	# ~ cursor.execute("INSERT INTO personas VALUES(?,?,?)", (id,nombre,edad))

# ~ conn.commit()
# ~ conn.close()


# leer datos

conn = sqlite3.connect("databaseCurso2.sqlite")
cursor = conn.cursor()

# ~ cursor.execute("SELECT * FROM personas")
# ~ personas = cursor.fetchall()
# ~ for id, nombre, edad in personas:
	# ~ print(id,nombre,edad)
# print(personas)	
	
# ~ cursor.execute("SELECT * FROM personas where nombre = 'Pedro'")
# ~ persona = cursor.fetchone()
# ~ print(persona)

try:
	cursor.execute("SELECT FROM personas")
except sqlite3.OperationalError:
	print("la consulta no se puede ejecutar")


conn.close()
