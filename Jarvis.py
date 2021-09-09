import os
import pyttsx3
import datetime
import webbrowser
import random
# import speech_recognition as sr
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty("voice",voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print("Jarvis:",audio)
# def takeCommand():
#     #It takes microphone input from the user and returns string output
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source)

#     try:
#         print("Recognizing...")    
#         query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
#         print(f"User said: {query}\n")  #User query will be printed.

#     except Exception as e:
#         # print(e)    
#         print("Say that again please...")   #Say that again will be printed in case of improper voice 
#         return "None" #None string will be returned
#     return query

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Muhammad Raiyaan sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Muhammad Raiyaan sir")
    else:
        speak("Good Evening Muhammad Raiyaan sir")
def web(url):
    webbrowser.register('chrome', None,webbrowser.BackgroundBrowser("C:\\Program Files\\Google\Chrome\\Application\\chrome.exe"))
    webbrowser.get('chrome').open("https://"+url)
wishMe()
while True:
    input1=input("You: ")
# programs
    if input1 == "open google":
        speak("Opening google")
        os.startfile("C:\\Program Files\\Google\Chrome\\Application\\chrome.exe")
    elif input1 == "open vs code":
        speak("Opening vs code")
        os.startfile("C:\\Users\\ASUS\\AppData\Local\\Programs\\Microsoft VS Code\Code.exe")
    elif input1 == "open zoom":
        speak("Opening zoom")
        os.startfile("C:\\Program Files (x86)\\Zoom\\bin\\Zoom.exe")
    elif input1 == "open pycharm":
        speak("Opening pycharm")
        os.startfile("C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.2.1\\bin\\pycharm64.exe")
    elif input1 == "open intellij idea":
        speak("Opening intellij idea")
        os.startfile("C:\\Program Files\\JetBrains\IntelliJ IDEA Community Edition 2021.2.1\\bin\\idea64.exe")
    elif input1 == "open edge":
        speak("Opening microsoft edge")
        os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
    elif input1 == "open dist":
        speak("Opening dist")
        os.startfile("D:\\coding\\Python\\dist")
    elif input1 == "what is time now":
        speak("the time is "+datetime.datetime.now().strftime("%H")+":"+datetime.datetime.now().strftime("%M"))
    elif input1 == "what is the time now":
        speak("the time is "+datetime.datetime.now().strftime("%H")+":"+datetime.datetime.now().strftime("%M"))
    elif input1 == "open web development":
        speak("Opening web development folder")
        os.startfile("D:\\coding\\Web development")
    elif input1 == "open coding":
        speak("Opening coding folder")
        os.startfile("D:\\coding")
    # website
    elif input1 == "open youtube":
        speak("Opening youtube")
        web("youtube.com")
    elif input1 == "open github":
        speak("Opening github")
        web("github.com/muhammedraiyaan2")
    elif input1 == "open backup github":
        speak("Opening backup github")
        web("github.com/muhammedraiyaan2/back-up-coding")
    elif input1 == "open github backup":
        speak("Opening github backup")
        web("github.com/muhammedraiyaan2/back-up-coding")
    elif input1 == "open github notes taking app":
        speak("Opening github notes taking app")
        web("github.com/muhammedraiyaan2/Notes-taking-app")
    elif input1 == "open server":
        speak("Opening server")
        web("github.com/muhammedraiyaan2/Server")
    elif input1 == "open drive backup":
        speak("Opening drive backup")
        web("drive.google.com/drive/quota")
    elif input1 == "open backup drive":
        speak("Opening drive backup")
        web("drive.google.com/drive/quota")
    elif input1 == "codewithharry":
        speak("Opening code with harry")
        web("youtube.com/results?search_query=codewithharry")
    elif input1 == "mansoor codes":
        speak("Opening mansoor codes")
        web("youtube.com/results?search_query=mansoor+codes")
    elif input1 == "dawood savage":
        speak("Opening Dawood savage")
        web("youtube.com/results?search_query=Dawood+Savage")
    elif input1 == "noor bhai":
        speak("Opening noor bhai")
        web("youtube.com/results?search_query=noor+bhai")
    elif input1 == "open analog clock":
        speak("Opening analog clock")
        web("muhammedraiyaan2.github.io/analog-clock")
    elif input1 == "open notes taking app":
        speak("Opening Notes taking app")
        web("muhammedraiyaan2.github.io/Notes-taking-app/")
    elif input1 == "open java sheet":
        speak("Opening java cheatsheet")
        web("muhammedraiyaan2.github.io/java-sheet/")
    elif input1 == "open html sheet":
        speak("Opening html cheatsheet")
        web("codewithharry.com/blogpost/html-cheatsheet")
    elif input1 == "open css sheet":
        speak("Opening css cheatsheet")
        web("codewithharry.com/blogpost/css-cheatsheet")
    elif input1 == "open javascript sheet":
        speak("Opening javascript cheatsheet")
        web("codewithharry.com/blogpost/javascript-cheatsheet")
    elif input1 == "open c sheet":
        speak("Opening c cheatsheet")
        web("codewithharry.com/blogpost/c-cheatsheet")
    elif input1 == "open c++ sheet":
        speak("Opening c++ cheatsheet")
        web("codewithharry.com/blogpost/cpp-cheatsheet")
    elif input1 == "open python sheet":
        speak("Opening python cheatsheet")
        web("codewithharry.com/blogpost/python-cheatsheet")
    elif input1 == "open php sheet":
        speak("Opening php cheatsheet")
        web("codewithharry.com/blogpost/php-cheatsheet")
    elif input1 == "open lido":
        speak("Opening lido learning")
        web("student.lidolearning.com/dashboard")
    elif input1 == "open ebeam":
        speak("Opening ebeam portal")
        web("ebeam.sunbeamschool.org/d2l/home/6660")
    elif input1 == "open whatsapp":
        speak("Opening whatsapp")
        web("web.whatsapp.com")
    elif input1 == "open youtube":
        speak("Opening youtube")
        web("youtube.com")
    elif input1 == "open bootstrap":
        speak("Opening bootstrap")
        web("getbootstrap.com")
    elif input1 == "open tailwind css":
        speak("Opening tailwind css")
        web("tailwindcss.com")
    elif input1 == "open tailblocks":
        speak("Opening tailblocks")
        web("tailblocks.cc")
    elif input1 == "open wikipedia":
        speak("Opening wikipedia")
        web("en.wikipedia.org")
    elif input1 == "open amazon in":
        speak("Opening amazon india")
        web("amazon.in")
    elif input1 == "open amazon sa":
        speak("Opening amazon saudi arabia")
        web("amazon.sa")
    elif input1 == "open amazon us":
        speak("Opening amazon america")
        web("amazon.us")
    elif input1 == "open readme.so":
        speak("Opening readme.so")
        web("readme.so")
    elif input1 == "open compressor":
        speak("Opening compressor")
        web("compressjpeg.com")
    elif input1 == "open header link":
        speak("Opening header link")
        web("muhammedraiyaan2.github.io/header-link")
    # google
    elif input1 == "open google.com":
        speak("Opening google")
        web("google.com")
    elif input1 == "open google fonts":
        speak("Opening google fonts")
        web("fonts.google.com")
    elif input1 == "open google word":
        speak("Opening google word")
        web("docs.google.com")
    elif input1 == "open google excel":
        speak("Opening google excel")
        web("docs.google.com/spreadsheets/u/0/")
    elif input1 == "open google excel":
        speak("Opening google excel")
        web("docs.google.com/spreadsheets/u/0/")
    elif input1 == "open google power point":
        speak("Opening google power point")
        web("docs.google.com/presentation/u/0/")
    elif input1 == "open google keep":
        speak("Opening google keep")
        web("keep.google.com")
    elif input1 == "open google meet":
        speak("Opening google meet")
        web("meet.google.com")
    elif input1 == "open google chat":
        speak("Opening google chat")
        web("chat.google.com")
    elif input1 == "open google drive":
        speak("Opening google drive")
        web("drive.google.com")
    elif input1 == "open google photos":
        speak("Opening google photos")
        web("photos.google.com")
    elif input1 == "open gmail":
        speak("Opening gmail")
        web("mail.google.com")
    elif input1 == "open google contact":
        speak("Opening google contact")
        web("contact.google.com")
    elif input1 == "open google calendar":
        speak("Opening google calendar")
        web("calendar.google.com")
    elif input1 == "open google duo":
        speak("Opening google duo")
        web("duo.google.com")
    elif input1 == "open google translatete":
        speak("Opening google translate")
        web("translate.google.com")
    elif input1 == "open google hangouts":
        speak("Opening google hangouts")
        web("hangouts.google.com")
    elif input1 == "search wikipedia":
        input3=input("Enter the word to search: ")
        speak("Searching wikipedia...")
        web("en.wikipedia.org/wiki/"+input3)
    elif input1 == "open":
        input4 = input("Enter the link to open: ")
        speak("Opening..."+input4)
        web(input4)
    elif input1 == "calculator":
        # here i print some message
        print("Welcome to the calculator")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        # here I take two input from the user and save the input a vairable int
        print("The addition of the two numbers is", a + b)
        print("the subraction of two number is", a - b)
        print("the multipltion of two number is", a * b)
        print("the division of two number is", a / b)
    elif input1 == "search":
        input2=input("Enter the word to search: ")
        speak("Searching...")
        web("google.com/search?q="+input2+"&rlz=1C1GCEA_enSA966SA966&oq=s&aqs=chrome..69i57j0i131i433i512j46i131i199i433i465i512j69i60l4j69i61.1764j0j7&sourceid=chrome&ie=UTF-8")
    elif input1 == "hi jarvis":
        speak("Hi Muhammad Raiyaan sir")
    elif input1 == "who are you":
        speak("I am Jarvis")
    else:
        speak("Sir didn't get try again")

