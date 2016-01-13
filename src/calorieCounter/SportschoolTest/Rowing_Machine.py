# This is a file used for the rowing machine in the gym
from tkinter import *
import time

# This are the global variables for this file
start = ""
sportTime = ""
frequency = ""


def main():
    """
    This is the main function, this function is used to call all other functions
    """
    interface()
    rowingMachine()


def startTime():
    """
    This function is the one who start the timer for the sportTime, this function is called when the start button is
    pressed
    """
    global start
    start = time.clock()


def stopTime():
    """
    This function is used to determine the time passed, this function is called when the stop button is pressed.
    """
    global sportTime
    sportTime = (time.clock() - start)/3600


def frequencyCounter():
    """
    This function does +1 by the frequency for every time the function is active, this function is called when
    the O button is pressed.
    """
    global frequency
    frequency += 1


def rowingMachine():
    """
    This function is used to count calories for the rowing machine
    """
    # This machine has an interface that count how many time you do a excersises in a certian time
    global frequency  # This number is based on doing 20 excersises in a minute wich is average tempo
    global sportTime  # Time in hours
    clientWeight = 70  # Weight of the client that comes form the database
    startWeight = 10
    # You have two different settings:
    #       - Average
    if frequency <= 20:
        startCalorie = 74
        calorieTotal = (startCalorie * ((clientWeight/startWeight)-1)) + startCalorie
        actualCalorie = calorieTotal * sportTime
        print(int(actualCalorie), "Kcal")
    #       - High frequency
    if frequency > 20:
        startCalorie = 90
        calorieTotal = (startCalorie * ((clientWeight/startWeight)-1)) + startCalorie
        actualCalorie = calorieTotal * sportTime
        print(int(actualCalorie), "Kcal")


def interface():
    """
    This function is used to start up de interface of the rowingmachine
    """
    window = Tk()

    Button(window, text="START", command=startTime).grid(row=0, column=1)
    Button(window, text="STOP", command=stopTime).grid(row=0, column=3)
    Label(window, text="Button voor de ferquentie").grid(row=1, column=2)
    Button(window, text="O", command=frequencyCounter).grid(row=2, column=2)
    Button(window, text="Bereken Calorieën", command=window.destroy)

    window.mainloop()

main()

