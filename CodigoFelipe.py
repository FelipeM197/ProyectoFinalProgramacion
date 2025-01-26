import csv
import os
import datetime
import pytz
from colorama import init, Fore

# Inicializar colorama
init(autoreset=True)

# Variables de archivos y zona horaria
tz = pytz.timezone("America/Guayaquil")
archivo_transacciones = "transacciones.csv"
archivo_cuentas = "cuentas.csv"

# Función para inicializar las cuentas si no existe el archivo
def inicializarCuentas():
    if not os.path.exists(archivo_cuentas):
        with open(archivo_cuentas, mode="w", newline="", encoding="utf-8") as archivo:
            campos = ["nombreUsuario", "saldo"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerow({"nombreUsuario": "USUARIO1", "saldo": "2500"})
            escritor.writerow({"nombreUsuario": "USUARIO2", "saldo": "1500"})

# Función para cargar cuentas desde el archivo
def cargarCuentas():
    cuentas = []
    if os.path.exists(archivo_cuentas):
        with open(archivo_cuentas, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                cuentas.append({"nombreUsuario": fila["nombreUsuario"], "saldo": float(fila["saldo"])})
    return cuentas

# Función para guardar cuentas en el archivo
def guardarCuentas(cuentas):
    with open(archivo_cuentas, mode="w", newline="", encoding="utf-8") as archivo:
        campos = ["nombreUsuario", "saldo"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        for cuenta in cuentas:
            escritor.writerow({"nombreUsuario": cuenta["nombreUsuario"], "saldo": cuenta["saldo"]})

# Función para cargar transacciones desde el archivo
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
        "saldo": usuario["saldo"]
    }
    with open(archivo_transacciones, mode="a", newline="", encoding="utf-8") as archivo:
        campos = ["fecha", "monto", "tipo", "nombreUsuario", "saldo"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        if archivo.tell() == 0:
            escritor.writeheader()
        escritor.writerow(transaccion)

# Función para mostrar historial de transacciones
def mostrarHistorial(usuario):
    transacciones = cargarTransacciones()
    transacciones_usuario = [t for t in transacciones if t["nombreUsuario"] == usuario["nombreUsuario"]]

    if not transacciones_usuario:
        print(Fore.YELLOW + "\nNo tienes transacciones registradas.")
        return

    print(Fore.CYAN + "\n##### Historial de Transacciones #####")
    for t in transacciones_usuario:
        print(Fore.WHITE + f"Fecha: {t['fecha']}, Tipo: {t['tipo']}, Monto: {t['monto']}, Saldo: {t['saldo']}")

# Función para consultar el saldo actual
def consultarSaldo(usuario):
    print(Fore.GREEN + f"Tu saldo actual es: {usuario['saldo']}")

# Función para transferir dinero entre cuentas
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
            registrarTransaccion(usuario, "Transferencia Enviada", -monto)
            registrarTransaccion(cuentaDestino, "Transferencia Recibida", monto)
            print(Fore.GREEN + f"Transferencia exitosa. Nuevo saldo: {usuario['saldo']:.2f}")
        else:
            print(Fore.RED + "Saldo insuficiente.")
    except ValueError:
        print(Fore.RED + "Por favor, ingresa un monto válido.")

# Menú principal del usuario
def menuUsuario(usuario, cuentas):
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
                    guardarCuentas(cuentas)
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
                    guardarCuentas(cuentas)
                    print(Fore.GREEN + "Depósito realizado con éxito.")
                else:
                    print(Fore.RED + "Monto inválido.")
            except ValueError:
                print(Fore.RED + "Monto ingresado no válido.")

        elif opcion == "3":
            transferirDinero(cuentas, usuario)

        elif opcion == "4":
            mostrarHistorial(usuario)

        elif opcion == "5":
            consultarSaldo(usuario)

        elif opcion == "6":
            print(Fore.GREEN + "Cerrando sesión...")
            break

        else:
            print(Fore.RED + "Selecciona una opción válida.")

# Inicialización del sistema
if __name__ == "__main__":
    inicializarCuentas()
    cuentas = cargarCuentas()
    usuario = next((c for c in cuentas if c["nombreUsuario"] == "USUARIO1"), None)

    if usuario:
        menuUsuario(usuario, cuentas)
    else:
        print(Fore.RED + "No se pudo cargar la cuenta.")