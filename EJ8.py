#Ejercicio 8: Eliminar elementos de un diccionario 

mascota = {
    "nombre" : "Firulais",
    "especie" : "perro",
    "edad" : "5"
}

mascota.pop("edad")

print(f"Diccionario luego de eleminar el elemento 'edad': {mascota}")