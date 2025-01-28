## Requisitos

### Software necesario
- Python 3.8 o superior.

### Librerías requeridas
- *colorama*: Para mejorar la experiencia en la consola con colores.

Puedes instalar las dependencias ejecutando:

bash
pip install colorama


---

## Estructura del Proyecto

- *CodigoZenan.py*: Archivo principal que contiene el código del sistema.
- *cuentas.csv*: Archivo donde se almacenan las cuentas de los usuarios y sus saldos. Se crea automáticamente al ejecutar el programa por primera vez si no existe.

---

## Funcionalidades

### 1. Gestión de Cuentas
- *Inicialización de cuentas*: Si no existe el archivo cuentas.csv, se genera con datos de prueba.
- *Carga y guardado*: Las cuentas se leen y actualizan automáticamente desde/para el archivo CSV.

### 2. Operaciones Disponibles
- *Transferencias*: Permite transferir dinero entre cuentas registradas.

---

## Registro de Datos

El archivo cuentas.csv contiene la información de las cuentas de usuarios en formato CSV, incluyendo:
- *nombreUsuario*: Nombre del usuario.
- *saldo*: Saldo disponible del usuario.

### Ejemplo de Usuario:
csv
nombreUsuario,saldo
USUARIO1,2500
USUARIO2,1500


---

## Ejecución del Programa

1. Al ejecutar el programa, se cargará la cuenta de USUARIO1 como usuario predeterminado.
2. Se mostrará un menú con opciones para realizar transferencias o salir del sistema.

---

## Notas

- No eliminar el archivo cuentas.csv para mantener la persistencia de datos.
- Ingresar valores válidos para evitar errores en las operaciones.

---

## Extensiones Futuras
- Implementación de autenticación de usuarios.
- Registro de transacciones detallado.