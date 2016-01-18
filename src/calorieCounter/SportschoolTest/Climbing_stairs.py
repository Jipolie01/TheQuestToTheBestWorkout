# This is a file for climbing stairs
from tkinter import *
import time

start = ""


def main():
    """
    This is the main function all the other functions are called from here
    """
    interface()

def startTime():
    """
    This function is used to start the timer, this function is called when the start button is pressed
    """
    global start
    start = time.clock()


def stopTime():
    """
    This function is used to determine the time passed, this function is called when the stop button is pressed.
    """
    global sportTime
    sportTime = (time.clock() - start) / 3600


def interface():
    """
    This function is used to call the interface for the stair climbing
    """
    window = Tk()
    Button(window, text="START", command=startTime).grid(row=0)
    Button(window, text="STOP", command=stopTime).grid(row=0, column=1)
    Button(window, text="Bereken calorieën", command=window.destroy).grid(row=1)
    window.mainloop()

def climbingStairs():
    """
    This function is used to calculate the amount of calories
    """
    clientWeight = 70
    startWeight = 10
    global sportTime
    hourTime = sportTime / 60
    # Climbing stairs only has one version
    startCalorie = 60
    calorieTotal = (startCalorie * ((clientWeight/startWeight)-1)) + startCalorie
    actualCalorie = calorieTotal * hourTime
    print(int(actualCalorie), "Kcal")