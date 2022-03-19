import sqlite3

# ~ conn = sqlite3.connect("databaseCurso2.sqlite")
# ~ cursor = conn.cursor()
# ~ cursor.execute("CREATE TABLE personas2 (nombre TEXT, edad NUMERIC)")
# ~ conn.commit()
# ~ conn.close()

# insertar datos


# ~ personas = (("Pablo", 30), ("Eva", 25), ("Pedro", 40))
# ~ conn = sqlite3.connect("databaseCurso2.sqlite")
# ~ cursor = conn.cursor()
# ~ for nombre, edad in personas:
	# ~ cursor.execute("INSERT INTO personas2 VALUES(?,?)", (nombre,edad))
	
	
nombre = input("nombre: ")
edad = input("edad: ")
conn = sqlite3.connect("databaseCurso2.sqlite")
cursor = conn.cursor()
cursor.executescript(f"INSERT INTO personas2 VALUES('{nombre}',{edad})")

conn.commit()
conn.close()
