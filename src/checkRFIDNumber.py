import accessMySQL as accDb

data = accDb.getData('RFIDNumber', 'customerInfo')

def checkRFID():
    for RFIDNumber in data:
        print(RFIDNumber[0])
        # RFIDNumber = (str(RFIDNumber).replace('(', '').replace(')', '').replace('\'','').replace('[', '')
        #               .replace(']', '')[:-1])
        # RFIDNumber = [int(s) for s in RFIDNumber.split(',')]
        if RFIDNumber[0]=='[52,188,189,222,235]':
            return True
        else: return False

def printSucces():
    succes = checkRFID()
    if succes==True:
        print(succes)
    else: print(succes)

printSucces()