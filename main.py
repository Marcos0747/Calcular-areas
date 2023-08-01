import math

def calcular_area_circulo(radio):
    return math.pi * radio**2

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_area_cuadrado(lado):
    return lado**2

if __name__ == "__main__":
    print("Gracias por usar este script")

    while True:
        print("\nOpciones:")
        print("1. Calcular área de un círculo")
        print("2. Calcular área de un triángulo")
        print("3. Calcular área de un cuadrado")
        print("4. Salir")

        opcion = input("Elige una opción (1/2/3/4): ")

        if opcion == '1':
            radio = float(input("Ingresa el radio del círculo: "))
            area = calcular_area_circulo(radio)
            print(f"El área del círculo es: {area:.2f}")
        elif opcion == '2':
            base = float(input("Ingresa la base del triángulo: "))
            altura = float(input("Ingresa la altura del triángulo: "))
            area = calcular_area_triangulo(base, altura)
            print(f"El área del triángulo es: {area:.2f}")
        elif opcion == '3':
            lado = float(input("Ingresa el lado del cuadrado: "))
            area = calcular_area_cuadrado(lado)
            print(f"El área del cuadrado es: {area:.2f}")
        elif opcion == '4':
            print("Nos veremos pronto")
            break
        else:
            print("Opción inválida. Por favor, elige una opción válida (1/2/3/4).")
