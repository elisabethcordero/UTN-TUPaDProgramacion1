
import random

def ejercicio_1():
    '''
    1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
    (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

    '''

    for numero in range(101):
        print(numero)
    

def ejercicio_2():
    '''
    2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
    dígitos que contiene.

    '''

    numero = input("Por favor ingrese un numero entero: ")
    cantidad_digitos = len(numero)
    print(f"El numero {numero} tiene {cantidad_digitos} digitos.")
    
    
def ejercicio_3():
    '''
    3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores.

    '''
    
    valorIngresado_1 = int(input("Por favor ingrese el primer valor (entero): "))
    valorIngresado_2 = int(input("Por favor ingrese el segundo valor (entero): "))
    suma = 0
    
    if valorIngresado_1 > valorIngresado_2:
        valor1 = valorIngresado_2
        valor2 = valorIngresado_1
    else:   
        valor1 = valorIngresado_1
        valor2 = valorIngresado_2
        
    for numero in range(valor1 + 1, valor2):
        suma += numero
        
    print(f"La suma de los numeros entre {valor1} y {valor2} es: {suma}")   
    

def ejercicio_4():
    '''
    4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0.
    '''

    suma = 0
    
    while True:
        numero = int(input("Por favor ingrese un numero entero (0 para finalizar): "))
        if numero == 0:
            break
        suma += numero

    print(f"La suma total es: {suma}")


def  ejercicio_5():
    '''
   5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

    '''
    
    numero_aleatorio = random.randint(0, 9)
    intentos = 0
    
    while True:
        numero_usuario = int(input("Por favor ingrese un numero entre 0 y 9: "))
        intentos += 1
        if numero_usuario == numero_aleatorio:
            break
        else:
            print("Numero incorrecto, intente nuevamente.")
            
    print(f"Felicidades! Ha adivinado el numero {numero_aleatorio} en {intentos} intentos.")
    
    
def ejercicio_6():
    '''
    6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
    entre 0 y 100, en orden decreciente.
    
    '''
    
    for cont in range(101,0,-1):
        if cont % 2 == 0:
            print(cont) 
              
            
def ejercicio_7():
    '''
    7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
    número entero positivo indicado por el usuario.
    
    '''
    
    num1 = 0
    num2 = -1
    sumatoria = 0
    
    while num2 < 0:    
        num2 = int(input("Por favor ingrese un numero (entero positivo): "))
        
        if num2 < 0:
            print(f"{num2}  es negativo! :(")

    if num1 > num2:
        num1 = num2
        num2 = num1
    else:   
        num1 = num1
        num2 = num2
        
    for numero in range(num1, num2 + 1):
        sumatoria += numero
        
    print(f"La suma de los numeros entre {num1} y {num2} es: {sumatoria}")   
    
    
def ejercicio_8():
    '''
    8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
    programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
    negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
    menor, pero debe estar preparado para procesar 100 números con un solo cambio).

    '''
    
    cantidad_numeros = 100
    contador_pares = 0
    contador_impares = 0
    contador_positivos = 0
    contador_negativos = 0
    
    for _ in range(cantidad_numeros):
        numero = int(input("Por favor ingrese un numero entero: "))
        
        if numero % 2 == 0:
            contador_pares += 1
        else:
            contador_impares += 1
            
        if numero > 0:
            contador_positivos += 1
        elif numero < 0:
            contador_negativos += 1
            
    print(f"Cantidad de numeros pares: {contador_pares}")
    print(f"Cantidad de numeros impares: {contador_impares}")
    print(f"Cantidad de numeros positivos: {contador_positivos}")
    print(f"Cantidad de numeros negativos: {contador_negativos}")
 
 
def ejercicio_9():
    '''
    9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
    media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
    poder procesar 100 números cambiando solo un valor).

    '''
    cantidad_numeros = 100
    suma = 0
    
    for _ in range(cantidad_numeros):
        numero = int(input("Por favor ingrese un numero entero: "))
        suma += numero
        
    media = suma / cantidad_numeros
    print(f"La media de los {cantidad_numeros} numeros ingresados es: {media}")


def ejercicio_10():
    '''
    10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

    '''
    
    numero = input("Por favor ingrese un numero entero: ")
    numero_invertido = ""

    for i in range(len(numero)-1, -1, -1):  
        numero_invertido += numero[i]

    print(f"El numero {numero} invertido es: {numero_invertido}")

    

if __name__ == "__main__":
    ejercicio_1()