#Ejercicio 9: Contar palabras en un texto 

texto = "manzana naranja manzana pera pera pera naranja manzana" 

palabras = texto.split()
conteo_palabras = {}

for palabra in palabras:
    if palabra in conteo_palabras:
        conteo_palabras[palabra] += 1
    else:
        conteo_palabras[palabra] = 1

print(conteo_palabras)