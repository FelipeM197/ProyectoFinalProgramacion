from graphviz import Digraph
from IPython.display import display
from PIL import Image

def crear_diagrama_flujo():
    dot = Digraph(format='png')
    dot.attr(size='10')
    
    # Nodos principales
    dot.node('A', 'Inicio', shape='oval', style='filled', fillcolor='lightblue')
    dot.node('B', 'Inicializar sistema\n(Verificar archivos CSV)', shape='parallelogram', style='filled', fillcolor='lightyellow')
    dot.node('C', 'Menú Principal', shape='box', style='filled', fillcolor='lightgrey')
    dot.node('D', 'Autenticación\n(Ingresar usuario y contraseña)', shape='parallelogram', style='filled', fillcolor='lightyellow')
    dot.node('E', 'Autenticación válida?', shape='diamond', style='filled', fillcolor='lightpink')
    dot.node('F', 'Acceso Denegado\nRegresar al Menú', shape='box', style='filled', fillcolor='lightcoral')
    dot.node('G', 'Menú de Usuario', shape='box', style='filled', fillcolor='lightgreen')
    dot.node('H', 'Retirar Dinero', shape='parallelogram', style='filled', fillcolor='lightyellow')
    dot.node('I', 'Depositar Dinero', shape='parallelogram', style='filled', fillcolor='lightyellow')
    dot.node('J', 'Transferir Dinero', shape='parallelogram', style='filled', fillcolor='lightyellow')
    dot.node('K', 'Historial de Transacciones', shape='parallelogram', style='filled', fillcolor='lightyellow')
    dot.node('L', 'Consultar Saldo', shape='parallelogram', style='filled', fillcolor='lightyellow')
    dot.node('M', 'Cerrar Sesión', shape='box', style='filled', fillcolor='lightgrey')
    dot.node('N', 'Confirmar Salida?', shape='diamond', style='filled', fillcolor='lightpink')
    dot.node('O', 'Salir del Sistema', shape='oval', style='filled', fillcolor='red')
    dot.node('P', 'Verificar Fondos', shape='diamond', style='filled', fillcolor='lightpink')
    dot.node('Q', 'Fondos Suficientes?', shape='diamond', style='filled', fillcolor='lightpink')
    dot.node('R', 'Transacción Exitosa', shape='box', style='filled', fillcolor='lightgreen')
    dot.node('S', 'Transacción Fallida', shape='box', style='filled', fillcolor='lightcoral')
    dot.node('T', 'Actualizar Saldo', shape='parallelogram', style='filled', fillcolor='lightyellow')
    dot.node('U', 'Generar Recibo', shape='parallelogram', style='filled', fillcolor='lightyellow')
    
    # Conexiones
    dot.edge('A', 'B')
    dot.edge('B', 'C')
    dot.edge('C', 'D')
    dot.edge('D', 'E')
    dot.edge('E', 'F', label='No', color='red')
    dot.edge('E', 'G', label='Sí', color='green')
    dot.edge('G', 'H')
    dot.edge('G', 'I')
    dot.edge('G', 'J')
    dot.edge('G', 'K')
    dot.edge('G', 'L')
    dot.edge('G', 'M')
    dot.edge('H', 'P')
    dot.edge('P', 'Q')
    dot.edge('Q', 'S', label='No', color='red')
    dot.edge('Q', 'T', label='Sí', color='green')
    dot.edge('T', 'R')
    dot.edge('R', 'U')
    dot.edge('U', 'G')
    dot.edge('M', 'N')
    dot.edge('N', 'C', label='No', color='red')
    dot.edge('N', 'O', label='Sí', color='green')
    
    # Guardar y renderizar el diagrama
    dot.render('diagrama_flujo_atm_completo')
    print("Diagrama de flujo generado como 'diagrama_flujo_atm_completo.png'")

# Crear el diagrama de flujo
crear_diagrama_flujo()

# Mostrar la imagen generada
img = Image.open("diagrama_flujo_atm_completo.png") 
display(img)