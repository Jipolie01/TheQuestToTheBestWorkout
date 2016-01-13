import sqlite3
"""opens the client database and sets a cursor in the file"""
conn = sqlite3.connect('sql/clientDatabase.db')
c = conn.cursor()


"""makes and empty list"""
rows = []

"""Selects a column from the client database and removes brackets and quotation marks."""
def readData(column):
    for row in c.execute("SELECT " +column+ " FROM clientInfo"):
        rowN = (str(row).replace(')', '').replace('(','').replace("'", ""))
        rowN = rowN[:-1]
        rows.append(rowN)

"""Checks if an item is in de rows list and returns true or false based on that."""
def checkAccess(column, item):
    readData(column)
    if item in rows:
        return True
    else: return False

"""Check if an item is in de database. Give the column where the item as string then, the item as string.
Example: checkAccess('name', 'Katrien')
This will return True"""
checkAccess('rfidNumber', '[52,188,189,222,235]')