#import pymysql
import MySQLdb



def getData(column, table):
    # Open database connection
    db = MySQLdb.connect("83.162.184.36","admin","geheim","customer_db" )
    #db = pymysql.connect("83.162.184.36","admin","geheim","customer_db" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # execute SQL query using execute() method.
    cursor.execute("select {} from {}".format(column, table))
    # Fetch a single row using fetchone() method.
    data = cursor.fetchall()
    return data
    # disconnect from server
    db.close()

def getDataWhere(column, table, where):
    # Open database connection
    db = MySQLdb.connect("83.162.184.36","admin","geheim","customer_db" )
    #db = pymysql.connect("83.162.184.36","admin","geheim","customer_db" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # execute SQL query using execute() method.
    cursor.execute("select {} from {} where {}".format(column, table, where))
    # Fetch a single row using fetchone() method.
    data = cursor.fetchall()
    return data
    # disconnect from server
    db.close()


def updateData(table, column, row):
    # Open database connection
    db = MySQLdb.connect("83.162.184.36","admin","geheim","customer_db" )
    #db = pymysql.connect("83.162.184.36","admin","geheim","customer_db" )
	
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # execute SQL query using execute() method.
    cursor.execute("update {} set {} where {}".format(table, column, row))
    db.commit()
    # disconnect from server
    db.close()

def insertData(table, values):
	# Open database connection
    db = MySQLdb.connect("83.162.184.36","admin","geheim","customer_db" )
    #db = pymysql.connect("83.162.184.36","admin","geheim","customer_db" )
	
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # execute SQL query using execute() method.
    cursor.execute("insert into {} values {}".format(table, values))
    db.commit()
    # disconnect from server
    db.close()

