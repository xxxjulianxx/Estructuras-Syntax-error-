from operaciones import suma, resta, multiplicacion, division, factorial, raiz_cuadrada, potencia

def mostrar_menu():
    print("\n💡 Bienvenido a la Calculadora Especial 💡")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Factorial")
    print("6. Raíz Cuadrada")
    print("7. Potencia")
    print("8. Salir")
    print("-------------------------")

def obtener_opcion():
    return input("Seleccione una opción: ").strip()

def ejecutar_operacion(opcion):
    try:
        a = int(input("Ingrese el primer número: "))
        if opcion in ["1", "2", "3", "4", "7"]:
            b = int(input("Ingrese el segundo número: "))
    except ValueError:
        print("❌ Por favor, ingrese solo números enteros.")
        return

    operaciones = {
        "1": suma,
        "2": resta,
        "3": multiplicacion,
        "4": division,
        "5": factorial,
        "6": raiz_cuadrada,
        "7": potencia
    }

    resultado = operaciones[opcion](a, b) if opcion in ["1", "2", "3", "4", "7"] else operaciones[opcion](a)
    print(f"✅ El resultado es: {resultado}")
