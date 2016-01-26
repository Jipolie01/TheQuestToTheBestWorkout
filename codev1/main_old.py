__author__ = 'timijntema'
import RPi.GPIO as GPIO
import RPiGPIO_keypad_edited as GPIO_KEYPAD
import MFRC522
import signal
import sys
import threading
from Tkinter import *
import tkMessageBox as message
from time import sleep

servoPin  = 12#This is the pin the servo is connected to
ledRed = 33#This is the pin the red cicuit of the rgb led is connected to
ledGreen = 35#This is the pin the green cicuit of the rgb led is connected to
ledBlue = 37#This is the pin the blue cicuit of the rgb led is connected to

window = RFID = servo = backData = keypad = thread = canvas = firstNameEntry = surnameEntry = streetEntry = postalCodeEntry = phoneNumberEntry = emailEntry = genderEntry = RFID = "" #this line defines variables beforehand to make sure they are globally accessible
continueReading = True#might not be needed. turns the rfid reader on or off
#scanPass = ""

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
    if version == "top":
        scanPass = Toplevel()#create a secundary window to ask for a acces pass
    else:
        scanPass = Tk()#create the same window but this time as a primairy window
    scanPass.configure(background="blue")
    scanPass.geometry('400x150')

    passImageFirst = PhotoImage(file='./pictures/keycard.png')#create an image to go onto the screen
    passImage=passImageFirst.subsample(5, 5)#seize the image 5 times down
    passLabel = Label(scanPass, image=passImage)#create a label for the image to go into
    passLabel.Image = passImage #keep the refference so the item won't be destroyed

    scanLabel = Label(scanPass,text="Houd uw pas voor de scanner.", background="Blue",foreground="white")#create a label to put text on

    scanLabel.place(x=180, y=40)
    passLabel.place(x=40, y=30)
    return scanPass

def sendInformation(firstName, surname, street, postalCode, phoneNumber, email):
    """
        This function first checks if any of the forms are empty.
        After that it tells you to hold the access card to the reader and it will write the information to the database.
    """
    global window, genderEntry, backData
    genderFunc = genderEntry.get() #create a gender variable to use inside this function

    if firstName == "" or surname == "" or street == "" or postalCode == "" or phoneNumber == "" or genderFunc == " " or email == "":
        message.showinfo("Informatie missende", "Een of meer invoervakken is leeg. Vul alstublieft alles in.")
    else:
        global voornaam_entry, achternaam_entry, straat_entry, postcode_entry, telefoon_entry, email_entry
        print(firstName + " " + surname + " " + street + " " + postalCode + " " + phoneNumber + " " + str(genderFunc) + " " + email)#verwijderen
        try:
            scanPass = scanPassScreen("top")#scanpass toevoegen
            thread = threading.Thread(target=reader, args=(scanPass,))#create a thread
            thread.start()
            scanPass.mainloop()#never ask for him??

            cardData = backData
            print(cardData)
            backData = ""

            #sql met invoeren van data
            message.showinfo("Gelukt", "U bent nu een klant van deze sportzaak")#veranderen naar naam

            firstNameEntry.delete(0, END)
            surnameEntry.delete(0, END)
            streetEntry.delete(0, END)
            postalCodeEntry.delete(0, END)
            phoneNumberEntry.delete(0, END)
            emailEntry.delete(0, END)
            genderEntry.set(" ")

        except:
            print("Unable to start thread")
            message.showinfo("Mislukt", "Het is niet gelukt om u als gebruiker toe te voegen. Probeer het later opnieuw.")

def adUser():#ander font voor de text
    """
        This function adds labels and text entry boxes to the basic window. This way it asks for user information so a user can register.
    """
    global window, canvas, firstNameEntry, surnameEntry, streetEntry, postalCodeEntry, phoneNumberEntry, emailEntry, genderEntry
    basicWindow("Add a user")
    genderEntry = StringVar() #create a new string variable for the radio buttons
    genderEntry.set(" ")

    #create text with transparant background
    canvas.create_text(258,129, text="Voornaam:")
    canvas.create_text(253,158, text="Achternaam:")
    canvas.create_text(270,187, text="Adres:")
    canvas.create_text(261,216, text="Postcode:")
    canvas.create_text(253,245, text="Telefoon nr.:")
    canvas.create_text(263,274, text="Geslacht:")
    canvas.create_text(268,303, text="E-mail:")
    canvas.create_text(260,332, text="Password:")

    #canvas.create_line(285, 90, 285,300)#This is to lineout the opbjects but can be removed once done

    #create all text entry boxes,  radioButtons and other buttons needed for the user interaction of this window
    firstNameEntry = Entry(window)
    surnameEntry = Entry(window)
    streetEntry = Entry(window)
    postalCodeEntry = Entry(window)
    phoneNumberEntry = Entry(window)
    r1Entry = Radiobutton(window, text="Man", variable=genderEntry, value="Man", background="orange",activebackground="light blue", cursor="dotbox", indicatoron=0, width=10, foreground="red")
    r2Entry = Radiobutton(window, text="Vrouw", variable=genderEntry, value="Vrouw", background="orange",activebackground="light blue", cursor="dotbox", indicatoron=0, width=10,foreground="red")
    emailEntry = Entry(window)
    passwordEntry = Entry(window, show="*")

    firstNameEntry.place(x=300, y=121)
    surnameEntry.place(x=300, y=150)
    streetEntry.place(x=300, y=179)
    postalCodeEntry.place(x=300, y=208)
    phoneNumberEntry.place(x=300, y=237)
    r1Entry.place(x=300, y=266)
    r2Entry.place(x=385, y=266)
    emailEntry.place(x=300, y=295)
    passwordEntry.place(x=300, y=324)


    registerButton = Button(text="Registreer",
                           background="orange",
                           activebackground="light blue",
                           borderwidth=4,
                           cursor="mouse",
                           foreground="red",
                           width=10,
                           command=(lambda: sendInformation(firstNameEntry.get(),
                                                     surnameEntry.get(),
                                                     streetEntry.get(),
                                                     postalCodeEntry.get(),
                                                     phoneNumberEntry.get(),
                                                     emailEntry.get())))
    registerButton.place(x=230,y=470)

    quitButton = Button(text="Sluiten",
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
        servo.ChangeDutyCycle(i)
        sleep(pauseTime)
    sleep(1)
    for i in range(50,-1, -1):
        servo.ChangeDutyCycle(i)
        sleep(pauseTime)
    sleep(1)

def reader(scanPass):
    """
        In this function we try to read rfid cards. At the end it returns the data it got.
    """
    global backData, keypad, RFID#, scanPass
    #global continue_reading
    #signal.signal(signal.SIGINT, end_read)
    print("reader")

    while True:#continue_reading
        (status,TagType) = RFID.MFRC522_Request(RFID.PICC_REQIDL)
        (status,backData) = RFID.MFRC522_Anticoll()

        if status == RFID.MI_OK:
            print("Card detected")
            print("Card read UID: "+str(backData[0])+","+str(backData[1])+","+str(backData[2])+","+str(backData[3])+","+str(backData[4]))
            #continue_reading = False
            #sleep(1)
            if scanPass != "":
                close(scanPass)
                break

        if keypad.getKey() == "*":
            print("Exit ingedrukt")
            sleep(1)
            if scanPass != "":
                close(scanPass)
                mainFunction()
        sleep(0.2)

def login():
    """
        Here we read a rfid card and try to log the user in.
    """
    global cardA, keypad, backData#, scanPass
    #scanPass = ""
    GPIO.output(ledRed, True)
    while True:
        scanPass = scanPassScreen("non-top")
        dataThread = threading.Thread(target=reader, args=(scanPass,))
        dataThread.start()
        scanPass.mainloop()

        cardData = backData
        backData = ""
        print("deze functie logt users in: " + str(cardData))#wijzigen of zo houden
        sqlCheck = "Data van de kaart" #vervangen door echt sql statement en toevoegen dat een persoon uitgelogd of ingelogd is
        if cardData == cardA:#veranderd met data uit sql database of zelfs volledig veranderd error based
            GPIO.output(ledRed, False)
            GPIO.output(ledGreen, True)
            turnServo()
            GPIO.output(ledGreen, False)
            GPIO.output(ledRed, True)
            sleep(1)
            scanPass = ""
            login()

        else:
            print("niet oke")
            for i in range(5):
                GPIO.output(ledRed, True)
                sleep(0.5)
                GPIO.output(ledRed, False)
                sleep(0.5)
                GPIO.output(ledRed, True)
                sleep(1)
            scanPass = ""
            login()

        if keypad.getKey() == "*":#make this a function?
            print("Exit ingedrukt")
            sleep(1)
            if scanPass != "":
                close(scanPass)
                scanPass = ""
            mainFunction()
        sleep(0.1)

def treadmill():
    """
        things and stuff
    """
    print("device 1")

def device1():
    print("device 1")

def device2():
    print("device 2")

def device3():
    print("device 3")

def device4():
    print("device 4")

def device5():
    print("device 5")


def mainFunction():
    """
        This is the mainfunction. Here we chose wich other function we want to run using a keypad that is connected to the raspberry pi.
    """
    global keypad
    print("Voer een getal in door middel van de keypad.")
    try:
        functions = [login, adUser, treadmill, device2, device3, device4, device5]#create a list of functions

        while True:
            if keypad.getKey() and 0 < int(keypad.getKey()) < 7:
                print("key pressed")
                keypadCharacter = int(keypad.getKey())#store the pressed key in the keypadCharacter variable
                keypadCharacter-=1
                functions[keypadCharacter]()

            elif keypad.getKey() and not 0 < int(keypad.getKey()) < 7:
                print("Het getal dat u ingevoerd heeft is te hoog of te laag") #needed to be split in to high or low?
                sleep(2)
            sleep(0.1)
    # except ValueError:
    #     print("Dit is geen getal voer altublieft een getal in.")
    #     mainFunction()
    # except:
    #     sleep(1)
    #     sys.exit()
    finally:

        print("exiting")
        GPIO.cleanup()


setup()
mainFunction()

#sportzaak naar naam veranderen
#toevoegen pas al in gebruik aanmaken van account
#exiting gaat heel snel
#verkeerd getal gaat heel snel
#sports guy meer naar links en logo meer naar rechts en kleiner. de rest meer naar onder