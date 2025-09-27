
import random

def ejercicio_1():
    """
    1) Crear una lista con las notas de 10 estudiantes.
    • Mostrar la lista completa.
    • Calcular y mostrar el promedio.
    • Indicar la nota más alta y la más baja.

    """
    notas = [7, 8.5, 6, 9, 5.5, 10, 4, 8, 7.5, 6.5]
    print("Lista de notas:", notas)
    
    promedio = sum(notas) / len(notas)
    print("Promedio de notas:", promedio)
    
    nota_mas_alta = max(notas)
    nota_mas_baja = min(notas)
    print("Nota más alta:", nota_mas_alta)
    print("Nota más baja:", nota_mas_baja)


def ejercicio_2():
    """
    2) Pedir al usuario que cargue 5 productos en una lista.
    • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
    • Preguntar al usuario qué producto desea eliminar y actualizar la lista.
    
    """
    productos = []
    for i in range(5):
        producto = input(f"Ingrese el nombre del producto {i+1}: ")
        productos.append(producto)
    
    print("Lista de productos ordenada alfabéticamente:", sorted(productos))
    
    producto_a_eliminar = input("Ingrese el nombre del producto que desea eliminar: ")
    if producto_a_eliminar in productos:
        productos.remove(producto_a_eliminar)
        print("Producto eliminado. Lista actualizada:", productos)
    else:
        print("El producto no se encuentra en la lista.")
    

def ejercicio_3():
    """
   3) Generar una lista con 15 números enteros al azar entre 1 y 100.
    • Crear una lista con los pares y otra con los impares.
    • Mostrar cuántos números tiene cada lista.

    """
    
    numeros = [random.randint(1, 100) for _ in range(15)]
    print("Lista de números generados:", numeros)
    
    pares = []
    impares = []
    
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    
    print("Números pares:", pares)
    print("La cantidad de números pares en la lista es:", len(pares))
    
    print("Números impares:", impares)
    print("La cantidad de números impares en la lista es:", len(impares))
   

def ejercicio_4():
    """
    4) Dada una lista con valores repetidos:
    [1,3,5,3,7,1,9,5,3]
    
    • Crear una nueva lista sin elementos repetidos.
    • Mostrar el resultado.
    
    """
    
    lista_original = [1, 3, 5, 3, 7, 1, 9, 5, 3]


    lista_sin_repetidos = []
    
    for numero in lista_original:
        if numero not in lista_sin_repetidos:
            lista_sin_repetidos.append(numero)


    print("Lista original:", lista_original)
    print("Lista sin repetidos:", lista_sin_repetidos)
 

def ejercicio_5():
    
    """
   5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
    • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
    • Mostrar la lista final actualizada.

    """
    
    estudiantes = ["Ana", "Luis", "Carlos", "Marta", "Sofía", "Jorge", "Lucía", "Pedro"]
    print("Lista de estudiantes:", estudiantes)
    
    accion = input("¿Desea agregar un nuevo estudiante (A) o eliminar uno existente (E)? ").upper()
    
    if accion == "A":
        nuevo_estudiante = input("Ingrese el nombre del nuevo estudiante: ")
        estudiantes.append(nuevo_estudiante)
        print("Estudiante agregado.")
    elif accion == "E":
        estudiante_a_eliminar = input("Ingrese el nombre del estudiante que desea eliminar: ")
        encontrado = False
        for est in estudiantes:
            if est.lower() == estudiante_a_eliminar.lower():
                estudiantes.remove(est)
                print("Estudiante eliminado.")
                encontrado = True
                break
        if not encontrado:
            print("El estudiante no se encuentra en la lista.")
    else:
        print("Acción no válida.")
    
    print("Lista final de estudiantes:", estudiantes)


def ejercicio_6():
    
    """
    6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
    último pasa a ser el primero).
   
    """
    
    numeros = [10, 20, 30, 40, 50, 60, 70]

    print("Lista original:", numeros)

    numeros_rotados = numeros[-1:] + numeros[:-1]

    print("Lista rotada:", numeros_rotados) 


def ejercicio_7():
    
    """
   7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
    semana.
    • Calcular el promedio de las mínimas y el de las máximas.
    • Mostrar en qué día se registró la mayor amplitud térmica.

    """
    
    temperaturas = [                                
        [15, 25],  # Lunes
        [17, 28],  # Martes
        [14, 22],  # Miércoles
        [16, 30],  # Jueves
        [18, 27],  # Viernes
        [19, 29],  # Sábado
        [13, 24]   # Domingo
    ]
    
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]        
    suma_minimas = 0
    suma_maximas = 0    
    mayor_amplitud = 0
    dia_mayor_amplitud = ""
    
    for i in range(len(temperaturas)):
        minima = temperaturas[i][0]
        maxima = temperaturas[i][1]
        suma_minimas += minima
        suma_maximas += maxima
        
        amplitud = maxima - minima
        if amplitud > mayor_amplitud:
            mayor_amplitud = amplitud
            dia_mayor_amplitud = dias_semana[i]
            
    promedio_minimas = suma_minimas / len(temperaturas)
    promedio_maximas = suma_maximas / len(temperaturas)
    
    print(f"El promedio de temperaturas mínimas es: {promedio_minimas:.2f}")
    print(f"El promedio de temperaturas máximas es: {promedio_maximas:.2f}")
    print(f"El día con mayor amplitud térmica fue {dia_mayor_amplitud} con una amplitud de {mayor_amplitud} grados.")
    
    
def ejercicio_8():
    """
   Crear una matriz con las notas de 5 estudiantes en 3 materias.
    • Mostrar el promedio de cada estudiante.
    • Mostrar el promedio de cada materia.
   
    """
    
    alumnos_notas = [
      [ 8, 10, 7], 
      [ 6, 5, 8], 
      [ 9, 9, 10], 
      [ 7, 8, 6], 
      [ 10, 9, 8], 
    ]
    
    suma_materias = [0, 0, 0]
    for alumno in range(5):
        suma_notas = 0
        for materia in range(3):
            suma_notas += alumnos_notas[alumno][materia]
            suma_materias[materia] += alumnos_notas[alumno][materia]
            
        promedio = suma_notas / 5
                
        print(f"El promedio del Alumno {alumno} es: {promedio:.2f}")
    
    for materia in range(3):
        promedio_materia = suma_materias[materia] / 3
        
        print(f"El promedio de la Materia {materia} es: {promedio_materia:.2f}")
    
   
def ejercicio_9():
    """
   9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
    • Inicializarlo con guiones "-" representando casillas vacías.
    • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
    • Mostrar el tablero después de cada jugada.

    """
    tablero = [
        ["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"]
    ]
    
    while True:    
    
        fila = int(input("Ingrese la fila (0, 1, 2): "))
        columna = int(input("Ingrese la columna (0, 1, 2): "))    
        valor = input("Ingrese el valor (X u O): ").upper()

        tablero[fila][columna] = valor
        
        print("")  
        print("Tablero:")
        for fila in range(3):
            print(tablero[fila])

        print("")
        
def ejercicio_10():
    """
    10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
• Mostrar el total vendido por cada producto.
• Mostrar el día con mayores ventas totales.
• Indicar cuál fue el producto más vendido en la semana.

    """
    
    ventas_dias = [
        [15, 20, 25, 16],  # Lunes
        [18, 22, 30, 20],  # Martes
        [14, 19, 24, 15],  # Miércoles
        [20, 25, 28, 22],  # Jueves
        [17, 21, 26, 18],  # Viernes
        [19, 23, 29, 21],  # Sábado
        [16, 18, 22, 17]   # Domingo
    ]
    
    cantidad_productos_semana = [0, 0, 0, 0]
    dia_mayor_venta = 0
    
    for dia in range(7):
        venta_dia = 0
        for producto in range(4):
            cantidad_productos_semana[producto] += ventas_dias[dia][producto]
            venta_dia += ventas_dias[dia][producto]
            
        if venta_dia > dia_mayor_venta:
            dia_mayor_venta = venta_dia
    
    producto_mas_vendido = 0
    for producto in range(4):
       print(f"Cantidad total vendida del producto {producto}:", cantidad_productos_semana[producto])
       if cantidad_productos_semana[producto] > cantidad_productos_semana[producto_mas_vendido]:
           producto_mas_vendido = producto
            
    print(f"El producto más vendido fue el producto {producto_mas_vendido}")
    print("El día con mayor venta tuvo un total de:", dia_mayor_venta)
    
if __name__ == "__main__":
    ejercicio_1()
    