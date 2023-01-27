# Registro de datos en MySQL desde una GUI en TkInter
# @autor: Oday y Creditos de Magno Efren
# Youtube: https://www.youtube.com/c/MagnoEfren

from tkinter import Entry, Label, Frame, Tk, Button, ttk, Scrollbar, VERTICAL, HORIZONTAL, StringVar, END, IntVar, messagebox
from conexion import *

# Frame son contenedores donde meter lo que queramos, la ventana principal es un Frame grande
class Registro(Frame): #Hereda de Frame
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
#Master es la ventana principal
        self.frame1 = Frame(master)#Frame del texto del titulo
        self.frame1.grid(columnspan=2, column=0, row=0) #columspan --> expande la columna hasta 2 huecos(es decir en este caso desde columna 0 hasta la 2)
        self.frame2 = Frame(master, bg='gray') #bg = background/fondo
        self.frame2.grid(column=0, row=1) #grid se usa para el tamanio de los contenedores
        self.frame3 = Frame(master) #Frame3 es donde se muestran los datos de la base de datos
        self.frame3.grid(rowspan=2, column=1, row=1)

        self.frame4 = Frame(master, bg='gray') #Frame de control
        self.frame4.grid(column=0, row=2)

        self.ID = IntVar() 
        self.ID.set('') #Vaciamos ya que el IntVar() por defecto pone 0
        self.Nombre = StringVar() #The Tkinter StringVar helps you manage the value of a widget such as a Label or Entry more effectively.
        self.Apellido1 = StringVar() #StringVar() --> Son String para interfaces
        self.Apellido2 = StringVar()
        self.Dni = StringVar()
        self.Fecha_Nacimiento = StringVar()
        self.Puesto = StringVar()
        self.Sueldo = IntVar()
        self.Sueldo.set('')
        self.Anios = StringVar()
        self.buscar = StringVar()

        self.base_datos = Registro_datos() #Igualamos la variable base_datos a la clase de conexion.py
        self.create_wietgs() #Llama al metodo

    def create_wietgs(self): #Metodo para crear los labels botones etc
# -------Frame 1 --------
        Label(self.frame1, text='\tR E G I S T R O \t D E \t D A T O S \t O D A Y', bg='gray', fg='white', #Label en el frame1 con texto fondo gris forefround blanco
              font=('Orbitron', 15, 'bold')).grid(column=0, row=0) #Fuente Orbitron tamanio 15 bold --> en negrita, columa 0 fila 0
        #Tambien se puede usar pack() para posicionar, pack(tk.LEFT) etc.
# -------Frame 2 --------
        Label(self.frame2, text='Agregar Nuevos Datos', fg='white', bg='gray2', font=('Rockwell', 12, 'bold')).grid(
            columnspan=2, column=0, row=0, pady=5) #pady es el margen que tienen eje y entre objetos en este caso de tamanio 5,
            #Tambien se puede hace padyleft o right etc.
        Label(self.frame2, text='ID', fg='white', bg='gray', font=('Rockwell', 13, 'bold')).grid(column=0, row=1,pady=2) #cada uno debe estar en su propia fila pero todos en la misma columna
        Label(self.frame2, text='Nombre', fg='white', bg='gray', font=('Rockwell', 13, 'bold')).grid(column=0, row=2,pady=2)
        Label(self.frame2, text='Apellido1', fg='white', bg='gray', font=('Rockwell', 13, 'bold')).grid(column=0, row=3,pady=2)
        Label(self.frame2, text='Apellido2', fg='white', bg='gray', font=('Rockwell', 13, 'bold')).grid(column=0, row=4, pady=2)
        Label(self.frame2, text='Dni', fg='white', bg='gray', font=('Rockwell', 13, 'bold')).grid(column=0, row=5, pady=2)
        Label(self.frame2, text='Fecha_Nacimiento', fg='white', bg='gray', font=('Rockwell', 13, 'bold')).grid(column=0, row=6, pady=2)
        Label(self.frame2, text='Puesto', fg='white', bg='gray', font=('Rockwell', 13, 'bold')).grid(column=0, row=7, pady=2)
        Label(self.frame2, text='Sueldo', fg='white', bg='gray', font=('Rockwell', 13, 'bold')).grid(column=0, row=8, pady=2)
        Label(self.frame2, text='Anios', fg='white', bg='gray', font=('Rockwell', 13, 'bold')).grid(column=0, row=9, pady=2)

        Entry(self.frame2, textvariable=self.ID, font=('Arial', 12)).grid(column=1, row=1, padx=5) #Entradas de texto que rellenara el usuario
        Entry(self.frame2, textvariable=self.Nombre, font=('Arial', 12)).grid(column=1, row=2) #Para ponerlo a la derecha del texto anterior lo ponemos en columna 1
        Entry(self.frame2, textvariable=self.Apellido1, font=('Arial', 12)).grid(column=1, row=3)
        Entry(self.frame2, textvariable=self.Apellido2, font=('Arial', 12)).grid(column=1, row=4)
        Entry(self.frame2, textvariable=self.Dni, font=('Arial', 12)).grid(column=1, row=5)
        Entry(self.frame2, textvariable=self.Fecha_Nacimiento, font=('Arial', 12)).grid(column=1, row=6)
        Entry(self.frame2, textvariable=self.Puesto, font=('Arial', 12)).grid(column=1, row=7)
        Entry(self.frame2, textvariable=self.Sueldo, font=('Arial', 12)).grid(column=1, row=8)
        Entry(self.frame2, textvariable=self.Anios, font=('Arial', 12)).grid(column=1, row=9)
#-------Frame 4 --------
        Label(self.frame4, text='CONTROL', fg='white', bg='gray2', font=('Rockwell', 12, 'bold')).grid(columnspan=3, column=0, row=0, pady=1, padx=4) #padx --> margen de espacio en el eje x <-- -->
        Button(self.frame4, command=self.agregar_datos, text='REGISTRAR', font=('Arial', 10, 'bold'), #pady margen de espacio en el eje y
               bg='gray').grid(column=0, row=1, pady=10, padx=4) #Boton con texto registrar, luego le aniadiremos funcionalidad
        Button(self.frame4, command=self.limpiar_datos, text='LIMPIAR', font=('Arial', 10, 'bold'),
               bg='gray').grid(column=1, row=1, padx=10)
        Button(self.frame4, command=self.eliminar_fila, text='ELIMINAR', font=('Arial', 10, 'bold'), bg='gray').grid(
            column=2, row=1, padx=4)
        Button(self.frame4, command=self.buscar_nombre, text='BUSCAR POR NOMBRE', font=('Arial', 8, 'bold'), #command se usa para llamar al metodo
               bg='gray').grid(columnspan=2, column=1, row=2)
        Entry(self.frame4, textvariable=self.buscar, font=('Arial', 12), width=10).grid(column=0, row=2, pady=1, padx=8)
        Button(self.frame4, command=self.mostrar_todo, text='MOSTRAR DATOS DE MYSQL', font=('Arial', 10, 'bold'),
               bg='gray').grid(columnspan=3, column=0, row=3, pady=8)
#-------Frame 3 --------
        self.tabla = ttk.Treeview(self.frame3, height=21) #Treeview es para crear tablas
        self.tabla.grid(column=0, row=0) #tamanio de la tabla

        ladox = Scrollbar(self.frame3, orient=HORIZONTAL, command=self.tabla.xview) #Barra de desplazamiento en el lado x
        ladox.grid(column=0, row=1, sticky='ew')
        ladoy = Scrollbar(self.frame3, orient=VERTICAL, command=self.tabla.yview) #Barra de desplazamiento en el lado y
        ladoy.grid(column=1, row=0, sticky='ns')

        self.tabla.configure(xscrollcommand=ladox.set, yscrollcommand=ladoy.set) #Aniadimos las barras

        self.tabla['columns'] = ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8') #Elegimos que columnas queremos

        self.tabla.column('#0', minwidth=50, width=60, anchor='center') #La #0 es la predeterminada y siempre se crea
        self.tabla.column('#1', minwidth=50, width=60, anchor='center') #minwidth minima anchura
        self.tabla.column('#2', minwidth=50, width=60, anchor='center')
        self.tabla.column('#3', minwidth=50, width=60, anchor='center')
        self.tabla.column('#4', minwidth=50, width=60, anchor='center')
        self.tabla.column('#5', minwidth=50, width=60, anchor='center')
        self.tabla.column('#6', minwidth=50, width=60, anchor='center')
        self.tabla.column('#7', minwidth=50, width=60, anchor='center')
        self.tabla.column('#8', minwidth=50, width=60, anchor='center')

        self.tabla.heading('#0', text='ID', anchor='center') #Le ponemos el texto que queramos y lo centramos
        self.tabla.heading('#1', text='Nombre', anchor='center') #Le asignamos para que columna es, en este caso #1
        self.tabla.heading('#2', text='Apellido1', anchor='center')
        self.tabla.heading('#3', text='Apellido2', anchor='center')
        self.tabla.heading('#4', text='Dni', anchor='center')
        self.tabla.heading('#5', text='Fecha_Nacimiento', anchor='center')
        self.tabla.heading('#6', text='Puesto', anchor='center')
        self.tabla.heading('#7', text='Sueldo', anchor='center')
        self.tabla.heading('#8', text='Anios', anchor='center')

        estilo = ttk.Style(self.frame3) #le aniadimos el estilo al frame3
        estilo.theme_use('alt')  # ('clam', 'alt', 'default', 'classic') tema a usar
        estilo.configure(".", font=('Helvetica', 12, 'bold'), foreground='red2')
        estilo.configure("Treeview", font=('Helvetica', 10, 'bold'), foreground='black', background='white')
        estilo.map('Treeview', background=[('selected', 'gray')], foreground=[('selected', 'black')]) #Cambiamos el fondo cuando seleccionamos una opcion

        self.tabla.bind("<<TreeviewSelect>>", self.obtener_fila)  # seleccionar  fila

    def agregar_datos(self):
        try:
            self.tabla.get_children()
            id = self.ID.get()
            nombre = self.Nombre.get()
            apellido1 = self.Apellido1.get()
            apellido2 = self.Apellido2.get()
            dni = self.Dni.get()
            fecha_nacimiento = self.Fecha_Nacimiento.get()
            puesto = self.Puesto.get()
            sueldo = self.Sueldo.get()
            anios = self.Anios.get()

            datos = (nombre, apellido1, apellido2, dni, fecha_nacimiento, puesto, sueldo, anios)
            if id and nombre and apellido1 and apellido2 and dni and fecha_nacimiento and puesto and sueldo and anios != '':
                self.base_datos.insertar_empleados(id, nombre, apellido1, apellido2, dni, fecha_nacimiento, puesto, sueldo, anios) #Funcion de conexion.py
                self.tabla.insert('', 0, text=id, values=datos)
                #Vaciamos las cajas de texto una vez usadas
                self.ID.set('')
                self.Nombre.set('')
                self.Apellido1.set('')
                self.Apellido2.set('')
                self.Dni.set('')
                self.Fecha_Nacimiento.set('')
                self.Puesto.set('')
                self.Sueldo.set('')
                self.Anios.set('')
        except mysql.connector.errors.IntegrityError: #Error que me salio al poner una id que ya exisitia, lo controlo con el try except
            mensaje = messagebox.showinfo("Cuidado", "La id introducida ya existe") #muestro un mensajito de error
            
    def limpiar_datos(self):
        self.tabla.delete(*self.tabla.get_children()) #set es para darle un valor en este caso vacio para borrarlo
        self.ID.set('')
        self.Nombre.set('')
        self.Apellido1.set('')
        self.Apellido2.set('')
        self.Dni.set('')
        self.Fecha_Nacimiento.set('')
        self.Puesto.set('')
        self.Sueldo.set('')
        self.Anios.set('')

    def buscar_nombre(self):
        nombre_empleado = self.buscar.get()
        nombre_empleado = str("'" + nombre_empleado + "'")
        nombre_buscado = self.base_datos.buscar_empleado(nombre_empleado) #nombre_buscado se convierte en una matriz ya que el metodo recoge todos los datos de una tabla bidimensional
        self.tabla.delete(self.tabla.get_children()) #borramos la tabla para mostrar solo lo buscado
        i = -1
        for dato in nombre_buscado:
            i = i + 1
            self.tabla.insert('', i, text=nombre_buscado[i][0:1], values=nombre_buscado[i][1:9]) #('',id,mete en la fila i los datos 1 y 2 y luego los de 2 a 9)

    def mostrar_todo(self):
        self.tabla.delete(*self.tabla.get_children())
        registro = self.base_datos.mostrar_empleados()
        i = -1
        for dato in registro: #text por alguna razon se refiere a la primera columna de la tabla, y values todas las demas, en nuestro caso text seria ID
            i = i + 1
            self.tabla.insert('', i, text=registro[i][0:1], values=registro[i][1:9]) #text [0 a 1] por que es la primera solo y values de [1 a 9] para las columnas restantes

    def eliminar_fila(self):
        print("Nombre a borrar antes --------------->",self.id_borrar)
        fila = self.tabla.selection()
        if len(fila) !=0:        
            self.tabla.delete(fila)
            nombre = ("'"+ str(self.id_borrar) + "'")
            self.base_datos.eliminar_empleado(nombre)

    def obtener_fila(self, event):
        current_item = self.tabla.focus()
        if not current_item:
            return
        data = self.tabla.item(current_item)
        self.id_borrar = data['text'][0] #text por alguna razon se refiere a la primera columna de la tabla, y values todas las demas, en nuestro caso text seria ID


def main():
    ventana = Tk() #creamos el objeto
    ventana.wm_title("Registro de Datos en MySQL") #titulo
    ventana.config(bg='gray') #color de fondo
    ventana.geometry('880x500') #tamanio de la ventana
    ventana.resizable(0, 0) #que no se pueda ajustar el tamanio por el usuario
    app = Registro(ventana) #aniadimos la ventana (Frame) a la clase registro que hemos creado y la igualamos a una variable llamada app
    app.mainloop() #abrimos la ventana


if __name__ == "__main__":
    main()
