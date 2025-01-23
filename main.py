# ------------------------ Librerías ------------------------
import csv  # para usar archivos csv
import os  # verifica la existencia de los archivos
import datetime  # para la fecha y hora en el historial de transacciones
import pytz
from getpass_asterisk.getpass_asterisk import getpass_asterisk  # para que en vez de la contraseña se vena asteriscos
from colorama import init, Fore, Style  # para colores en la consola

# Inicializar colorama
init(autoreset=True)

# ------------------------ Variables ------------------------
archivoCuentas = "cuentas.csv"  # los dos son archivos de bases de datos
archivoTransacciones = "transacciones.csv"
zona_horaria = pytz.timezone("America/Guayaquil")  # Ecuador
fecha_con_zona = datetime.datetime.now(zona_horaria)

# ------------------------ Funciones ------------------------

# Inicializar archivo con datos iniciales si no existe
def inicializarSistema():
    if not os.path.exists(archivoCuentas):
        print(
            Fore.YELLOW + "Archivo 'cuentas.csv' no encontrado. Creando archivo con datos iniciales..."
        )
        cuentasIniciales = [
            {
                "nombreUsuario": "FELIPE",
                "contraseña": "ABC123",
                "saldo": "1000",
            },
            {"nombreUsuario": "URIEL", "contraseña": "XYZ789", "saldo": "1500"},
            {"nombreUsuario": "ZENAN", "contraseña": "123", "saldo": "2000"},
            {"nombreUsuario": "AIDAN", "contraseña": "532", "saldo": "2500"},
            {"nombreUsuario": "JOSUE", "contraseña": "423", "saldo": "3000"},
        ]
        guardarCuentas(cuentasIniciales)
    if not os.path.exists(archivoTransacciones):
        print(Fore.YELLOW + "Archivo 'transacciones.csv' no encontrado. Creando archivo vacío...")
        with open(
            archivoTransacciones, mode="w", newline="", encoding="utf-8"
        ) as archivo:
            campos = ["fecha", "monto", "tipo", "nombreUsuario", "saldo"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()


def guardarCuentas(cuentas):
    with open(
        archivoCuentas, mode="w", newline="", encoding="utf-8"
    ) as archivo:
        campos = [
            "nombreUsuario",
            "contraseña",
            "saldo",
        ]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        for cuenta in cuentas:
            escritor.writerow(cuenta)


def cargarCuentas():
    cuentas = []
    with open(
        archivoCuentas, mode="r", encoding="utf-8"
    ) as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            cuentas.append(fila)
    return cuentas


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


def cargarTransacciones():
    transacciones = []
    if os.path.exists(archivoTransacciones):
        with open(
            archivoTransacciones, mode="r", encoding="utf-8"
        ) as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                transacciones.append(fila)
    return transacciones


def autenticarUsuario():
    usuario = (
        input(Fore.CYAN + "Ingrese su usuario: ").strip().upper()
    )
    contraseña = (
        getpass_asterisk(Fore.CYAN + "Ingresa tu contraseña: ").strip().upper()
    )

    for cuenta in cuentas:
        if cuenta["nombreUsuario"] == usuario and cuenta["contraseña"] == contraseña:
            print(Fore.GREEN + "Autenticación exitosa.")
            return cuenta
    print(Fore.RED + "Usuario o contraseña incorrectos.")
    return None


def retirarDinero(usuario):
    try:
        monto = float(input(Fore.CYAN + "Ingresa el monto que deseas retirar: "))
        if monto <= 0:
            print(Fore.RED + "El monto debe ser mayor a 0.")
            return

        saldo_actual = float(usuario["saldo"])
        if saldo_actual >= monto:
            usuario["saldo"] = str(saldo_actual - monto)
            registrarTransaccion(usuario, "Retiro", -monto)
            print(Fore.GREEN + f"Retiro exitoso. Tu nuevo saldo es: {usuario['saldo']}")
            guardarCuentas(cuentas)
        else:
            print(Fore.RED + "Saldo insuficiente.")
    except ValueError:
        print(Fore.RED + "Por favor, ingresa un número válido.")


def depositar_dinero(usuario):
    try:
        monto = float(input(Fore.CYAN + "Ingresa el monto que deseas depositar: "))
        if monto <= 0:
            print(Fore.RED + "El monto debe ser mayor a 0.")
            return

        saldo_actual = float(usuario["saldo"])
        usuario["saldo"] = str(saldo_actual + monto)
        registrarTransaccion(usuario, "Depósito", monto)
        print(Fore.GREEN + f"Depósito exitoso. Tu nuevo saldo es: {usuario['saldo']}")
        guardarCuentas(cuentas)
    except ValueError:
        print(Fore.RED + "Por favor, ingresa un número válido.")


def transferir_dinero(usuario):
    print(Fore.CYAN + "\nTransferencia de Dinero")
    destinatario = (
        input("Por favor ingrese el nombre de usuario del destinatario: ")
        .strip()
        .upper()
    )
    cuentaDestino = next(
        (c for c in cuentas if c["nombreUsuario"] == destinatario),
        None,
    )

    if not cuentaDestino:
        print(Fore.RED + "Error: La cuenta del destinatario no coincide.")
        return

    try:
        cantidad = float(input("Por favor digite la cantidad de dinero a transferir: "))
        if cantidad <= 0:
            print(Fore.RED + "Error: La cantidad de dinero a transferir debe ser positiva.")
            return
        if float(usuario["saldo"]) < cantidad:
            print(Fore.RED + "Error: Fondos insuficientes para llevar a cabo la transferencia.")
            return

        usuario["saldo"] = str(float(usuario["saldo"]) - cantidad)
        cuentaDestino["saldo"] = str(float(cuentaDestino["saldo"]) + cantidad)
        registrarTransaccion(usuario, "Transferencia (envío)", -cantidad)
        registrarTransaccion(cuentaDestino, "Transferencia (recibo)", cantidad)
        print(Fore.GREEN + f"Se ha transferido ${cantidad:.2f} a {destinatario} exitosamente.")
        guardarCuentas(cuentas)
    except ValueError:
        print(Fore.RED + "Cantidad invalida. Por favor digite un número valido.")


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


def salida_programa():
    while True:
        respuesta = (
            input(Fore.CYAN + "¿Está seguro que desea salir del sistema? (si/no): ")
            .strip()
            .upper()
        )
        if respuesta == "SI":
            print(Fore.GREEN + "Saliendo del sistema...")
            exit()
        elif respuesta == "NO":
            print(Fore.YELLOW + "Continuando en el sistema...")
            return
        else:
            print(Fore.RED + "Es necesario que elija 'si' o 'no'.")


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
            retirarDinero(usuario)
        elif opcion == "2":
            depositar_dinero(usuario)
        elif opcion == "3":
            transferir_dinero(usuario)
        elif opcion == "4":
            mostrar_historial(usuario)
        elif opcion == "5":
            print(Fore.GREEN + f"Tu saldo actual es: {usuario['saldo']}")
        elif opcion == "6":
            salida_programa()
        else:
            print(Fore.RED + "Selecciona una opción válida.")

# ------------------------- Programa Principal -----------------------------
inicializarSistema()
cuentas = cargarCuentas()

while True:
    print(Fore.CYAN + "########## MENÚ PRINCIPAL ##########")
    print(Fore.WHITE + "1. Iniciar sesión")
    print("2. Salir")
    seleccionar_opcion = input("Selecciona una opción: ").strip()

    if seleccionar_opcion == "1":
        usuario_actual = autenticarUsuario()
        if usuario_actual:
            menuUsuario(usuario_actual)
    elif seleccionar_opcion == "2":
        salida_programa()
    else:
        print(Fore.RED + "Selecciona una opción válida.")