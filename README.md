# Historial de transacciones
## Requisitos

### Software necesario
- Python 3.8 o superior

### Librerías requeridas
- `colorama`: Para mejorar la experiencia en la consola con colores.
- `pytz`: Para manejar zonas horarias.

Puedes instalar las dependencias ejecutando:
```
pip install colorama
pip install pytz
```

## Estructura del Proyecto

- **`CodigoFelipe.py`**: Archivo principal que contiene todo el código del sistema.
- **`transacciones.csv`**: Archivo donde se almacenan las transacciones realizadas por los usuarios.
- **`cuentas.csv`**: Archivo donde se almacenan las cuentas de los usuarios y sus saldos.

# Nota: Al ejecutar el código se crearán automáticamente los dos archivos .csv

## Funcionalidades

### 1. Gestión de Cuentas
- **Inicialización de cuentas**: Si no existe el archivo `cuentas.csv`, se crea con cuentas predeterminadas.
- **Carga y guardado**: Las cuentas se leen y actualizan automáticamente desde/para el archivo CSV.

### 2. Operaciones Disponibles
- **Retiro**: Permite retirar dinero del saldo del usuario.
- **Depósito**: Permite agregar dinero al saldo del usuario.
- **Transferencia**: Permite transferir dinero entre cuentas registradas.
- **Historial de transacciones**: Muestra un registro detallado de las transacciones realizadas.
- **Consulta de saldo**: Muestra el saldo actual del usuario.

### 3. Registro de Transacciones
Cada operación se registra automáticamente en el archivo `transacciones.csv`, incluyendo:
- Fecha y hora de la operación.
- Tipo de operación (retiro, depósito, transferencia).
- Monto involucrado.
- Usuario que realizó la operación.
- Saldo resultante.

# Sigue las instrucciones del menú para interactuar con el sistema.

## Ejemplo de Usuario

El sistema incluye usuarios de prueba que puedes modificar directamente en el archivo `cuentas.csv`. Ejemplo:
```
nombreUsuario,saldo
USUARIO1,2500
USUARIO2,1500
```

## Extensiones Futuras
- Implementación de la autenticación de usuarios.

## Notas
- No eliminar los archivos `cuentas.csv` y `transacciones.csv` para mantener la persistencia de datos.
- Asegurarse de ingresar montos válidos para evitar errores durante las transacciones.

---
