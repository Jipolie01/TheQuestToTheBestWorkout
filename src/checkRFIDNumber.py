import accessMySQL as accDb

data = accDb.getData('RFIDNumber', 'customerInfo')

def checkRFID():
    for RFIDNumber in data:
        RFIDNumber = (str(RFIDNumber).replace('(', '').replace(')', '').replace('\'','').replace('[', '')
                      .replace(']', '')[:-1])
        RFIDNumber = [int(s) for s in RFIDNumber.split(',')]
        if RFIDNumber==[12,235,179,213,129]:
            return True
        else: return False

def printSucces():
    succes = checkRFID()
    if succes==True:
        print(succes)
    else: print(succes)

printSucces()