
# Funciones auxiliares para manejo de productos en archivo
# ----------------------------------------------------------------

def listar_productos():  
    with open("productos.txt", "r") as archivo_productos:
        for linea in archivo_productos:
            linea = linea.strip()
            partes = linea.split(",")
            print(partes[0], "| Precio: $"+partes[1], "| Cantidad:", partes[2])
            
def agregar_producto_a_archivo():
    with open("productos.txt", "a") as archivo_productos:
        nombre = input("Ingrese el nombre del producto: ").capitalize()
        precio = input("Ingrese el precio del producto: ").capitalize()
        cantidad = input("Ingrese la cantidad del producto: ").capitalize()
        archivo_productos.write(f"{nombre},{precio},{cantidad}\n")
        
        print("Producto agregado exitosamente.")

def guardar_productos_desde_lista(productos):
    """
    Sobrescribe el archivo productos.txt con los productos de la lista proporcionada.
    Cada producto en la lista debe ser un diccionario con las claves: nombre, precio, cantidad.
    """
    with open("productos.txt", "w") as archivo_productos:
        for producto in productos:
            archivo_productos.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")

# ----------------------------------------------------------------
# Funciones auxiliares para manejo de productos en lista
# ----------------------------------------------------------------     
       
def listar_productos_desde_lista(productos):
    print("\nLista de productos:")
    for producto in productos:
        print(f"{producto["nombre"]} | Precio: ${producto["precio"]} | Cantidad: {producto["cantidad"]}")
    print("-"*40)
    
def agregar_producto_a_lista(productos):
    nombre = input("Ingrese el nombre del producto: ").capitalize()
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    nuevo_producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    productos.append(nuevo_producto)
    print("Producto agregado exitosamente a la lista.")
        
def obtener_productos_como_lista():
    """ 
    Lee el archivo productos.txt y devuelve una lista de diccionarios con los productos.
    Cada diccionario contiene las claves: nombre, precio, cantidad.
    """
    productos = []
    with open("productos.txt", "r") as archivo_productos:
        for linea in archivo_productos:
            linea = linea.strip()
            partes = linea.split(",")
            producto = {
                "nombre": partes[0],
                "precio": float(partes[1]),
                "cantidad": int(partes[2])
            }
            productos.append(producto)
    return productos
        
def buscar_producto_en_lista(productos, nombre_buscar):
    """
    Busca un producto por nombre en la lista de productos.
    Devuelve el diccionario del producto si se encuentra, o None si no existe.
    """
    for producto in productos:
        if producto["nombre"].lower() == nombre_buscar.lower():
            return producto
    return None

# ----------------------------------------------------------------

        
# ----------------------------------------------------------------
# Ejercicios:
# ----------------------------------------------------------------   

def ejercicio_1():
    """
    1) Crear archivo inicial con productos: Crear un archivo de texto llamado
    productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad    
    """
    productos = [
        { "nombre": "Manzana", "precio": 100, "cantidad": 50 },
        { "nombre": "Naranja", "precio": 250.0, "cantidad": 20 },
        { "nombre": "Banana", "precio": 1500.75, "cantidad": 20 }
    ]
    guardar_productos_desde_lista(productos)
    
        
def ejercicio_2():
    """
    2) . Leer y mostrar productos: 
    Crear un programa que abra productos.txt, lea cada línea, la procese con .strip() y .split(","), 
    y muestre los productos en el siguiente formato:
    Producto: Lapicera | Precio: $120.5 | Cantidad: 30  
    """
    listar_productos()
            

def ejercicio_3():
    """
    3)  Agregar productos desde teclado: Modificar el programa para que luego de mostrar
    los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
    cantidad) y lo agregue al archivo sin borrar el contenido existente.

    """ 
    listar_productos()
    agregar_producto_a_archivo()
    

def ejercicio_4():
    """
    4) Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
    una lista llamada productos, donde cada elemento sea un diccionario con claves:
    nombre, precio, cantidad.
    """
    productos = obtener_productos_como_lista()
    print(productos)
   

def ejercicio_5():
    """
    5)  Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
    producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
    no existe, mostrar un mensaje de error.
    """
    
    productos = obtener_productos_como_lista()
    buscar_producto = input("\nIngrese el nombre del producto a buscar: ").capitalize()
    producto_buscado = None
    
    for producto in productos:
        if producto["nombre"] == buscar_producto:
            producto_buscado = producto
    
    if producto_buscado:
        print(f"Producto encontrado: {producto_buscado['nombre']} | Precio: ${producto_buscado['precio']} | Cantidad: {producto_buscado['cantidad']}")
    else:
        print("Producto no encontrado.")
    
                
def ejercicio_6():
    """
    6) Guardar los productos actualizados: Después de haber leído, buscado o agregado productos, 
    sobrescribir el archivo productos.txt escribiendo nuevamente todos los productos actualizados desde la lista.

    """
    
    productos = obtener_productos_como_lista()
    
    while True:
        
        print("\nMenú de opciones:")
        print("1. Listar productos")
        print("2. Agregar producto")
        print("3. Buscar producto por nombre")
        print("4. Guardar y salir")
        
        opcion = input("Seleccione una opción (1-4): ")
        if opcion == "1":
            listar_productos_desde_lista(productos)
        elif opcion == "2":
            agregar_producto_a_lista(productos)
        elif opcion == "3":
            producto_buscado = input("\nIngrese el nombre del producto a buscar: ")
            resultado = buscar_producto_en_lista(productos, producto_buscado)
            if resultado:
                print(f"Producto encontrado: {resultado['nombre']} | Precio: ${resultado['precio']} | Cantidad: {resultado['cantidad']}")
            else:
                print("Producto no encontrado.")
                
        elif opcion == "4":
            guardar_productos_desde_lista(productos)
            print("Archivo productos.txt actualizado exitosamente.")
            break
    
     
if __name__ == "__main__":
    ejercicio_6()
    