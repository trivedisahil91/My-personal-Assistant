import typing
import pyttsx3 #install package
import speech_recognition as sr  #install package sathe sathe microfone ne access karava mate pyaudio packege pan inatall kara vu pade
import datetime
import os
from requests import get #install package
import wikipedia
import webbrowser
import pywhatkit #install package
import smtplib #install package #read package
import sys
import time
import pyjokes#install package
import pyautogui
import requests
import instadownloader#install package
import PyPDF2 #install package
#install PyQt5
# install pyqt5-tools
#and desgine jarvis  help qt desginer and convert python file 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import instaloader #install package
import operator#for calculations using voice
# from PyQt5 import QtWidgets,QtCore,QtGui
# from PyQt5.QtCore import QObject, QTimer,QTime,QDate,Qt
# from PyQt5.QtGui import QMovie
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# from PyQt5.uic import loadUiType
# from jarvisui import Ui_JarvisUi
from bs4 import BeautifulSoup #install package bs4
import speedtest_cli #install package speedtest-cli
import speedtest






engine=pyttsx3.init('sapi5')#engine nu object banavel chhe
voices =engine.getProperty('voices')#voices ni property define karel chhe
engine.setProperty('voices',voices[0].id)#ahiya voices devil ni apava haru range ma 0 lidhel chhe jo bija ni voices joti hoy to 0 ni jagaya ye koy bijo number use kari sako total 3 voices chhe



# bolava mate speek module creat kariyu 
def speak(audio):
    engine.say(audio)# engine duwara audio ma raheli value bolay chhe 
    print(audio)# te audio print thay chhe 
    engine.runAndWait()#runandwaite atale ke te audio bolay ane print  thay jay tayar bad te thodik var ubhu rahe chhe  chhe



#for news
def news():
    # news name nu function chhe 
    main_url='http://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=7f3088b60fdf403ebd6c77daf826e198'
    # aa url  a news api.org nu chhe jaya thi chhele lakheli key te website thi lidhel chhe aa url main url veriabel ma store thay chhe
    main_page=requests.get(main_url).json()
    #main url dura maine page leva ni try kare chhe 

    articles=main_page["articles"]
    #main page mathi article j access karave chhe
    head=[]#list banavel chhe je emty chhe  
    day=["first","second","third","fourt","sixth","seven","eight","ninth","tenth"]
    # day name ni list chhe jema days lakhel chhe
    for ar in articles:# for loop ma articales lidha chhe je news  na main page upar hata 
        head.append(ar["title"])#have articales ma rahel maine title ne j head name ni empty list ma add karave chhe 
    for i in range (len(day)):#for loop ma top 10 news batavi chhe mate len(day) no upayog karo je day name ni upper list chhe
        speak(f"today's  {day[i]} news is : {head[i]}")#have te news ne speak user difine function duwara bolav dav se 



# to wish
def wish():
    hour=int(datetime.datetime.now().hour)#datetime.datetime.now(). hour ni mada thi curent hour integer ma hour name na virebel ma store thay chhe
    tt=time.strftime("%I:%M:%p")#time name na package ni madad thi curent time a tt name na veriable ma store kare chhe 
    if hour>=0 and hour<12:
        speak(f"Good Morning sir")#speek function thi ("message") peramiter ma rahel message bolay chhe
        speak(f"its time {tt}")#curent time bole chhe
    elif hour>=12 and hour<18:
        speak(f"Good Afternoon sir")
        speak(f"its time {tt}")
    else:
        speak(f"Good Evening sir")
        speak(f"its time {tt}")
    speak("i am jarvis sir please tell me sir how can i help you?")


#read pdf
def pdf_reader():
    speak("okey sir, please enter your pdf path")
    npath=input("enter your pdf path here :-")
    book = open(npath, "rb")
    pdfreader = PyPDF2.PdfFileReader(book)
    pages = pdfreader.numPages
    print(page)
    speak(f"total numbers of pages in theis pdf {pages}")
    print(f"total numbers of pages in theis pdf {pages}")
    speak("sir please enter the page number  i have to read")
    pg=int(input("Enter page number :- "))
    page= pdfreader.getPage(pg+1)
    text=page.extractText()
    speak(text)


# class MainThread(QThread):
#     def __init__(self):
#         super(MainThread,self).__init__()
    
#     def run(self):
#         TaskExecution()

    # voice ne speech ma convert kare chhe
def takecommand():
    r= sr.Recognizer()#recognizer package madad thi voice ne capture thay chhe
    with sr.Microphone() as source:#voice capture karava mate microphone ne source tarike lidhel chhe 
        print("Listening...")#khabar pade ke Listening kare chhe 
        r.pause_threshold = 1  # pause atala mate 1 aapiyu chhe karan ke vache 1 second mate user bole nay to aa stop na thay jay 1 second pachhi nu pan sabha de 
        audio=r.listen(source,timeout=1,phrase_time_limit=3)#listen function thi sabhadave chhe 

    try:
        print("recognizing...")# khabar pade ke recognize thay chhe
        query=r.recognize_google(audio,language='en-in')#speech recognition packege duwara (speech recognition.recognize.recognize_google) function thi audio ane language aapiye chhe
        print(f"user said {query}\n")# user je kay command aape te print thay ne aave 
    except Exception as e:# jo bolava ma kay error ave to except block run thay chhe 
        speak=("say that again please")
        return "None"
    return query

    

    # def sendEmail(to,content):
    #     server=smtplib.SMTP('smtp.gmail.com',587)
    #     server.ehlo()
    #     server.starttls()
    #     server.ehlo()
    #     server.login("<EMAIL>","<PASSWORD>")
    #     server.sendmail("<your EMAIL>",to,content)
    #     server.close()
    #     speak("email has been sent") 

    # def TaskExecution(self):
if __name__ == "__main__":
    wish()# wise function call thay chhe
    while True:
# if 1:
        query=takecommand().lower()

        #open youtube
        if "open youtube" in query:
            speak("okey sir, opening youtube")
            webbrowser.open("https://www.youtube.com//?feature=ytca")#webbrowser package ni madad thi open (url) open ni andar jeno url hoy te ni website khule chhe  

        #open notepad
        elif"open notepad" in query:
            speak("okey sir, opening notepad")
            npath="C:\\Windows\\notepad.exe"
            os.startfile(npath)
        
        #close notepad
        elif "close notepad" in query:
            speak("okey sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        #open command prompt
        elif "open command" in query or "open command prompt" in query:
            speak("okey sir, open command prompt")
            time.sleep(1)
            os.system("start cmd")
        
        #open command prompt
        elif "open c m d" in query:
            speak("okey sir, open command prompt")
            os.system("start cmd")       
        
        #my ip address
        elif "what is my ip address" in query:
            speak("okey sir,i will check your ip address")
            time.sleep(1)
            ip=get('http://api.ipify.org').text
            speak(f"sir  your ip address is {ip}")
        
        #open whatsapp
        elif "open whatsapp" in query:
            speak("okey sir, open whatsapp")
            webbrowser.open("https://web.whatsapp.com//")
        
        
        #serching data on wikipedia
        elif "wikipedia" in query:
            speak("serching wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            speak(results)
            print(results)
            
        #open instagram
        elif "open instagram" in query:
            speak("okey sir, open instagram")
            webbrowser.open("https://www.instagram.com//")
        
        #open fesbook
        elif "open facebook" in query:
            speak("okey sir, open Facebook")
            webbrowser.open("https://www.facebook.com//login//")
        
        #open gtu portal
        elif "open gtu portal" in query:
            speak("okey sir, open gtu portal")
            webbrowser.open("https://student.gtu.ac.in/Login.aspx")
        
        #open gtu syllabus
        elif "open gtu syllabus"in query:
            speak("okey sir, open open gtu syllabus")
            webbrowser.open("https://syllabus.gtu.ac.in//Syllabus.aspx?tp=DI")
        
        #open google and search data on google 
        elif "open google" in query:
            speak("sir, what should i search on google")
            cm=takecommand().lower()
            webbrowser.open(f"{cm}")
        
        #jarvis shutdown
        elif "you can sleep jarvis"in query:
            speak("I am always available for you sir")  
            speak("have a good day")
            sys.exit()
        
        #open vs code
        elif "open vs code" in query:
            speak("okey sir, open vs code")
            npath="C:\\Users\\91982\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(npath)
        
        #close vs code
        elif "close vs code" in query:
            speak("okey sir, closing notepad")
            os.system("taskkill /f /im Code.exe")
        
        #open setings
        elif "open seting" in query:
            speak("okey sir, open setings")
            npath="C:\\Users\\91982\\Desktop\\Settings.lnk"
            os.system(npath)
        
        #shutdown jarvis
        elif "shut down jarvis"in query:
            speak("I am always available for you sir")  
            speak("have a good day")
            sys.exit()
        
        #shutdown jarvis
        elif "you can sleep jarvis"in query:
            speak("I am always available for you sir")  
            speak("have a good day")
            sys.exit()
        # speak("sir,do you have any other work")
        
        #tell me jokes 
        elif "tell me jokes" in query:
            joke=pyjokes.get_joke()#pyjokes package ni madad thi jokes access thay chhe ane joke name na veriable ma store thay chhe 
            speak(joke)#te joke speak user difine function dwara bolay chhe
            
        
        #sutdown system
        elif "shut down the system" in query:
            speak("system is shut down")
            os.system("shutdown /s /t 5")
        
        #sutdown window
        elif "shut down window" in query:
            speak("system is shut down")
            os.system("shutdown /s /t 5")
        
        #restart the system
        elif "restart the system" in query:
            speak("system is shut down")
            os.system("shutdown /r /t 5")
        
        #restart the system 
        elif "restart the window" in query:
            speak("system is shut down")
            os.system("shutdown /r /t 5")
        
        #switch the window
        elif "switch the window" in query:
            speak("switch the window sir")
            pyautogui.keyDown("alt")# key down no matalab paramiter ma aapel value ne dabav jaya sudhi key up na kare taya sudhi te key down j rahe chhe
            pyautogui.press("tab")#tayar bad tab press thay chhe
            time.sleep(1)#te 1 second sudhi j press rahase
            pyautogui.keyDown("alt")# keydown atale je peramitar ma value aapel chhe te  ni key down kari le chhe
        
        #tell me news
        elif "tell me news" in query:
            speak ("please wait sir, feteching the letest news...")
            news()

        #location accessing
        elif "where i am" in query:
            speak("wite sir,let me check")
            try:
                ipadd=requests.get('https://api.ipify.org').text  #url na madad thi ip address return kare chhe 
                print(ipadd)# te ip address ne print kare chhe
                url='https://get.geojs.io/v1/ip/geo/'+ipadd+'.json' #https://get.geojs.io/v1/ip/geo/ aa website ip address add kar vathi badhi detile aave je thi aa ne aavij rite aaya mukel chhe +ipadd+ kari ne ane te apan ne jsfom jotu chhe te thi .json lakhayu chhe
                geo_request = requests.get(url)# reqest module ni madad thi get karel chhe 
                geo_data = geo_request.json()# ahi je data malel hato te ne aapade geo_request ma store karel hato te data aapan ne json formet ma joto chhe atale .json karel chhe 
                #json for mate atale te dictonary for mate ma convert karel hoy chhe
                city=geo_data['city']# te dictionary mathi city ni value ne access kari ne city name na veriable ma store kare chhe 
                country=geo_data['country']#te dictionary mathi country ni value ne access kari ne country name na veriable ma store kare chhe 
                speak(f"i am not sure but sir i think we are in {city} city of {country} country ")
            except Exception as e:
                speak("sorry sir , due to network issues i am not able to find where we are.")
                pass
        
        
        elif "open photos" in query:
            npath="C:\\Users\\91982\\Desktop\\Photos.lnk"
            os.startfile(npath)
        
        # elif "close photos" in query:
        #     speak("okey sir, closing notepad")
        #     os.system("taskkill /f /im photos.lnk")

        elif "open excel" in query:
            speak("okey sir, open excel")
            npath="C:\\Users\\91982\\Desktop\\Excel.lnk"
            os.startfile(npath)

        elif "open powerpoint" in query:
            speak("okey sir, open powerpoint")
            npath="C:\\Users\\91982\\Desktop\\PowerPoint.lnk"
            os.startfile(npath)

        elif "open access" in query:
            speak("okey sir, open access")
            npath="C:\\Users\\91982\\Desktop\\Access.lnk"
            os.startfile(npath)

        elif "open word" in query:
            speak("okey sir, open word")
            npath="C:\\Users\\91982\\Desktop\\Word.lnk"
            os.startfile(npath)
        
        elif "open microsoft" in query:
            speak("okey sir, open microsoft")
            npath="C:\\Users\\Public\\Desktop\\Microsoft Edge.lnk"
            os.startfile(npath)

        elif "open office" in query:
            speak("okey sir, open office")
            npath="C:\\Users\\91982\\Desktop\\Office.lnk"
            os.startfile(npath)

        elif "open publisher" in query:
            speak("okey sir, open publisher")
            npath="C:\\Users\\91982\\Desktop\\Publisher.lnk"
        
        elif "open a360 desktop" in query:
            speak("okey sir, open a360 desktop")
            npath="C:\\Users\\Public\\Desktop\\A360 Desktop.lnk"
            os.startfile(npath)

        elif "open pdf x" in query:
            speak("okey sir, open pdf x")
            npath="C:\\Users\\91982\\Desktop\\PDF X.lnk"

        elif "open express vpn" in query:
            speak("okey sir, open express vpn")
            npath="C:\\Users\\91982\\Desktop\\ExpressVPN.lnk"
            os.startfile(npath)

        elif "open spotify" in query:
            speak("okey sir, open spotify")
            npath="C:\\Users\\91982\\Desktop\\Spotify.lnk"
            os.startfile(npath)
        
        #any profile open 
        elif"instagram profile" in query or "check instagram profile" in query:
            speak("sir please enter the user name correctly")
            name =input("enter user name here:- ")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"sir here is the profile of the user {name}")
            time.sleep(5)
            speak(f"sir would you like to download profile picture of this account...")
            print(f"sir would you like to download profile picture of this account...")
            condition = takecommand().lower()
            if "yes" in condition:
                mod=instadownloader.instaloader()
                mod.download_profile(name,profile_pic_only=True)
                speak(f"i am done sir ,profile picture is saved in our folder . now i am ready to next command ...")
            else:
                pass
        
        elif"open instagram profile" in query:
            speak("sir please enter the user name correctly")
            name =input("enter user name here:- ")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"sir here is the profile of the user {name}")
            time.sleep(5)
            speak(f"sir would you like to download profile picture of this account...")
            print(f"sir would you like to download profile picture of this account...")
            condition = takecommand().lower()
            if "yes" in condition:
                mod=instadownloader.instaloader()
                mod.download_profile(name,profile_pic_only=True)
                speak(f"i am done sir ,profile picture is saved in our folder . now i am ready to next command ...")
            else:
                pass


        elif "take screenshot" in query or "take a screenshot" in query:
            speak("sir , please tell me the name for this screenshot file")
            name = takecommand().lower()
            speak("please sir hold for few seconds , i am taking a screenshot")
            time.sleep(3)
            ing=pyautogui.screenshot()
            ing.save(f"{name}.png")
            speak(f"i am done sir,the screenshot is saved in our folder. now i am ready to next command...")
        

        elif "how are you jarvis" in query:
            speak("i am fine sir , what about you")

        elif "how are you" in query:
            speak("i am fine sir , what about you")

        elif "open android studio" in query:
            npath="C:\\Users\\91982\\Desktop\\Android Studio.lnk"
            os.startfile(npath)


        elif "hello jarvis" in query:
            speak("hello sir , may i help you with something")

        elif "open playstore" in query:
            speak("okey sir, open playstore")
            webbrowser.open("https://play.google.com//store//games?device=windows")


        elif "i am also good" in query:
            speak("that's great to hear from you")

        elif "i am also fine" in query:
            speak("that's great to hear from you")
        
        elif "i am good" in query or "i am fine" in query:
            speak("that's great to hear from you")

        elif "thanks jarvis" in query:
            speak("it's my pleasure sir.")

        elif "open android studio" in query:
            speak("okey sir, open android studio")
            npath="C:\\Users\\91982\\Desktop\\Android Studio.lnk"
            os.startfile(npath)

        elif "search current temperature" in query:
            speak("please speak your current place")
            cm=takecommand().lower()
            search=f"temperature in {cm}"
            url=f"http://www.google.com/search?q={search}"
            r=requests.get(url)
            data=BeautifulSoup(r.text,"html.parser")
            temp=data.find("div",class_="BNeawe").text
            speak(f"sir current temperature is {temp}")


        elif "internet speed" in query or "check internet speed" in query:
            speak("okey sir i will check internet speed")
            import speedtest
            st=speedtest.Speedtest()
            dl=st.download()
            up=st.upload()
            speak(f"sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed")


        elif "tell me internet speed" in query:
            speak("okey sir i will check internet speed")
            import speedtest
            st=speedtest.Speedtest()
            dl=st.download()
            up=st.upload()
            speak(f"sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed")


        elif "please tell me about this laptop properties" in query or "properties of this laptop" in query:
            speak("okey sir i will checking this laptop properties")
            time.sleep(2)
            speak("Device name :- AcerAspire \n Processor ;- AMD Ryzen 5 5500U with Radeon Graphics 2.10 GHz \n Installed RAM :- 8.00 GB (7.34 GB usable) \n Device ID:-EF5DDD91-48A2-4903-860F-E8644A6CF49A \n Product ID :- 00356-24621-19197-AAOEM \n System type :- 64-bit operating system, x64-based processor")


    # elif "read this pdf" in query or "read a pdf" in query or "read pdf" in query:
    #     pdf_reader()

    # elif "send email" in query: 
    #     try:
    #         speak("sir, what should i send?")
    #         content=takecommand().lower()
    #         to="trivedik711@gmail.com"
    #         sendemail(to, content)
    #         speak("Email has been sent")
    #     except Exception as e:"C:\Users\91982\Downloads\DocScanner 27 Jun 2023 9-48 am (5).pdf"
    #         print(e)
    
    # elif "send message" in query:
    #     kit.sendmessage("+919712045867","message",2,25)
    # elif"play song on youtube" in query:
    # kit.playonyt("see you again")

# startExecution=MainThread()

# class Main(QMainWindow):

#     def __init__(self):
#         super().__init__()
#         ui=Ui_JarvisUi()
#         ui.setupUi(self)
#         ui.toolButton_2.clicked.connect(startTask)
#         ui.toolButton_3.clicked.connect(close)
 
#     def startTask(self):


#         ui.movie = QtGui.QMovie("../../Extara Gui/ExtraGui/initial.gif")
#         ui.GUI.setMovie(ui.movie)
#         ui.movie.start()


#         ui.movie = QtGui.QMovie("../../Extara Gui/ExtraGui/Earth_Template.gif")
#         ui.GUI_3.setMovie(ui.movie)
#         ui.movie.start()


#         ui.movie = QtGui.QMovie("../../Voive R/VoiceReg/__1.gif")
#         ui.RecodGUI.setMovie(ui.movie)
#         ui.movie.start()


#         ui.movie = QtGui.QMovie("../../../Downloads/O1SC.gif")
#         ui.GUI_6.setMovie(ui.movie)
#         ui.movie.start()
        
#         ui.movie = QtGui.QMovie("../../Extara Gui/ExtraGui/live.gif")
#         ui.GUI_IRON_MAN_2.setMovie(ui.movie)
#         ui.movie.start()

#         ui.movie = QtGui.QMovie("../../Extara Gui/ExtraGui/Hero_Template.gif")
#         ui.GUI_7.setMovie(ui.movie)
#         ui.movie.start()

#         ui.movie = QtGui.QMovie("../../Extara Gui/ExtraGui/B.G_Template_1.gif")
#         ui.GUI_4.setMovie(ui.movie)
#         ui.movie.start()

        

#         timer=QTimer(self)
#         timer=QTimer(self)
#         timer.timeout.connect(showTime)
#         timer.start(1000)
#         startExecution.start()

#     def showTime(self):
#         current_time=QTime.currentTime()
#         current_date=QDate.currentDate()

#         search="temperature in Rajkot"
#         url=f"http://www.google.com/search?q={search}"
#         r=requests.get(url)
#         data=BeautifulSoup(r.text,"html.parser")
#         temp=data.find("div",class_="BNeawe").text

#         label_time=current_time.toString('hh:mm:ss')
#         label_date=current_date.toString('dd/MM/yyyy')

#         ui.text_time.setText(label_time)
#         ui.Text_Date.setText(label_date)
#         ui.Text_Temp.setText(f"curent temp {temp}")


# app=QApplication(sys.argv)
# jarvis=Main()
# jarvis.show()
# exit(app.exec_())
