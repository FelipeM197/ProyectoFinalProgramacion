from colorama import init, Fore  # agregar color al texto en la terminal

# Inicializar colorama
init(autoreset=True)


def menuUsuario(usuario):
    while True:
        print(Fore.CYAN + "\n##### Menú del Usuario #####")
        print(Fore.WHITE + "1. Retirar dinero")
        print("2. Depositar dinero")
        print("3. Transferir dinero")
        print("4. Historial de transacciones")
        print("5. Ver saldo")
        print("6. Cerrar sesión")
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            print(Fore.YELLOW + "Opción para retirar dinero seleccionada.")
            # Aquí iría la lógica para retirar dinero
        elif opcion == "2":
            print(Fore.YELLOW + "Opción para depositar dinero seleccionada.")
            # Aquí iría la lógica para depositar dinero
        elif opcion == "3":
            print(Fore.YELLOW + "Opción para transferir dinero seleccionada.")
            # Aquí iría la lógica para transferir dinero
        elif opcion == "4":
            print(
                Fore.YELLOW + "Opción para ver historial de transacciones seleccionada."
            )
            # Aquí iría la lógica para mostrar el historial de transacciones
        elif opcion == "5":
            print(Fore.GREEN + f"Tu saldo actual es: {usuario['saldo']}")
            # Simula ver el saldo actual
        elif opcion == "6":
            print(Fore.GREEN + "Cerrando sesión...")
            break
        else:
            print(Fore.RED + "Selecciona una opción válida.")


# Simulación de un usuario
usuario = {"nombreUsuario": "Ejemplo", "saldo": 1000}  # Saldo inicial del usuario

# Llamada al menú del usuario
menuUsuario(usuario)
