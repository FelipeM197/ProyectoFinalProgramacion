# Sistema de Gestión de Cuentas con Autenticación

## Requisitos

### Software necesario
- Python 3.8 o superior

### Librerías requeridas
- **colorama**: Para mejorar la experiencia en la consola con colores.


## Estructura del Proyecto

- **codigoJosue.py**: Archivo principal que contiene todo el código del sistema.
- **cuentas.csv**: Archivo donde se almacenan las cuentas de los usuarios y sus saldos.

**Nota**: Al ejecutar el código, se creará automáticamente el archivo `cuentas.csv` si no existe.

## Funcionalidades

### 1. Gestión de Cuentas
- **Inicialización de cuentas**: Si no existe el archivo `cuentas.csv`, el sistema lo crea con cuentas predeterminadas.
- **Carga y guardado**: Las cuentas se leen y actualizan automáticamente desde/para el archivo CSV.

### 2. Operaciones Disponibles
- **Autenticación de usuarios**: Permite a los usuarios iniciar sesión con su nombre de usuario y contraseña.
- **Salir del sistema**: Los usuarios pueden salir del sistema tras confirmar su decisión.

## Detalles Técnicos

- Los datos de las cuentas incluyen:
  - Nombre de usuario
  - Contraseña
  - Saldo

El archivo `cuentas.csv` se inicializa con los siguientes usuarios de prueba:

```plaintext
nombreUsuario,contrasena,saldo
FELIPE,ABC123,1000
URIEL,XYZ789,1500
ZENAN,123,2000
AIDAN,532,2500
JOSUE,423,3000
```

## Extensiones Futuras

Se sugiere implementar las siguientes mejoras:
- **Historial de transacciones**: Registrar todas las operaciones realizadas, incluyendo fecha, hora y tipo de operación.
- **Operaciones adicionales**:
  - Consulta de saldo.
  - Depósitos y retiros.
  - Transferencias entre cuentas.
- **Cifrado de contraseñas**: Asegurar las contraseñas almacenadas en el archivo `cuentas.csv`.
- **Validación avanzada**: Asegurarse de que los datos ingresados por el usuario sean válidos para prevenir errores.

## Notas
- No elimines el archivo `cuentas.csv` para mantener la persistencia de datos.
- Asegúrate de ingresar información válida, especialmente durante la autenticación, para evitar bloqueos.
