import csv
import os

# Archivo necesario para almacenar el saldo
archivoCuentas = "cuentas.csv"

# Función para inicializar el archivo con datos iniciales
def inicializarSistema():
    if not os.path.exists(archivoCuentas):
        with open(archivoCuentas, mode="w", newline="", encoding="utf-8") as archivo:
            campos = ["nombreUsuario", "saldo"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerow({"nombreUsuario": "USUARIO", "saldo": "2500"})

# Función para cargar la cuenta
def cargarCuenta():
    with open(archivoCuentas, mode="r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            if fila["nombreUsuario"] == "USUARIO":
                return {"nombreUsuario": fila["nombreUsuario"], "saldo": float(fila["saldo"])}
    return None

# Función para guardar la cuenta
def guardarCuenta(usuario):
    with open(archivoCuentas, mode="w", newline="", encoding="utf-8") as archivo:
        campos = ["nombreUsuario", "saldo"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerow({"nombreUsuario": usuario["nombreUsuario"], "saldo": usuario["saldo"]})

# Función para retirar dinero
def retirarDinero(usuario):
    try:
        monto = float(input("Ingresa el monto que deseas retirar: "))
        if monto <= 0:
            print("El monto debe ser mayor a 0.")
            return

        if usuario["saldo"] >= monto:
            usuario["saldo"] -= monto
            guardarCuenta(usuario)
            print(f"Retiro exitoso. Tu nuevo saldo es: {usuario['saldo']:.2f}")
        else:
            print("Saldo insuficiente.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

# Función para depositar dinero
def depositarDinero(usuario):
    try:
        monto = float(input("Ingresa el monto que deseas depositar: "))
        if monto <= 0:
            print("El monto debe ser mayor a 0.")
            return

        usuario["saldo"] += monto
        guardarCuenta(usuario)
        print(f"Depósito exitoso. Tu nuevo saldo es: {usuario['saldo']:.2f}")
    except ValueError:
        print("Por favor, ingresa un número válido.")

# Simulación del programa
if __name__ == "__main__":
    inicializarSistema()
    usuario = cargarCuenta()

    if usuario:
        while True:
            print("\nOpciones:")
            print("1. Retirar dinero")
            print("2. Depositar dinero")
            print("3. Salir")
            opcion = input("Selecciona una opción: ").strip()

            if opcion == "1":
                retirarDinero(usuario)
            elif opcion == "2":
                depositarDinero(usuario)
            elif opcion == "3":
                print("Gracias por usar el sistema. ¡Adiós!")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")
    else:
        print("No se pudo cargar la cuenta.")
