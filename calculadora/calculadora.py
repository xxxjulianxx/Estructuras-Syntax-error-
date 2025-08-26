from menu_opciones import mostrar_menu, obtener_opcion, ejecutar_operacion

def main():
    while True:
        mostrar_menu()
        opcion = obtener_opcion()

        if opcion == "8":
            print("Saliendo del programa... ¡Gracias por usar la calculadora! 👋")
            break

        if opcion not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("❌ Opción no válida. Intente de nuevo.")
            continue

        ejecutar_operacion(opcion)

if __name__ == "__main__":
    main()
