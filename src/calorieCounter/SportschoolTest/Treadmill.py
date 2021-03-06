# This file contains a calorietracker the treadmill in the gym
import time
from tkinter import *

# This are the global variables for this file
setting = ""
start = ""
timeHours = ""


def main():
    """
    This function is the main function in the program
    """
    interface()
    treadmill()


def settings1():
    """ This is a function that makes the setting = 1 when the setting 1 button is pressed"""
    global setting
    setting = 1
    print(setting)


def settings2():
    """ This is a function that makes the setting = 2 when the setting 2 button is pressed"""
    global setting
    setting = 2
    print(setting)


def settings3():
    """ This is a function that makes the setting = 3 when the setting 3 button is pressed"""
    global setting
    setting = 3
    print(setting)


def settings4():
    """ This is a function that makes the setting = 4 when the setting 4 button is pressed"""
    global setting
    setting = 4
    print(setting)


def settings5():
    """This is a function that makes the setting = 5 when the setting 5 button is pressed"""
    global setting
    setting = 5
    print(setting)


def timetracker():
    """
    This function is used to start the clock to measure the time between the press of the start button and the
    press of the stop button
    """
    global start
    start = time.clock()


def timestopper():
    """
    This function is used to stop the clock and print the time elapsed
    """
    sportTime = time.clock() - start
    global timeHours
    timeHours = sportTime/3600
    print(sportTime)


def treadmill():
    """
    This function is a calorietracker for running on a treadmill with different settings for the speed of the runner
    """
    global setting
    clientWeight = 85  # This value should be acquired out of the database
    startWeight = 10
    # Different setting on the treadmill:

    #       - 1: Walking 3km/h
    if setting == 1:
        startCalorie = 25
        calorieTotal = (startCalorie * ((clientWeight/startWeight)-1)) + startCalorie
    #       - 2: Walking 6 km/h
    if setting == 2:
        startCalorie = 50
        calorieTotal = (startCalorie * ((clientWeight/startWeight)-1)) + startCalorie
    #       - 3: Running 10km/h
    if setting == 3:
        startCalorie = 100
        calorieTotal = (startCalorie * ((clientWeight/startWeight)-1)) + startCalorie
    #       - 4: Running 12 km/h
    if setting == 4:
        startCalorie = 120
        calorieTotal = (startCalorie * ((clientWeight/startWeight)-1)) + startCalorie
    #       - 4: Running 15 km/h
    if setting == 5:
        startCalorie = 150
        calorieTotal = (startCalorie * ((clientWeight/startWeight)-1)) + startCalorie
    # Calculating the amount of burned calories with the time the client actually ran
    actualCalorie = calorieTotal * timeHours
    actualCalorie = int(actualCalorie)
    print(actualCalorie, "Kcal")


def interface():
    """
    This function is the interface function for the interface of the treadmill
    """
    window = Tk()
    # start and stop buttons
    startButton = Button(window, text="START", command=timetracker)
    startButton.grid(row=0, column=3, columnspan=2)
    stopButton = Button(window, text="STOP", command=timestopper)
    stopButton.grid(row=0, column=4, columnspan=3)

    labelSetting = Label(window, text="Kies een setting voor de snelheid")
    labelSetting.grid(row=2, column=2, columnspan=5)
    # the setting buttons for the speed of the treadmill
    setting1Button = Button(window, text=" 1 ", command=settings1)
    setting1Button.grid(row=3, column=2)
    setting2Button = Button(window, text=" 2 ", command=settings2)
    setting2Button.grid(row=3, column=3)
    setting3Button = Button(window, text=" 3 ", command=settings3)
    setting3Button.grid(row=3, column=4)
    setting4Button = Button(window, text=" 4 ", command=settings4)
    setting4Button.grid(row=3, column=5)
    setting5Button = Button(window, text=" 5 ", command=settings5)
    setting5Button.grid(row=3, column=6)
    # Button for the calorietracker
    calorietracker = Button(window, text=" Bereken de caloriën ", command=window.destroy)
    calorietracker.grid(row=4, column=2, columnspan=5)

    window.mainloop()


main()

# Nog te doen:
#       - Manier om de hoeveelheid caloriën op te slaan
#       - Grafiek maken van calorie verbruik
#       - Advies geven

# Ideeën:
#       - TAGS geven aan de persoon bijv: cardio
#       - Aan de hand van die tags advies geven
