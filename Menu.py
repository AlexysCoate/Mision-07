#Nombre: Alexys Martin Coate Reyes
#Descripción: Crear un programa que pueda elegir entre dividir o elegir un número mayor

def dividir(dividendo, divisor):
    dividendoInicial= dividendo
    contador = 0

    while divisor & dividendo <= 0:
        print("El divisor no puede ser 0 y no se acepta números negativos. Por favor ingresa otro número")
        dividendo = int(input("Ingresa el dividendo: "))
        divisor = int(input("Ingresa el divisor: "))

    while dividendo >= divisor:
        contador += 1
        dividendo -= divisor
        print(dividendo)
    print("{} / {} = {}, sobra {} " .format(dividendoInicial, divisor, contador, dividendo))


def calcularMayor(nuevoNumero):
    numeroAnterior = 0

    while nuevoNumero != -1:
        if (nuevoNumero > numeroAnterior) & (nuevoNumero > 0):
            numeroAnterior = nuevoNumero
            nuevoNumero = int(input("Ingresa un número (Teclea -1 para salir): "))
        elif (nuevoNumero <= numeroAnterior) & (nuevoNumero > 0):
            nuevoNumero = int(input("Ingresa un número (Teclea -1 para salir): "))
        elif nuevoNumero <= 0:
            print("Ingresa un entero positivo o un número diferente de 0")
            nuevoNumero = int(input("Ingresa un número (Teclea -1 para salir): "))


    if numeroAnterior == 0:
        print("No hay valor mayor")
    else:
        print("El mayor es: ", numeroAnterior)


def menu(opcion):
    print("""
    Misión 07. Ciclos While
    Autor: Alexys Martín Coate Reyes
    Matrícula: A01746998
        1. Calcular divisiones
        2. Encontrar el mayor
        3. Salir""")

def main():
    opcion = 0
    menu(opcion)
    opcion = int(input("    Teclea tu opción: "))
    while opcion != 3:
        if opcion == 1:
            dividendo = int(input("Ingresa el dividendo: "))
            divisor = int(input("Ingresa el divisor: "))
            dividir(dividendo, divisor)
            menu(opcion)
            opcion = int(input("    Teclea tu opción: "))
        elif opcion == 2:
            nuevoNumero = int(input("Ingresa un número (Teclea -1 para salir): "))
            calcularMayor(nuevoNumero)
            menu(opcion)
            opcion = int(input("    Teclea tu opción: "))
        else:
            print("""Ingresa un número enlistado!
            """)
            menu(opcion)
            opcion = int(input("    Teclea tu opción: "))

main()