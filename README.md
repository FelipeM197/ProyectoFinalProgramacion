# Proyecto Final de Programación 1

Este proyecto es un sistema bancario básico que permite a los usuarios realizar operaciones como depósitos, retiros, transferencias 
y consultar su historial de transacciones. 
También incluye un sistema de autenticación para garantizar la seguridad de las cuentas de los usuarios.

El proyecto fue desarrollado en repl.it, por lo que puede ser fácilmente ejecutado en dicho IDE

## Requisitos

### Software necesario
- Python 3.8 o superior

### Librerías requeridas
- `colorama`: Para mejorar la experiencia del usuario con colores en la consola.
- `pytz`: Para manejar la zona horaria de las transacciones.
- `getpass-asterisk`: Para ocultar la entrada de contraseñas al mostrarlas como asteriscos.

Puedes instalar las dependencias necesarias con:
```
pip install colorama
pip install pytz
pip install getpass-asterisk
```

## Estructura del Proyecto

- **`ProyectoFinalProgramacion1.py`**: Archivo principal que contiene todo el código del sistema.
- **`cuentas.csv`**: Archivo que almacena las cuentas de los usuarios con sus contraseñas y saldos.
- **`transacciones.csv`**: Archivo que almacena el historial de transacciones realizadas.

# Nota: Los archivos .csv se crearán por si solos si solo ejecutas el código
## Funcionalidades

### 1. Gestión de Usuarios
- Autenticación de usuarios mediante nombre de usuario y contraseña.
- Sistema de inicialización que crea un archivo `cuentas.csv` con usuarios predeterminados si no existe.

### 2. Operaciones Disponibles
- **Retiro**: Permite retirar dinero del saldo del usuario.
- **Depósito**: Permite agregar dinero al saldo del usuario.
- **Transferencia**: Permite transferir dinero entre cuentas registradas.
- **Historial de transacciones**: Muestra un registro detallado de todas las transacciones realizadas por el usuario.
- **Consulta de saldo**: Muestra el saldo actual del usuario.

# Clona este repositorio:
   ```
   git clone https://github.com/FelipeM197/ProyectoFinalProgramacion
   ```

## Ejemplo de Cuentas Iniciales

El sistema crea automáticamente un archivo `cuentas.csv` con las siguientes cuentas de ejemplo:
```
nombreUsuario,contraseña,saldo
FELIPE,ABC123,1000
URIEL,XYZ789,1500
ZENAN,123,2000
AIDAN,532,2500
JOSUE,423,3000
```
Puedes modificar este archivo para agregar o cambiar las cuentas según tus necesidades.

## Notas Importantes
- El sistema limita los retiros, depósitos y transferencias a un monto máximo de $10,000 por operación.
- Asegúrate de ingresar montos válidos para evitar errores en las transacciones.

---
