import csv  # Para manejar archivos CSV
import os  # Para verificar la existencia de archivos
import datetime  # Para trabajar con fechas y horas
import pytz
from colorama import init, Fore  # Para colores en la consola

# Inicializar colorama
init(autoreset=True)

# Variables
tz = pytz.timezone("America/Guayaquil")  # Zona horaria de Ecuador
archivo_transacciones = "transacciones.csv"

# Función para cargar transacciones desde el archivo CSV
def cargarTransacciones():
    transacciones = []
    if os.path.exists(archivo_transacciones):
        with open(archivo_transacciones, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                transacciones.append(fila)
    return transacciones

# Función para registrar una transacción
def registrarTransaccion(usuario, operacion, valor):
    transaccion = {
        "fecha": datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S"),
        "monto": valor,
        "tipo": operacion,
        "nombreUsuario": usuario["nombreUsuario"],
        "saldo": usuario["saldo"],
    }
    with open(archivo_transacciones, mode="a", newline="", encoding="utf-8") as archivo:
        campos = ["fecha", "monto", "tipo", "nombreUsuario", "saldo"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        if archivo.tell() == 0:
            escritor.writeheader()
        escritor.writerow(transaccion)

# Función para mostrar el historial de transacciones del usuario
def mostrar_historial(usuario):
    transacciones = cargarTransacciones()
    transacciones_usuario = [t for t in transacciones if t["nombreUsuario"] == usuario["nombreUsuario"]]

    if not transacciones_usuario:
        print(Fore.YELLOW + "\nNo tienes transacciones registradas.")
        return

    print(Fore.CYAN + "\n##### Historial de Transacciones #####")
    for t in transacciones_usuario:
        print(Fore.WHITE + f"Fecha: {t['fecha']}, Tipo: {t['tipo']}, Monto: {t['monto']}, Saldo: {t['saldo']}")

# Función para consultar el saldo actual del usuario
def consultar_saldo(usuario):
    print(Fore.GREEN + f"Tu saldo actual es: {usuario['saldo']}")

# Menú principal del usuario
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
            try:
                valor = float(input("Ingresa el monto a retirar: ").strip())
                if valor > 0 and usuario["saldo"] >= valor:
                    usuario["saldo"] -= valor
                    registrarTransaccion(usuario, "Retiro", -valor)
                    print(Fore.GREEN + "Retiro realizado con éxito.")
                else:
                    print(Fore.RED + "Fondos insuficientes o monto inválido.")
            except ValueError:
                print(Fore.RED + "Monto ingresado no válido.")

        elif opcion == "2":
            try:
                valor = float(input("Ingresa el monto a depositar: ").strip())
                if valor > 0:
                    usuario["saldo"] += valor
                    registrarTransaccion(usuario, "Depósito", valor)
                    print(Fore.GREEN + "Depósito realizado con éxito.")
                else:
                    print(Fore.RED + "Monto inválido.")
            except ValueError:
                print(Fore.RED + "Monto ingresado no válido.")

        elif opcion == "3":
            print(Fore.YELLOW + "Funcionalidad de transferencias no implementada aún.")

        elif opcion == "4":
            mostrar_historial(usuario)

        elif opcion == "5":
            consultar_saldo(usuario)

        elif opcion == "6":
            print(Fore.GREEN + "Cerrando sesión...")
            break

        else:
            print(Fore.RED + "Selecciona una opción válida.")

# Simulación de un usuario
usuario = {
    "nombreUsuario": "Ejemplo",
    "saldo": 1000.0  # Saldo inicial del usuario
}

# Llamada al menú del usuario
if __name__ == "__main__":
    menuUsuario(usuario)
