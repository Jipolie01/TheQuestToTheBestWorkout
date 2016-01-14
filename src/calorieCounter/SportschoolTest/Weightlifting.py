# This file is used for the weightlifting
from tkinter import *
import time

start = ""
sportTime = ""


def main():
    """
    This function is used to call all other function in this file
    """
    interface()
    weightlifting()


def interface():
    """
    This function is used to call the interface for the weightlifting
    """
    window = Tk()
    Button(window, text="START", command=startTime).grid(row=0)
    Button(window, text="STOP", command=stopTime).grid(row=0, column=1)
    Button(window, text="Bereken calorieën", command=window.destroy).grid(row=1)
    window.mainloop()


def weightlifting():
    """
    This function is used to count te calories used by the client
    """
    liftingWeight = 75
    clientWeight = 70
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


def startTime():
    """
    This function is used to start the timer, this function is called when the start button is pressed
    """
    global start
    start = time.clock()


def stopTime():
    """
    This function is used to stop the timer, and is called when the stop button is pressed
    """
    global sportTime
    sportTime = (time.clock() - start)/3600


main()
