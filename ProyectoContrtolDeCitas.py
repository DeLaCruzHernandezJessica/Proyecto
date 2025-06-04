import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Registrar_enfermero:
   def __init__(self, nombre, apellidop, apellidom, sexo, edad, telefono):
        self.nombre = nombre
        self.apellidop = apellidop
        self.apellidom = apellidom
        self.sexo = sexo
        self.edad = edad
        self.telefono = telefono
   def dato(self):
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
     mensaje = registro.datos()
     messagebox.showinfo("Datos Registrados", mensaje)
   except ValueError as e:
     messagebox.showwarning("error", "no se pudo completar el registro, porfavor intente de nuevo")


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
     mensaje = registro.datos()
     messagebox.showinfo("Datos Registrados", mensaje)
 except ValueError as e:
    messagebox.showwarning("error", str(e))

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
def registro_paciente():
    try:
     nombre=en_nombre.get()
     apellidop=en_apellidop.get()
     apellidom=en_apellidom.get()
     telefono=en_telefono.get()
     area=en_area.get()
     especialista=en_especialista.get()
     if not all([nombre, apellidop, apellidom, telefono, area]):
         raise ValueError("Todos los campos son obligatorios")
     nuevo_paciente=Pacientes(nombre, apellidop, apellidom, telefono, area, especialista, id_paciente=None)
     messagebox.showinfo("Paciente registrado",str(nuevo_paciente))
    except ValueError as e:
        messagebox.showerror("Error", str(e))

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
   global en_nombre, en_apellidom, en_apellidop, en_telefono, en_edad, en_cargo, en_sexo, id_paciente, en_area, en_especialista
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

ventana.mainloop()
