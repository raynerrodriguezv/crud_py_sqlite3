from os import system
from unittest import result
from venv import create
from click import option
import paramiko
import conexion as conn
import time


db = conn.DB()
# result = db.ejecutar_consulta("SELECT * FROM sistema")
# print(result.fetchall())

def create():
    name = str(input("Ingrese su nombre: "))
    email = str(input("Ingrese su correo: "))
    if(len(name) > 0 and len(email)>0):
        sql_insert = "INSERT INTO sistema(name, email) VALUES(?,?)"
        parametros = (name, email)
        db.ejecutar_consulta(sql_insert,parametros)
        print("Insertados...")



def read():
    result = db.ejecutar_consulta("SELECT * FROM sistema")
    for data in result:
        print("""
        ID: {}
        NOMBRE: {}
        EMAIL : {}
        """.format(data[0], data[1], data[2]))

def update():
    id = int(input("Ingrese el ID: "))
    name = str(input("Ingrese su nombre: "))
    email = str(input("Ingrese su correo: "))
    if(id != 0):
        sql_update = "UPDATE sistema SET name=?, email=? WHERE id=?"
        parametros = (name, email, id)
        db.ejecutar_consulta(sql_update,parametros)
        print("Actualizado!")


def delete():
    id = int(input("Ingrese el ID: "))
    if (id != 0):
        sql_delete = "DELETE FROM sistema WHERE id=?"
        parametros = (id,)
        db.ejecutar_consulta(sql_delete, parametros)
        print("Eliminado!")


def search():
    name = str(input("Ingrese su nombre: "))
    if (len(name) > 0):
        sql_search = "SELECT * FROM sistema WHERE name LIKE ?"
        parametros = ('%{}%'.format(name),) #tupla
        result = db.ejecutar_consulta(sql_search, parametros)
        for data in result:
            print("""
            +ID:{}
            +NOMBRE:{}
            +EMAIL : {}
            
            """.format(data[0], data[1], data[2]))

while True:
    print("=================")
    print("\tCRUD PYTHON")
    print("=================")
    print("\t[1] Insertar registro")
    print("\t[2] Listar registro")
    print("\t[3] Actualizar registro")
    print("\t[4] Eliminar registro")
    print("\t[5] Buscar registros")
    print("\t[6] Salir")
    print("=================")


    try:
        option = int(input("Seleccionar una opcion: "))
        if(option == 1):
            create()
            time.sleep(1)
            system("clear")

        elif(option == 2):
            read()

        elif(option == 3):
            update()
            time.sleep(1)
            system("clear")

        elif(option == 4):
            delete()
            time.sleep(1)
            system("clear")

        elif(option == 5):
            search()

        elif(option == 6):
            break
    except:
        print("Error en elegir las opciones")
    
