import mysql.connector


db = mysql.connector.connect(
    host="localhost",  
    user="root",  
    password="12345678",  
    database="FINANCE"  
)


cursor = db.cursor()

add_record = ("INSERT INTO RECORDS (TYPE, QUANTITY, ORIGIN) VALUES (%s, %s, %s)")

switch = True
while switch:
    txt = """
    Bienvenido tu sistema de finanzas Eduardo!
    __________________________________________
    1. Registrar un ingreso.
    2. Registrar un ahorro.
    3. Regisrar un gasto.
    4. Ver balance actual.
    5. Ver registros.
    __________________________________________
"""
    print(txt)
    type = int(input("Elige una opción: "))
    if type == 1:
        cantidad = int(input("Cantidad: "))
        origen = input("Origen de tu ingreso?: ")
        data = ("ingreso", cantidad, origen)
        cursor.execute(add_record, data)
    elif type == 2: 
        cantidad = int(input("Cantidad: "))
        origen = input("A dónde se dirige tu ahorro?: | NU | CETES | :").lower()
        data = ("ahorro", cantidad, origen)
        cursor.execute(add_record, data)
    elif type == 3: 
        cantidad = int(input("Cantidad: "))
        origen = input("En que gastaste?: ")
        data = ("gasto", cantidad, origen)
        cursor.execute(add_record, data)
    elif type == 4:
        print("___________________Balance__________________")
        table = "ACTUAL_BALANCE"
        cursor.execute(f"SELECT CURRENT, SAVINGS, SPENT FROM {table}")
        for row in cursor:
            current, saving, spent = row
            print(f"Dinero actual: {current}")
            print(f"Ahorros: {saving}")
            print(f"Gastos: {spent}")
    elif type == 5:
        print("___________________Registros_________________")
        table = "RECORDS"
        cursor.execute(f"SELECT TYPE, QUANTITY, DATE FROM {table}")
        for row in cursor:
            type, quantity, date = row
            print(f"Tipo de reggistro: {type}")
            print(f"Cantidad: {quantity}")
            print(f"Fecha: {date}")
    else:
        print("Elige una opción correcta. xd")

    db.commit()

    cont = input("Quieres agregar otro registro?  Si | No: ").lower()
    if cont == "no":
        print("___________________Adiós__________________")
        table = "ACTUAL_BALANCE"
        cursor.execute(f"SELECT CURRENT, SAVINGS, SPENT FROM {table}")
        for row in cursor:
            current, saving, spent = row
            print(f"Dinero actual: {current}")
            print(f"Ahorros: {saving}")
            print(f"Gastos: {spent}")
        switch = False


# Cerrar la conexión
cursor.close()
db.close()
