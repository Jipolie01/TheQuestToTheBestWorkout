# This file is used for the spinning machine in the gym
from Tkinter import *
import time
import getData as gD

start = ""
sportTime = ""


def main(customerID):
    """
    This is the main function, all the function will be called from here
    """
    global ID

    ID = customerID

    interface()
    spinningMachine()


def startTime():
    """
    This function is the one who start the timer for the sportTime, this function is called when the start button is
    pressed
    """
    global localTime
    localTime = (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))#time. added 2x
    global start
    start = time.time()


def stopTime():
    """
    This function is used to determine the time passed, this function is called when the stop button is pressed.
    """
    global dateEnd
    dateEnd = (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))#time. added 2x
    global sportTime
    sportTime = (time.time() - start)/3600


def spinningMachine():
    """
    This function is used to count the amount of calories the client uses while spinning
    """
    clientWeight = gD.getDataWhere('weight', 'customerInfo', "customerID = {}".format(ID))  # Weight of the client that comes form the database
    clientWeight = clientWeight[0][0]
    startWeight = 10
    global sportTime
    hourTime = sportTime / 60
    # Spinning has only one setting
    startCalorie = 117
    calorieTotal = (startCalorie * ((clientWeight/startWeight)-1)) + startCalorie
    actualCalorie = int(calorieTotal) * hourTime
    print(int(actualCalorie), "Kcal")
    gD.insertData('customerPerformanceInfo (customerID, startSession, endSession, fitnessDevice, burntCalories)',
              '{}, \'{}\', \'{}\', \'Spinning machine\', {}'.format(ID, localTime, dateEnd, actualCalorie))



def interface():
    """
    This function is used to view the interface
    """
    window = Tk()
    Button(window, text="START", command=startTime).grid(row=0)
    Button(window, text="STOP", command=stopTime).grid(row=0, column=1)
    Button(window, text="Bereken Calorieen", command=window.destroy).grid(row=1)
    window.mainloop()

