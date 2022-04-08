import datetime, time
from os import system
import sqlite3 as sql
import os



def createBD_createTable():
    conn = sql.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE inventario (
            codigo integer,
            ubicacion text,
            descripcion text,
            unidad text,
            tipo text,
            disponibilidad text
        )       
        """
    )
    conn.commit()
    conn.close()


def insertRows(articuloList):
    global articulos
    conn = sql.connect("database.db")
    cursor = conn.cursor()
    insert_query = f"INSERT INTO inventario VALUES (?,?,?,?,?,?)"
    cursor.executemany(insert_query, articuloList)
    conn.commit()
    conn.close()


def view_inventario():
    conn = sql.connect("database.db")
    cursor = conn.cursor()
    read_query = f"SELECT * FROM inventario"
    cursor.execute(read_query)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)


def add_items():
    # ingreso de datos
    global articulos
    codigo = int(input("Ingrese el codigo del articulo: "))
    ubicacion  = input("Ubicacion del articulo: ")
    descripcion = input("Descripcion: ")
    unidad = input("Unidad del articulo: ")
    tipo = input("Tipo de articulo: ")
    disponibilidad = input("Disponibilidad: ")

    # articulos[codigo] = ubicacion, descripcion, unidad, tipo, disponibilidad
    # print(articulos)
    # # articulos = {}

    insertRows(articuloList=articulos)    

articulos = {}

if __name__ == '__main__': 
    
    
    if os.path.exists('./database.db') == True:
        print("Base de datos creada...")
    else:
        createBD_createTable()
        

    while True:
        print("-------- Inventario del   ---------\n")
        print("\t[1] Visualizar inventario  ")
        print("\t[2] Agregar Articulo ")    
        print("\t[3] Modificar inventario del supermercado ")
        print("\t[4] Borrar articulo x codigo ")
        print("\t[5] Buscar en inventario x producto")
        print("\t[6] Inventario Total")
        print("\t[7] Salir ")

        try:
            option = int(input("Seleccionar una opcion: "))
            if(option == 1):                
                view_inventario()
                # time.sleep(1)
                # system("clear")

            elif(option == 2):
                print("dentro de la opcion 2")
                add_items()

            # elif(option == 3):
            #     update_items()
            #     time.sleep(1)
            #     system("clear")

            # elif(option == 4):
            #     delete_items()
            #     time.sleep(1)
            #     system("clear")

            # elif(option == 5):
            #     search_items()

            elif(option == 7):
                break
        except:
            print("Error en elegir las opciones")
        

    