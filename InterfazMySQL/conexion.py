# Registro de datos en MySQL desde una GUI en TkInter
# @autor: Oday

import mysql.connector  # pip install mysql-connector-python


class Registro_datos():
#Constructor que se crea siempre
    def __init__(self):
        self.conexion = mysql.connector.connect(host='localhost',
                                                database='mydb',
                                                user='root',
                                                password='admin')
#Funcion insertar producto en la que ejecutamos un codigo sql
#self se pone siempre en todas las funciones
    def insertar_empleados(self, ID,Nombre,Apellido1,Apellido2,Dni,Fecha_Nacimiento,Puesto,Sueldo,Anios):
        cur = self.conexion.cursor() #la clase cursor sirve para manejar la base de datos y poder hacer lo que queramos
        #Escribimos el codigo sql que queremos ejecutar
        #Ejemplo .format() --> txt3 = "My name is {}, I'm {}".format("John",36)
        sql = '''INSERT INTO empleados (ID, Nombre, Apellido1, Apellido2, Dni, Fecha_Nacimiento, Puesto, Sueldo, Anios) 
        VALUES('{}', '{}','{}', '{}','{}','{}','{}','{}','{}')'''.format(ID,Nombre,Apellido1,Apellido2, Dni,Fecha_Nacimiento,Puesto,Sueldo,Anios)
        cur.execute(sql) #Ejecutamos la linea de codigo sql
        self.conexion.commit() #Guardamos los cambios
        cur.close() #Cerramos para que se ejecute y no de error
#Funcion de mostrar los productos
    def mostrar_empleados(self):
        cursor = self.conexion.cursor()
        #Selecciona todo de empleados
        sql = "SELECT * FROM empleados "
        cursor.execute(sql)
        registro = cursor.fetchall() #fetch-all sirve para recoger todos los datos y los guardamos en registro
        return registro #devolvemos los datos recogidos
#Funcion de buscar algo en concreto
    def buscar_empleado(self, nombre_empleado):
        cur = self.conexion.cursor()
        #Selecciona todo de empleados donde nombre = nombre que pongamos
        sql = "SELECT * FROM empleados WHERE Nombre = {}".format(nombre_empleado)
        cur.execute(sql)
        nombreX = cur.fetchall()
        cur.close() #Cerramos para que se ejecute y no de error
        return nombreX #devolvemos los datos recogidos
#Funcion para borrar fila de datos de la tabla
    def eliminar_empleado(self, id):
        cur = self.conexion.cursor()
        # Borra de empleados donde nombre = nombre que pongamos
        sql = '''DELETE FROM empleados WHERE ID = {}'''.format(id)
        cur.execute(sql)
        self.conexion.commit()
        cur.close()
