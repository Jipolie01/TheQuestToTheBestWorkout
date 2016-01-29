# This file contains a calorietracker the treadmill in the gym
import time
from tkinter import *
import getData as gD


# These are the global variables for this file
setting = ""
start = ""
sportTime= ""



def main(customerID):
    """
    This function is the main function in the program
    """
    global ID

    ID = customerID
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


def startTime():
    """
    This function is the one who start the timer for the sportTime, this function is called when the start button is
    pressed
    """
    global localTime
    localTime = (time.strftime("%d %b %Y %H:%M:%S", time.localtime()))#time. added 2x
    global start
    start = time.time()


def stopTime():
    """
    This function is used to determine the time passed, this function is called when the stop button is pressed.
    """
    global dateEnd
    dateEnd = (time.strftime("%d %b %Y %H:%M:%S", time.localtime()))#time. added 2x
    global sportTime
    sportTime = (time.time() - start)/3600


def treadmill():
    """
    This function is a calorietracker for running on a treadmill with different settings for the speed of the runner
    """
    global setting
    global sportTime
    clientWeight = gD.getDataWhere('weight', 'customerInfo', '{}'.format(ID))  # Weight of the client that comes form the database
    clientWeight = clientWeight[0][0]
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
    actualCalorie = (int(calorieTotal) * sportTime)
    actualCalorie = int(actualCalorie)
    print(actualCalorie, "Kcal")
    gD.insertData('customerPerformanceInfo (customerID, startSession, endSession, fitnessDevice, burntCalories)',
              '{}, \'{}\', \'{}\', \'Rowing Machine\', {}'.format(ID, startTime, endTime, actualCalorie))



def interface():
    """
    This function is the interface function for the interface of the treadmill
    """
    window = Tk()
    # start and stop buttons
    startButton = Button(window, text="START", command=startTime)
    startButton.grid(row=0, column=3, columnspan=2)
    stopButton = Button(window, text="STOP", command=stopTime)
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
    calorietracker = Button(window, text=" Bereken de calorieen ", command=window.destroy)
    calorietracker.grid(row=4, column=2, columnspan=5)

    window.mainloop()


# Nog te doen:
#       - Manier om de hoeveelheid calorieen op te slaan
#       - Grafiek maken van calorie verbruik
#       - Advies geven

# Ideeen:
#       - TAGS geven aan de persoon bijv: cardio
#       - Aan de hand van die tags advies geven
