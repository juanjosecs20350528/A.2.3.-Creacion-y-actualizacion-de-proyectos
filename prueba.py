from tkinter import Tk, Label, Entry, Button, messagebox
from pymongo import MongoClient

# Función para guardar los datos en MongoDB
def guardar_datos():
    # Conexión a la base de datos MongoDB
    client = MongoClient('localhost', 27017)
    db = client['prueba']  # Nombre de la base de datos
    collection = db['datos_generales']  # Nombre de la colección

    # Datos ingresados por el usuario
    datos = {
        "RFC": entry_rfc.get(),
        "nombre": entry_nombre.get(),
        "apellido_paterno": entry_apellido_paterno.get(),
        "apellido_materno": entry_apellido_materno.get(),
        "fecha_de_nacimiento": entry_fecha_nacimiento.get(),
        "edad": entry_edad.get(),
        "sexo": entry_sexo.get(),
        "estado_civil": entry_estado_civil.get(),
        "CURP": entry_CURP.get(),
        "telefono": entry_telefono.get(),
        "calle": entry_calle.get(),
        "numero_de_casa": entry_numero_de_casa.get(),
        "colonia": entry_colonia.get(),
        "ciudad": entry_ciudad.get(),
        "estado": entry_estado.get(),
        "codigo_postal": entry_codigo_postal.get(),
        "numero_de_credencial": entry_numero_de_credencial.get(),
        "estatus": entry_estatus.get()
    }

    # Insertar los datos en la colección
    collection.insert_one(datos)
    messagebox.showinfo("Éxito", "Los datos se han guardado correctamente en la base de datos.")

# Crear la ventana principal
ventana = Tk()
ventana.title("Formulario de trabajo")

# Crear etiquetas y campos de entrada para cada dato
Label(ventana, text="RFC:").grid(row=0, column=0)
entry_rfc = Entry(ventana)
entry_rfc.grid(row=0, column=1)

Label(ventana, text="Nombre:").grid(row=1, column=0)
entry_nombre = Entry(ventana)
entry_nombre.grid(row=1, column=1)

Label(ventana, text="Nombre:").grid(row=1, column=0)
entry_nombre = Entry(ventana)
entry_nombre.grid(row=1, column=1)

Label(ventana, text="Apellido Paterno:").grid(row=2, column=0)
entry_apellido_paterno = Entry(ventana)
entry_apellido_paterno.grid(row=2, column=1)

Label(ventana, text="Apellido Materno:").grid(row=3, column=0)
entry_apellido_materno = Entry(ventana)
entry_apellido_materno.grid(row=3, column=1)

Label(ventana, text="Fecha de Nacimiento:").grid(row=4, column=0)
entry_fecha_nacimiento = Entry(ventana)
entry_fecha_nacimiento.grid(row=4, column=1)

Label(ventana, text="Edad:").grid(row=5, column=0)
entry_edad = Entry(ventana)
entry_edad.grid(row=5, column=1)

Label(ventana, text="Sexo:").grid(row=6, column=0)
entry_sexo = Entry(ventana)
entry_sexo.grid(row=6, column=1)

Label(ventana, text="Estado Civil:").grid(row=7, column=0)
entry_estado_civil = Entry(ventana)
entry_estado_civil.grid(row=7, column=1)

Label(ventana, text="CURP:").grid(row=8, column=0)
entry_CURP = Entry(ventana)
entry_CURP.grid(row=8, column=1)

Label(ventana, text="Teléfono:").grid(row=9, column=0)
entry_telefono = Entry(ventana)
entry_telefono.grid(row=9, column=1)

Label(ventana, text="Calle:").grid(row=10, column=0)
entry_calle = Entry(ventana)
entry_calle.grid(row=10, column=1)

Label(ventana, text="Número de Casa:").grid(row=11, column=0)
entry_numero_de_casa = Entry(ventana)
entry_numero_de_casa.grid(row=11, column=1)

Label(ventana, text="Colonia:").grid(row=12, column=0)
entry_colonia = Entry(ventana)
entry_colonia.grid(row=12, column=1)

Label(ventana, text="Ciudad:").grid(row=13, column=0)
entry_ciudad = Entry(ventana)
entry_ciudad.grid(row=13, column=1)

Label(ventana, text="Estado:").grid(row=14, column=0)
entry_estado = Entry(ventana)
entry_estado.grid(row=14, column=1)

Label(ventana, text="Código Postal:").grid(row=15, column=0)
entry_codigo_postal = Entry(ventana)
entry_codigo_postal.grid(row=15, column=1)

Label(ventana, text="Número de Credencial:").grid(row=16, column=0)
entry_numero_de_credencial = Entry(ventana)
entry_numero_de_credencial.grid(row=16, column=1)

Label(ventana, text="Estatus:").grid(row=17, column=0)
entry_estatus = Entry(ventana)
entry_estatus.grid(row=17, column=1)

# Continuar con las etiquetas y campos de entrada para los demás datos...

# Botón para guardar los datos
Button(ventana, text="Guardar", command=guardar_datos).grid(row=20, columnspan=2)

# Ejecutar el bucle principal
ventana.mainloop()