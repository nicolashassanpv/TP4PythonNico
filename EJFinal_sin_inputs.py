#Ejercicio Final 
#Sistema de Gestión de Inventario de Tienda 

inventario = {
    "A001" : ("Monitor LG", 260),
    "A002" : ("Teclado Razer", 50),
    "A003" : ("Auricular Hyperx", 30),
    "A004" : ("Procesador Ryzen 7", 420),
    "A005" : ("Mouse Logitech", 90),
    "A006" : ("IPhone X", 380),
    "A007" : ("Cable USB C", 15)
}

#mostrar_inventario(inventario): Muestra todos los productos del 
#inventario con su código, descripción y precio. 
def mostrar_inventario(inventario):
    for codigo, (descripcion, precio) in inventario.items():
        print(f"Código : {codigo}, Descripción : {descripcion}, Precio : ${precio}.")

#como usarla
#mostrar_inventario(inventario)

#buscar_producto(inventario, codigo): Busca un producto por su código. 
#Si existe, muestra su descripción y precio.
def buscar_producto(inventario, codigo):
    if codigo in inventario:
        descripcion, precio = inventario[codigo]
        print(f"Producto encontrado: {descripcion}, Precio: ${precio}.")
    else:
        print(f"El producto con código {codigo} no fue encontrado.")

#como usarla
#buscar_producto(inventario, "A001")

#modificar_precio(inventario, codigo, nuevo_precio): Modifica el precio 
#de un producto dado su código. 
def modificar_precio(inventario, codigo, nuevo_precio):
    if codigo in inventario:
        descripcion, _ = inventario[codigo]
        inventario[codigo] = (descripcion, nuevo_precio)
        print(f"El precio del producto con codigo {codigo} ha sido actualizado a ${nuevo_precio}.")
    else:
        print(f"El producto con código {codigo} no fue encontrado.")

#como usarla
#modificar_precio(inventario, "A001", 270)

#eliminar_producto(inventario, codigo): Elimina un producto del 
#inventario usando su código.
def eliminar_producto(inventario, codigo):
    try:
        producto = inventario.pop(codigo)
        print(f"El producto con codigo {codigo} ha sido eliminado del inventario")
    except KeyError:
        print(f"El producto con código {codigo} no fue encontrado.")

#como usarla
#eliminar_producto(inventario, "A002")

#productos_por_rango_de_precio(inventario, min_precio, max_precio): 
#Muestra todos los productos cuyo precio esté entre min_precio y 
#max_precio. 
def productos_por_rango_de_precio(inventario, min_precio, max_precio):
    print(f"Productos en el rango de precio entre ${min_precio} y ${max_precio}:")
    for codigo, (descripcion, precio) in inventario.items():
        if min_precio <= precio <= max_precio:
            print(f"Codigo : {codigo}, Descripción : {descripcion}, Precio : ${precio}.")
#como usarla
#productos_por_rango_de_precio(inventario, 1000, 1200)

