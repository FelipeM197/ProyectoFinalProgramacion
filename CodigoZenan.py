import csv
import os
from colorama import init, Fore  # Para colores en la consola

# Inicializar colorama
init(autoreset=True)

# Archivo necesario para almacenar las cuentas
archivoCuentas = "cuentas.csv"

# Función para inicializar las cuentas si no existe el archivo
def inicializarCuentas():
    if not os.path.exists(archivoCuentas):
        with open(archivoCuentas, mode="w", newline="", encoding="utf-8") as archivo:
            campos = ["nombreUsuario", "saldo"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerow({"nombreUsuario": "USUARIO1", "saldo": "2500"})
            escritor.writerow({"nombreUsuario": "USUARIO2", "saldo": "1500"})

# Función para cargar las cuentas desde el archivo
def cargarCuentas():
    cuentas = []
    if os.path.exists(archivoCuentas):
        with open(archivoCuentas, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                cuentas.append({"nombreUsuario": fila["nombreUsuario"], "saldo": float(fila["saldo"])})
    return cuentas

# Función para guardar las cuentas en el archivo
def guardarCuentas(cuentas):
    with open(archivoCuentas, mode="w", newline="", encoding="utf-8") as archivo:
        campos = ["nombreUsuario", "saldo"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        for cuenta in cuentas:
            escritor.writerow({"nombreUsuario": cuenta["nombreUsuario"], "saldo": cuenta["saldo"]})

# Función para realizar una transferencia entre cuentas
def transferirDinero(cuentas, usuario):
    destinatario = input("Ingresa el nombre del destinatario: ").strip()
    cuentaDestino = next((c for c in cuentas if c["nombreUsuario"] == destinatario), None)

    if not cuentaDestino:
        print(Fore.RED + "La cuenta del destinatario no existe.")
        return

    try:
        monto = float(input("Ingresa el monto que deseas transferir: "))
        if monto <= 0:
            print(Fore.RED + "El monto debe ser mayor a 0.")
            return

        if usuario["saldo"] >= monto:
            usuario["saldo"] -= monto
            cuentaDestino["saldo"] += monto
            guardarCuentas(cuentas)
            print(Fore.GREEN + f"Transferencia exitosa. Nuevo saldo: {usuario['saldo']:.2f}")
        else:
            print(Fore.RED + "Saldo insuficiente.")
    except ValueError:
        print(Fore.RED + "Por favor, ingresa un monto válido.")

# Simulación del programa
if __name__ == "__main__":
    inicializarCuentas()
    cuentas = cargarCuentas()

    usuario = next((c for c in cuentas if c["nombreUsuario"] == "USUARIO1"), None)

    if usuario:
        while True:
            print(Fore.CYAN + "\n##### Menú #####")
            print(Fore.WHITE + "1. Transferir dinero")
            print("2. Salir")
            opcion = input("Selecciona una opción: ").strip()

            if opcion == "1":
                transferirDinero(cuentas, usuario)
            elif opcion == "2":
                print(Fore.GREEN + "Saliendo del sistema...")
                break
            else:
                print(Fore.RED + "Selecciona una opción válida.")
    else:
        print(Fore.RED + "No se pudo cargar la cuenta.")
