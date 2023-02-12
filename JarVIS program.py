# JARVIS program

# Import modules
import pyttsx3  # for TTS
import speech_recognition as sr  # For Speech Recognition
import datetime  # For finding the Date
import cv2  # for opening camera and taking photos
import random  # for piking random responses
import os  # for accessing and opering on the Operating System
import sys  # Used to consle the entire System as a whole
import winsound  # for playing sound files using wav file formats on Windows
import requests  # for finding IP Address
from requests import get  # use the get function
import wikipedia  # for gettingh results from wikipedia
import urllib
from urllib import request  # Used to check internet connection
import webbrowser  # To Open Links to specific web pages in the default web browser
try:
    import pywhatkit  # to Send messages on Whats App andďto open videos on YouTube
except Exception as e:
    print("Import Failed")
import psutil  # Fetch Battery Information


# Global Variables
botname = "WARREN"


# GUI Components
#
# Adapts for Light and Dark Mode in System


# initialize tts engine
engine = pyttsx3.init()


def SpeakOutput(message):
    # function fot perform Text to speech
    engine.say(message)
    print(message)
    engine.runAndWait()


def CheckInternet():
    try:
        testurl = "https://www.google.co.in/"
        urllib.request.urlopen(testurl)
        return True
    except urllib.error.URLError as e:
        print(str(e))
        return False


def TakUserInput():
    # function to take input form user

    r = sr.Recognizer()
    with sr.Microphone() as mic:
        print("listening...")
        winsound.PlaySound('sound\Speech On.wav', winsound.SND_ASYNC)
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(mic, 0.2)
        audio = r.listen(source=mic, timeout=1, phrase_time_limit=10)
        try:
            if CheckInternet():
                winsound.PlaySound(
                    'sound\Speech Off.wav', winsound.SND_ASYNC)
                UserQuery = r.recognize_google(audio, language='en-in')
            else:
                SpeakOutput(
                    "Please Connect to the Internet and Try Again ")
        except sr.UnknownValueError:
            return "none"
        except sr.RequestError:
            SpeakOutput("Say that again")
            return "none"
    return UserQuery


def GetUserLogin_Username():
    # Get User Login Name
    return os.getlogin()


def Greetings():
    # Function to greet the user depending on the time of day
    hour = int(datetime.datetime.now().hour)

    if (hour >= 8 and hour < 12):
        SpeakOutput("Good Morning "+os.getlogin())
        print("Good Morning "+os.getlogin())
    elif (hour >= 12 and hour < 18):
        SpeakOutput("Good Afternoon "+os.getlogin())
        print("Good Afternoon "+os.getlogin())
    else:
        SpeakOutput("Good Evening "+os.getlogin())
        print("Good Evening "+os.getlogin())
    SpeakOutput("I am "+botname+" How may I help you")


def TakePhoto():
    # Function to open camera and take a photo
    webcam = cv2.VideoCapture(0)

    imageCounter = 0
    flag = True
    while flag:
        if 1:
            ret, frames = webcam.read()
            if not ret:
                print("Failed to grab image")
                SpeakOutput("Failed to Capture")
                flag = False
                break
            cv2.imshow("Image Capture Window", frames)

            # Close webcame when presing the ESC key
            k = cv2.waitKey(50)

            # Take Screenshort when space key is pressed
            if k == 32:
                imagename = f"image_{imageCounter}.png"
                winsound.PlaySound(
                    'sound\camera-shutter.wav', winsound.SND_ASYNC)
                cv2.imwrite(imagename, frames)
                print("Image Captured")

                imageCounter += 1
            # CLose the camera when ESC key is pressed
            elif k == 27:
                webcam.release()
                cv2.destroyAllWindows()
                ret = False
                break

# Open Applications


def OpenCMD():
    path = "C:\\Windows\\system32\\cmd.exe"
    os.startfile(path)


def OpenChome():
    path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    os.startfile(path)

# Get info form Internet


def GetSystemIPAddress():
    if CheckInternet():
        ip = get("https://api.ipify.org").text
        SpeakOutput(f"Your Public IP Address is {ip}")
    else:
        SpeakOutput("Your System is not connected to the Internet")


def Searchwikipedia(query):
    if CheckInternet():
        SpeakOutput("Searching wikipedia")
        query = query.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=5)
        SpeakOutput("According to wikipedia...")
        SpeakOutput(result)
    else:
        SpeakOutput("Sorry !There is no Internet")


def OpenYouTube():
    if CheckInternet():
        webbrowser.open_new_tab('youtube.com')
    else:
        SpeakOutput("Sorry! There is no Internet")


def OpenAmazon():
    if CheckInternet():
        webbrowser.open_new_tab('https://www.amazon.in/')
    else:
        SpeakOutput("Sorry! There is no Internet")


def GoogleSearch():
    if CheckInternet():
        webbrowser.open_new_tab("google.com")
    else:
        SpeakOutput("Sorry! There is no Internet")


def GetUserAccountName():
    SpeakOutput(os.getlogin())

# Send message using WhatsApp


def SendWhatsAppMessage():
    if CheckInternet():
        SpeakOutput("Enter Phone Number with Country Code")
        phoneno = input("Enter Phone Number with Country Code")

        SpeakOutput("Speak the Message that you want to send")
        message = TakUserInput()

        pywhatkit.sendwhatmsg_instantly(phoneno, message)
        print("Message Sent")
        SpeakOutput(message+" was sent Successfully to "+phoneno)
    else:
        SpeakOutput("Sorry! There is no Internet")


def PlayVidoesOnYouTube():
    if CheckInternet():
        SpeakOutput("Mention the name of the Video to Play")
        VideoName = TakUserInput()
        pywhatkit.playonyt(VideoName)
        SpeakOutput("Sure Playing "+VideoName + " from Youtube")
    else:
        SpeakOutput("Sorry! There is no Internet")

# Get Date and Time from System


def FetchYear():
    current_time = datetime.datetime.now()
    year = current_time.year
    SpeakOutput("The Current Year is "+str(year))


def FetchMonth():
    current_time = datetime.datetime.now()
    month = current_time.month
    if month == 1:
        SpeakOutput("The Current Month is January")
    elif month == 2:
        SpeakOutput("The Current Month is February")
    elif month == 3:
        SpeakOutput("The Current Month is March")
    elif month == 4:
        SpeakOutput("The Current Month is April")
    elif month == 5:
        SpeakOutput("The Current Month is May")
    elif month == 6:
        SpeakOutput("The Current Month is June")
    elif month == 7:
        SpeakOutput("The Current Month is July")
    elif month == 8:
        SpeakOutput("The Current Month is Augest")
    elif month == 9:
        SpeakOutput("The Current Month is September")
    elif month == 10:
        SpeakOutput("The Current Month is October")
    elif month == 11:
        SpeakOutput("The Current Month is November")
    elif month == 12:
        SpeakOutput("The Current Month is Descember")


def FetchDay():
    weekday = datetime.datetime.now().weekday()
    if weekday == 0:
        SpeakOutput("Today is is Monday")
    elif weekday == 1:
        SpeakOutput("Today is Tuesday")
    elif weekday == 2:
        SpeakOutput("Today is Wednessday")
    elif weekday == 3:
        SpeakOutput("Today is Thirsday")
    elif weekday == 4:
        SpeakOutput("Today is Friday")
    elif weekday == 5:
        SpeakOutput("Today is Saturday")
    elif weekday == 6:
        SpeakOutput("Today is Sunday")


def Extract_Day_Of_Week_From_Day(day):
    day = day.weekday()
    if day == 0:
        return "Monday"
    elif day == 1:
        return "Tuesday"
    elif day == 2:
        return "Wednessday"
    elif day == 3:
        return "Thursday"
    elif day == 4:
        return "Friday"
    elif day == 5:
        return "Saturday"
    elif day == 6:
        return "Sunday"


def Extract_Month_of_the_Year(month):

    if month == 1:
        return "January"
    elif month == 2:
        return "February"
    elif month == 3:
        return "March"
    elif month == 4:
        return "April"
    elif month == 5:
        return "May"
    elif month == 6:
        return "June"
    elif month == 7:
        return "July"
    elif month == 8:
        return "August"
    elif month == 9:
        return "September"
    elif month == 10:
        return "October"
    elif month == 11:
        return "November"
    elif month == 12:
        return "Descember"


def FetchDate():
    current_time = datetime.datetime.now()
    dd = current_time.day
    mm = current_time.month
    yyyy = current_time.year
    weekday = current_time.weekday()

    DayOfWeek = Extract_Day_Of_Week_From_Day(current_time)
    MonthOfYear = Extract_Month_of_the_Year(mm)

    SpeakOutput("Today is "+DayOfWeek + " "+str(dd) +
                " "+MonthOfYear+" "+str(yyyy))


# Fetch System time
def FetchTime():
    Time_hour = datetime.datetime.now()
    # %I is used for outputing Hours in 12 Hours Format
    # %M is used to output Minits
    # %p is used to display AMM/PM

    Time_hour_12 = Time_hour.strftime("%I:%M %p")
    SpeakOutput("The time is "+Time_hour_12)


def BatteryLevel():
    Battery = psutil.sensors_battery()
    SpeakOutput("Your Computer is at "+str(Battery.percent)+" %")


def MyName():
    username = GetUserLogin_Username()
    SpeakOutput("I am talking to "+username)


def Yourname():
    SpeakOutput("My Name is "+botname)


Greetings()


while True:
    query = TakUserInput().lower()
    if "command prompt" in query or "cmd" in query:
        SpeakOutput("Sure")
        OpenCMD()
    elif "cmd" in query:
        SpeakOutput("Sure")
        OpenCMD()

    elif "google chrome" in query:
        SpeakOutput("Sure")
        OpenChome()
    elif "chrome" in query:
        SpeakOutput("Sure")
        OpenChome()
    elif "camera" in query:
        SpeakOutput("Sure Press ESC to close and Space to Capture")
        TakePhoto()
    elif "what is my ip" in query:
        SpeakOutput("Sure")
        GetSystemIPAddress()
    elif "wikipedia" in query:
        Searchwikipedia(query=query)
    elif "youtube" in query:
        SpeakOutput("Sure Opening YouTube")
        OpenYouTube()
    elif "amazon" in query:
        SpeakOutput("Sure Opening Amazon India")
        OpenAmazon()
    elif "google" in query:
        GoogleSearch()
    elif "whatsapp" in query:
        SendWhatsAppMessage()
    elif "online video" in query:
        PlayVidoesOnYouTube()

    elif "what day is today" in query:
        FetchDay()
    elif "month" in query:
        FetchMonth()
    elif "year" in query:
        FetchYear()
    elif "date" in query:
        FetchDate()
    elif "battery" in query:
        BatteryLevel()

    elif "time" in query:
        FetchTime()
    elif "your name" in query:
        Yourname()
    elif "my name" in query:
        MyName()

    elif "no thinks " in query or "no" in query:
        SpeakOutput("Thank You for using "+botname+" Have a good day")
        sys.exit()
    SpeakOutput("Do you have any other question...")