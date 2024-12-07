# Paso 1.1: Imprimir un mensaje en la consola
print("¡Hola! Estas viendo un programa que muestra ejemplos básicos de Python.")


# Paso 1.2: Declarar variables de diferentes tipos y realizar operaciones matemáticas simples
numero_entero = 24 
numero_decimal = 2.5  
cadena_texto = "Python es GOD"  

# Operaciones matemáticas
suma = numero_entero + numero_decimal
resta = numero_entero - numero_decimal
multiplicacion = numero_entero * numero_decimal
division = numero_entero / numero_decimal

# Mostrar resultados de las operaciones matemáticas
print(f"La suma de {numero_entero} y {numero_decimal} es: {suma}")
print(f"La resta de {numero_entero} y {numero_decimal} es: {resta}")
print(f"La multiplicación de {numero_entero} y {numero_decimal} es: {multiplicacion}")
print(f"La división de {numero_entero} entre {numero_decimal} es: {division}")


# Paso 1.3: Concatenar cadenas de texto y usar funciones básicas como print() y input().
mensaje = "¡Bienvenido a " + cadena_texto + "!"
print(mensaje)

nombre = input("¿Cuál es tu nombre? ")
print("¡Encantado de conocerte, " + nombre + "!")


#-----------------------------------------------------------------------------------------------

# Paso 2.1: Script para determinar si un número es par o impar
numero = int(input("Por favor, ingresa un número: "))

if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")


# Paso 2.2: Usar un bucle for para imprimir los cuadrados (multiplicarlo por el mismo) de una lista de números
numeros = [1, 2, 3, 4, 5]
print("\nLos cuadrados de los números en la lista son:")
for n in numeros:
    print(f"El cuadrado de {n} es {n**2}")


# Paso 2.3: Usar un bucle while para solicitar repetidamente la entrada del usuario
print("\nIntroduce un número mayor a 5 para salir del bucle.")
while True:
    entrada = int(input("Ingresa un número: "))
    if entrada > 5:
        print("Número mayor a 5 detectado. ¡Saliendo del bucle!")
        break
    else:
        print("El número no es mayor a 5. Intenta de nuevo.")



#-------------------------------------------------------------------------------------------------------

# Paso 3.1: Crear una lista de nombres y mostrar cada uno usando un bucle
nombres_estudiantes = ["Ricardo", "Andres", "Andrea", "Luis", "Camila"]
print("Lista de estudiantes:")
for nombre in nombres_estudiantes:
    print(f"- {nombre}")


# Paso 3.2: Crear un diccionario de información de contacto y mostrar claves y valores
info_contacto = {
    "nombre": "Ricardo Daza",
    "correo": "rikadaza11@hotmail.com"
}

print("\nInformación de contacto:")
for clave, valor in info_contacto.items():
    print(f"{clave.capitalize()}: {valor}")


# Paso 3.3: Permitir al usuario agregar elementos a una lista o actualizar un diccionario
while True:
    print("\n¿Qué deseas hacer?")
    print("1. Agregar un estudiante a la lista")
    print("2. Actualizar información de contacto")
    print("3. Mostrar todos los datos")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nuevo_estudiante = input("Escribe el nombre del estudiante: ")
        nombres_estudiantes.append(nuevo_estudiante)
        print(f"{nuevo_estudiante} ha sido agregado a la lista.")
    elif opcion == "2":
        clave = input("¿Qué deseas actualizar? (nombre o correo): ").lower()
        if clave in info_contacto:
            nuevo_valor = input(f"Escribe el nuevo valor para {clave}: ")
            info_contacto[clave] = nuevo_valor
            print(f"El {clave} ha sido actualizado a: {nuevo_valor}")
        else:
            print("Clave no válida. Intenta de nuevo.")
    elif opcion == "3":
        print("\nLista de estudiantes:")
        for nombre in nombres_estudiantes:
            print(f"- {nombre}")
        print("\nInformación de contacto:")
        for clave, valor in info_contacto.items():
            print(f"{clave.capitalize()}: {valor}")
    elif opcion == "4":
        print("¡Saliendo :)!")
        break
    else:
        print("Opción no válida. Por favor, intenta de nuevo.")


#-------------------------------------------------------------------------------------------------

# Calculadora Básica
def calculadora():
    print("Bienvenido a la calculadora básica")
    print("Opciones disponibles: suma, resta, multiplicacion, division")
    while True:
        operacion = input("Escribe la operación que deseas realizar (o 'salir' para terminar): ").lower()
        if operacion == "salir":
            print("¡Adiós!")
            break
        if operacion not in ["suma", "resta", "multiplicacion", "division"]:
            print("Operación no válida. Intenta de nuevo.")
            continue
        
        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Por favor, ingresa números válidos.")
            continue

        if operacion == "suma":
            print(f"Resultado: {num1 + num2}")
        elif operacion == "resta":
            print(f"Resultado: {num1 - num2}")
        elif operacion == "multiplicacion":
            print(f"Resultado: {num1 * num2}")
        elif operacion == "division":
            if num2 == 0:
                print("No se puede dividir entre cero.")
            else:
                print(f"Resultado: {num1 / num2}")

calculadora()





import random

# Juego de adivinanza
def juego_adivinanza():
    print("¡Bienvenido al juego de adivinanza!")
    numero_secreto = random.randint(1, 100)
    intentos = 0

    while True:
        try:
            adivina = int(input("Adivina el número (entre 1 y 100): "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        intentos += 1
        if adivina < numero_secreto:
            print("El número es mayor.")
        elif adivina > numero_secreto:
            print("El número es menor.")
        else:
            print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
            break

juego_adivinanza()




