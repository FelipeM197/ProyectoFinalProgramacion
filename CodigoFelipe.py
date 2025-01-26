import csv  # Para manejar archivos CSV
import os  # Para verificar la existencia de archivos
import datetime  # Para trabajar con fechas y horas
import pytz
from colorama import init, Fore  # Para colores en la consola

# Inicializar colorama
init(autoreset=True)

# Variables
archivoTransacciones = "transacciones.csv"
zona_horaria = pytz.timezone("America/Guayaquil")  # Zona horaria de Ecuador

# Función para cargar transacciones desde el archivo CSV
def cargarTransacciones():
    transacciones = []
    if os.path.exists(archivoTransacciones):
        with open(archivoTransacciones, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                transacciones.append(fila)
    return transacciones

# Función para registrar una transacción
def registrarTransaccion(usuario, operacion, valor):
    transaccion = {
        "fecha": datetime.datetime.now(zona_horaria).strftime("%Y-%m-%d %H:%M:%S"),
        "monto": valor,
        "tipo": operacion,
        "nombreUsuario": usuario["nombreUsuario"],
        "saldo": usuario["saldo"],
    }
    with open(
        archivoTransacciones, mode="a", newline="", encoding="utf-8"
    ) as archivo:
        campos = [
            "fecha",
            "monto",
            "tipo",
            "nombreUsuario",
            "saldo",
        ]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        if archivo.tell() == 0:
            escritor.writeheader()
        escritor.writerow(transaccion)

# Función para mostrar el historial de transacciones del usuario
def mostrar_historial(usuario):
    transacciones = cargarTransacciones()
    transacciones_usuario = [
        t for t in transacciones if t["nombreUsuario"] == usuario["nombreUsuario"]
    ]

    if not transacciones_usuario:
        print(Fore.YELLOW + "\nNo tienes transacciones registradas.")
        return

    print(Fore.CYAN + "\n##### Historial de Transacciones #####")
    for t in transacciones_usuario:
        print(
            Fore.WHITE
            + f"Fecha: {t['fecha']}, Tipo: {t['tipo']}, Monto: {t['monto']}, Saldo: {t['saldo']}"
        )

# Función para consultar el saldo actual del usuario
def consultar_saldo(usuario):
    print(Fore.GREEN + f"Tu saldo actual es: {usuario['saldo']}")

# Función principal
if __name__ == "__main__":
    # Ejemplo de usuario autenticado
    usuario_actual = {
        "nombreUsuario": "FELIPE",
        "saldo": "1000"
    }

    while True:
        print(Fore.CYAN + "\n##### Menú #####")
        print(Fore.WHITE + "1. Consultar saldo")
        print("2. Ver historial de transacciones")
        print("3. Registrar una transacción")
        print("4. Salir")
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            consultar_saldo(usuario_actual)
        elif opcion == "2":
            mostrar_historial(usuario_actual)
        elif opcion == "3":
            operacion = input("Ingrese el tipo de operación (Deposito/Retiro): ").strip()
            try:
                valor = float(input("Ingrese el monto: ").strip())
                if operacion.lower() in ["deposito", "retiro"] and valor > 0:
                    if operacion.lower() == "retiro" and float(usuario_actual["saldo"]) < valor:
                        print(Fore.RED + "Fondos insuficientes para realizar el retiro.")
                    else:
                        usuario_actual["saldo"] = str(float(usuario_actual["saldo"]) + valor if operacion.lower() == "deposito" else float(usuario_actual["saldo"]) - valor)
                        registrarTransaccion(usuario_actual, operacion.capitalize(), valor if operacion.lower() == "deposito" else -valor)
                        print(Fore.GREEN + "Transacción realizada con éxito.")
                else:
                    print(Fore.RED + "Operación no válida o monto incorrecto.")
            except ValueError:
                print(Fore.RED + "Monto ingresado no es válido.")
        elif opcion == "4":
            print(Fore.GREEN + "Saliendo del sistema...")
            break
        else:
            print(Fore.RED + "Selecciona una opción válida.")