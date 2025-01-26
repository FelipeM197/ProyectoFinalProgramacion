import csv
import os
from getpass import getpass
from colorama import init, Fore

# Inicializar colorama
init(autoreset=True)

# Archivo necesario para almacenar las cuentas
archivoCuentas = "cuentas.csv"

# Funcion para inicializar las cuentas si no existe el archivo
def inicializarCuentas():
    if not os.path.exists(archivoCuentas):
        with open(archivoCuentas, mode="w", newline="", encoding="utf-8") as archivo:
            campos = ["nombreUsuario", "contrasena", "saldo"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerow({"nombreUsuario": "FELIPE", "contrasena": "ABC123", "saldo": "1000"})
            escritor.writerow({"nombreUsuario": "URIEL", "contrasena": "XYZ789", "saldo": "1500"})
            escritor.writerow({"nombreUsuario": "ZENAN", "contrasena": "123", "saldo": "2000"})
            escritor.writerow({"nombreUsuario": "AIDAN", "contrasena": "532", "saldo": "2500"})
            escritor.writerow({"nombreUsuario": "JOSUE", "contrasena": "423", "saldo": "3000"})

# Funcion para cargar las cuentas desde el archivo
def cargarCuentas():
    cuentas = []
    if os.path.exists(archivoCuentas):
        with open(archivoCuentas, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                cuentas.append({
                    "nombreUsuario": fila["nombreUsuario"],
                    "contrasena": fila["contrasena"],
                    "saldo": float(fila["saldo"])
                })
    return cuentas

# Funcion para autenticar al usuario
def autenticarUsuario(cuentas):
    usuario = input(Fore.CYAN + "Ingrese su usuario: ").strip()
    contrasena = getpass(Fore.CYAN + "Ingrese su contrasena: ").strip()

    cuenta = next((c for c in cuentas if c["nombreUsuario"] == usuario and c["contrasena"] == contrasena), None)

    if cuenta:
        print(Fore.GREEN + "Autenticacion exitosa.")
        return cuenta
    else:
        print(Fore.RED + "Usuario o contrasena incorrectos.")
        return None

# Funcion para salir del sistema
def salirSistema():
    while True:
        respuesta = input(Fore.CYAN + "Esta seguro que desea salir del sistema? (si/no): ").strip().lower()
        if respuesta == "si":
            print(Fore.GREEN + "Saliendo del sistema...")
            exit()
        elif respuesta == "no":
            print(Fore.YELLOW + "Continuando en el sistema...")
            return
        else:
            print(Fore.RED + "Por favor, responda con 'si' o 'no'.")

# Simulacion del programa
if __name__ == "__main__":
    inicializarCuentas()
    cuentas = cargarCuentas()

    usuarioAutenticado = None

    while not usuarioAutenticado:
        usuarioAutenticado = autenticarUsuario(cuentas)

    while True:
        print(Fore.CYAN + "\n##### Menu #####")
        print(Fore.WHITE + "1. Salir del sistema")
        opcion = input("Selecciona una opcion: ").strip()

        if opcion == "1":
            salirSistema()
        else:
            print(Fore.RED + "Selecciona una opcion valida.")