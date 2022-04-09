import datetime, time
from os import system
import sqlite3 as sql
import pandas as pd
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
    
    conn = sql.connect("database.db")
    cursor = conn.cursor()
    insert_query = f"INSERT INTO inventario VALUES (?,?,?,?,?,?)"


    codigo = int(input("Ingrese el codigo del articulo: "))
    ubicacion  = input("Ubicacion del articulo: ").lower
    descripcion = input("Descripcion: ").lower
    unidad = input("Unidad del articulo: ").lower
    tipo = input("Tipo de articulo: ").lower
    disponibilidad = input("Disponibilidad: ").lower



    articuloList = [codigo, ubicacion , descripcion , unidad, tipo, disponibilidad]
    


    cursor.executemany(insert_query, articuloList)
    print(articuloList)

    # insertRows(articuloList=articulos)  

    conn.commit()
    conn.close()


def view_inventario():
    conn = sql.connect("database.db")
    cursor = conn.cursor()
    read_query = f"SELECT * FROM inventario"
    cursor.execute(read_query)
    cursor.fetchall() # datos =
    df = pd.read_sql_query("SELECT * FROM inventario", conn)
    print(df)
    conn.commit()
    conn.close()
        

def search_items():
    conn = sql.connect("database.db")
    cursor = conn.cursor()
    producto = input("Nombre del producto a buscar: ")
    search_query = f"SELECT * FROM inventario WHERE descripcion like '{producto}%'"
    cursor.execute(search_query)
    cursor.fetchall() # datos = 
    df = pd.read_sql_query(search_query, conn)
    print(df)
    conn.commit()
    conn.close()


def deleteRow():
    conn = sql.connect("database.db")
    cursor = conn.cursor()
    cod_items = input("Ingrese el codigo del items: ")
    delete_query = f"DELETE FROM inventario WHERE codigo={cod_items}"
    cursor.execute(delete_query)    
    conn.commit()
    conn.close()
    

def updateFields():
    conn = sql.connect("database.db")
    cursor = conn.cursor()
    updated_codigo = int(input("Codigo de producto: ")) 
    update_ubicacion  = input("Ubicacion del articulo: ").lower
    update_descripcion = input("Descripcion: ").lower
    update_unidad = input("Unidad del articulo: ").lower
    update_tipo = input("Tipo de articulo: ").lower
    update_disponibilidad = input("Disponibilidad: ").lower

    update_query = f"""UPDATE inventario SET codigo='{updated_codigo}', ubicacion = '{update_ubicacion}', descripcion='{update_descripcion}', 
     unidad='{update_unidad}', tipo='{update_tipo}', disponibilidad ='{update_disponibilidad}'  WHERE codigo={updated_codigo}"""
    
    cursor.execute(update_query)    
    conn.commit()
    conn.close()


    
if __name__ == '__main__': 
    
    
    if os.path.exists('./database.db') == True:
        print("Base de datos creada...")
    else:
        createBD_createTable()
        

    while True:
        print("-------- Inventario del   ---------\n")
        print("\t[1] Visualizar inventario  ") # done
        print("\t[2] Agregar Articulo ")    
        print("\t[3] Modificar inventario del supermercado ")
        print("\t[4] Borrar articulo x codigo ") #done
        print("\t[5] Buscar en inventario x producto") # done
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
                insertRows(articuloList=articulos)

            elif(option == 3):
                updateFields()
                time.sleep(1)
                system("clear")

            elif(option == 4):
                deleteRow()
                print("Eliminando Registro... ")
                time.sleep(2)
                system("clear")

            elif(option == 5):
                search_items()

            elif(option == 7):
                break
        except:
            print("Error en elegir las opciones")
        

    