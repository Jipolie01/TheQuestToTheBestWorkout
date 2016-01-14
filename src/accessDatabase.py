import sqlite3
from time import localtime, strftime
import calorieCounter.SportschoolTest.Rowing_Machine as RM


"""opens the client database and sets a cursor in the file"""
conn = sqlite3.connect('sql/clientDatabase.db')
c = conn.cursor()

"""makes and empty list"""
rows = []

"""Selects a column from the client database and removes brackets and quotation marks."""
def readData(table, column):
    for row in c.execute("SELECT " +column+ " FROM " +table):
        rowN = (str(row).replace(')', '').replace('(','').replace("'", ""))
        rowN = rowN[:-1]
        rows.append(rowN)

"""Check if an item is in de database and returns true or false based on that.
Give the table, the column and the item as string like this: checkExistence('table', 'column', 'item')."""
def checkExistence(table, column, item):
    readData(table, column)
    if item in rows:
        return True
    else: return False

"""
table name:  | column's:
clientInfo   = "(rfidNumber, surname, name, gender, cellphoneNumber, adresNumber, zipcode, subscriptionName)"
subscription = "(subscriptionName, price)"
adresInfo    = "(adresNumber, zipcode, street, town, country)"
logInfo      = "(rfidNumber, username, password, email)"
"""

"""You can add a a row of data with the addData(table, column, value) function.
First define the table you want the add to. Second the column's and lastly the value('s) for the rows."""
def addData(table, column, value):
    if table == 'clientInfo' or table == 'subscription' or table == 'adresInfo'or table == 'logInfo' or table == 'caloriesInfo':
        c.execute("INSERT INTO "+table+" "+column+" VALUES "+value)
    else: print('ERROR table not found!')
    conn.commit()

RM.main()
#print(test.sportTime)

localTime = (strftime("%d %b %Y %H:%M:%S", localtime()))
dateEnd = (strftime("%d %b %Y %H"++":%M:%S", localtime()))
addData('caloriesInfo', '(clientID, date, machine, calories)', '(1, \''+localTime+'\', \'loopband\',300)')
