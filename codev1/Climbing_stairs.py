# This is a file for climbing stairs
from Tkinter import *
import time
import getData as gD
import main as mn

start = ""


def main():
    """
    This is the main function all the other functions are called from here
    """
    interface()
    climbingStairs()
    global ID
    ID = mn.getcustomerId()


def startTime():
    """
    This function is used to start the timer, this function is called when the start button is pressed
    """
    global startTime
    startTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    global start
    start = time.clock()


def stopTime():
    """
    This function is used to determine the time passed, this function is called when the stop button is pressed.
    """
    global endTime
    endTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    global sportTime
    sportTime = (time.clock() - start) / 3600


def interface():
    """
    This function is used to call the interface for the stair climbing
    """
    window = Tk()
    Button(window, text="START", command=startTime).grid(row=0)
    Button(window, text="STOP", command=stopTime).grid(row=0, column=1)
    Button(window, text="Bereken calorieen", command=window.destroy).grid(row=1)
    window.mainloop()


def climbingStairs():
    """
    This function is used to calculate the amount of calories
    """
    clientWeight = gD.getDataWhere('weight', 'customerInfo', '{}'.format(ID))  # Weight of the client that comes form the database
    clientWeight = clientWeight[0][0]
    startWeight = 10
    global sportTime
    hourTime = sportTime / 60
    # Climbing stairs only has one setting
    startCalorie = 60
    calorieTotal = (startCalorie * ((clientWeight/startWeight)-1)) + startCalorie
    actualCalorie = calorieTotal * hourTime
    print(int(actualCalorie), "Kcal")
    gD.insertData('customerPerformanceInfo (customerID, startSession, endSession, fitnessDevice, burntCalories)',
              '{}, \'{}\', \'{}\', \'Rowing Machine\', {}'.format(ID, startTime, endTime, actualCalorie))