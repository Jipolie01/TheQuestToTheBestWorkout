import mysql.connector as sql
from mysql.connector import errorcode

try:
    cnx = sql.connect(user='maarten', password='maartenmn',
                      host = 'bennos-sportschool.adeklerk.nl',
                      database = 'maarten')

except sql.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cnx.close()