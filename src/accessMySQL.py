import mysql.connector as sql
from mysql.connector import errorcode
import getpass

def connectDatabase():
    #p = getpass.getpass("Enter password: ")

    try:
        global cnx
        cnx = sql.connect(user='admin', password='geheim',
                          host = 'bennos-sportschool.adeklerk.nl',
                          database = 'customer_db')

    except sql.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        print("connected to database")


def getData(column ,table):
    connectDatabase()
    global cursor
    cursor = cnx.cursor(buffered=True)

    query = (
        "SELECT {} FROM {}".format(column, table)
    )

    cursor.execute(query)

    return cursor

    disconnectDatabase()

def disconnectDatabase():
    cursor.close()
    cnx.close()