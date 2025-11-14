
def ejercicio_1():
    """
    1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
    función para calcular y mostrar en pantalla el factorial de todos los números enteros 
    entre 1 y el número que indique el usuario
    """

    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)

    numero = int(input("Ingrese un número entero positivo: "))
    print(f"Factoriales desde 1 hasta {numero}:")
    for i in range(1, numero + 1):
        print(f"{i}! = {factorial(i)}")


def ejercicio_2():
    """
   2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
    indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
    especifique. 
    """

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    posicion = int(input("Ingrese la posición hasta la cual desea ver la serie de Fibonacci: "))
    print(f"Serie de Fibonacci hasta la posición {posicion}:")
    for i in range(posicion):
        print(fibonacci(i), end=" ")
    
    
def ejercicio_3():
    """
    3) Crea una función recursiva que calcule la potencia de un número base elevado a un 
    exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un 
    algoritmo general. 
    """

    def potencia(base, exponente):
        if exponente == 0:
            return 1
        else:
            return base * potencia(base, exponente - 1)
        
    base = float(input("Ingrese la base: "))
    exponente = int(input("Ingrese el exponente (entero no negativo): "))
    resultado = potencia(base, exponente)
    
    print(f"{base} elevado a la {exponente} es igual a {resultado}")
        
        
def ejercicio_4():
        
    """
    4) Crear una función recursiva en Python que reciba un número entero positivo en base 
    decimal y devuelva su representación en binario como una cadena de texto.
    """

    def decimal_a_binario(n):
        if n == 0:
            return ""
        else:
            return decimal_a_binario(n // 2) + str(n % 2)

    numero = int(input("Ingrese un número entero positivo: "))
    if numero == 0:
        binario = "0"
    else:
        binario = decimal_a_binario(numero)
    
    print(f"La representación binaria de {numero} es: {binario}")
    
    
def ejercicio_5():
    """
    5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
    cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no 
    lo es. 
     Requisitos: 
    La solución debe ser recursiva. 
    No se debe usar [::-1] ni la función reversed().
    """

    def es_palindromo(palabra):
        if len(palabra) <= 1:
            return True
        elif palabra[0] != palabra[-1]:
            return False
        else:
            return es_palindromo(palabra[1:-1])
        
    palabra = input("Ingrese una palabra sin espacios ni tildes: ").lower()
    if es_palindromo(palabra):
        print(f"La palabra '{palabra}' es un palíndromo.")
    else:
        print(f"La palabra '{palabra}' no es un palíndromo.")
        
        
def ejercicio_6():
    """
    6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
    número entero positivo y devuelva la suma de todos sus dígitos. 
     Restricciones: 
    No se puede convertir el número a string. 
    Usá operaciones matemáticas (%, //) y recursión. 
    Ejemplos: 
    suma_digitos(1234)   → 10  (1 + 2 + 3 + 4) 
    suma_digitos(9)      → 9 
    suma_digitos(305)    → 8   (3 + 0 + 5) 
    """

    def suma_digitos(n):
        if n == 0:
            return 0
        else:
            return n % 10 + suma_digitos(n // 10)
    numero = int(input("Ingrese un número entero positivo: "))
    resultado = suma_digitos(numero)
    
    print(f"La suma de los dígitos de {numero} es: {resultado}")
    
    
def ejercicio_7():
    """
    7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
    bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
    último nivel con un solo bloque. 
 
    Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
    nivel más bajo y devuelva el total de bloques que necesita para construir toda la 
    pirámide. 
    
        Ejemplos: 
    contar_bloques(1)   → 1         (1) 
    contar_bloques(2)   → 3         (2 + 1) 
    contar_bloques(4)   → 10        (4 + 3 + 2 + 1)
    """

    def contar_bloques(n):
        if n == 1:
            return 1
        else:
            return n + contar_bloques(n - 1)
    niveles = int(input("Ingrese el número de bloques en el nivel más bajo: "))
    total_bloques = contar_bloques(niveles)
    
    print(f"El total de bloques necesarios para construir la pirámide es: {total_bloques}")
    
    
def ejercicio_8():
    """
    8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
    número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
    aparece ese dígito dentro del número. 
        Ejemplos: 
    contar_digito(12233421, 2)   → 3   
    contar_digito(5555, 5)       → 4   
    contar_digito(123456, 7)     → 0  
    """

    def contar_digito(numero, digito):
        if numero == 0:
            return 0
        else:
            cuenta = 1 if numero % 10 == digito else 0
            return cuenta + contar_digito(numero // 10, digito)
        
    numero = int(input("Ingrese un número entero positivo: "))
    digito = int(input("Ingrese un dígito (0-9) a contar: "))
    cantidad = contar_digito(numero, digito)    
    
    print(f"El dígito {digito} aparece {cantidad} veces en el número {numero}.")
        
    

if __name__ == "__main__":
    ejercicio_8()