import os
import sys
import time
import pyttsx3
import datetime
import webbrowser
import random
import pyjokes
import wikipedia
# import speech_recognition as sr
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty("voice",voices[0].id)
def speak(audio):
    """This function speak and say some thing that you want to be say to him"""
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
    """This function open the website in chrome with the url you don't have to add any https for link you can use like web("youtube.com")"""
    webbrowser.register('chrome', None,webbrowser.BackgroundBrowser("C:\\Program Files\\Google\Chrome\\Application\\chrome.exe"))
    webbrowser.get('chrome').open("https://"+url)
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
wishMe()
while True:
    input1=input("You: ")
# programs
    if input1 == "open google":
        speak("Opening chorme")
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
    elif input1 == "open word":
        speak("Opening microsoft word")
        os.startfile("C:\\Users\\ASUS\Desktop\\Word 2016.lnk")
    elif input1 == "open excel":
        speak("Opening microsoft excel")
        os.startfile("C:\\Users\\ASUS\Desktop\\Excel 2016.lnk")
    elif input1 == "open power point":
        speak("Opening microsoft power point")
        os.startfile("C:\\Users\\ASUS\Desktop\\PowerPoint 2016.lnk")
    elif input1 == "open repl":
        speak("Opening repl")
        web("replit.com/repls")
    elif input1 == "open notepad":
        speak("Opening notepad")
        os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.lnk")
    elif input1 == "open wordpad":
        speak("Opening wordpad")
        os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Wordpad.lnk")
    elif input1 == "open paint":
        speak("Opening paint")
        os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Paint.lnk")
    elif input1 == "open cmd":
        speak("Opening command prompt")
        os.startfile("C:\\Users\\ASUS\\AppData\\Roaming\\Microsoft\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk")
    elif input1 == "open control panel":
        speak("Opening control panel")
        os.startfile("C:\\Users\\ASUS\\AppData\\Roaming\\Microsoft\Windows\\Start Menu\\Programs\\System Tools\\Control Panel.lnk")
    elif input1 == "open run":
        speak("Opening run")
        os.startfile("C:\\Users\\ASUS\\AppData\\Roaming\\Microsoft\Windows\\Start Menu\\Programs\\System Tools\\Run.lnk")
    elif input1 == "open this pc":
        speak("Opening this pc")
        os.startfile("C:\\Users\\ASUS\\AppData\\Roaming\\Microsoft\Windows\\Start Menu\\Programs\\System Tools\\computer.lnk")
    elif input1 == "open powershell":
        speak("Opening powershell")
        os.startfile("C:\\Users\\ASUS\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Windows PowerShell\Windows PowerShell.lnk")
    elif input1 == "search youtube":
        speak("Enter the search for youtube")
        input11=input("Enter the search for youtube: ")
        speak("Searching "+input11)
        web("youtube.com/results?search_query="+input11)
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
    elif input1 == "open task manager":
        speak("Opening task manager")
        os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Task Manager.lnk")
    elif input1 == "check the performance":
        speak("Checking the computer performance")
        os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Task Manager.lnk")
    elif input1 == "check performance":
        speak("Checking the computer performance")
        os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Task Manager.lnk")
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
    elif input1 == "I am sad":
        speak("Don't worry sir I will open a website for duaa")
        web("quran.com/3/139?translations=20,85,101")
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
    elif input1 == "open google":
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
    elif input1 == "what is the date today":
        speak("The date is ")
        speak(datetime.datetime.now().date()
              )
    elif input1 == "what is the date":
        speak("The date is ")
        speak(datetime.datetime.now().date())
    elif input1 == "what is date today":
        speak("The date is ")
        speak(datetime.datetime.now().date())
    elif input1 == "remover":
        print("Hi welcome to remover")
        speak("Enter the path where you have to remove the file")
        input5 = input("Enter the path where you have to remove the file: ")
        time.sleep(2)
        speak("Removed succesfully")
        os.remove(input5)
    elif input1 == "writter":
        print("Hi Welcome to the writer software")
        speak("Enter the path")
        input6 = input("Enter the path: ")
        speak("Enter the text")
        input7 = input("Enter the text: ")
        root1 = open(input6, "a")
        root1.write(input7)
        root1.close()
        time.sleep(2)
        speak("Succesfully")
    elif input1 == "random choice":
        # here I imported random libary
        print("Welcome to the random choice")
        rn = int(input("Enter the number of things: "))
        # rn is the input range of things
        for rn in range(0, rn):
            things = input("Enter the thing: ")
            # And i am aadding for loop range 0 to rn input and i take input from the user for rn times
        random = random.randint(0, rn)
        # And i adding the random and randint to think a number between 1 to rn
        print(random)
        # And finally i printed the output
    elif input1 == "lists":
        print("Welcome to lists")
        speak("Enter the path")
        input8 = input("Enter the path: ")
        print(os.listdir(input8))
    elif input1 == "creater":
        print("Welcome to the creater")
        speak("Enter the path")
        input9 = input("Enter the path: ")
        root2 = open(input9, "x")
        root2.close()
        time.sleep(2)
        speak("Succesfully created")
    elif input1 == "rock paper sccisor":
        # here I imported the random library
        rand = random.randint(1, 3)
        # Here I told the computer to think 1 number to 3 number
        speak("Enter rock or paper or sccisor")
        inpu = input("Enter rock or paper or sccisor: ")
        if (rand == 1 and inpu == "sccisor" or rand == 2 and inpu == "rock" or rand == 3 and inpu == "paper"):
            speak("Computer Won")
            # here add computer win function
        elif (rand == 1 and inpu == "paper" or rand == 2 and inpu == "sccisor" or rand == 3 and inpu == "rock"):
            speak("user won")
            # Here I add user win function
        else:
            speak("draw")
            # here I add the draw function
        if (rand == 1):
            ad = "rock"
        elif (rand == 2):
            ad = "paper"
        else:
            ad = "sccisor"
        time.sleep(2)
        speak("Computer think number is ", rand, "is", ad)
    elif input1 == "exit":
        sys.exit()
    elif input1 == "search wikipedia":
        speak("Enter the word to search")
        input3=input("Enter the word to search: ")
        speak(f"Searching {input3} wikipedia")
        web("en.wikipedia.org/wiki/"+input3)
    elif input1 == "open":
        speak("Enter the link to open")
        input4 = input("Enter the link to open: ")
        speak(f"Opening {input4}")
        web(input4)
    elif input1 == "speak":
        speak("Enter the text to speak: ")
        input10=input("Enter the text to speak: ")
        speak(input10)
    elif input1 == "calculator":
        # here i print some message
        print("Welcome to the calculator")
        speak("Enter the first number: ")
        a = int(input("Enter the first number: "))
        speak("Enter the second number: ")
        b = int(input("Enter the second number: "))
        # here I take two input from the user and save the input a vairable int
        speak(f"The addition of the two numbers is {a + b}")
        speak(f"the subraction of two number is {a - b}")
        speak(f"the multipltion of two number is {a * b}")
        speak(f"the division of two number is { a / b}")
    elif input1 == "word length":
        speak("Enter the word to get the length of the word")
        input12=input("Enter the word to get the length of the word: ")
        speak(len(input12))
    elif input1 == "test passed":
        var=0
        for i in range(0,10):
            var+=1
            print(bcolors.OKGREEN+ f"✅ test {var} passed")
            time.sleep(1)
    elif input1 == "wikipedia":
        speak("Enter the word to search in wikipeedia")
        input12=input("Enter the word to search in wikipedia: ")
        result=wikipedia.summary(input12,sentences=2)
        speak(result)
    elif input1 == "search":
        speak("Enter the word to search: ")
        input2=input("Enter the word to search: ")
        speak(f"Searching {input2}")
        web("google.com/search?q="+input2+"&rlz=1C1GCEA_enSA966SA966&oq=s&aqs=chrome..69i57j0i131i433i512j46i131i199i433i465i512j69i60l4j69i61.1764j0j7&sourceid=chrome&ie=UTF-8")
    elif input1 == "hi jarvis":
        speak("Hi Muhammad Raiyaan sir")
    elif input1 == "who are you":
        speak("I am Jarvis")
    elif input1 == "tell me a joke":
        speak(pyjokes.get_joke())
    else:
        arra=["Sir didn't get try again",f"No result for {input1}"]
        speak(random.choice(arra))

