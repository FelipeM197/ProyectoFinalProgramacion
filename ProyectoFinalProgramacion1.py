# ------------------------ Librerías ------------------------
import csv  # para usar archivos csv
import os  # verifica la existencia de los archivos y limpiar consola
import datetime  # para la fecha y hora en el historial de transacciones
import pytz
from getpass_asterisk.getpass_asterisk import getpass_asterisk  # para que en vez de la contraseña se vena asteriscos
from colorama import init, Fore, Style  # para colores en la consola
from getpass import getpass  # para ocultar la entrada en "Presione Enter para continuar"

# Inicializar colorama
init(autoreset=True)

# ------------------------ Variables ------------------------
archivoCuentas = "cuentas.csv"  # los dos son archivos de bases de datos
archivoTransacciones = "transacciones.csv"
zonaHoraria = pytz.timezone("America/Guayaquil")  # Ecuador
fechaConZona = datetime.datetime.now(zonaHoraria)

# ------------------------ Funciones ------------------------

def limpiarConsola(mensaje=None):
    if mensaje:
        print(Fore.YELLOW + mensaje)
        getpass(Fore.CYAN + "Presiona Enter para continuar...") #Usamos getpass para que no se vea lo que escribe el usuario antes de presionar ENTER
    os.system("cls" if os.name == "nt" else "clear")

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
            },  # si el archivo no existe inicia un documento con estos datos
            {"nombreUsuario": "URIEL", "contraseña": "XYZ789", "saldo": "1500"},
            {"nombreUsuario": "ZENAN", "contraseña": "123", "saldo": "2000"},
            {"nombreUsuario": "AIDAN", "contraseña": "532", "saldo": "2500"},
            {"nombreUsuario": "JOSUE", "contraseña": "423", "saldo": "3000"},
        ]
        guardarCuentas(cuentasIniciales)
    # Verificar archivo de transacciones
    if not os.path.exists(archivoTransacciones):  # de igual forma si no existe el archivo de transacciones, crea uno
        print(Fore.YELLOW + "Archivo 'transacciones.csv' no encontrado. Creando archivo vacío...")
        with open(
            archivoTransacciones, mode="w", newline="", encoding="utf-8"
        ) as archivo:
            campos = ["fecha", "monto", "tipo", "nombreUsuario", "saldo"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()

# Guardar cuentas en el archivo CSV
def guardarCuentas(cuentas): # es un formato que define los campos "columnas"
    with open(archivoCuentas, mode="w", newline="", encoding="utf-8") as archivo: # sobreescribe en la fila
        campos = ["nombreUsuario", "contraseña", "saldo", "estado", "intentosFallidos"] # si no hay nada escribe estos campos
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        for cuenta in cuentas:
            escritor.writerow(cuenta)

# Cargar cuentas desde el archivo CSV

# Cargar cuentas desde el archivo CSV
def cargarCuentas():
    cuentas = []
    with open(archivoCuentas, mode="r", encoding="utf-8") as archivo:  # abre el archivo modo de lectura
        lector = csv.DictReader(archivo)
        for fila in lector:
            intentos = fila["intentosFallidos"].strip()  # obtenemos el valor y eliminamos espacios en blanco
            if intentos == "":
                intentos = "0"  # si viene vacío, asignamos "0"
            cuenta = {
                "nombreUsuario": fila["nombreUsuario"],
                "contraseña": fila["contraseña"],
                "saldo": fila["saldo"],
                "estado": fila["estado"],  # Cargar el estado de la cuenta
                "intentosFallidos": int(intentos),  # Convertir a entero
            }
            cuentas.append(cuenta)
    return cuentas

# Registrar transacción en el archivo CSV
def registrarTransaccion(usuario, operacion, valor):
    transaccion = {  # aqui detallo los campos del otro archivo
        "fecha": datetime.datetime.now(zonaHoraria).strftime("%Y-%m-%d %H:%M:%S"),
        "monto": valor,
        "tipo": operacion,
        "nombreUsuario": usuario["nombreUsuario"],
        "saldo": usuario["saldo"],
    }  # con esto cargo los procesos al archivo
    with open(
        archivoTransacciones, mode="a", newline="", encoding="utf-8"
    ) as archivo:  # el archivo se abre en funcion de añadir una nueva fila
        campos = [
            "fecha",
            "monto",
            "tipo",
            "nombreUsuario",
            "saldo",
        ]  # si esta vacio escribe esto
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        if archivo.tell() == 0:
            escritor.writeheader()
        escritor.writerow(transaccion)

# Cargar transacciones desde el archivo CSV
def cargarTransacciones():
    transacciones = []
    if os.path.exists(archivoTransacciones):
        with open(
            archivoTransacciones, mode="r", encoding="utf-8"
        ) as archivo:  # se abre el archivo en modo lectura, no cambia nada
            lector = csv.DictReader(archivo)
            for fila in lector:
                transacciones.append(fila)
    return transacciones

# Autenticación del usuario
def autenticarUsuario():
    limpiarConsola()
    usuario = input(Fore.CYAN + "Ingrese su usuario: ").strip().upper() # con esto leemos el usuario de tal forma que eliminamos espacios y lee mayúsculas y minúsculas como iguales

    # Buscar si el usuario existe en las cuentas
    cuenta = next((c for c in cuentas if c["nombreUsuario"] == usuario), None)  # verifica el usuario en el archivo de cuentas

    if not cuenta:
        limpiarConsola("Usuario no encontrado.")
        return None

    if cuenta["estado"] == "BLOQUEADA":  # Si la cuenta está bloqueada
        limpiarConsola("Tu cuenta está bloqueada. Contacta al administrador.")
        return None

    # Si no está bloqueada, pedir contraseña
    contraseña = getpass_asterisk(Fore.CYAN + "Ingresa tu contraseña: ").strip().upper() # importamos la librería para que se vea en asteriscos

    if cuenta["contraseña"] == contraseña:
        # Resetear intentos fallidos si la contraseña es correcta
        cuenta["intentosFallidos"] = 0
        guardarCuentas(cuentas)
        print(Fore.GREEN + "Autenticación exitosa.")
        return cuenta
    else:
        # Incrementar el contador de intentos fallidos
        cuenta["intentosFallidos"] += 1
        guardarCuentas(cuentas)
        limpiarConsola(f"Contraseña incorrecta. Intentos restantes: {3 - cuenta['intentosFallidos']}")

        if cuenta["intentosFallidos"] >= 3:
            cuenta["estado"] = "BLOQUEADA"  # Cambiar el estado a "BLOQUEADA"
            cuenta["intentosFallidos"] = 0  # Resetear los intentos fallidos
            guardarCuentas(cuentas)
            limpiarConsola("Tu cuenta ha sido bloqueada por demasiados intentos fallidos.")
        return None

# Retirar dinero
def retirarDinero(usuario):
    try:
        limpiarConsola()
        monto = float(input(Fore.CYAN + "Ingresa el monto que deseas retirar: "))
        if monto <= 0:
            limpiarConsola("El monto debe ser mayor a 0.")  # tratamos con valores positivos
            return
        if monto > 10000:
            limpiarConsola("El monto máximo para retirar es 10000.")
            return

        saldoActual = float(usuario["saldo"])  # el retiro va a restar su saldo del archivo de cuentas
        if saldoActual >= monto:
            usuario["saldo"] = str(saldoActual - monto)
            registrarTransaccion(usuario, "Retiro", -monto)
            limpiarConsola(f"Retiro exitoso. Tu nuevo saldo es: {usuario['saldo']}")  # también vamos a mostrar el saldo después del retiro
            guardarCuentas(cuentas)
        else:
            limpiarConsola("Saldo insuficiente.")  # en caso de que el retiro sea mayor al saldo, irá un error
    except ValueError:
        limpiarConsola("Por favor, ingresa un número válido.")

# Depositar dinero
def depositarDinero(usuario):
    try:
        limpiarConsola()
        monto = float(input(Fore.CYAN + "Ingresa el monto que deseas depositar: "))
        if monto <= 0:
            limpiarConsola("El monto debe ser mayor a 0.")  # proceso similar al del retiro
            return
        if monto > 10000:
            limpiarConsola("El monto máximo para depositar es 10000.")
            return

        saldoActual = float(usuario["saldo"])  # la diferencia es que este valor se suma al saldo
        usuario["saldo"] = str(saldoActual + monto)
        registrarTransaccion(usuario, "Depósito", monto)
        limpiarConsola(f"Depósito exitoso. Tu nuevo saldo es: {usuario['saldo']}")
        guardarCuentas(cuentas)
    except ValueError:
        limpiarConsola("Por favor, ingresa un número válido.")

# Transferir dinero
def transferirDinero(usuario):
    limpiarConsola()
    print(Fore.CYAN + "\nTransferencia de Dinero")
    destinatario = (
        input("Por favor ingrese el nombre de usuario del destinatario: ").strip().upper()  # de igual forma eliminamos espacios y trabajamos con datos mayúsculas=minúsculas
    )
    if destinatario == usuario["nombreUsuario"]: 
        limpiarConsola("no es posible transferirte a ti mismo") 
        return
   
    cuentaDestino = next(
        (c for c in cuentas if c["nombreUsuario"] == destinatario), None  # lee el archivo y verifica el usuario
    )

    if not cuentaDestino:
        limpiarConsola("Error: La cuenta del destinatario no coincide.")  # si no hay coincidencias arroja un error
        return

    try:
        cantidad = float(input("Por favor digite la cantidad de dinero a transferir: "))
        if cantidad <= 0:
            limpiarConsola("Error: La cantidad de dinero a transferir debe ser positiva.")  # igual manejo de errores en cuanto a cantidades
            return
        if cantidad > 10000:
            limpiarConsola("El monto máximo para transferir es 10000.")
            return
        if float(usuario["saldo"]) < cantidad:
            limpiarConsola("Error: Fondos insuficientes para llevar a cabo la transferencia.")
            return

        # Realizar transferencia
        usuario["saldo"] = str(float(usuario["saldo"]) - cantidad)  # le restamos el valor a quien deposita
        cuentaDestino["saldo"] = str(float(cuentaDestino["saldo"]) + cantidad)  # se lo sumamos a quien es transferido
        registrarTransaccion(usuario, "Transferencia (envío)", -cantidad) 
        registrarTransaccion(cuentaDestino, "Transferencia (recibo)", cantidad)  # reescribimos los datos en los archivos para guardar la transacción
        limpiarConsola(f"Se ha transferido ${cantidad:.2f} a {destinatario} exitosamente.")  # mensaje de verificación
        guardarCuentas(cuentas)
    except ValueError:
        limpiarConsola("Cantidad inválida. Por favor digite un número válido.")  # si hay algún otro error

# Mostrar historial de transacciones de un usuario
def mostrarHistorial(usuario):  # este es el proceso que nos va a mostrar todo lo que hemos guardado en el archivo
    limpiarConsola()
    transacciones = cargarTransacciones()
    transaccionesUsuario = [
        t for t in transacciones if t["nombreUsuario"] == usuario["nombreUsuario"]
    ]

    if not transaccionesUsuario:
        limpiarConsola("No tienes transacciones registradas.")  # si no hay nada a tu nombre de usuario, te lo dice
        return

    print(Fore.CYAN + "\n##### Historial de Transacciones #####")  # si lo hay te lo muestra todo
    for t in transaccionesUsuario:
        print(
            Fore.WHITE + f"Fecha: {t['fecha']}, Tipo: {t['tipo']}, Monto: {t['monto']}, Saldo: {t['saldo']}"
        )
    limpiarConsola(Fore.CYAN + "...")

# Salida del programa
def salidaPrograma():  # es una validación para verificar que de verdad quiere el usuario salir del sistema
    while True:
        limpiarConsola()
        respuesta = (
            input(Fore.CYAN + "¿Está seguro que desea salir del sistema? (si/no): ").strip().upper()  # trabajamos sin espacios y mayúsculas como en todo el proceso
        )
        if respuesta == "SI":
            print(Fore.GREEN + "Saliendo del sistema...")  # si dice que sí, cierra el sistema
            exit()
        elif respuesta == "NO":
            limpiarConsola("Continuando en el sistema...")  # sino abre un return
            return
        else:
            limpiarConsola("Es necesario que elija 'si' o 'no'.")  # sino es ninguna de las dos, arroja un error

# Menú del usuario autenticado
def menuUsuario(usuario):  # interfaz del sistema que muestra todas las opciones
    while True:
        limpiarConsola()
        print(Fore.CYAN + "\n##### Menú del Usuario #####")
        print(Fore.WHITE + "1. Retirar dinero")
        print("2. Depositar dinero")
        print("3. Transferir dinero")
        print("4. Historial de transacciones")
        print("5. Ver saldo")
        print("6. Cerrar sesión")
        opcion = input("Selecciona una opción: ").strip()  # eliminamos los espacios y leemos la respuesta para abrir el proceso
        if opcion == "1":
            retirarDinero(usuario)
        elif opcion == "2":
            depositarDinero(usuario)
        elif opcion == "3":
            transferirDinero(usuario)
        elif opcion == "4":
            mostrarHistorial(usuario)
        elif opcion == "5":
            limpiarConsola(f"Tu saldo actual es: {usuario['saldo']}")
        elif opcion == "6":
            salidaPrograma()
        else:
            limpiarConsola("Selecciona una opción válida.")  # manejo de errores

# ------------------------- Programa Principal -----------------------------
# Inicializar el sistema y cargar las cuentas
inicializarSistema()  # Verifica si los archivos existen, de no ser así los crea con datos iniciales
cuentas = cargarCuentas()  # Carga las cuentas desde el archivo CSV para usarlas en el sistema

# Menú Principal
while True:
    limpiarConsola()  # Limpiamos la consola para mostrar el menú limpio
    print(Fore.CYAN + "########## MENÚ PRINCIPAL ##########")
    print(Fore.WHITE + "1. Iniciar sesión")  # Opción para autenticar al usuario
    print("2. Salir")  # Opción para salir del programa
    seleccionarOpcion = input("Selecciona una opción: ").strip()  # Leer la opción seleccionada por el usuario

    if seleccionarOpcion == "1":
        usuarioActual = autenticarUsuario()  # Llama a la función que autentica al usuario
        if usuarioActual:  # Si el usuario es autenticado correctamente
            menuUsuario(usuarioActual)  # Llama a la función que maneja el menú del usuario
    elif seleccionarOpcion == "2":
        salidaPrograma()  # Si la opción es salir, ejecuta la función para salir del programa
    else:
        limpiarConsola("Selecciona una opción válida.")  # Si la opción no es válida, muestra un error y limpia la consola
    elif seleccionarOpcion == "2":
        salidaPrograma()  # Si la opción es salir, ejecuta la función para salir del programa
    else:
        limpiarConsola("Selecciona una opción válida.")  # Si la opción no es válida, muestra un error y limpia la consola
