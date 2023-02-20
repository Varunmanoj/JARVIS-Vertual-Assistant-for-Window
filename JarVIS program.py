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
import nltk
from nltk.chat.util import Chat, reflections


# Global Variables
botname = "JARVIS"


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


def OpenWord():
    path = "C:\Program Files\Microsoft Office\root\Office16\\WINWORD.exe"
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
    match month:
        case 1:
         SpeakOutput("The Current Month is January")
        case 2:
            SpeakOutput("The Current Month is February")
        case 3:
            SpeakOutput("The Current Month is March")
        case 4:
            SpeakOutput("The Current Month is April")
        case 5:
            SpeakOutput("The Current Month is May")
        case 6:
            SpeakOutput("The Current Month is June")
        case 7:
            SpeakOutput("The Current Month is July")
        case 8:
            SpeakOutput("The Current Month is Augest")
        case 9:
            SpeakOutput("The Current Month is September")
        case 10:
            SpeakOutput("The Current Month is October")
        case 11:
            SpeakOutput("The Current Month is November")
        case 12:
            SpeakOutput("The Current Month is Descember")


def FetchDay():
    weekday = datetime.datetime.now().weekday()
    match weekday:
        case 0:
            SpeakOutput("Today is is Monday")
        case 1:
            SpeakOutput("Today is Tuesday")
        case 2:
            SpeakOutput("Today is Wednessday")
        case 3:
            SpeakOutput("Today is Thirsday")
        case 4:
            SpeakOutput("Today is Friday")
        case 5:
            SpeakOutput("Today is Saturday")
        case 6:
            SpeakOutput("Today is Sunday")


def Extract_Day_Of_Week_From_Day(day):
    day = day.weekday()
    match day:
        case 0:
            return "Monday"
        case 1:
            return "Tuesday"
        case 2:
            return "Wednessday"
        case 3:
            return "Thursday"
        case 4:
            return "Friday"
        case 5:
            return "Saturday"
        case 6:
            return "Sunday"


def Extract_Month_of_the_Year(month):
    match month:
        case 1:
            return "January"
        case 2:
            return "February"
        case 3:
            return "March"
        case 4:
            return "April"
        case 5:
            return "May"
        case 6:
            return "June"
        case 7:
            return "July"
        case 8:
            return "August"
        case 9:
            return "September"
        case 10:
            return "October"
        case 11:
            return "November"
        case 12:
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
    
def responses():
    query = TakUserInput().lower()
    if "command prompt" in query or "cmd" in query:
        OpenCMD()
        return 'cmd'
    elif "google chrome" in query or "chrome" in query:
        OpenChome()
        return 'chrome'
    elif "camera" in query:
        TakePhoto()
        return 'camera'
    elif "what is my ip" in query or "ip" in query:
        GetSystemIPAddress()
        return 'ip'
    elif "wikipedia" in query:
        Searchwikipedia(query=query)
        return 'wiki'
    elif "youtube" in query:
        OpenYouTube()
        return 'youtube'
    elif "amazon" in query:
        OpenAmazon()
        return 'amazon'
    elif "google" in query:
        GoogleSearch()
        return 'google'
    elif "whatsapp" in query:
        SendWhatsAppMessage()
        return 'whatsapp'
    elif "online video" in query:
        PlayVidoesOnYouTube()
        return 'video'

    elif "what day is today" in query:
        FetchDay()
        return 'day'
    elif "month" in query:
        FetchMonth()
        return 'month'
    elif "year" in query:
        FetchYear()
        return 'year'
    elif "date" in query:
        FetchDate()
        return 'date'
    elif "battery" in query:
        BatteryLevel()
        return 'battery'

    elif "time" in query:
        FetchTime()
        return 'time'
    elif "your name" in query:
        Yourname()
        return 'your name'
    elif "my name" in query:
        MyName()
        return 'my name'

    elif "no thanks " in query or "no" in query or "goodbye":
        return 'exit'
    else:
        return query
    
greeting_1 = "My name is "+botname+", how can I help you today?"
farewell = "Thank You for using "+botname+". Have a nice day!"
greeting_2 = "Hello! "+  str(os.getlogin)
greeting_3 = "Hi there! " + str(os.getlogin)
        
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?"]
    ],
    [
        r"cmd",
        ["Opening Command prompt!"]
     ],
    [   
        r"chrome",
        ["Opening Google Chrome!"]
     ],
    [
        r"camera|wiki|amazon|ip|youtube|google|month|day|date|battery|whatsapp|video",
        [""]
     ],
    [
        r"hi  (.*)|hello  (.*)|hey  (.*)",
        [greeting_2, greeting_3 ]
    ],
    [
        r"how are you  (.*)",
        ["I'm doing well, thank you for asking."]
    ],
    [
        r"what is your name",
        [greeting_1]
    ],
    [
        r"exit",
        [farewell]
    ],
    [
        r"I am sleepy  (.*)|I am tired  (.*)|I am bored  (.*)|I am exhausted  (.*)",
        ["You should take a short rest!"]
    ],
    [
        r"I am happy|I am joyful|joy",
        ["Thats great!"]
    ],
    [
        r"(.*) favourite movie|movie you enjoy(.*) |(.*) movies you like|(.*) movie you like|(.*) like any movie",
        ["I don't watch any movie but I would say the Godfather!"]
    ],
    [
        r"(.*) coffee|(.*) tea|(.*) drink",
        ["I enjoy drinking herbal tea!"]
    ],
    [
        r"(.*) sweet|(.*) sweets|(.*) chocolate",
        ["Though too many sweets may not be good for health, it is ok to have them once in a while. I like Dairy Milk chocolates"]
    ],
    [
        r"(.*) favourite music|(.*) music you enjoy|(.*) music you like|(.*) like any music",
        ["Though I am just an AI, I enjoy Pop music!!!"]
    ],
    [
        r"(.*) animal",
        ["I love playing with dogs but even cats are cute"]
    ],
    [
        r"(.*) father|(.*) mother|(.*) brother|(.*) sister|(.*) sibling|(.*) siblings|(.*) parent|(.*) parents|(.*) cousin|(.*) family|(.*) relative",
        ["As I am an AI, I dont have any relatives."]
    ],
    [
        r"(.*) favourite sport|(.*) sports you enjoy|(.*) sport you like|(.*) like any sport",
        ["I enjoy watching hockey matches!"]
    ]
    
]

chatbot = Chat(pairs, reflections)



Greetings()



while True:
    text = responses()
    if text.lower() == 'exit':
        response = chatbot.respond(text)
        #print(response)
        SpeakOutput(response)
        break
        sys.exit()
        
    response = chatbot.respond(text)
    #print(response)
    SpeakOutput(response)
    
    SpeakOutput("Do you have any other question...")