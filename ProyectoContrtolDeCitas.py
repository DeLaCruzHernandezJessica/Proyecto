import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import csv
import os


class Registrar_enfermero:
   def __init__(self, nombre, apellidop, apellidom, sexo, edad, telefono):
        self.nombre = nombre
        self.apellidop = apellidop
        self.apellidom = apellidom
        self.sexo = sexo
        self.edad = edad
        self.telefono = telefono
   def datos(self):
      return f"{self.nombre} {self.apellidop} {self.apellidom} a sido registrado exitosamente"
def registro_enfermeria():
   try:
     nombre = en_nombre.get()
     apellidop = en_apellidop.get()
     apellidom = en_apellidom.get()
     sexo = en_sexo.get()
     edad = en_edad.get()
     telefono = en_telefono.get()
     if not all([nombre, apellidop, apellidom, sexo, edad, telefono]):
        raise ValueError("Todos los campos son obligatorios")
     registro = Registrar_enfermero(nombre, apellidop, apellidom, sexo, edad, telefono)
     guardar_enfermero_en_csv(registro)
     mensaje = registro.datos()
     messagebox.showinfo("Datos Registrados", mensaje)
   except ValueError as e:
     messagebox.showwarning("error", "no se pudo completar el registro, porfavor intente de nuevo")

def guardar_enfermero_en_csv(enfermero):
    archivo = "enfermeros.csv"
    existe = os.path.isfile(archivo)

    with open(archivo, mode="a", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        if not existe:
            writer.writerow(["Nombre", "Apellido Paterno", "Apellido Materno", "Sexo", "Edad", "Teléfono"])
        writer.writerow([
            enfermero.nombre,
            enfermero.apellidop,
            enfermero.apellidom,
            enfermero.sexo,
            enfermero.edad,
            enfermero.telefono
        ])

def mostrar_medicos():
    archivo = "medicos.csv"
    if not os.path.isfile(archivo):
        messagebox.showinfo("Sin registros", "Aún no hay médicos registrados.")
        return

    ventana_medicos = tk.Toplevel(ventana)
    ventana_medicos.title("Médicos Registrados")
    ventana_medicos.geometry("800x400")

    tk.Label(ventana_medicos, text="Médicos Registrados", font=("Arial", 14, "bold")).pack(pady=10)

    tree = ttk.Treeview(ventana_medicos, columns=("Nombre", "Apellido Paterno", "Apellido Materno", "Sexo", "Edad", "Teléfono", "Cargo", "Medico", "Enfermero"), show='headings')
    tree.pack(expand=True, fill="both")
    encabezados = ["Nombre", "Apellido Paterno", "Apellido Materno", "Sexo", "Edad", "Teléfono", "Cargo", "Medico", "Enfermero"]
    for col in encabezados:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    with open(archivo, newline='', encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        for fila in reader:
            tree.insert("", "end", values=fila)

def mostrar_enfermeros():
    archivo = "enfermeros.csv"
    if not os.path.isfile(archivo):
        messagebox.showinfo("Sin registros", "Aún no hay enfermeros registrados.")
        return

    ventana_enfermeros = tk.Toplevel(ventana)
    ventana_enfermeros.title("Enfermeros Registrados")
    ventana_enfermeros.geometry("800x400")

    tk.Label(ventana_enfermeros, text="Enfermeros Registrados", font=("Arial", 14, "bold")).pack(pady=10)

    tree = ttk.Treeview(ventana_enfermeros, columns=("Nombre", "Apellido Paterno", "Apellido Materno", "Sexo", "Edad", "Teléfono"), show='headings')
    tree.pack(expand=True, fill="both")

    encabezados = ["Nombre", "Apellido Paterno", "Apellido Materno", "Sexo", "Edad", "Teléfono"]
    for col in encabezados:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    with open(archivo, newline='', encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)  
        for fila in reader:
            tree.insert("", "end", values=fila)


class Registrar_medico:
    def __init__(self, nombre, apellidop, apellidom, sexo, edad, telefono, cargo):
        self.nombre = nombre
        self.apellidop = apellidop
        self.apellidom = apellidom
        self.sexo = sexo
        self.edad = edad
        self.telefono = telefono
        self.cargo = cargo
    def datos(self):
        return f"{self.nombre} {self.apellidop} {self.apellidom} a sido registrado exitosamente"
def registrar_usuario():
 try:
     nombre = en_nombre.get()
     apellidop = en_apellidop.get()
     apellidom = en_apellidom.get()
     sexo = en_sexo.get()
     edad = en_edad.get()
     telefono = en_telefono.get()
     cargo = en_cargo.get()
     if not all([nombre, apellidop, apellidom, sexo, edad, telefono, cargo]):
        raise ValueError("Todos los campos son obligatorios")
     registro = Registrar_medico(nombre, apellidop, apellidom, sexo, edad, telefono, cargo)
     guardar_medico_en_csv(registro)
     mensaje = registro.datos()
     messagebox.showinfo("Datos Registrados", mensaje)
 except ValueError as e:
    messagebox.showwarning("error", str(e))

def guardar_medico_en_csv(medico):
    archivo = "medicos.csv"
    existe = os.path.isfile(archivo)

    with open(archivo, mode="a", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        if not existe:
            writer.writerow(["Nombre", "Apellido Paterno", "Apellido Materno", "Sexo", "Edad", "Teléfono", "Cargo"])
        writer.writerow([
            medico.nombre,
            medico.apellidop,
            medico.apellidom,
            medico.sexo,
            medico.edad,
            medico.telefono,
            medico.cargo
        ])

def obtener_medicos():
    medicos = []
    archivo = "medicos.csv"
    if os.path.isfile(archivo):
        with open(archivo, newline='', encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)
            for fila in reader:
                nombre_completo = f"{fila[0]} {fila[1]} {fila[2]}"
                medicos.append(nombre_completo)
    return medicos

def obtener_enfermeros():
    enfermeros = []
    archivo = "enfermeros.csv"
    if os.path.isfile(archivo):
        with open(archivo, newline='', encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)
            for fila in reader:
                nombre_completo = f"{fila[0]} {fila[1]} {fila[2]}"
                enfermeros.append(nombre_completo)
    return enfermeros



class Pacientes:
    def __init__(self, nombre, apellidop, apellidom, telefono, area, especialista, id_paciente=None):
        self.nombre=nombre
        self.apellidop=apellidop
        self.apellidom=apellidom
        self.telefono=telefono
        self.area=area
        self.especialista=especialista
        self.id_paciente=id_paciente if id_paciente else format(id(self), "x")
    def __str__(self):
        return f"Paciente registrado, ID paciente: {self.id_paciente}"
    
class PacienteCama(Pacientes):
    camas_ocupadas = set()

    @staticmethod
    def obtener_cama(area):
        if area=="Urgencias":
            rango=range(1, 25)
        elif area=="Hospitalizacion":
            rango=range(25, 50)
        elif area=="Cuidados Intensivos":
            rango=range(50, 101)
        else:
            return None 
        for cama in rango:
            if cama not in PacienteCama.camas_ocupadas:
                PacienteCama.camas_ocupadas.add(cama)
                return cama
        return None 

    def __init__(self, nombre, apellidop, apellidom, telefono, area, especialista=None, medico_asignado=None, enfermero_asignado=None):
        super().__init__(nombre, apellidop, apellidom, telefono, area, especialista)
        cama=self.obtener_cama(area)
        if cama is None:
            raise Exception(f"No hay camas disponibles para el área: {area}")
        self.cama_asignada = cama
        self.medico_asignado = medico_asignado
        self.enfermero_asignado = enfermero_asignado

    def __str__(self):
        return super().__str__() + f" - Cama asignada: {self.cama_asignada}"

def guardar_paciente_en_csv(paciente_obj):
    archivo = "pacientes.csv"
    existe = os.path.isfile(archivo)

    with open(archivo, mode="a", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        if not existe:
            writer.writerow([
                "ID", "Nombre", "Apellido Paterno", "Apellido Materno",
                "Teléfono", "Área", "Especialista", "Cama Asignada",
                "Médico Asignado", "Enfermero Asignado"
            ])
        
        writer.writerow([
            paciente_obj.id_paciente,
            paciente_obj.nombre,
            paciente_obj.apellidop,
            paciente_obj.apellidom,
            paciente_obj.telefono,
            paciente_obj.area,
            paciente_obj.especialista if paciente_obj.especialista else "N/A",
            paciente_obj.cama_asignada if hasattr(paciente_obj, 'cama_asignada') else "No requiere",
            paciente_obj.medico_asignado if hasattr(paciente_obj, 'medico_asignado') else "No asignado",
            paciente_obj.enfermero_asignado if hasattr(paciente_obj, 'enfermero_asignado') else "No asignado"
        ])



def registro_paciente():
    try:
        nombre = en_nombre.get()
        apellidop = en_apellidop.get()
        apellidom = en_apellidom.get()
        telefono = en_telefono.get()
        area = en_area.get()
        especialista = en_especialista.get() if en_area.get() == "Cita Medica(medico especialista)" else ""
        medico = en_medico.get()
        enfermero = en_enfermero.get()

        if not all([nombre, apellidop, apellidom, telefono, area]):
            raise ValueError("Todos los campos son obligatorios")

        if area in ["Urgencias", "Hospitalizacion", "Cuidados Intensivos"]:
            nuevo_paciente = PacienteCama(nombre, apellidop, apellidom, telefono, area, especialista, medico, enfermero)
        else:
            nuevo_paciente = Pacientes(nombre, apellidop, apellidom, telefono, area, especialista)

        guardar_paciente_en_csv(nuevo_paciente)
        messagebox.showinfo("Paciente registrado", str(nuevo_paciente))

    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", str(e))


def mostrar_todos_los_pacientes():
    archivo = "pacientes.csv"
    if not os.path.isfile(archivo):
        messagebox.showinfo("Sin registros", "Aún no hay pacientes registrados.")
        return

    ventana_lista = tk.Toplevel(ventana)
    ventana_lista.title("Todos los pacientes registrados")
    ventana_lista.geometry("900x450")

    tk.Label(ventana_lista, text="Pacientes Registrados", font=("Arial", 14, "bold")).pack(pady=10)

    tree = ttk.Treeview(ventana_lista, columns=("ID", "Nombre", "Paterno", "Materno", "Teléfono", "Área", "Especialista", "Cama", "Medico", "Enfermero"), show='headings')
    tree.pack(expand=True, fill="both")

    encabezados = ["ID", "Nombre", "Paterno", "Materno", "Teléfono", "Área", "Especialista", "Cama", "Medico", "Enfermero"]
    for col in encabezados:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    with open(archivo, newline='', encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)  
        for fila in reader:
            tree.insert("", "end", values=fila)

    def eliminar_paciente():
        seleccionado = tree.selection()
        if not seleccionado:
            messagebox.showwarning("Error", "Seleccione un paciente")
            return
        
        confirm = messagebox.askyesno("Aviso", "¿Quiere eliminar el paciente seleccionado?")
        if not confirm:
            return

        item = tree.item(seleccionado)
        id_paciente = item['values'][0]

        with open(archivo, newline='', encoding="utf-8") as f:
            filas = list(csv.reader(f))
        filas_nuevas = [filas[0]] + [fila for fila in filas[1:] if fila[0] != id_paciente]

        with open(archivo, 'w', newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(filas_nuevas)

        tree.delete(seleccionado)

        messagebox.showinfo("Eliminado", " El paciente ha sido eliminado")

    def editar_paciente():
        seleccionado = tree.selection()
        if not seleccionado:
            messagebox.showwarning("Error", "Seleccione un paciente")
            return

        item = tree.item(seleccionado)
        datos = item['values']

        ventana_editar = tk.Toplevel(ventana_lista)
        ventana_editar.title("Editar paciente")
        ventana_editar.geometry("400x400")

        labels = ["ID", "Nombre", "Apellido Paterno", "Apellido Materno", "Teléfono", "Área", "Especialista", "Cama"]
        entradas = {}

        for i, label in enumerate(labels):
            tk.Label(ventana_editar, text=label).grid(row=i, column=0, pady=5, sticky="e")
            if label == "ID" or label == "Cama":
                entry = tk.Label(ventana_editar, text=datos[i])
                entry.grid(row=i, column=1, pady=5)
                entradas[label] = datos[i]
            else:
                entry = tk.Entry(ventana_editar)
                entry.grid(row=i, column=1, pady=5)
                entry.insert(0, datos[i])
                entradas[label] = entry

        def guardar_cambios():
            nuevos_datos = []
            for label in labels:
                if label == "ID" or label == "Cama":
                    nuevos_datos.append(entradas[label])
                else:
                    valor = entradas[label].get().strip()
                    if not valor:
                        messagebox.showerror("Error", f"El campo '{label}' no puede estar vacío.")
                        return
                    nuevos_datos.append(valor)

            with open(archivo, newline='', encoding="utf-8") as f:
                filas = list(csv.reader(f))
            for i, fila in enumerate(filas):
                if i > 0 and fila[0] == nuevos_datos[0]:
                    filas[i] = nuevos_datos
                    break

            with open(archivo, 'w', newline='', encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(filas)

            tree.item(seleccionado, values=nuevos_datos)

            messagebox.showinfo("Guardado", "Cambios guardados correctamente.")
            ventana_editar.destroy()

        btn_guardar = tk.Button(ventana_editar, text="Guardar cambios", command=guardar_cambios)
        btn_guardar.grid(row=len(labels), column=0, columnspan=2, pady=10)

    frame_botones = tk.Frame(ventana_lista)
    frame_botones.pack(pady=10)

    btn_editar = tk.Button(frame_botones, text="Editar paciente", command=editar_paciente)
    btn_editar.grid(row=0, column=0, padx=10)

    btn_eliminar = tk.Button(frame_botones, text="Eliminar paciente", command=eliminar_paciente)
    btn_eliminar.grid(row=0, column=1, padx=10)



ventana=tk.Tk()
ventana.title("Inicio")
ventana.geometry("600x500")
frame=tk.Frame(ventana)
frame.pack(pady=20)

valor=tk.StringVar()
valor.set("Elige una opcion")

frame2=tk.Frame(ventana)
frame2.pack(pady=10)
tk.Label(frame2, text="¿Quien quieres registrar?", font=("calibri", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
opc = tk.OptionMenu(frame2, valor, "Medico", "Enfermero(a)", "Paciente")
opc.grid(row=0, column=1, padx=10, pady=10, sticky="w")

def formulario(var, indx, mode):
   global en_nombre, en_apellidom, en_apellidop, en_telefono, en_edad, en_cargo, en_sexo, id_paciente, en_area, en_especialista, en_enfermero, en_medico
   en_especialista=None
   
   for widget in frame.winfo_children():
    widget.destroy()
   seleccion=valor.get()
  
   if seleccion=="Medico":
      tk.Label(frame, text="Nombre:").grid(row=1, column=0, sticky="e")
      en_nombre=tk.Entry(frame)
      en_nombre.grid(row=1, column=1, padx=10, pady=5)
      tk.Label(frame, text="Apellido Paterno:").grid(row=2, column=0, sticky="e")
      en_apellidop=tk.Entry(frame)
      en_apellidop.grid(row=2, column=1, padx=10, pady=5)
      tk.Label(frame, text="Apellido materno:").grid(row=3, column=0, sticky="e")
      en_apellidom=tk.Entry(frame)
      en_apellidom.grid(row=3, column=1, padx=10, pady=5)
      tk.Label(frame, text="Sexo").grid(row=4, column=0, sticky="e")
      en_sexo=tk.StringVar()
      combo_sexo = ttk.Combobox(frame, textvariable=en_sexo, values=["Masculino", "Femenino"])
      combo_sexo.grid(row=4, column=1, padx=10, pady=5)
      tk.Label(frame, text="Edad:").grid(row=5, column=0, sticky="e")
      en_edad=tk.Entry(frame)
      en_edad.grid(row=5, column=1, padx=10, pady=5)
      tk.Label(frame, text="Telefono:").grid(row=6, column=0, sticky="e")
      en_telefono=tk.Entry(frame)
      en_telefono.grid(row=6, column=1, padx=10, pady=5)
      tk.Label(frame, text="Cargo:").grid(row=7, column=0, sticky="e")
      en_cargo=tk.StringVar()
      ttk.Combobox(frame, textvariable=en_cargo, values=["Medico general", "Medico especialista"]).grid(row=7, column=1, padx=10, pady=5)
      boton_medico=tk.Button(frame, text="Registrar personal", command=registrar_usuario)
      boton_medico.grid(row=8, column=0, columnspan=2, pady=10)
   elif seleccion=="Enfermero(a)":
      tk.Label(frame, text="Nombre:").grid(row=1, column=0, sticky="e")
      en_nombre=tk.Entry(frame)
      en_nombre.grid(row=1, column=1, padx=10, pady=5)
      tk.Label(frame, text="Apellido Paterno:").grid(row=2, column=0, sticky="e")
      en_apellidop=tk.Entry(frame)
      en_apellidop.grid(row=2, column=1, padx=10, pady=5)
      tk.Label(frame, text="Apellido materno:").grid(row=3, column=0, sticky="e")
      en_apellidom=tk.Entry(frame)
      en_apellidom.grid(row=3, column=1, padx=10, pady=5)
      tk.Label(frame, text="Sexo").grid(row=4, column=0, sticky="e")
      en_sexo=tk.StringVar()
      combo_sexo = ttk.Combobox(frame, textvariable=en_sexo, values=["Masculino", "Femenino"])
      combo_sexo.grid(row=4, column=1, padx=10, pady=5)
      tk.Label(frame, text="Edad:").grid(row=5, column=0, sticky="e")
      en_edad=tk.Entry(frame)
      en_edad.grid(row=5, column=1, padx=10, pady=5)
      tk.Label(frame, text="Telefono:").grid(row=6, column=0, sticky="e")
      en_telefono=tk.Entry(frame)
      en_telefono.grid(row=6, column=1, padx=10, pady=5)
      boton_enfermero=tk.Button(frame, text="Registrar personal", command=registro_enfermeria)
      boton_enfermero.grid(row=8, column=0, columnspan=2, pady=10)
   elif seleccion=="Paciente":
      tk.Label(frame, text="Registro de Pacientes").grid(row=0, column=0, columnspan=2, pady=10)
      tk.Label(frame, text="Nombre:").grid(row=1, column=0, sticky="e")
      en_nombre=tk.Entry(frame)
      en_nombre.grid(row=1, column=1, padx=10, pady=5)
      tk.Label(frame, text="Apellido Paterno:").grid(row=2, column=0, sticky="e")
      en_apellidop=tk.Entry(frame)
      en_apellidop.grid(row=2, column=1, padx=10, pady=5)
      tk.Label(frame, text="Apellido materno:").grid(row=3, column=0, sticky="e")
      en_apellidom=tk.Entry(frame)
      en_apellidom.grid(row=3, column=1, padx=10, pady=5)
      tk.Label(frame, text="Telefono:").grid(row=4, column=0, sticky="e")
      en_telefono=tk.Entry(frame)
      en_telefono.grid(row=4, column=1, padx=10, pady=5)

      tk.Label(frame, text="Area").grid(row=5, column=0, sticky="e")
      en_area=tk.StringVar()
      en_area.set
      combo_area=ttk.Combobox(frame, textvariable=en_area, values=["Urgencias", "Cuidados Intensivos", "Hospitalizacion", "Cita Medica(medico especialista)", "Chequeo medico"])
      combo_area.grid(row=5, column=1, padx=10, pady=5)

      tk.Label(frame, text="Asignar Médico").grid(row=7, column=0, sticky="e")
      en_medico = tk.StringVar()
      combo_medico = ttk.Combobox(frame, textvariable=en_medico, values=obtener_medicos())
      combo_medico.grid(row=7, column=1, padx=10, pady=5)

      tk.Label(frame, text="Asignar Enfermero(a)").grid(row=8, column=0, sticky="e")
      en_enfermero = tk.StringVar()
      combo_enfermero = ttk.Combobox(frame, textvariable=en_enfermero, values=obtener_enfermeros())
      combo_enfermero.grid(row=8, column=1, padx=10, pady=5)



      en_especialista_label=tk.Label(frame, text="Ingrese especialista a consultar")
      en_especialista=tk.Entry(frame)
      def mostrar_especialista(*args):
          if en_area.get()=="Cita Medica(medico especialista)":
             en_especialista_label.grid(row=6, column=0, sticky="e")
             en_especialista.grid(row=6, column=1, padx=10, pady=5)
          else:
             en_especialista_label.grid_forget()
             en_especialista.grid_forget()
      en_area.trace_add("write", mostrar_especialista)

      boton_paciente=tk.Button(frame, text="Registrar paciente", command=registro_paciente)
      boton_paciente.grid(row=7, column=0, columnspan=3, pady=10)
   
valor.trace_add("write", formulario)

ventana.configure(bg="#f0f4f7") 

titulo = tk.Label(ventana, text="Sistema de Registro Hospitalario", font=("Calibri", 16, "bold"), bg="#f0f4f7", fg="#2c3e50")
titulo.pack(pady=10)

estilo = ttk.Style()
estilo.theme_use("clam") 
estilo.configure("TLabel", background="#f0f4f7", font=("Calibri", 11))
estilo.configure("TButton", padding=6, relief="flat", background="#4a90e2", foreground="white", font=("Calibri", 10))
estilo.map("TButton", background=[("active", "#357ABD")])
estilo.configure("TCombobox", padding=4)
estilo.configure("Treeview", font=("Calibri", 10), rowheight=24)
estilo.configure("Treeview.Heading", font=("Calibri", 11, "bold"))

for frame_ref in [frame, frame2]:
    frame_ref.configure(bg="#ffffff", bd=2, relief="groove", padx=10, pady=10)

def aplicar_fondo_widgets(widget):
    for child in widget.winfo_children():
        try:
            if isinstance(child, tk.Label):
                child.configure(bg="#ffffff", font=("Calibri", 11))
            elif isinstance(child, tk.Entry):
                child.configure(bg="#eef2f7", relief="groove")
            elif isinstance(child, tk.Button):
                child.configure(bg="#4a90e2", fg="white", relief="flat", font=("Calibri", 10), activebackground="#5389BF")
            elif isinstance(child, ttk.Combobox):
                child.configure(style="TCombobox")
        except:
            pass
        aplicar_fondo_widgets(child)

aplicar_fondo_widgets(ventana)

tk.Button(ventana, text="Ver todos los pacientes registrados", command=mostrar_todos_los_pacientes, width=40).pack(pady=10)
tk.Button(ventana, text="Ver médicos registrados", command=mostrar_medicos, width=40).pack(pady=5)
tk.Button(ventana, text="Ver enfermeros registrados", command=mostrar_enfermeros, width=40).pack(pady=5)


ventana.mainloop()
