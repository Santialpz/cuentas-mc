import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime

# Estructura de datos para almacenar tareas y usuarios
tareas = []
usuarios = {
    "admin": {"nivel": "administrador", "contraseña": "admin123"},
    "trabajador1": {"nivel": "trabajador", "contraseña": "trab123"},
}

# Función para registrar una tarea
def registrar_tarea(usuario, nombre_tarea, hora_tarea):
    tareas.append({
        "usuario": usuario,
        "tarea": nombre_tarea,
        "hora": hora_tarea,
    })
    messagebox.showinfo("Éxito", f"Tarea '{nombre_tarea}' registrada por {usuario} a las {hora_tarea}")

# Función para imprimir un reporte de tareas
def imprimir_reporte():
    reporte = "Reporte de Tareas:\n"
    for tarea in tareas:
        reporte += f"- Usuario: {tarea['usuario']}, Tarea: {tarea['tarea']}, Hora: {tarea['hora']}\n"
    messagebox.showinfo("Reporte de Tareas", reporte)

# Función para la interfaz del administrador
def interfaz_administrador():
    def crear_tarea():
        nombre_tarea = simpledialog.askstring("Crear Tarea", "Ingrese el nombre de la tarea:")
        if nombre_tarea:
            registrar_tarea("admin", nombre_tarea, datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    ventana_admin = tk.Toplevel()
    ventana_admin.title("Panel de Administrador")
    ventana_admin.geometry("300x200")

    tk.Button(ventana_admin, text="Crear Tarea", command=crear_tarea).pack(pady=10)
    tk.Button(ventana_admin, text="Imprimir Reporte", command=imprimir_reporte).pack(pady=10)

# Función para la interfaz del trabajador
def interfaz_trabajador(usuario):
    def registrar_tarea_trabajador():
        nombre_tarea = simpledialog.askstring("Registrar Tarea", "Ingrese el nombre de la tarea:")
        if nombre_tarea:
            hora_tarea = simpledialog.askstring("Registrar Hora", "Ingrese la hora de la tarea (Formato: YYYY-MM-DD HH:MM:SS):")
            if hora_tarea:
                registrar_tarea(usuario, nombre_tarea, hora_tarea)

    ventana_trabajador = tk.Toplevel()
    ventana_trabajador.title(f"Panel de Trabajador - {usuario}")
    ventana_trabajador.geometry("300x200")

    tk.Button(ventana_trabajador, text="Registrar Tarea", command=registrar_tarea_trabajador).pack(pady=10)

# Función de inicio de sesión
def iniciar_sesion():
    usuario = simpledialog.askstring("Inicio de Sesión", "Ingrese su usuario:")
    contraseña = simpledialog.askstring("Inicio de Sesión", "Ingrese su contraseña:", show="*")

    if usuario in usuarios and usuarios[usuario]["contraseña"] == contraseña:
        nivel = usuarios[usuario]["nivel"]
        if nivel == "administrador":
            interfaz_administrador()
        elif nivel == "trabajador":
            interfaz_trabajador(usuario)
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# Interfaz principal
ventana_principal = tk.Tk()
ventana_principal.title("Gestión de Tareas")
ventana_principal.geometry("300x200")

tk.Label(ventana_principal, text="Bienvenido al Sistema de Gestión de Tareas", font=("Arial", 12)).pack(pady=20)
tk.Button(ventana_principal, text="Iniciar Sesión", command=iniciar_sesion).pack(pady=10)

ventana_principal.mainloop()