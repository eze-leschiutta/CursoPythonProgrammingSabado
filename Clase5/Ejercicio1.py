import requests

# ~ r = requests.get("https://jsonplaceholder.typicode.com/posts")

# ~ print("codigo de estado respuesta:",r.status_code)

# ~ respuesta = r.json()

# ~ print("------------SALIDA--------------------")

# ~ print("contenido de la respuesta:", respuesta)


# EJEMPLO GET

# ~ r = requests.get("https://5cfdb2b8ca949b00148d38ba.mockapi.io/student")

# ~ print("codigo de estado respuesta:",r.status_code)

# ~ respuesta = r.json()

# ~ print("------------SALIDA--------------------")

# ~ print("contenido de la respuesta:", respuesta)


# EJEMPLO POST


r = requests.post("https://5cfdb2b8ca949b00148d38ba.mockapi.io/student", json =  {"name": "Juan", "courses": 15})
print("codigo de estado respuesta:",r.status_code)

respuesta = r.json()
print("contenido de la respuesta:", respuesta)
