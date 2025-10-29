
def ejercicio_1():

    """ 
    1) Dado el diccionario precios_frutas
    precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melon': 3000, 'Uva': 1450} 
    Añadir las siguientes frutas con sus respectivos precios: 
    ● Naranja = 1200 
    ● Manzana = 1500 
    ● Pera = 2300 
    """

    precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melon': 3000, 'Uva': 1450}

    precios_frutas['Naranja'] = 1200
    precios_frutas['Manzana'] = 1500
    precios_frutas['Pera'] = 2300

    print(precios_frutas) 

def ejercicio_2():
    """
     Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
    desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
    ● Banana = 1330 
    ● Manzana = 1700 
    ● Melon = 2800
    """
    
    precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melon': 3000, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}

    precios_frutas['Banana'] = 1330
    precios_frutas['Manzana'] = 1700
    precios_frutas['Melon'] = 2800
    
    print(precios_frutas) 

def ejercicio_3():
    """
    3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
    desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
    precios.
    """
    precios_frutas = {'Banana': 1330, 'Ananá': 2500, 'Melon': 2800, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1700, 'Pera': 2300}
   
    lista_frutas = list(precios_frutas.keys())

    print(lista_frutas)
    
    
def ejercicio_4():
    """
    4)  Escribí un programa que permita almacenar y consultar números telefónicos. 
    • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
    • Luego, pedí un nombre y mostrale el número asociado, si existe.
    """
    
    contactos = {}

    for _ in range(5):
        nombre = input("Ingrese el nombre del contacto: ")
        numero = input("Ahora ingrese el número telefónico: ")
        contactos[nombre] = numero

    consulta_contacto = input("Ingrese el nombre del contacto que desea consultar: ".upper())

    if consulta_contacto in contactos:
        print(f"El número de telefóno {consulta_contacto} es {contactos[consulta_contacto]}.")
    else:
        print(f"No se encontró un contacto con el nombre {consulta_contacto}.")        


def ejercicio_5():
    """
    Solicita al usuario una frase e imprime: 
    • Las palabras únicas (usando un set). 
    • Un diccionario con la cantidad de veces que aparece cada palabra. 
    """

    frase = input("Por favor ingrese una frase: ")
    
    contador_palabras = {}

    palabras = frase.split(" ")
    
    palabras_unicas = set(palabras)
    
    print("Palabras unicas: ",palabras_unicas)
    
    contador_palabras = {}
    
    for palabra in palabras:
        if palabra in contador_palabras:
            contador_palabras[palabra] += 1
        else:
            contador_palabras[palabra] = 1
            
    print("Contador de palabras: ",contador_palabras)

def ejercicio_6():
    """
    6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
    Luego, mostrá el promedio de cada alumno. 
    """
    
    alumnos = {}
    
    for alumno in range(3):
        nombre = input("Ingrese el nombre del alumno: ")
        notas = []
        for nota in range(3):
            nota = float(input("Ingrese la nota del alumno: "))
            notas.append(nota)
            
        alumnos[nombre] = tuple(notas)
        
    print(alumnos)
    
   
def ejercicio_7():
    """
    7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
    y Parcial 2: 
    • Mostrá los que aprobaron ambos parciales. 
    • Mostrá los que aprobaron solo uno de los dos. 
    • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
    """
    
    parcial1 = [101, 102, 103, 104, 105]
    parcial2 = [104, 101, 102, 106, 107]
    
    print("Alumnos que aprobaron ambos parciales: ", set(parcial1) & set(parcial2)) 
    print("Alumnos que aprobaron solo un parcial: ", set(parcial1) ^ set(parcial2))
    print("Alumnos que aprobaron al menos un parcial: ", set(parcial1) | set(parcial2))
   
   
def ejercicio_8():
    """
    8)  Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
    Permití al usuario: 
    • Consultar el stock de un producto ingresado. 
    • Agregar unidades al stock si el producto ya existe. 
    • Agregar un nuevo producto si no existe.
    """
    
    productos = {
        "Mesa": 150,
        "Silla": 50, 
        "Estante": 250,
        "Lampara": 70,
        "Cama": 300,
    }     
    
    while True:
        print("\n\n")
        print("="*80)
        print("Listado de productos disponibles:", list(productos.keys()))
       
        producto = input("Ingrese el nombre del producto que desea saber el stock o presione 0 para salir: ").capitalize()
        
        if producto == "0":
            print("Finalizando el programa...")
            break 
        
        if producto in productos:
            print(f"El stock actual del producto: {producto} es {productos[producto]}.")
            
            agregar_stock = input("¿Desea agregar más unidades a este producto? (si/no): ").lower()
            if agregar_stock == "si":
                cantidad_agregar = int(input("Ingrese la cantidad a agregar: "))
                productos[producto] += cantidad_agregar
                print(f"El nuevo stock de {producto} ahora es: {productos[producto]}")
   
        else:
            print("El producto ingresado no existe en el inventario.") 
            agregar_producto = input("¿Desea agregar este producto al inventario? (si/no): ").lower()
            if agregar_producto == "si":
                nuevo_producto = (input("Ingrese el nuevo producto: "))
                productos[producto] = nuevo_producto
                print(f"Producto {producto} agregado con exito!")
                
            else:
                print("No se agregó ningún producto nuevo.")
   
def ejercicio_9():
    """
    9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. 
    Permití consultar qué actividad hay en cierto día y hora.
    """
    
    agenda = {('Lunes', '10:00'): 'Reunión con el equipo',
             ('Martes', '14:00'): 'Cita con el médico',
             ('Miercoles', '16:00'): 'Clase de yoga',
             ('Jueves', '09:00'): 'Desayuno con amigos',
             ('Viernes', '18:00'): 'Cena familiar'
             }

    while True:
        dia = input("Ingrese el día de la semana para consultar su agenda (o salir para terminar): ").capitalize()
        
        if dia == "Salir":
            print("Finalizando la consulta de agenda...")
            break
        
        hora = input("Ingrese la hora (formato HH:MM) para consultar su agenda: ")

        if (dia, hora) in agenda:
            print(f"Tiene programado: {agenda[(dia, hora)]} el {dia} a las {hora}.")  
        else:
            print(f"No tiene ningún evento programado el {dia} a las {hora}.")
    

def ejercicio_10():
    """
    10) 
    """
    paises_ciudades = {
        'Argentina': 'Buenos Aires',
        'Brasil': 'Brasilia',
        'Chile': 'Santiago',
        'Colombia': 'Bogotá',
        'Perú': 'Lima'
    }
    
    print("Listado inicial:", paises_ciudades)
    ciudades_paises = {}
    
    for pais, ciudad in paises_ciudades.items():
        ciudades_paises[ciudad] = pais
        
        
    print("Listado invertido:", ciudades_paises)
   

if __name__ == "__main__":
    ejercicio_10()
    