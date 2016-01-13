import sqlite3

conn = sqlite3.connect('sql/clientDatabase.db')
c = conn.cursor()

rows = []

def readData(column):
    for row in c.execute("SELECT " +column+ " FROM clientInfo"):
        rowN = (str(row).replace(')', '').replace('(','').replace("'", "").replace(',',''))
        rows.append(rowN)
    print(rows)

readData("surname")
