#importamos librería pymongo
import pymongo

#Creamos la conexión a mongodb
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

#Creamos la base de datos mydatabase
mydb = myclient["videojuegos"]

#Mostramos un listado de las bases de datos
print(myclient.list_database_names())

#Comprobamos que nuestra base de datos está en el listado de bd
dblist = myclient.list_database_names()
if "videojuegos" in dblist:
  print("La base de datos existe")


#Creamos una colección customers
#No lo meto una una funcion ya que necesitarias devolverlo(return) y crear variables en otras funciones
mycol = mydb["MMO"]


def ComprobarColeccion():
    #Comprobar que existe la colección
    print(mydb.list_collection_names())
    collist = mydb.list_collection_names()
    if "MMO" in collist:
      print("La colección existe")

#Trabajamos con la colección
def InsertarDatos():
    #Inserción de documentos en la colección 
    mydict = { "ID": 1, "Nombre": "World of Warcraft", "Desarrolador": "Blizzard Entertainment", "Editor": "Blizzard Entertainment", "Fecha_Lanzamiento": "03/05/2004" }
    x = mycol.insert_one(mydict)
    #inserted_id devuelve el identificador del documento insertado
    print(x.inserted_id)
    print("insertamos World of Warcraft")
    #Insertamos otro documento
    mydict = { "ID": 2, "Nombre": "Black Dessert Online", "Desarrolador": "Pearl Abyss", "Editor": "Pearl Abyss", "Fecha_Lanzamiento": "04/05/2014" }
    x = mycol.insert_one(mydict)
    print(x.inserted_id)
    print("insertamos Black Dessert Online")
    #Inserción de varios documentos
    mylist = [
    { "ID": 3, "Nombre": "New World", "Desarrolador": "Amazon Games", "Editor": "Amazon Games", "Fecha_Lanzamiento": "04/05/2021"},
    { "ID": 4, "Nombre": "Lost Ark", "Desarrolador": "Amazon Games", "Editor": "Amazon Games", "Fecha_Lanzamiento": "04/05/2019"},
    ]

    x = mycol.insert_many(mylist)

    #Imprime los ids de los documentos insertados
    print(x.inserted_ids)
    print("insertamos varios objetos en la colección")

def Find():  
    #Método Find
    #Encuentra el primer documento en la colección customers
    x = mycol.find_one()
    print(x)
    print("Busca el primero")
    #Devuelve todos los documentos de la colección
    for x in mycol.find():
        print(x)
    print("Devuelve todos")


#Devuelve algunos documentos de la colección
#for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
#  print(x)
#No se puede especificar valores 0 y 1 en el mismo objeto (solo _id puede ser 0)  
#for x in mycol.find({},{ "name": 1, "address": 0 }):
#  print(x)

def FiltrarNombre(nombre):
    #Filtrar la búsqueda. Filtrar por Nombre New World
    myquery = { "Nombre": nombre }
    mydoc = mycol.find(myquery)
    for x in mydoc:
      print(x)
    print("filtra busqueda")

def FiltrarAvanzado():
    #Filtrar consultas avanzadas. Direcciones mayores que "S" 
    myquery = { "ID": { "$gt": 1 } }
    mydoc = mycol.find(myquery)
    for x in mydoc:
      print(x)
    print("consulta avanzada")

def OrdenarNombre():
    #Ordenar el resultado. Utilizamos sort(nombre_campo) 1 asc -1 desc
    #Ordenamos la colección por el campo nombre
    mydoc = mycol.find().sort("Nombre",1)
    for x in mydoc:
        print(x)
    print("consulta ordenada por nombre")

def ActualizarNombre(nombreDoc, nuevoNom):
    #Actualizar doucmentos de una colección. update_one/update_many
    #Actualiza un documento
    myquery = { "Nombre": nombreDoc }
    newvalues = { "$set": { "Nombre": nuevoNom } }
    mycol.update_one(myquery, newvalues)

def ImprimirColeccion():
    #Imprime los clientes después de actualizar:
    for x in mycol.find():
        print(x)

def BorrarDoc(id):
    #Eliminar documentos. Eliminar documento cuya ID sea 2
    myquery = { "ID": id }
    mycol.delete_one(myquery)
    print("eliminar ID ", id)

def BorrarTodosDoc():
    #Eliminar todos los documentos
    x = mycol.delete_many({})
    print(x.deleted_count, " documentos eliminados.")

def BorrarColeccion():
    #Borrar colección
    mycol.drop()
    print("borra colección")


#ComprobarColeccion()
#InsertarDatos()
#Find()
#FiltrarNombre("Elden Ring")
#FiltrarAvanzado()
#OrdenarNombre()
#ActualizarNombre("World of Warcraft", "Warcraft")
#ImprimirColeccion()
#BorrarDoc(1)
#BorrarTodosDoc()
#BorrarColeccion()