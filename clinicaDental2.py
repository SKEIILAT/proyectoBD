import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime
import pymysql
from datetime import time
# Conexión a la base de datos
# cambio
def conectar_bd():
    return pymysql.connect(
        host='localhost',
        user='root',
        password="javier",
        database='ClinicaDentalDB'
    )
def mostrar_datos(tabla):
    # Crear una ventana nueva para mostrar los datos de la tabla
    top = tk.Toplevel(root)
    top.title(tabla)

    conn = conectar_bd()
    cur = conn.cursor()
    cur.execute(f"DESCRIBE {tabla}")
    columnas = [col[0] for col in cur.fetchall()]

    cur.execute(f"SELECT * FROM {tabla}")
    datos = cur.fetchall()

    for col_num, columna in enumerate(columnas):
        tk.Label(top, text=columna, font=("sans-serif", 12, "bold")).grid(row=0, column=col_num, padx=10, pady=5)

    for row_num, fila in enumerate(datos, start=1):
        for col_num, valor in enumerate(fila):
            tk.Label(top, text=valor).grid(row=row_num, column=col_num, padx=10, pady=5)

    conn.close()

    if tabla == "Paciente":
        tk.Button(top, text="Opciones Pacientes", font=("sans-serif", 15, "bold"),
                  command=mostrar_opciones_pacientes).grid(row=len(datos) + 1, columnspan=len(columnas), pady=20)
    elif tabla == "Dentista":
        tk.Button(top, text="Opciones Dentistas", font=("sans-serif", 15, "bold"),
                  command=mostrar_opciones_dentistas).grid(row=len(datos) + 1, columnspan=len(columnas), pady=20)
    elif tabla == "Asistente":
        tk.Button(top, text="Opciones Asistentes", font=("sans-serif", 15, "bold"),
                  command=mostrar_opciones_asistentes).grid(row=len(datos) + 1, columnspan=len(columnas), pady=20)
    elif tabla == "Cita":
        tk.Button(top, text="Opciones Citas", font=("sans-serif", 15, "bold"), command=mostrar_opciones_citas).grid(
            row=len(datos) + 1, columnspan=len(columnas), pady=20)
    elif tabla == "Tratamiento":
        tk.Button(top, text="Opciones Tratamientos", font=("sans-serif", 15, "bold"),
                  command=mostrar_opciones_tratamientos).grid(row=len(datos) + 1, columnspan=len(columnas), pady=20)
    elif tabla == "Historia_Clinica":
        tk.Button(top, text="Opciones Historias Clínicas", font=("sans-serif", 15, "bold"),
                  command=mostrar_opciones_historias_clinicas).grid(row=len(datos) + 1, columnspan=len(columnas),
                                                                    pady=20)


def mostrar_opciones_pacientes():
    top = tk.Toplevel(root)
    top.title("Opciones Pacientes")
    tk.Label(top, text="Seleccione una opción:", font=("sans-serif", 14, "bold")).pack(pady=10)

    opciones = {
        "Agregar Paciente": agregar_paciente,
        "Consultar Paciente": consultar_paciente,
        "Actualizar Paciente": actualizar_paciente,
        "Eliminar Paciente": eliminar_paciente,
    }

    for texto, funcion in opciones.items():
        tk.Button(top, text=texto, font=("sans-serif", 12, "bold"), command=funcion).pack(pady=5)

def mostrar_opciones_dentistas():
    top = tk.Toplevel(root)
    top.title("Opciones Dentistas")
    tk.Label(top, text="Seleccione una opción:", font=("sans-serif", 14, "bold")).pack(pady=10)

    opciones = {
        "Agregar Dentista": agregar_dentista,
        "Consultar Dentista": consultar_dentista,
        "Actualizar Dentista": actualizar_dentista,
        "Eliminar Dentista": eliminar_dentista,
    }

    for texto, funcion in opciones.items():
        tk.Button(top, text=texto, font=("sans-serif", 12, "bold"), command=funcion).pack(pady=5)

def mostrar_opciones_asistentes():
    top = tk.Toplevel(root)
    top.title("Opciones Asistentes")
    tk.Label(top, text="Seleccione una opción:", font=("sans-serif", 14, "bold")).pack(pady=10)

    opciones = {
        "Agregar Asistente": agregar_asistente,
        "Consultar Asistente": consultar_asistente,
        "Actualizar Asistente": actualizar_asistente,
        "Eliminar Asistente": eliminar_asistente,
    }

    for texto, funcion in opciones.items():
        tk.Button(top, text=texto, font=("sans-serif", 12, "bold"), command=funcion).pack(pady=5)

def mostrar_opciones_consultas():
    top = tk.Toplevel(root)
    top.title("Opciones Consultas")
    tk.Label(top, text="Seleccione una consulta:", font=("sans-serif", 14, "bold")).pack(pady=10)

    consultas = {
        "Pacientes con Mayor Número de Citas y Tratamientos Activos": lambda: ejecutar_consulta(1),
        "Ingresos Totales por Paciente, Dentista, y Tratamiento": lambda: ejecutar_consulta(2),
        "Tratamientos Más Populares y Su Duración Promedio": lambda: ejecutar_consulta(3),
        "Dentistas con Mayor Número de Citas y Asistentes Asociados": lambda: ejecutar_consulta(4),
    }

    for texto, funcion in consultas.items():
        tk.Button(top, text=texto, font=("sans-serif", 12, "bold"), command=funcion).pack(pady=5)


def mostrar_opciones_citas():
    top = tk.Toplevel(root)
    top.title("Opciones Citas")
    tk.Label(top, text="Seleccione una opción:", font=("sans-serif", 14, "bold")).pack(pady=10)

    opciones = {
        "Agregar Cita": agregar_cita,
        "Consultar Cita": consultar_cita,
        "Actualizar Cita": actualizar_cita,
        "Eliminar Cita": eliminar_cita,
    }

    for texto, funcion in opciones.items():
        tk.Button(top, text=texto, font=("sans-serif", 12, "bold"), command=funcion).pack(pady=5)

def mostrar_opciones_tratamientos():
    top = tk.Toplevel(root)
    top.title("Opciones Tratamientos")
    tk.Label(top, text="Seleccione una opción:", font=("sans-serif", 14, "bold")).pack(pady=10)

    opciones = {
        "Agregar Tratamiento": agregar_tratamiento,
        "Consultar Tratamiento": consultar_tratamiento,
        "Actualizar Tratamiento": actualizar_tratamiento,
        "Eliminar Tratamiento": eliminar_tratamiento,
    }

    for texto, funcion in opciones.items():
        tk.Button(top, text=texto, font=("sans-serif", 12, "bold"), command=funcion).pack(pady=5)

def mostrar_opciones_historias_clinicas():
    top = tk.Toplevel(root)
    top.title("Opciones Historias Clínicas")
    tk.Label(top, text="Seleccione una opción:", font=("sans-serif", 14, "bold")).pack(pady=10)

    opciones = {
        "Agregar Historia Clínica": agregar_historia_clinica,
        "Consultar Historia Clínica": consultar_historia_clinica,
        "Actualizar Historia Clínica": actualizar_historia_clinica,
        "Eliminar Historia Clínica": eliminar_historia_clinica,
    }

    for texto, funcion in opciones.items():
        tk.Button(top, text=texto, font=("sans-serif", 12, "bold"), command=funcion).pack(pady=5)

def mostrar_opciones_consultas():
    top = tk.Toplevel(root)
    top.title("Opciones Consultas")
    tk.Label(top, text="Seleccione una consulta:", font=("sans-serif", 14, "bold")).pack(pady=10)

    consultas = {
        "Pacientes con Mayor Número de Citas y Tratamientos Activos": lambda: ejecutar_consulta(1),
        "Ingresos Totales por Paciente, Dentista, y Tratamiento": lambda: ejecutar_consulta(2),
        "Tratamientos Más Populares y Su Duración Promedio": lambda: ejecutar_consulta(3),
        "Dentistas con Mayor Número de Citas y Asistentes Asociados": lambda: ejecutar_consulta(4),
    }

    for texto, funcion in consultas.items():
        tk.Button(top, text=texto, font=("sans-serif", 12, "bold"), command=funcion).pack(pady=5)


def agregar_paciente():
    def guardar():
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        telefono = entry_telefono.get()
        email = entry_email.get()
        fecha_nac = entry_fecha_nac.get()
        direccion = entry_direccion.get()
        if not all([nombre, apellido, telefono, email]):
            messagebox.showerror("Error", "Todos los campos deben estar llenos.")
            return
        try:
            if int(telefono) < 0 :
                messagebox.showerror("Error", "Los valores numéricos no pueden ser negativos.")
                return
        except ValueError:
            messagebox.showerror("Error", "ID Dentista y Teléfono deben ser números válidos.")
            return
        try:
            datetime.strptime(fecha_nac, "%Y-%m-%d")  # Formato: Año-Mes-Día
        except ValueError:
            messagebox.showerror("Error", "La fecha de nacimiento debe tener el formato AAAA-MM-DD.")
            return
        conn = conectar_bd()
        cur = conn.cursor()
        consulta = "INSERT INTO Paciente (nombre, apellido, telefono, email, fecha_nacimiento, direccion) VALUES (%s, %s, %s, %s, %s, %s);"
        cur.execute(consulta, (nombre, apellido, telefono, email, fecha_nac, direccion))
        conn.commit()
        conn.close()
        messagebox.showinfo("Éxito", "Paciente agregado con éxito")
        top.destroy()

    top = tk.Toplevel(root)
    top.title("Agregar Paciente")

    tk.Label(top, text="Nombre:").pack(pady=5)
    entry_nombre = tk.Entry(top)
    entry_nombre.pack(pady=5)

    tk.Label(top, text="Apellido:").pack(pady=5)
    entry_apellido = tk.Entry(top)
    entry_apellido.pack(pady=5)

    tk.Label(top, text="Teléfono:").pack(pady=5)
    entry_telefono = tk.Entry(top)
    entry_telefono.pack(pady=5)

    tk.Label(top, text="Email:").pack(pady=5)
    entry_email = tk.Entry(top)
    entry_email.pack(pady=5)

    tk.Label(top, text="Fecha de Nacimiento (año-mes-día):").pack(pady=5)
    entry_fecha_nac = tk.Entry(top)
    entry_fecha_nac.pack(pady=5)

    tk.Label(top, text="Dirección:").pack(pady=5)
    entry_direccion = tk.Entry(top)
    entry_direccion.pack(pady=5)

    tk.Button(top, text="Guardar", command=guardar).pack(pady=10)

def consultar_paciente():
    def buscar():
        id_paciente = entry_id.get()
        if not id_paciente:
            messagebox.showerror("Error", "El campo ID Paciente debe estar lleno.")
            return

            # Validación de ID negativo
        try:
            id_paciente = int(id_paciente)
            if id_paciente < 0:
                messagebox.showerror("Error", "El ID Paciente no puede ser negativo.")
                return
        except ValueError:
            messagebox.showerror("Error", "El ID Paciente debe ser un número válido.")
            return
        conn = conectar_bd()
        cur = conn.cursor()
        consulta = "SELECT id_paciente, nombre, apellido, telefono, email, fecha_nacimiento, direccion FROM Paciente WHERE id_paciente = %s;"
        cur.execute(consulta, (id_paciente,))
        datos = cur.fetchall()
        conn.close()

        top_resultado = tk.Toplevel(root)
        top_resultado.title("Resultado Consulta")
        if datos:
            for col_num, columna in enumerate(["id_paciente", "nombre", "apellido", "telefono", "email", "fecha_nacimiento", "direccion"]):
                tk.Label(top_resultado, text=columna, font=("sans-serif", 12, "bold")).grid(row=0, column=col_num, padx=10, pady=5)
            for row_num, fila in enumerate(datos, start=1):
                for col_num, valor in enumerate(fila):
                    tk.Label(top_resultado, text=valor).grid(row=row_num, column=col_num, padx=10, pady=5)
        else:
            tk.Label(top_resultado, text="No se encontró el paciente.", font=("sans-serif", 12, "bold")).pack(pady=20)

    top = tk.Toplevel(root)
    top.title("Consultar Paciente")

    tk.Label(top, text="ID Paciente:").pack(pady=5)
    entry_id = tk.Entry(top)
    entry_id.pack(pady=5)

    tk.Button(top, text="Buscar", command=buscar).pack(pady=10)

def actualizar_paciente():
    def actualizar():
        id_paciente = entry_id.get()
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        telefono = entry_telefono.get()
        email = entry_email.get()
        fecha_nac = entry_fecha_nac.get()
        direccion = entry_direccion.get()
        # Validación de campos vacíos
        if not all([nombre, apellido, telefono, email, fecha_nac, direccion]):
            messagebox.showerror("Error", "Todos los campos deben estar llenos.")
            return

        # Validación de teléfono
        try:
            if int(telefono) < 0:
                messagebox.showerror("Error", "Los valores numéricos no pueden ser negativos.")
                return
        except ValueError:
            messagebox.showerror("Error", "El teléfono debe ser un número válido.")
            return

        # Validación de la fecha de nacimiento
        try:
            fecha_nac_obj = datetime.strptime(fecha_nac, "%Y-%m-%d")  # Formato: Año-Mes-Día
        except ValueError:
            messagebox.showerror("Error", "La fecha de nacimiento debe tener el formato AAAA-MM-DD.")
            return

        # Validación de la dirección
        if not direccion.strip():  # Verifica que la dirección no esté vacía o solo con espacios
            messagebox.showerror("Error", "La dirección no puede estar vacía.")
            return

        conn = conectar_bd()
        cur = conn.cursor()
        consulta = "UPDATE Paciente SET nombre = %s, apellido = %s, telefono = %s, email = %s, fecha_nacimiento = %s, direccion = %s WHERE id_paciente = %s;"
        cur.execute(consulta, (nombre, apellido, telefono, email, fecha_nac, direccion, id_paciente))
        conn.commit()
        conn.close()
        messagebox.showinfo("Éxito", "Paciente actualizado con éxito")
        top.destroy()

    top = tk.Toplevel(root)
    top.title("Actualizar Paciente")

    tk.Label(top, text="ID Paciente:").pack(pady=5)
    entry_id = tk.Entry(top)
    entry_id.pack(pady=5)

    tk.Label(top, text="Nombre:").pack(pady=5)
    entry_nombre = tk.Entry(top)
    entry_nombre.pack(pady=5)

    tk.Label(top, text="Apellido:").pack(pady=5)
    entry_apellido = tk.Entry(top)
    entry_apellido.pack(pady=5)

    tk.Label(top, text="Teléfono:").pack(pady=5)
    entry_telefono = tk.Entry(top)
    entry_telefono.pack(pady=5)

    tk.Label(top, text="Email:").pack(pady=5)
    entry_email = tk.Entry(top)
    entry_email.pack(pady=5)

    tk.Label(top, text="Fecha de Nacimiento (año-mes-día):").pack(pady=5)
    entry_fecha_nac = tk.Entry(top)
    entry_fecha_nac.pack(pady=5)

    tk.Label(top, text="Dirección:").pack(pady=5)
    entry_direccion = tk.Entry(top)
    entry_direccion.pack(pady=5)

    tk.Button(top, text="Actualizar", command=actualizar).pack(pady=10)

def eliminar_paciente():
    def eliminar():
        id_paciente = entry_id.get()
        if not id_paciente:
            messagebox.showerror("Error", "El campo ID Paciente debe estar lleno.")
            return

            # Validación de ID negativo
        try:
            id_paciente = int(id_paciente)
            if id_paciente < 0:
                messagebox.showerror("Error", "El ID Paciente no puede ser negativo.")
                return
        except ValueError:
            messagebox.showerror("Error", "El ID Paciente debe ser un número válido.")
            return
        conn = conectar_bd()
        cur = conn.cursor()
        consulta = "DELETE FROM Paciente WHERE id_paciente = %s;"
        cur.execute(consulta, (id_paciente,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Éxito", "Paciente eliminado con éxito")
        top.destroy()

    top = tk.Toplevel(root)
    top.title("Eliminar Paciente")

    tk.Label(top, text="ID Paciente:").pack(pady=5)
    entry_id = tk.Entry(top)
    entry_id.pack(pady=5)

    tk.Button(top, text="Eliminar", command=eliminar).pack(pady=10)

# Funciones para Dentistas
def agregar_dentista():
    def guardar():
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        telefono = entry_telefono.get()
        email = entry_email.get()
        especialidad = entry_especialidad.get()
        disponibilidad_inicio = entry_disponibilidad_inicio.get()
        disponibilidad_fin = entry_disponibilidad_fin.get()
        # Validación de campos vacíos
        if not all([nombre, apellido, telefono, email, especialidad, disponibilidad_inicio, disponibilidad_fin]):
            messagebox.showerror("Error", "Todos los campos deben estar llenos.")
            return

        # Validación de teléfono
        try:
            if int(telefono) < 0:
                messagebox.showerror("Error", "El número de teléfono no puede ser negativo.")
                return
        except ValueError:
            messagebox.showerror("Error", "El teléfono debe ser un número válido.")
            return

        # Validación de formato de email
        if "@" not in email or "." not in email.split('@')[-1]:
            messagebox.showerror("Error", "El email no es válido.")
            return

        # Validación de disponibilidad de tiempo
        try:
            disponibilidad_inicio_obj = time.fromisoformat(disponibilidad_inicio)
            disponibilidad_fin_obj = time.fromisoformat(disponibilidad_fin)
            if disponibilidad_inicio_obj >= disponibilidad_fin_obj:
                messagebox.showerror("Error", "La hora de inicio debe ser antes de la hora de fin.")
                return
        except ValueError:
            messagebox.showerror("Error", "Las horas de disponibilidad deben estar en el formato HH:MM:SS.")
            return

        conn = conectar_bd()
        cur = conn.cursor()
        consulta = """
        INSERT INTO Dentista (nombre, apellido, telefono, email, especialidad, disponibilidad_inicio, disponibilidad_fin)
        VALUES (%s, %s, %s, %s, %s, %s, %s);
        """
        cur.execute(consulta, (nombre, apellido, telefono, email, especialidad, disponibilidad_inicio, disponibilidad_fin))
        conn.commit()
        conn.close()
        messagebox.showinfo("Éxito", "Dentista agregado con éxito")
        top.destroy()

    top = tk.Toplevel(root)
    top.title("Agregar Dentista")

    tk.Label(top, text="Nombre:").pack(pady=5)
    entry_nombre = tk.Entry(top)
    entry_nombre.pack(pady=5)

    tk.Label(top, text="Apellido:").pack(pady=5)
    entry_apellido = tk.Entry(top)
    entry_apellido.pack(pady=5)

    tk.Label(top, text="Teléfono:").pack(pady=5)
    entry_telefono = tk.Entry(top)
    entry_telefono.pack(pady=5)

    tk.Label(top, text="Email:").pack(pady=5)
    entry_email = tk.Entry(top)
    entry_email.pack(pady=5)

    tk.Label(top, text="Especialidad:").pack(pady=5)
    entry_especialidad = tk.Entry(top)
    entry_especialidad.pack(pady=5)

    tk.Label(top, text="Disponibilidad Inicio (HH:MM:SS):").pack(pady=5)
    entry_disponibilidad_inicio = tk.Entry(top)
    entry_disponibilidad_inicio.pack(pady=5)

    tk.Label(top, text="Disponibilidad Fin (HH:MM:SS):").pack(pady=5)
    entry_disponibilidad_fin = tk.Entry(top)
    entry_disponibilidad_fin.pack(pady=5)

    tk.Button(top, text="Guardar", command=guardar).pack(pady=10)

def consultar_dentista():
    def buscar():
        id_dentista = entry_id.get()
        if not id_dentista:
            messagebox.showerror("Error", "El campo ID Dentista debe estar lleno.")
            return

            # Validación de ID negativo
        try:
            id_paciente = int(id_dentista)
            if id_paciente < 0:
                messagebox.showerror("Error", "El ID Dentista no puede ser negativo.")
                return
        except ValueError:
            messagebox.showerror("Error", "El ID Dentista debe ser un número válido.")
            return
        conn = conectar_bd()
        cur = conn.cursor()
        consulta = "SELECT id_dentista, nombre, especialidad, telefono, email FROM Dentista WHERE id_dentista = %s;"
        cur.execute(consulta, (id_dentista,))
        datos = cur.fetchall()
        conn.close()

        top_resultado = tk.Toplevel(root)
        top_resultado.title("Resultado Consulta")
        if datos:
            for col_num, columna in enumerate(["id_dentista", "nombre", "especialidad", "telefono", "email"]):
                tk.Label(top_resultado, text=columna, font=("sans-serif", 12, "bold")).grid(row=0, column=col_num, padx=10, pady=5)
            for row_num, fila in enumerate(datos, start=1):
                for col_num, valor in enumerate(fila):
                    tk.Label(top_resultado, text=valor).grid(row=row_num, column=col_num, padx=10, pady=5)
        else:
            tk.Label(top_resultado, text="No se encontró el dentista.", font=("sans-serif", 12, "bold")).pack(pady=20)

    top = tk.Toplevel(root)
    top.title("Consultar Dentista")

    tk.Label(top, text="ID Dentista:").pack(pady=5)
    entry_id = tk.Entry(top)
    entry_id.pack(pady=5)

    tk.Button(top, text="Buscar", command=buscar).pack(pady=10)

def actualizar_dentista():
    def actualizar():
        id_dentista = entry_id.get()
        nombre = entry_nombre.get()
        especialidad = entry_especialidad.get()
        telefono = entry_telefono.get()
        email = entry_email.get()

        # Validación de campos vacíos
        if not all([id_dentista, nombre, especialidad, telefono, email]):
            messagebox.showerror("Error", "Todos los campos deben estar llenos.")
            return

        # Validación de ID Dentista
        try:
            if int(id_dentista) < 0:
                messagebox.showerror("Error", "El ID del dentista no puede ser negativo.")
                return
        except ValueError:
            messagebox.showerror("Error", "El ID del dentista debe ser un número válido.")
            return

        # Validación de teléfono
        try:
            if int(telefono) < 0:
                messagebox.showerror("Error", "El número de teléfono no puede ser negativo.")
                return
        except ValueError:
            messagebox.showerror("Error", "El teléfono debe ser un número válido.")
            return

        # Validación de formato de email
        if "@" not in email or "." not in email.split('@')[-1]:
            messagebox.showerror("Error", "El email no es válido.")
            return

        conn = conectar_bd()
        cur = conn.cursor()
        consulta = "UPDATE Dentista SET nombre = %s, especialidad = %s, telefono = %s, email = %s WHERE id_dentista = %s;"
        cur.execute(consulta, (nombre, especialidad, telefono, email, id_dentista))
        conn.commit()
        conn.close()
        messagebox.showinfo("Éxito", "Dentista actualizado con éxito")
        top.destroy()

    top = tk.Toplevel(root)
    top.title("Actualizar Dentista")

    tk.Label(top, text="ID Dentista:").pack(pady=5)
    entry_id = tk.Entry(top)
    entry_id.pack(pady=5)

    tk.Label(top, text="Nombre:").pack(pady=5)
    entry_nombre = tk.Entry(top)
    entry_nombre.pack(pady=5)

    tk.Label(top, text="Especialidad:").pack(pady=5)
    entry_especialidad = tk.Entry(top)
    entry_especialidad.pack(pady=5)

    tk.Label(top, text="Teléfono:").pack(pady=5)
    entry_telefono = tk.Entry(top)
    entry_telefono.pack(pady=5)

    tk.Label(top, text="Email:").pack(pady=5)
    entry_email = tk.Entry(top)
    entry_email.pack(pady=5)

    tk.Button(top, text="Actualizar", command=actualizar).pack(pady=10)

def eliminar_dentista():
    def eliminar():
        id_dentista = entry_id.get()
        if not id_dentista:
            messagebox.showerror("Error", "El campo ID Dentista debe estar lleno.")
            return

            # Validación de ID negativo
        try:
            id_paciente = int(id_dentista)
            if id_paciente < 0:
                messagebox.showerror("Error", "El ID Dentista no puede ser negativo.")
                return
        except ValueError:
            messagebox.showerror("Error", "El ID Dentista debe ser un número válido.")
            return

        conn = conectar_bd()
        cur = conn.cursor()
        consulta = "DELETE FROM Dentista WHERE id_dentista = %s;"
        cur.execute(consulta, (id_dentista,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Éxito", "Dentista eliminado con éxito")
        top.destroy()

    top = tk.Toplevel(root)
    top.title("Eliminar Dentista")

    tk.Label(top, text="ID Dentista:").pack(pady=5)
    entry_id = tk.Entry(top)
    entry_id.pack(pady=5)

    tk.Button(top, text="Eliminar", command=eliminar).pack(pady=10)

def agregar_asistente():
    def guardar():
        id_dentista = entry_id_dentista.get()
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        telefono = entry_telefono.get()
        email = entry_email.get()
        if not all([id_dentista, nombre, apellido, telefono, email]):
            messagebox.showerror("Error", "Todos los campos deben estar llenos.")
            return

            # Validación de ID Dentista
        try:
            if int(id_dentista) < 0:
                messagebox.showerror("Error", "El ID del dentista no puede ser negativo.")
                return
        except ValueError:
            messagebox.showerror("Error", "El ID del dentista debe ser un número válido.")
            return

            # Validación de teléfono
        try:
            if int(telefono) < 0:
                messagebox.showerror("Error", "El número de teléfono no puede ser negativo.")
                return
        except ValueError:
            messagebox.showerror("Error", "El teléfono debe ser un número válido.")
            return

            # Validación de formato de email
        if "@" not in email or "." not in email.split('@')[-1]:
            messagebox.showerror("Error", "El email no es válido.")
            return

        conn = conectar_bd()
        cur = conn.cursor()
        consulta = """
        INSERT INTO Asistente (id_dentista, nombre, apellido, telefono, email)
        VALUES (%s, %s, %s, %s, %s);
        """
        cur.execute(consulta, (id_dentista, nombre, apellido, telefono, email))
        conn.commit()
        conn.close()
        messagebox.showinfo("Éxito", "Asistente agregado con éxito")
        top.destroy()

    top = tk.Toplevel(root)
    top.title("Agregar Asistente")

    tk.Label(top, text="ID Dentista:").pack(pady=5)
    entry_id_dentista = tk.Entry(top)
    entry_id_dentista.pack(pady=5)

    tk.Label(top, text="Nombre:").pack(pady=5)
    entry_nombre = tk.Entry(top)
    entry_nombre.pack(pady=5)

    tk.Label(top, text="Apellido:").pack(pady=5)
    entry_apellido = tk.Entry(top)
    entry_apellido.pack(pady=5)

    tk.Label(top, text="Teléfono:").pack(pady=5)
    entry_telefono = tk.Entry(top)
    entry_telefono.pack(pady=5)

    tk.Label(top, text="Email:").pack(pady=5)
    entry_email = tk.Entry(top)
    entry_email.pack(pady=5)

    tk.Button(top, text="Guardar", command=guardar).pack(pady=10)

def consultar_asistente():
    def buscar():
        id_asistente = entry_id.get()
        if not id_asistente:
            messagebox.showerror("Error", "El campo ID Asistente debe estar lleno.")
            return

            # Validación de ID Asistente
        try:
            if int(id_asistente) < 0:
                messagebox.showerror("Error", "El ID del asistente no puede ser negativo.")
                return
        except ValueError:
            messagebox.showerror("Error", "El ID del asistente debe ser un número válido.")
            return
        conn = conectar_bd()
        cur = conn.cursor()
        consulta = "SELECT id_asistente, id_dentista, nombre, apellido, telefono, email FROM Asistente WHERE id_asistente = %s;"
        cur.execute(consulta, (id_asistente,))
        datos = cur.fetchall()
        conn.close()

        top_resultado = tk.Toplevel(root)
        top_resultado.title("Resultado Consulta")
        if datos:
            for col_num, columna in enumerate(["id_asistente", "id_dentista", "nombre", "apellido", "telefono", "email"]):
                tk.Label(top_resultado, text=columna, font=("sans-serif", 12, "bold")).grid(row=0, column=col_num, padx=10, pady=5)
            for row_num, fila in enumerate(datos, start=1):
                for col_num, valor in enumerate(fila):
                    tk.Label(top_resultado, text=valor).grid(row=row_num, column=col_num, padx=10, pady=5)
        else:
            tk.Label(top_resultado, text="No se encontró el asistente.", font=("sans-serif", 12, "bold")).pack(pady=20)

    top = tk.Toplevel(root)
    top.title("Consultar Asistente")

    tk.Label(top, text="ID Asistente:").pack(pady=5)
    entry_id = tk.Entry(top)
    entry_id.pack(pady=5)

    tk.Button(top, text="Buscar", command=buscar).pack(pady=10)

def actualizar_asistente():
    def actualizar():
        id_asistente = entry_id.get()
        id_dentista = entry_id_dentista.get()
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        telefono = entry_telefono.get()
        email = entry_email.get()
        # Validación de campos vacíos
        if not all([id_asistente, id_dentista, nombre, apellido, telefono, email]):
            messagebox.showerror("Error", "Todos los campos deben estar llenos.")
            return

        # Validación de ID Asistente e ID Dentista
        try:
            if int(id_asistente) < 0 or int(id_dentista) < 0:
                messagebox.showerror("Error", "Los valores numéricos no pueden ser negativos.")
                return
        except ValueError:
            messagebox.showerror("Error", "ID Asistente e ID Dentista deben ser números válidos.")
            return

        # Validación de Teléfono
        try:
            if int(telefono) < 0:
                messagebox.showerror("Error", "El teléfono no puede ser un número negativo.")
                return
        except ValueError:
            messagebox.showerror("Error", "El teléfono debe ser un número válido.")
            return

        # Validación de Email
        if "@" not in email or "." not in email.split('@')[-1]:
            messagebox.showerror("Error", "El email no es válido.")
            return

        conn = conectar_bd()
        cur = conn.cursor()
        consulta = "UPDATE Asistente SET id_dentista = %s, nombre = %s, apellido = %s, telefono = %s, email = %s WHERE id_asistente = %s;"
        cur.execute(consulta, (id_dentista, nombre, apellido, telefono, email, id_asistente))
        conn.commit()
        conn.close()
        messagebox.showinfo("Éxito", "Asistente actualizado con éxito")
        top.destroy()

    top = tk.Toplevel(root)
    top.title("Actualizar Asistente")

    tk.Label(top, text="ID Asistente:").pack(pady=5)
    entry_id = tk.Entry(top)
    entry_id.pack(pady=5)

    tk.Label(top, text="ID Dentista:").pack(pady=5)
    entry_id_dentista = tk.Entry(top)
    entry_id_dentista.pack(pady=5)

    tk.Label(top, text="Nombre:").pack(pady=5)
    entry_nombre = tk.Entry(top)
    entry_nombre.pack(pady=5)

    tk.Label(top, text="Apellido:").pack(pady=5)
    entry_apellido = tk.Entry(top)
    entry_apellido.pack(pady=5)

    tk.Label(top, text="Teléfono:").pack(pady=5)
    entry_telefono = tk.Entry(top)
    entry_telefono.pack(pady=5)

    tk.Label(top, text="Email:").pack(pady=5)
    entry_email = tk.Entry(top)
    entry_email.pack(pady=5)

    tk.Button(top, text="Actualizar", command=actualizar).pack(pady=10)

def eliminar_asistente():
    def eliminar():
        id_asistente = entry_id.get()
        if not id_asistente:
            messagebox.showerror("Error", "El campo ID Asistente debe estar lleno.")
            return

            # Validación de ID Asistente
        try:
            if int(id_asistente) < 0:
                messagebox.showerror("Error", "El ID del asistente no puede ser negativo.")
                return
        except ValueError:
            messagebox.showerror("Error", "El ID del asistente debe ser un número válido.")
            return
        conn = conectar_bd()
        cur = conn.cursor()
        consulta = "DELETE FROM Asistente WHERE id_asistente = %s;"
        cur.execute(consulta, (id_asistente,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Éxito", "Asistente eliminado con éxito")
        top.destroy()

    top = tk.Toplevel(root)
    top.title("Eliminar Asistente")

    tk.Label(top, text="ID Asistente:").pack(pady=5)
    entry_id = tk.Entry(top)
    entry_id.pack(pady=5)

    tk.Button(top, text="Eliminar", command=eliminar).pack(pady=10)


def agregar_cita():
    def guardar():
        id_paciente = entry_id_paciente.get()
        id_historia = entry_id_historia.get()
        id_dentista = entry_id_dentista.get()
        id_asistente = entry_id_asistente.get()
        id_tratamiento = entry_id_tratamiento.get()
        cita_fecha = entry_cita_fecha.get()
        estado = entry_estado.get()
        costo = entry_costo.get()
        # Validación de campos vacíos
        if not all([id_paciente, id_historia, id_dentista, id_asistente, id_tratamiento, cita_fecha, estado, costo]):
            messagebox.showerror("Error", "Todos los campos deben estar llenos.")
            return

        # Validación de IDs y costo
        try:
            if int(id_paciente) < 0 or int(id_historia) < 0 or int(id_dentista) < 0 or int(id_asistente) < 0 or int(
                    id_tratamiento) < 0 or float(costo) < 0:
                messagebox.showerror("Error", "Los valores numéricos no pueden ser negativos.")
                return
        except ValueError:
            messagebox.showerror("Error", "IDs y costo deben ser números válidos.")
            return

        # Validación de la fecha
        try:
            datetime.strptime(cita_fecha, "%Y-%m-%d %H:%M:%S")  # Formato: Año-Mes-Día Hora:Minuto:Segundo
        except ValueError:
            messagebox.showerror("Error", "La fecha debe tener el formato AAAA-MM-DD HH:MM:SS.")
            return

        # Validación del estado
        estados_validos = ['Pendiente', 'Cancelado', 'En curso', 'Finalizado']
        if estado not in estados_validos:
            messagebox.showerror("Error", f"El estado debe ser uno de los siguientes: {', '.join(estados_validos)}.")
            return

        conn = conectar_bd()
        cur = conn.cursor()
        consulta = """
        INSERT INTO Cita (id_paciente, id_historia, id_dentista, id_asistente, id_tratamiento, cita_fecha, estado, costo)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """
        cur.execute(consulta, (id_paciente, id_historia, id_dentista, id_asistente, id_tratamiento, cita_fecha, estado, costo))
        conn.commit()
        conn.close()
        messagebox.showinfo("Éxito", "Cita agregada con éxito")
        top.destroy()

    top = tk.Toplevel(root)
    top.title("Agregar Cita")

    tk.Label(top, text="ID Paciente:").pack(pady=5)
    entry_id_paciente = tk.Entry(top)
    entry_id_paciente.pack(pady=5)

    tk.Label(top, text="ID Historia:").pack(pady=5)
    entry_id_historia = tk.Entry(top)
    entry_id_historia.pack(pady=5)

    tk.Label(top, text="ID Dentista:").pack(pady=5)
    entry_id_dentista = tk.Entry(top)
    entry_id_dentista.pack(pady=5)

    tk.Label(top, text="ID Asistente:").pack(pady=5)
    entry_id_asistente = tk.Entry(top)
    entry_id_asistente.pack(pady=5)

    tk.Label(top, text="ID Tratamiento:").pack(pady=5)
    entry_id_tratamiento = tk.Entry(top)
    entry_id_tratamiento.pack(pady=5)

    tk.Label(top, text="Fecha y Hora (YYYY-MM-DD HH:MM:SS):").pack(pady=5)
    entry_cita_fecha = tk.Entry(top)
    entry_cita_fecha.pack(pady=5)

    tk.Label(top, text="Estado:").pack(pady=5)
    entry_estado = tk.Entry(top)
    entry_estado.pack(pady=5)

    tk.Label(top, text="Costo:").pack(pady=5)
    entry_costo = tk.Entry(top)
    entry_costo.pack(pady=5)

    tk.Button(top, text="Guardar", command=guardar).pack(pady=10)

def consultar_cita():
    def buscar():
        id_cita = entry_id.get()
        if not id_cita:
            messagebox.showerror("Error", "El campo ID Cita debe estar lleno.")
            return

            # Validación de ID Cita
        try:
            id_cita = int(id_cita)
            if id_cita < 0:
                messagebox.showerror("Error", "El ID Cita no puede ser negativo.")
                return
        except ValueError:
            messagebox.showerror("Error", "El ID Cita debe ser un número válido.")
            return
        conn = conectar_bd()
        cur = conn.cursor()
        consulta = """
        SELECT id_cita, id_paciente, id_historia, id_dentista, id_asistente, id_tratamiento, cita_fecha, estado, costo
        FROM Cita
        WHERE id_cita = %s;
        """
        cur.execute(consulta, (id_cita,))
        datos = cur.fetchall()
        conn.close()

        top_resultado = tk.Toplevel(root)
        top_resultado.title("Resultado Consulta")
        if datos:
            columnas = ["id_cita", "id_paciente", "id_historia", "id_dentista", "id_asistente", "id_tratamiento", "cita_fecha", "estado", "costo"]
            for col_num, columna in enumerate(columnas):
                tk.Label(top_resultado, text=columna, font=("sans-serif", 12, "bold")).grid(row=0, column=col_num, padx=10, pady=5)
            for row_num, fila in enumerate(datos, start=1):
                for col_num, valor in enumerate(fila):
                    tk.Label(top_resultado, text=valor).grid(row=row_num, column=col_num, padx=10, pady=5)
        else:
            tk.Label(top_resultado, text="No se encontró la cita.", font=("sans-serif", 12, "bold")).pack(pady=20)

    top = tk.Toplevel(root)
    top.title("Consultar Cita")

    tk.Label(top, text="ID Cita:").pack(pady=5)
    entry_id = tk.Entry(top)
    entry_id.pack(pady=5)

    tk.Button(top, text="Buscar", command=buscar).pack(pady=10)

def actualizar_cita():
    def actualizar():
        id_cita = entry_id.get()
        id_paciente = entry_id_paciente.get()
        id_historia = entry_id_historia.get()
        id_dentista = entry_id_dentista.get()
        id_asistente = entry_id_asistente.get()
        id_tratamiento = entry_id_tratamiento.get()
        cita_fecha = entry_cita_fecha.get()
        estado = entry_estado.get()
        costo = entry_costo.get()

        # Validación de campos vacíos
        if not all([id_paciente, id_historia, id_dentista, id_asistente, id_tratamiento, cita_fecha, estado, costo]):
            messagebox.showerror("Error", "Todos los campos deben estar llenos.")
            return

        # Validación de ID y Costo
        try:
            id_paciente = int(id_paciente)
            id_historia = int(id_historia)
            id_dentista = int(id_dentista)
            id_asistente = int(id_asistente)
            id_tratamiento = int(id_tratamiento)
            costo = float(costo)

            if any(x < 0 for x in [id_paciente, id_historia, id_dentista, id_asistente, id_tratamiento, costo]):
                messagebox.showerror("Error", "Los valores numéricos no pueden ser negativos.")
                return
        except ValueError:
            messagebox.showerror("Error",
                                 "ID Paciente, ID Historia, ID Dentista, ID Asistente, ID Tratamiento y Costo deben ser números válidos.")
            return

        # Validación de la fecha
        try:
            datetime.strptime(cita_fecha, "%Y-%m-%d %H:%M:%S")  # Formato: Año-Mes-Día Hora:Minuto:Segundo
        except ValueError:
            messagebox.showerror("Error", "La fecha de la cita debe tener el formato AAAA-MM-DD HH:MM:SS.")
            return

        # Validación del estado
        estados_validos = ['Pendiente', 'Cancelado', 'En curso', 'Finalizado']
        if estado not in estados_validos:
            messagebox.showerror("Error",
                                 "El estado debe ser uno de los siguientes: Pendiente, Cancelado, En curso, Finalizado.")
            return

        conn = conectar_bd()
        cur = conn.cursor()
        consulta = """
        UPDATE Cita
        SET id_paciente = %s, id_historia = %s, id_dentista = %s, id_asistente = %s, id_tratamiento = %s, cita_fecha = %s, estado = %s, costo = %s
        WHERE id_cita = %s;
        """
        cur.execute(consulta, (id_paciente, id_historia, id_dentista, id_asistente, id_tratamiento, cita_fecha, estado, costo, id_cita))
        conn.commit()
        conn.close()
        messagebox.showinfo("Éxito", "Cita actualizada con éxito")
        top.destroy()

    top = tk.Toplevel(root)
    top.title("Actualizar Cita")

    tk.Label(top, text="ID Cita:").pack(pady=5)
    entry_id = tk.Entry(top)
    entry_id.pack(pady=5)

    tk.Label(top, text="ID Paciente:").pack(pady=5)
    entry_id_paciente = tk.Entry(top)
    entry_id_paciente.pack(pady=5)

    tk.Label(top, text="ID Historia:").pack(pady=5)
    entry_id_historia = tk.Entry(top)
    entry_id_historia.pack(pady=5)

    tk.Label(top, text="ID Dentista:").pack(pady=5)
    entry_id_dentista = tk.Entry(top)
    entry_id_dentista.pack(pady=5)

    tk.Label(top, text="ID Asistente:").pack(pady=5)
    entry_id_asistente = tk.Entry(top)
    entry_id_asistente.pack(pady=5)

    tk.Label(top, text="ID Tratamiento:").pack(pady=5)
    entry_id_tratamiento = tk.Entry(top)
    entry_id_tratamiento.pack(pady=5)

    tk.Label(top, text="Fecha y Hora (YYYY-MM-DD HH:MM:SS):").pack(pady=5)
    entry_cita_fecha = tk.Entry(top)
    entry_cita_fecha.pack(pady=5)

    tk.Label(top, text="Estado:").pack(pady=5)
    entry_estado = tk.Entry(top)
    entry_estado.pack(pady=5)

    tk.Label(top, text="Costo:").pack(pady=5)
    entry_costo = tk.Entry(top)
    entry_costo.pack(pady=5)

    tk.Button(top, text="Actualizar", command=actualizar).pack(pady=10)

def eliminar_cita():
    def eliminar():
        id_cita = entry_id.get()
        if not id_cita:
            messagebox.showerror("Error", "El campo ID Cita debe estar lleno.")
            return

            # Validación de ID Cita
        try:
            id_cita = int(id_cita)
            if id_cita < 0:
                messagebox.showerror("Error", "El ID Cita no puede ser negativo.")
                return
        except ValueError:
            messagebox.showerror("Error", "El ID Cita debe ser un número válido.")
            return
        conn = conectar_bd()
        cur = conn.cursor()
        consulta = "DELETE FROM Cita WHERE id_cita = %s;"
        cur.execute(consulta, (id_cita,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Éxito", "Cita eliminada con éxito")
        top.destroy()

    top = tk.Toplevel(root)
    top.title("Eliminar Cita")

    tk.Label(top, text="ID Cita:").pack(pady=5)
    entry_id = tk.Entry(top)
    entry_id.pack(pady=5)

    tk.Button(top, text="Eliminar", command=eliminar).pack(pady=10)

def agregar_tratamiento():
    def guardar():
        id_paciente = entry_id_paciente.get()
        nombre = entry_nombre.get()
        descripcion = entry_descripcion.get()
        duracion_dias = entry_duracion.get()
        # Validación de campos vacíos
        if not all([id_paciente, nombre, descripcion, duracion_dias]):
            messagebox.showerror("Error", "Todos los campos deben estar llenos.")
            return

        # Validación de ID Paciente y Duración
        try:
            id_paciente = int(id_paciente)
            duracion_dias = int(duracion_dias)

            if id_paciente < 0 or duracion_dias < 0:
                messagebox.showerror("Error", "Los valores numéricos no pueden ser negativos.")
                return
        except ValueError:
            messagebox.showerror("Error", "ID Paciente y Duración deben ser números válidos.")
            return

        conn = conectar_bd()
        cur = conn.cursor()
        consulta = """
        INSERT INTO Tratamiento (id_paciente, nombre, descripcion, duracion_dias)
        VALUES (%s, %s, %s, %s);
        """
        cur.execute(consulta, (id_paciente, nombre, descripcion, duracion_dias))
        conn.commit()
        conn.close()
        messagebox.showinfo("Éxito", "Tratamiento agregado con éxito")
        top.destroy()

    top = tk.Toplevel(root)
    top.title("Agregar Tratamiento")

    tk.Label(top, text="ID Paciente:").pack(pady=5)
    entry_id_paciente = tk.Entry(top)
    entry_id_paciente.pack(pady=5)

    tk.Label(top, text="Nombre:").pack(pady=5)
    entry_nombre = tk.Entry(top)
    entry_nombre.pack(pady=5)

    tk.Label(top, text="Descripción:").pack(pady=5)
    entry_descripcion = tk.Entry(top)
    entry_descripcion.pack(pady=5)

    tk.Label(top, text="Duración (días):").pack(pady=5)
    entry_duracion = tk.Entry(top)
    entry_duracion.pack(pady=5)

    tk.Button(top, text="Guardar", command=guardar).pack(pady=10)

def consultar_tratamiento():
    def buscar():
        id_tratamiento = entry_id.get()
        # Validación de campo vacío
        if not id_tratamiento:
            messagebox.showerror("Error", "El ID del tratamiento no puede estar vacío.")
            return

        # Validación de ID del tratamiento
        try:
            id_tratamiento = int(id_tratamiento)
            if id_tratamiento < 0:
                messagebox.showerror("Error", "El ID del tratamiento no puede ser negativo.")
                return
        except ValueError:
            messagebox.showerror("Error", "El ID del tratamiento debe ser un número válido.")
            return

        conn = conectar_bd()
        cur = conn.cursor()
        consulta = "SELECT id_tratamiento, id_paciente, nombre, descripcion, duracion_dias FROM Tratamiento WHERE id_tratamiento = %s;"
        cur.execute(consulta, (id_tratamiento,))
        datos = cur.fetchall()
        conn.close()

        top_resultado = tk.Toplevel(root)
        top_resultado.title("Resultado Consulta")
        if datos:
            for col_num, columna in enumerate(["id_tratamiento", "id_paciente", "nombre", "descripcion", "duracion_dias"]):
                tk.Label(top_resultado, text=columna, font=("sans-serif", 12, "bold")).grid(row=0, column=col_num, padx=10, pady=5)
            for row_num, fila in enumerate(datos, start=1):
                for col_num, valor in enumerate(fila):
                    tk.Label(top_resultado, text=valor).grid(row=row_num, column=col_num, padx=10, pady=5)
        else:
            tk.Label(top_resultado, text="No se encontró el tratamiento.", font=("sans-serif", 12, "bold")).pack(pady=20)

    top = tk.Toplevel(root)
    top.title("Consultar Tratamiento")

    tk.Label(top, text="ID Tratamiento:").pack(pady=5)
    entry_id = tk.Entry(top)
    entry_id.pack(pady=5)

    tk.Button(top, text="Buscar", command=buscar).pack(pady=10)

def actualizar_tratamiento():
    def actualizar():
        try:
            id_tratamiento = entry_id.get()
            id_paciente = entry_id_paciente.get()
            nombre = entry_nombre.get()
            descripcion = entry_descripcion.get()
            duracion_dias = entry_duracion.get()

            # Validar que todos los campos están llenos
            if not all([id_tratamiento, id_paciente, nombre, descripcion, duracion_dias]):
                messagebox.showerror("Error", "Todos los campos deben estar llenos.")
                return

            # Validar id_tratamiento y id_paciente
            try:
                id_tratamiento = int(id_tratamiento)
                id_paciente = int(id_paciente)
                if id_tratamiento < 0 or id_paciente < 0:
                    messagebox.showerror("Error", "Los ID deben ser números no negativos.")
                    return
            except ValueError:
                messagebox.showerror("Error", "ID del tratamiento y del paciente deben ser números válidos.")
                return

            # Validar duracion_dias
            try:
                duracion_dias = int(duracion_dias)
                if duracion_dias <= 0:
                    messagebox.showerror("Error", "La duración en días debe ser un número entero positivo.")
                    return
            except ValueError:
                messagebox.showerror("Error", "La duración en días debe ser un número entero válido.")
                return

            conn = conectar_bd()
            cur = conn.cursor()
            consulta = "UPDATE Tratamiento SET id_paciente = %s, nombre = %s, descripcion = %s, duracion_dias = %s WHERE id_tratamiento = %s;"
            cur.execute(consulta, (id_paciente, nombre, descripcion, duracion_dias, id_tratamiento))
            conn.commit()
            conn.close()
            messagebox.showinfo("Éxito", "Tratamiento actualizado con éxito")
            top.destroy()
        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")

    top = tk.Toplevel(root)
    top.title("Actualizar Tratamiento")

    tk.Label(top, text="ID Tratamiento:").pack(pady=5)
    entry_id = tk.Entry(top)
    entry_id.pack(pady=5)

    tk.Label(top, text="ID Paciente:").pack(pady=5)
    entry_id_paciente = tk.Entry(top)
    entry_id_paciente.pack(pady=5)

    tk.Label(top, text="Nombre:").pack(pady=5)
    entry_nombre = tk.Entry(top)
    entry_nombre.pack(pady=5)

    tk.Label(top, text="Descripción:").pack(pady=5)
    entry_descripcion = tk.Entry(top)
    entry_descripcion.pack(pady=5)

    tk.Label(top, text="Duración (días):").pack(pady=5)
    entry_duracion = tk.Entry(top)
    entry_duracion.pack(pady=5)

    tk.Button(top, text="Actualizar", command=actualizar).pack(pady=10)

def eliminar_tratamiento():
    def eliminar():
        try:
            id_tratamiento = entry_id.get()
            if not id_tratamiento:
                messagebox.showerror("Error", "El ID del tratamiento no puede estar vacío.")
                return

                # Validar que el ID sea un número entero positivo
            try:
                id_tratamiento = int(id_tratamiento)
                if id_tratamiento < 0:
                    messagebox.showerror("Error", "El ID del tratamiento debe ser un número entero no negativo.")
                    return
            except ValueError:
                messagebox.showerror("Error", "El ID del tratamiento debe ser un número válido.")
                return

            conn = conectar_bd()
            cur = conn.cursor()
            consulta = "DELETE FROM Tratamiento WHERE id_tratamiento = %s;"
            cur.execute(consulta, (id_tratamiento,))
            conn.commit()
            conn.close()
            messagebox.showinfo("Éxito", "Tratamiento eliminado con éxito")
            top.destroy()
        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")

    top = tk.Toplevel(root)
    top.title("Eliminar Tratamiento")

    tk.Label(top, text="ID Tratamiento:").pack(pady=5)
    entry_id = tk.Entry(top)
    entry_id.pack(pady=5)

    tk.Button(top, text="Eliminar", command=eliminar).pack(pady=10)



def agregar_historia_clinica():
    def guardar():
        try:
            id_paciente = entry_id_paciente.get()
            observaciones = entry_observaciones.get()
            # Validar que todos los campos estén llenos
            if not id_paciente or not observaciones:
                messagebox.showerror("Error", "Todos los campos deben estar llenos.")
                return

            # Validar que el ID del paciente sea un número entero no negativo
            try:
                id_paciente = int(id_paciente)
                if id_paciente < 0:
                    messagebox.showerror("Error", "El ID del paciente debe ser un número entero no negativo.")
                    return
            except ValueError:
                messagebox.showerror("Error", "El ID del paciente debe ser un número válido.")
                return

            conn = conectar_bd()
            cur = conn.cursor()
            consulta = """
            INSERT INTO Historia_Clinica (id_paciente, observaciones)
            VALUES (%s, %s);
            """
            cur.execute(consulta, (id_paciente, observaciones))
            conn.commit()
            conn.close()
            messagebox.showinfo("Éxito", "Historia Clínica agregada con éxito")
            top.destroy()
        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")

    top = tk.Toplevel(root)
    top.title("Agregar Historia Clínica")

    tk.Label(top, text="ID Paciente:").pack(pady=5)
    entry_id_paciente = tk.Entry(top)
    entry_id_paciente.pack(pady=5)

    tk.Label(top, text="Observaciones:").pack(pady=5)
    entry_observaciones = tk.Entry(top)
    entry_observaciones.pack(pady=5)

    tk.Button(top, text="Guardar", command=guardar).pack(pady=10)



def consultar_historia_clinica():
    def buscar():
        try:
            id_historia = entry_id.get()

            if not id_historia:
                messagebox.showerror("Error", "El ID de la historia clínica no puede estar vacío.")
                return

                # Validar que el ID sea un número entero no negativo
            try:
                id_historia = int(id_historia)
                if id_historia < 0:
                    messagebox.showerror("Error", "El ID de la historia clínica debe ser un número entero no negativo.")
                    return
            except ValueError:
                messagebox.showerror("Error", "El ID de la historia clínica debe ser un número válido.")
                return

            conn = conectar_bd()
            cur = conn.cursor()
            consulta = "SELECT id_historia, id_paciente, observaciones FROM Historia_Clinica WHERE id_historia = %s;"
            cur.execute(consulta, (id_historia,))
            datos = cur.fetchall()
            conn.close()

            top_resultado = tk.Toplevel(root)
            top_resultado.title("Resultado Consulta")
            if datos:
                for col_num, columna in enumerate(["id_historia", "id_paciente", "observaciones"]):
                    tk.Label(top_resultado, text=columna, font=("sans-serif", 12, "bold")).grid(row=0, column=col_num, padx=10, pady=5)
                for row_num, fila in enumerate(datos, start=1):
                    for col_num, valor in enumerate(fila):
                        tk.Label(top_resultado, text=valor).grid(row=row_num, column=col_num, padx=10, pady=5)
            else:
                tk.Label(top_resultado, text="No se encontró la historia clínica.", font=("sans-serif", 12, "bold")).pack(pady=20)
        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")

    top = tk.Toplevel(root)
    top.title("Consultar Historia Clínica")

    tk.Label(top, text="ID Historia Clínica:").pack(pady=5)
    entry_id = tk.Entry(top)
    entry_id.pack(pady=5)

    tk.Button(top, text="Buscar", command=buscar).pack(pady=10)



def actualizar_historia_clinica():
    def actualizar():
        try:
            id_historia = entry_id.get()
            id_paciente = entry_id_paciente.get()
            observaciones = entry_observaciones.get()

            # Validar que todos los campos estén llenos
            if not all([id_historia, id_paciente, observaciones]):
                messagebox.showerror("Error", "Todos los campos deben estar llenos.")
                return

            # Validar que el ID sea un número entero no negativo
            try:
                id_historia = int(id_historia)
                id_paciente = int(id_paciente)
                if id_historia < 0 or id_paciente < 0:
                    messagebox.showerror("Error",
                                         "El ID de la historia clínica y el ID del paciente deben ser números enteros no negativos.")
                    return
            except ValueError:
                messagebox.showerror("Error",
                                     "El ID de la historia clínica y el ID del paciente deben ser números válidos.")
                return


            conn = conectar_bd()
            cur = conn.cursor()
            consulta = "UPDATE Historia_Clinica SET id_paciente = %s, observaciones = %s WHERE id_historia = %s;"
            cur.execute(consulta, (id_paciente, observaciones, id_historia))
            conn.commit()
            conn.close()
            messagebox.showinfo("Éxito", "Historia Clínica actualizada con éxito")
            top.destroy()
        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")

    top = tk.Toplevel(root)
    top.title("Actualizar Historia Clínica")

    tk.Label(top, text="ID Historia Clínica:").pack(pady=5)
    entry_id = tk.Entry(top)
    entry_id.pack(pady=5)

    tk.Label(top, text="ID Paciente:").pack(pady=5)
    entry_id_paciente = tk.Entry(top)
    entry_id_paciente.pack(pady=5)

    tk.Label(top, text="Observaciones:").pack(pady=5)
    entry_observaciones = tk.Entry(top)
    entry_observaciones.pack(pady=5)

    tk.Button(top, text="Actualizar", command=actualizar).pack(pady=10)



def eliminar_historia_clinica():
    def eliminar():
        id_historia = entry_id.get()
        # Validar que el campo ID esté lleno
        if not id_historia:
            messagebox.showerror("Error", "El campo ID debe estar lleno.")
            return

        # Validar que el ID sea un número entero no negativo
        try:
            id_historia = int(id_historia)
            if id_historia < 0:
                messagebox.showerror("Error", "El ID debe ser un número entero no negativo.")
                return
        except ValueError:
            messagebox.showerror("Error", "El ID debe ser un número válido.")
            return
        conn = conectar_bd()
        cur = conn.cursor()
        consulta = "DELETE FROM Historia_Clinica WHERE id_historia = %s;"
        cur.execute(consulta, (id_historia,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Éxito", "Historia Clínica eliminada con éxito")
        top.destroy()

    top = tk.Toplevel(root)
    top.title("Eliminar Historia Clínica")

    tk.Label(top, text="ID Historia Clínica:").pack(pady=5)
    entry_id = tk.Entry(top)
    entry_id.pack(pady=5)

    tk.Button(top, text="Eliminar", command=eliminar).pack(pady=10)

def create_button(image_path, text, row, col, tabla):
    image = Image.open(image_path)
    ajuste_image = image.resize((110, 110))
    img = ImageTk.PhotoImage(ajuste_image)
    font=("sans-serif", 13, "bold")
    button = tk.Button(button_frame, image=img, text=text, compound=tk.BOTTOM, font=font, command=lambda: mostrar_datos(tabla))
    button.grid(row=row, column=col, padx=5, pady=5)
    button.image = img
    return button


def mostrar_resultados(consulta, columnas):
    conn = conectar_bd()
    cur = conn.cursor()
    cur.execute(consulta)
    datos = cur.fetchall()
    conn.close()

    top_resultado = tk.Toplevel(root)
    top_resultado.title("Resultado Consulta")

    if datos:
        # Mostrar encabezados de columnas
        for col_num, columna in enumerate(columnas):
            tk.Label(top_resultado, text=columna, font=("sans-serif", 12, "bold")).grid(row=0, column=col_num, padx=10, pady=5)

        # Mostrar filas de datos
        for row_num, fila in enumerate(datos, start=1):
            for col_num, valor in enumerate(fila):
                tk.Label(top_resultado, text=valor).grid(row=row_num, column=col_num, padx=10, pady=5)
    else:
        tk.Label(top_resultado, text="No hay datos para mostrar", font=("sans-serif", 12)).pack(pady=20)

def mostrar_resultados(consulta, columnas):
    conn = conectar_bd()
    cur = conn.cursor()
    cur.execute(consulta)
    datos = cur.fetchall()
    conn.close()

    top_resultado = tk.Toplevel(root)
    top_resultado.title("Resultado Consulta")

    if datos:
        for col_num, columna in enumerate(columnas):
            tk.Label(top_resultado, text=columna, font=("sans-serif", 12, "bold")).grid(row=0, column=col_num, padx=10, pady=5)
        for row_num, fila in enumerate(datos, start=1):
            for col_num, valor in enumerate(fila):
                tk.Label(top_resultado, text=valor).grid(row=row_num, column=col_num, padx=10, pady=5)
    else:
        tk.Label(top_resultado, text="No se encontraron resultados", font=("sans-serif", 12)).pack(pady=10)

def ejecutar_consulta(opcion):
    if opcion == 1:
        consulta = """
        SELECT id_paciente, nombre, apellido, numero_de_citas, tratamientos_activos
        FROM reporte_pacientes_citas_tratamientos;
        """
        columnas = ["id_paciente", "nombre", "apellido", "numero_de_citas", "tratamientos_activos"]
        mostrar_resultados(consulta, columnas)
    elif opcion == 2:
        consulta = """
        SELECT id_paciente, id_dentista, id_tratamiento, ingresos_totales
        FROM reporte_ingresos_pacientes_dentistas_tratamientos;
        """
        columnas = ["id_paciente", "id_dentista", "id_tratamiento", "ingresos_totales"]
        mostrar_resultados(consulta, columnas)
    elif opcion == 3:
        consulta = """
        SELECT id_tratamiento, nombre_tratamiento, numero_de_citas, duracion_promedio
        FROM reporte_tratamientos_populares;
        """
        columnas = ["id_tratamiento", "nombre_tratamiento", "numero_de_citas", "duracion_promedio"]
        mostrar_resultados(consulta, columnas)
    elif opcion == 4:
        consulta = """
        SELECT id_dentista, nombre_dentista, apellido_dentista, numero_de_citas, numero_de_asistentes, tratamiento_comun
        FROM reporte_dentistas_citas_asistentes;
        """
        columnas = ["id_dentista", "nombre_dentista", "apellido_dentista", "numero_de_citas", "numero_de_asistentes", "tratamiento_comun"]
        mostrar_resultados(consulta, columnas)
    else:
        messagebox.showerror("Error", "Opción no válida")

def consultas():
    top = tk.Toplevel(root)
    top.title("Opciones Consultas")
    tk.Label(top, text="Seleccione una consulta:", font=("sans-serif", 14, "bold")).pack(pady=10)

    consultas = {
        "Pacientes con Mayor Número de Citas y Tratamientos Activos": 1,
        "Ingresos Totales por Paciente, Dentista, y Tratamiento": 2,
        "Tratamientos Más Populares y Su Duración Promedio": 3,
        "Dentistas con Mayor Número de Citas y Asistentes Asociados": 4,
    }

    for texto, opcion in consultas.items():
        tk.Button(top, text=texto, font=("sans-serif", 12, "bold"), command=lambda op=opcion: ejecutar_consulta(op)).pack(pady=5)

# Crear el botón para Consultas
def create_buttonn(image_path, text, row, col, tabla):
    image = Image.open(image_path)
    ajuste_image = image.resize((110, 110))
    img = ImageTk.PhotoImage(ajuste_image)
    font=("sans-serif", 13, "bold")
    button = tk.Button(button_frame, image=img, text=text, compound=tk.BOTTOM, font=font, command=consultas)
    button.grid(row=row, column=col, padx=5, pady=5)
    button.image = img
    return button

# Crear la ventana principal
root = tk.Tk()
root.title("Proyecto de BD")
root.geometry("1000x600")

# Parte superior de los botones
etiqueta = tk.Label(root, text="🦷 Clinica Dental Ayora", bg="#2b72ff", fg="#ffffff", height=3, width=10, anchor="w", font=("sans-serif", 15, "bold"))
etiqueta.pack(fill=tk.X)

etiquetaMenu = tk.Label(root, text="Menú de opciones", fg="#000000", anchor="w", font=("sans-serif", 30, "bold"))
etiquetaMenu.pack(anchor="w", padx=250, pady=20)

etiquetaDescripcion = tk.Label(root, text="Selecciona tu consulta", fg="#6E6E77", anchor="w", font=("sans-serif", 12, "bold"))
etiquetaDescripcion.pack(anchor="w", padx=250)

# Es un contenedor para los botones
button_frame = tk.Frame(root)
button_frame.pack(padx=10, pady=10)

# Crear los botones para las tablas
create_button("icono_paciente.png", "Pacientes", 0, 0, "Paciente")
create_button("icono_dentista.png", "Dentistas", 0, 1, "Dentista")
create_button("icono_asistente.png", "Asistente", 0, 2, "Asistente")
create_button("icono_cita.png", "Cita", 0, 3, "Cita")
create_button("icono_tratamiento.png", "Tratamiento", 1, 0, "Tratamiento")
create_button("icono_historial.png", "Historia Clinica", 1, 1, "Historia_Clinica")
create_buttonn("icono_consulta.png", "Consultas", 1, 2, "Consulta")

# Inicio del bucle para la ventana
root.mainloop()
