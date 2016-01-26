# This file is used for the spinning machine in the gym
from Tkinter import *
import time
import main as mn

start = ""
sportTime = ""


def main():
    """
    This is the main function, all the function will be called from here
    """
    interface()
    spinningMachine()
	ID = mn.getcustomerId

def startTime():
    """
    This function is used to start the timer, this function is called when the start button is pressed
    """
	global localTime
    localTime = (strftime("%d %b %Y %H:%M:%S", localtime()))
    global start
    start = time.clock()


def stopTime():
    """
    This function is used to determine the time passed, this function is called when the stop button is pressed.
    """
	global dateEnd
    dateEnd = (strftime("%d %b %Y %H:%M:%S", localtime()))
    global sportTime
    sportTime = (time.clock() - start) / 3600


def spinningMachine():
    """
    This function is used to count the amount of calories the client uses while spinning
    """
    clientWeight = 70
    startWeight = 10
    global sportTime
    hourTime = sportTime / 60
    # Spinning has only one setting
    startCalorie = 117
    calorieTotal = (startCalorie * ((clientWeight/startWeight)-1)) + startCalorie
    actualCalorie = calorieTotal * hourTime
    print(int(actualCalorie), "Kcal")


def interface():
    """
    This function is used to view the interface
    """
    window = Tk()
    Button(window, text="START", command=startTime).grid(row=0)
    Button(window, text="STOP", command=stopTime).grid(row=0, column=1)
    Button(window, text="Bereken Calorieen", command=window.destroy).grid(row=1)
    window.mainloop()

