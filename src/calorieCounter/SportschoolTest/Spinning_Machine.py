# This file is used for the spinning machine in the gym
from tkinter import *
import time

start = ""
sportTime = ""


def main():
    """
    This is the main function, all the function will be called from here
    """
    interface()
    spinningMachine()


def startTime():
    global start
    start = time.clock()


def stopTime():
    global sportTime
    sportTime = (time.clock() - start) / 60


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
    Button(window, text="Bereken Calorieën", command=window.destroy).grid(row=1)
    window.mainloop()

main()
