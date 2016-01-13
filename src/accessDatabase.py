import sqlite3

conn = sqlite3.connect('sql/clientDatabase.db')
c = conn.cursor()

rows = []

def readData(column):
    for row in c.execute("SELECT " +column+ " FROM clientInfo"):
        rowN = (str(row).replace(')', '').replace('(','').replace("'", ""))
        rowN = rowN[:-1]
        rows.append(rowN)

def checkAccess(column, item):
    readData(column)
    if item in rows:
        return True
    else: return False

"""Check if an item is in de database. Give the column where the item as string then, the item as string.
Example: checkAccess('name', 'Katrien')
This will return True"""
checkAccess('rfidNumber', '[52,188,189,222,235]')