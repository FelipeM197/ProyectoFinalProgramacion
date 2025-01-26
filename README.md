# Sistema de Cajero Automático en Python

## Descripción
Este programa es una simulación básica de un **cajero automático**, desarrollado en Python. Permite a un usuario realizar operaciones comunes como **retirar** y **depositar dinero**, además de mantener un registro del saldo en un archivo **CSV**. Está diseñado como una aplicación sencilla para proyectos educativos o como punto de partida para sistemas más complejos.

## Funcionalidades
- **Inicialización del sistema**: Crea un archivo CSV para almacenar las cuentas de usuario con un saldo inicial si este no existe.
- **Cargar cuenta**: Lee los datos del archivo CSV y recupera la información del usuario y su saldo.
- **Guardar cuenta**: Actualiza el archivo CSV con los cambios realizados en el saldo del usuario.
- **Retirar dinero**: Permite al usuario retirar una cantidad específica de su saldo, validando que sea suficiente.
- **Depositar dinero**: Permite al usuario depositar dinero en su cuenta.

## Estructura del Código
- **inicializarSistema()**: Comprueba si el archivo `cuentas.csv` existe. Si no, lo crea con datos iniciales.
- **cargarCuenta()**: Carga los datos del usuario desde el archivo CSV.
- **guardarCuenta(usuario)**: Guarda los cambios en la cuenta del usuario en el archivo CSV.
- **retirarDinero(usuario)**: Realiza la operación de retiro, actualizando el saldo en caso de éxito.
- **depositarDinero(usuario)**: Realiza la operación de depósito, actualizando el saldo del usuario.
- **Simulación principal**: Proporciona un menú interactivo para que el usuario seleccione una acción.

## Requisitos
- Python 3.6 o superior.
- Módulo `csv` (incluido en la biblioteca estándar de Python).
- Archivo `cuentas.csv` (se genera automáticamente si no existe).
## Uso
1. **Ejecutar el programa**: Ejecuta el archivo Python directamente.
    ```bash
    python CodigoAidan.py
    ```
2. **Interactuar con el menú**:
    - Opción 1: **Retirar dinero**.
    - Opción 2: **Depositar dinero**.
    - Opción 3: **Salir del sistema**.

>[!NOTE]
> El programa utiliza un usuario predeterminado llamado **USUARIO** con un saldo inicial de **2500**.
> Las operaciones se registran y persisten en el archivo `cuentas.csv`.

## Futuras Mejoras
- Agregar soporte para **múltiples usuarios**.
- Mejorar la **interfaz** con un sistema gráfico o web.
- Implementar medidas de **seguridad** como autenticación de usuario.
- Agregar **validaciones** más robustas para las entradas.
