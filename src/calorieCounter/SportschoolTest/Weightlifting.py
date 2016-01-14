# This file is used for the weightlifting
from tkinter import *
import time

start = ""
sportTime = ""


def main():
    """
    This function is used to call all other function in this file
    """


def interface():
    """
    This function is used to call the interface for the weightlifting
    """
    window = Tk()

    Button(window, text="START", command=startTime).grid(row=0)
    Button(window, text="STOP", command=stopTime).grid(row=0, column=1)
    Label(window)


    window.mainloop()


def weightlifting():
    """
    This function is used to count te calories used by the client
    """



def startTime():
    """
    This function is used to start the timer, this function is called when the start button is pressed
    """

def stopTime():
    """
    This function is used to stop the timer, and is called when the stop button is pressed
    """