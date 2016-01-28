# importing al the nessesairy library's
import RPi.GPIO as GPIO
import RPiGPIO_keypad_edited as GPIO_KEYPAD
import MFRC522
import threading
import tkMessageBox as message
from Tkinter import *
from time import sleep
import Rowing_Machine
import Treadmill
import Spinning_Machine
import Weightlifting
import Climbing_stairs
import getData as gD
# import signal
# import sys

servoPin  = 12# This is the pin the servo is connected to
ledRed = 33# This is the pin the red cicuit of the rgb led is connected to
ledGreen = 35#This is the pin the green cicuit of the rgb led is connected to
ledBlue = 37#This is the pin the blue cicuit of the rgb led is connected to

#window = RFID = servo = scanPass = backData = weightEntry = keypad = thread = canvas = firstNameEntry = surnameEntry = streetEntry = postalCodeEntry = phoneNumberEntry = emailEntry = genderEntry = RFID = "" #this line defines variables beforehand to make sure they are globally accessible
#continueReading = True#might not be needed. turns the rfid reader on or off

#card numbers
cardA = [52,188,189,222,235]#the id of the blue tag
cardB = [12,235,179,213,129]#the id of the white card

def setup():
    """
        This function is used for setting up the pinout of the raspberry pi and creating de variables used by devices that are connected to the raspberry pi.
    """
    global servo, keypad, RFID

    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    keypad = GPIO_KEYPAD.keypad()#creates a new keypad element
    RFID = MFRC522.MFRC522()#creates a new rfid reader element

    GPIO.setup(servoPin, GPIO.OUT)
    GPIO.setup(ledRed, GPIO.OUT)
    GPIO.setup(ledGreen, GPIO.OUT)
    GPIO.setup(ledBlue, GPIO.OUT)

    servo = GPIO.PWM(servoPin, 100)#creates a new servo element
    servo.start(0)

def basicWindow(windowTitle):
    """
        This creates a basic tkinter window with a background. Any items that are needed can be added to the window in different functions.
        After adding all the items needed mainloop can be called and the window wil stay open.
    """
    global window, canvas

    window = Tk()#creates a tkinter window
    window.eval('tk::PlaceWindow %s center' % window.winfo_pathname(window.winfo_id()))#toegevoegd
    window.geometry('736x552')
    window.title(windowTitle)
    window.resizable(width=FALSE, height=FALSE)

    canvas = Canvas(window, width=736, height=552)#creates a canvas inside the window (for the background and transparent text labels)
    canvas.pack()

    canvas.background=PhotoImage(file='./pictures/orangeachtergrond.png')#create a background image
    canvas.create_image(368,276, image=canvas.background)

    canvas.logo1 = PhotoImage(file='./pictures/strongman.png')
    canvas.logo1Smaller=canvas.logo1.subsample(2, 2)#seize the image 2 times down
    canvas.create_image(100,60, image=canvas.logo1Smaller)

    canvas.logo2 = PhotoImage(file='./pictures/logo.png')
    canvas.logo2Smaller=canvas.logo2.subsample(2, 2)#seize the image 2 times down
    canvas.create_image(370,70, image=canvas.logo2Smaller)

def closeScreen():
    """
        This wil close the basic window
    """
    global window
    window.destroy()
    mainFunction()

def close(screen):
    """
        This function is used to close the window wich indicates that you have to hold your access card in front of the reader
    """
    screen.destroy()
    screen.quit()

def scanPassScreen(version):
    """
        This sets up the screen wich indicates that you have to hold the acces card to the reader.
        However it dusn't ad it to the mainloop because the thread has to be started first.
    """
    global scanPass
    scanPass = Toplevel()#create a secundary window to ask for a acces pass
    scanPass.configure(background="blue")
    scanPass.geometry('400x150')

    passImageFirst = PhotoImage(file='./pictures/keycard.png')#create an image to go onto the screen
    passImage=passImageFirst.subsample(5, 5)#seize the image 5 times down
    passLabel = Label(scanPass, image=passImage)#create a label for the image to go into
    passLabel.Image = passImage #keep the refference so the item won't be destroyed

    scanLabel = Label(scanPass,text="Hold your access card against the scanner.", background="Blue",foreground="white")#create a label to put text on

    scanLabel.place(x=180, y=40)
    passLabel.place(x=40, y=30)

def sendInformation(firstName, surname, street, addressNumber, postalCode, town, country, phoneNumber, email, password, weight, IBAN):
    """
        This function first checks if any of the forms are empty.
        After that it tells you to hold the access card to the reader and it will write the information to the database.
    """
    global window, backData, scanPass
    gender = genderEntry.get() #create a gender variable to use inside this function

    if IBAN == "" or firstName == "" or surname == "" or street == "" or addressNumber == "" or postalCode == "" or town == "" or country == "" or phoneNumber == "" or gender == " " or email == "" or password == "" or weight == "":
        message.showinfo("Information missing", "At least one input box is still empty. Please make sure you filled in al the required information.")

    else:
        try:
            scanPassScreen("top")
            thread = threading.Thread(target=reader, args=(True,))#create a thread to scan access cards while having a window open
            thread.start()
            scanPass.mainloop()
            
            cardData = backData
            backData = ""

            cardDataDb = ("rfidNumber='" + str(cardData) + "'")
            checkRFIDData = gD.getDataWhere("count(*)", "loginInfo", cardDataDb)
            
            if checkRFIDData[0][0] == 0:
                gD.insertInto("customerInfo", "surname, name, gender, cellphoneNumber, weight, IBAN", "'{}', '{}', '{}', '{}', {}, '{}'".format(surname, firstName, gender, phoneNumber, weight, IBAN))
                gD.insertInto("addressInfo", "street, zipcode, addressNumber, town, country", "'{}', '{}', '{}', '{}', '{}'".format(street, postalCode, addressNumber, town, country))
                gD.insertInto("loginInfo","password, email, rfidNumber", "'{}', '{}', '{}'".format(password, email, str(cardData)))

                message.showinfo("It worked", "U are hereby a customer of benno's gym.")

                IBANEntry.delete(0, END)
                firstNameEntry.delete(0, END)
                surnameEntry.delete(0, END)
                streetEntry.delete(0, END)
                addressNumberEntry.delete(0, END)
                postalCodeEntry.delete(0, END)
                townEntry.delete(0, END)
                countryEntry.delete(0, END)
                phoneNumberEntry.delete(0, END)
                emailEntry.delete(0, END)
                genderEntry.set(" ")
                passwordEntry.delete(0, END)
                weightEntry.delete(0, END)

            else:
                message.showinfo("Already in use", "This access card is already registered. Try a different one")
                sendInformation(firstName, surname, street, addressNumber, postalCode, town, country, phoneNumber, email, password, weight, IBAN)
        except:
            message.showinfo("Failed", "Something went wrong. Please try again later.")

def addUser():#ander font voor de text
    """
        This function adds labels and text entry boxes to the basic window. This way it asks for user information so a user can register.
    """
    global canvas, firstNameEntry, surnameEntry, streetEntry, addressNumberEntry, postalCodeEntry, townEntry, countryEntry, phoneNumberEntry, emailEntry, genderEntry, passwordEntry, weightEntry, IBANEntry
    basicWindow("Add a user")
    genderEntry = StringVar() #create a new string variable for the radio buttons
    genderEntry.set(" ")

    #create text with transparant background
    canvas.create_text(270,100, text="IBAN:")
    canvas.create_text(252,129, text="First Name:")
    canvas.create_text(243,158, text="Second name:")
    canvas.create_text(260,187, text="Address:")
    canvas.create_text(234,216, text="Address Number:")
    canvas.create_text(260,245, text="Zipcode:")
    canvas.create_text(270,274, text="Town:")
    canvas.create_text(262,303, text="Country:")
    canvas.create_text(240,332, text="Phone number:")
    canvas.create_text(263,361, text="gender:")
    canvas.create_text(267,390, text="E-mail:")
    canvas.create_text(256,419, text="Password:")
    canvas.create_text(264,448, text="Weight:")

    #canvas.create_line(285, 90, 285,500)#This is to lineout the opbjects but can be removed once done

    #create all text entry boxes,  radioButtons and other buttons needed for the user interaction of this window
    IBANEntry = Entry(window)
    firstNameEntry = Entry(window)
    surnameEntry = Entry(window)
    streetEntry = Entry(window)
    addressNumberEntry = Entry(window)
    postalCodeEntry = Entry(window)
    townEntry = Entry(window)
    countryEntry = Entry(window)
    phoneNumberEntry = Entry(window)
    r1Entry = Radiobutton(window, text="Male", variable=genderEntry, value="Male", background="orange",activebackground="light blue", cursor="dotbox", indicatoron=0, width=10, foreground="red")
    r2Entry = Radiobutton(window, text="Female", variable=genderEntry, value="Female", background="orange",activebackground="light blue", cursor="dotbox", indicatoron=0, width=10,foreground="red")
    emailEntry = Entry(window)
    passwordEntry = Entry(window, show="*")
    weightEntry = Entry(window)

    IBANEntry.place(x=300, y=92)
    firstNameEntry.place(x=300, y=121)
    surnameEntry.place(x=300, y=150)
    streetEntry.place(x=300, y=179)
    addressNumberEntry.place(x=300, y=208)
    postalCodeEntry.place(x=300, y=237)
    townEntry.place(x=300, y=266)
    countryEntry.place(x=300, y=295)
    phoneNumberEntry.place(x=300, y=324)
    r1Entry.place(x=300, y=353)
    r2Entry.place(x=385, y=353)
    emailEntry.place(x=300, y=382)
    passwordEntry.place(x=300, y=411)
    weightEntry.place(x=300, y=440)


    registerButton = Button(text="Register",
                           background="orange",
                           activebackground="light blue",
                           borderwidth=4,
                           cursor="mouse",
                           foreground="red",
                           width=10,
                           command=(lambda: sendInformation(firstNameEntry.get(),
                                                            surnameEntry.get(),
                                                            streetEntry.get(),
                                                            addressNumberEntry.get(),
                                                            postalCodeEntry.get(),
                                                            townEntry.get(),
                                                            countryEntry.get(),
                                                            phoneNumberEntry.get(),
                                                            emailEntry.get(),
                                                            passwordEntry.get(),
                                                            weightEntry.get(),
                                                            IBANEntry.get())))
    registerButton.place(x=230,y=470)

    quitButton = Button(text="Close",
                        background="orange",
                        activebackground="light blue",
                        borderwidth=4,
                        cursor="cross",
                        foreground="red",
                        width=10,
                        command=closeScreen)
    quitButton.place(x=400,y=470)

    window.mainloop()

def turnServo():
    """
        Here we turn the servo 90 degrees and then back after waiting.
    """
    global servo

    pauseTime = 0.02 #create variable for the time between servo move percentage
    for i in range(0,51):
        servo.ChangeDutyCycle(i)#change this
        sleep(pauseTime)
    sleep(1)
    for i in range(50,-1, -1):
        servo.ChangeDutyCycle(i)#change this
        sleep(pauseTime)
    sleep(1)

def reader(closeWindow):
    """
        In this function we try to read rfid cards. At the end it returns the data it got.
    """
    global backData, keypad, RFID, scanPass
    #global continue_reading
    #signal.signal(signal.SIGINT, end_read)
    print("reader")
    breakOut = False
    GPIO.output(ledRed, True)
    GPIO.output(ledGreen, True)
    while True:
        (status,TagType) = RFID.MFRC522_Request(RFID.PICC_REQIDL)
        (status,backData) = RFID.MFRC522_Anticoll()
        if status == RFID.MI_OK:
            print("Card read UID: "+str(backData[0])+","+str(backData[1])+","+str(backData[2])+","+str(backData[3])+","+str(backData[4]))

            GPIO.output(ledRed, False)

            if closeWindow == True:
                close(scanPass)
            #breakOut = False#might not be needed
            #sleep(0.5)#might need to be increased
            break

        if keypad.getKey() == "*":
            print("Exit ingedrukt")
            breakOut = True
            break
        sleep(0.2)
    return breakOut

def login():
    """
        Here we read a rfid card and try to log the user in.
        firstly we get the rfidCards from the database.
    """
    dbData = gD.getData('loggedIn, rfidNumber, customerID', 'loginInfo')

    global cardA, keypad, backData, scanPass
    while True:
        breakOut = reader(False)
        cardData = backData
        cardData = str(cardData)
        backData = ""
        if keypad.getKey() == "*" or breakOut == True:
            sleep(1)
            if scanPass != "":
                close(scanPass)
                scanPass = ""
            #turn off all led colors
            GPIO.output(ledRed, False)
            GPIO.output(ledGreen, False)
            GPIO.output(ledBlue, False)
            break

        else:
            rowCounter = 1
            for row in dbData:
                    if cardData == row[1] and row[0] == 1:
                        servoThread = threading.Thread(target=turnServo)
                        servoThread.start()
                        for i in range(3):
                            GPIO.output(ledGreen, False)
                            sleep(0.3)
                            GPIO.output(ledGreen, True)
                            sleep(0.3)
                        updateInjection = ('customerID = ' + str(row[2]))
                        gD.updateData('loginInfo', 'loggedIn = false', updateInjection)# 0 en 1?
                        sleep(1)

                    elif cardData == row[1] and row[0] == 0:
                        servoThread = threading.Thread(target=turnServo)
                        servoThread.start()
                        for i in range(3):
                            GPIO.output(ledGreen, False)
                            sleep(0.3)
                            GPIO.output(ledGreen, True)
                            sleep(0.3)
                        updateInjection = ('customerID = ' + str(row[2]))
                        gD.updateData('loginInfo', 'loggedIn = true', updateInjection)# 0 en 1?
                        sleep(1)

                    elif cardData != row[1] and rowCounter == len(dbData):
                        print("niet oke")
                        GPIO.output(ledGreen, False)
                        for i in range(5):
                            GPIO.output(ledRed, True)
                            sleep(0.5)
                            GPIO.output(ledRed, False)
                            sleep(0.5)
                        sleep(1)
                        GPIO.output(ledGreen, True)
            rowCounter += 1
        sleep(0.1)


def treadmill():
    """
        callable function to be able to start running on a treadmill
    """
    global scanPass, backData
    scanPassScreen("top")
    thread = threading.Thread(target=reader, args=(True,))
    thread.start()
    scanPass.mainloop()

    cardData = backData
    cardDataDb = ("rfidNumber = '" + str(cardData) + "'")
    backData = ""
    customerID = gD.getDataWhere("customerID", "loginInfo", cardDataDb)
    
    Treadmill.main(customerID[0][0])

def rowingMachine():
    global scanPass, backData
    scanPassScreen("top")
    thread = threading.Thread(target=reader, args=(True,))
    thread.start()
    scanPass.mainloop()

    cardData = backData
    cardDataDb = ("rfidNumber = '" + str(cardData) + "'")
    backData = ""
    customerID = gD.getDataWhere("customerID", "loginInfo", cardDataDb)

    Rowing_Machine.main(customerID[0][0])

def spinningMachine():
    global scanPass, backData
    scanPassScreen("top")
    thread = threading.Thread(target=reader, args=(True,))
    thread.start()
    scanPass.mainloop()

    cardData = backData
    cardDataDb = ("rfidNumber = '" + str(cardData) + "'")
    backData = ""
    customerID = gD.getDataWhere("customerID", "loginInfo", cardDataDb)

    Spinning_Machine.main(customerID[0][0])

def weightLifing():
    global scanPass, backData
    scanPassScreen("top")
    thread = threading.Thread(target=reader, args=(True,))
    thread.start()
    scanPass.mainloop()

    cardData = backData
    cardDataDb = ("rfidNumber = '" + str(cardData) + "'")
    backData = ""
    customerID = gD.getDataWhere("customerID", "loginInfo", cardDataDb)

    Weightlifting.main(customerID[0][0])

def climbingStairs():
    global scanPass, backData
    scanPassScreen("top")
    thread = threading.Thread(target=reader, args=(True,))
    thread.start()
    scanPass.mainloop()

    cardData = backData
    cardDataDb = ("rfidNumber = '" + str(cardData) + "'")
    backData = ""
    customerID = gD.getDataWhere("customerID", "loginInfo", cardDataDb)

    Climbing_stairs.main(customerID[0][0])


def numberOfCustomers():
    basicWindow("Number of customers")


def mainFunction():
    """
        This is the mainfunction. Here we chose wich other function we want to run using a keypad that is connected to the raspberry pi.
    """
    global keypad

    GPIO.output(ledRed, False)
    GPIO.output(ledGreen, False)
    GPIO.output(ledBlue, False)

    print("Press the number of the device you want to use.")
    try:
        functions = [loginThreads, addUser, treadmill, rowingMachine, spinningMachine, weightLifing, climbingStairs]#create a list of functions

        devices = ["Login user", "Add a user", "Treadmill", "Rowing", "Spinning", "Weightlifting", "Climbing stairs"]
        deviceNumber = 1
        for device in devices:
            print(str(deviceNumber) + ": " + device)
            deviceNumber +=1

        while True:
            if keypad.getKey() and 0 < int(keypad.getKey()) < 7:
                print("key pressed")
                keypadCharacter = int(keypad.getKey())#store the pressed key in the keypadCharacter variable
                sleep(1)
                keypadCharacter-=1
                functions[keypadCharacter]()

            elif keypad.getKey() and not 0 < int(keypad.getKey()) < 7:
                print("The number that we got was either to high or to low.") #needed to be split in to high or low?
                sleep(2)
            sleep(0.1)
    #except ValueError:
    #    print("Dit is geen getal voer altublieft een getal in.")
    #    sleep(1)
    #    mainFunction()
    # except:
    #     sleep(1)
    #     sys.exit()
    finally:
        GPIO.output(ledRed, False)
        GPIO.output(ledGreen, False)
        GPIO.output(ledBlue, False)
        print("exiting")
        GPIO.cleanup()


def loginThreads():
    global scanPass
    scanPassScreen("top")

    loginThread = threading.Thread(target=login)
    loginThread.start()

    scanPass.mainloop()
    mainFunction()


setup()
mainFunction()

# toevoegen pas al in gebruik aanmaken van account
# exiting gaat heel snel
