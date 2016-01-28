# This file is used for the weightlifting
from Tkinter import *
import time
import getData as gD

start = ""
sportTime = ""


def main(customerID):
    """
    This function is used to call all other function in this file
    """
    global ID

    ID = customerID

    interface()
    weightlifting()


def interface():
    """
    This function is used to call the interface for the weightlifting
    """
    window = Tk()
    Button(window, text="START", command=startTime).grid(row=0)
    Button(window, text="STOP", command=stopTime).grid(row=0, column=1)
    Button(window, text="Bereken calorieen", command=window.destroy).grid(row=1)
    window.mainloop()


def weightlifting():
    """
    This function is used to count te calories used by the client
    """
    liftingWeight = 75
    clientWeight = gD.getDataWhere('weight', 'customerInfo', '{}'.format(ID))  # Weight of the client that comes form the database
    clientWeight = clientWeight[0][0]
    startWeight = 10
    global sportTime
    print(sportTime)
    if liftingWeight <= 80:
        startCalorie = 32
        calorieTotal = (startCalorie * ((clientWeight/startWeight)-1)) + startCalorie
        actualCalorie = calorieTotal * sportTime
        print(int(actualCalorie), "Kcal")
    elif liftingWeight > 80:
        startCalorie = 63
        calorieTotal = (startCalorie * ((clientWeight/startWeight)-1)) + startCalorie
        actualCalorie = calorieTotal * sportTime
        print(int(actualCalorie), "Kcal")
    gD.insertData('customerPerformanceInfo (customerID, startSession, endSession, fitnessDevice, burntCalories)',
              '{}, \'{}\', \'{}\', \'Rowing Machine\', {}'.format(ID, startTime, endTime, actualCalorie))



def startTime():
    """
    This function is used to start the timer, this function is called when the start button is pressed
    """
    global start
    global startTime
    startTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    start = time.time()


def stopTime():
    """
    This function is used to stop the timer, and is called when the stop button is pressed
    """
    global sportTime
    global endTime
    endTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    sportTime = (time.time() - start)/3600

