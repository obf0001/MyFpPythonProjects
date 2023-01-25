from tkinter import *
from tkinter import Label, Frame, Tk, ttk

class interfaz:
    def __init__(self):
        main = Tk()
        main.geometry("900x600+720+240")
        main.title("Base de Datos")
        #bg --> background #Frame--> bloques
        
        bloque1 = Frame(main, bg="black")
        
        titulo= Label(bloque1,text="Base de Datos",fg="black")
        titulo.pack(side="top")
        
        bloque1.pack(fill="both")
        
        bloque2 = Frame(main, bg="yellow")
        #Agregamos el numero de columnas
        #no incluimos la #0 por que ya se crea por defecto
        self.tabla = ttk.Treeview(bloque2, height=10, columns=('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8'))

        self.tabla.heading("#0", text="ID", anchor=CENTER,)#Centra el texto de l a cabecera
        self.tabla.heading("#1", text="Nombre", anchor=CENTER)
        self.tabla.heading("#2", text="Apellido1", anchor=CENTER)
        self.tabla.heading("#3", text="Apellido2", anchor=CENTER)
        self.tabla.heading("#4", text="Dni", anchor=CENTER)
        self.tabla.heading("#5", text="Fecha\nNacimiento", anchor=CENTER)
        self.tabla.heading("#6", text="Puesto\nTrabajo", anchor=CENTER)
        self.tabla.heading("#7", text="Sueldo", anchor=CENTER)
        self.tabla.heading("#8", text="Años\nAntiguedad", anchor=CENTER)

        self.tabla.column('#0', minwidth=20, width=70, anchor='center')
        self.tabla.column('#1', minwidth=20, width=70, anchor='center')
        self.tabla.column('#2', minwidth=20, width=70, anchor='center')
        self.tabla.column('#3', minwidth=20, width=70, anchor='center')
        self.tabla.column('#4', minwidth=20, width=70, anchor='center')
        self.tabla.column('#5', minwidth=20, width=70, anchor='center')
        self.tabla.column('#6', minwidth=20, width=70, anchor='center')
        self.tabla.column('#7', minwidth=20, width=70, anchor='center')
        self.tabla.column('#8', minwidth=20, width=70, anchor='center')

        self.tabla.pack(pady=20)
        
        bloque2.pack(fill="both")
        
        
        bloque3 = Frame(main, bg="black")
        entrada = ttk.Entry(bloque3)
        entrada.pack(anchor="center")
        bloque3.pack(fill="both", anchor= "center")
        main.mainloop()
        
interfaz()