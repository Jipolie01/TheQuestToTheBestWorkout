__author__ = 'TimIJntema'
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
    sql = ("select {} from {} where {}".format(column, table, where))
    # execute SQL query using execute() method.
    #print(sql)
    cursor.execute(sql)
    # Fetch a single row using fetchone() method.
    data = cursor.fetchall()
    # disconnect from server
    db.close()
    return data


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

def insertInto(table, column, values):
    # Open database connection
    db = MySQLdb.connect("83.162.184.36","admin","geheim","customer_db" )
    #db = pymysql.connect("83.162.184.36","admin","geheim","customer_db" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    cursor.execute("SET FOREIGN_KEY_CHECKS=0")
    sql = ("INSERT INTO {} ({}) VALUES ({})".format(table, column, values))
    # execute SQL query using execute() method.
    cursor.execute(sql)
    db.commit()
    cursor.execute("SET FOREIGN_KEY_CHECKS=1")
    
    # disconnect from server
    db.close()

def insertData(table, values):
	# Open database connection
    db = MySQLdb.connect("83.162.184.36","admin","geheim","customer_db" )
    #db = pymysql.connect("83.162.184.36","admin","geheim","customer_db" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    sql = ("insert into {} values ({})".format(table, values))
    #print(sql)
    # execute SQL query using execute() method.
    cursor.execute(sql)
    db.commit()
    # disconnect from server
    db.close()
