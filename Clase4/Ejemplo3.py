
import pymysql

# ~ conn = pymysql.connect(host="localhost", user="root", passwd="", database="pythoncurso")
# ~ cursor = conn.cursor()
# ~ cursor.execute("CREATE TABLE personas (id INT, nombre VARCHAR(50), edad INT)")
# ~ conn.commit()
# ~ conn.close()



# insertar datos


personas = ((1, "Pablo", 30), (2, "Eva", 25), (3, "Pedro", 40))
conn = pymysql.connect(host="localhost", user="root", passwd="", database="pythoncurso")
cursor = conn.cursor()
for id, nombre, edad in personas:
	cursor.execute("INSERT INTO personas VALUES(%s,%s,%s)", (id,nombre,edad))

conn.commit()
conn.close()
