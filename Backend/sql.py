import datetime
import mysql.connector

__cnx = None

def get_sql():
    print("Connecting to Database.")
    global __cnx

    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='Bubblers56?!?', database='grocery_store')

        return __cnx