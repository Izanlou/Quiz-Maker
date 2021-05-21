#Codoffee-Quiz-Maker:--------------------------------------------------------------------------------------------------------------------------------------------------
#import-packages:------------------------------------------------------------------------------------------------------------------------------------------------------
import playsound
import time
import os
import turtle as t
import tkinter as tk
import ftplib
import jdatetime
from turtle import mainloop, Turtle
from datetime import datetime
from threading import Thread
from tkinter import filedialog
from tkinter import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#start-progress:-------------------------------------------------------------------------------------------------------------------------------------------------------
m=t.Turtle()
m.ht()
dcw=t.Turtle()
dcw.ht()
try:
    #GUI1 making:
    t.setup(410,410)
    t.title("Codoffee Quiz Maker 1.6 | آزمون ساز کدفي 1.6")
    t.speed(0)
    t.ht()
    scr=t.Screen()
    file=open("db1.db")
    bg_color=file.read()
    file.close()
    file=open("db2.db")
    p_color=file.read()
    file.close()
    file=open("db3.db")
    b_color=file.read()
    file.close()
    file=open("db4.db")
    t_v=file.read()
    file.close()
    t.bgcolor("#ffffb3")
    t.pencolor("gray")
    t.write("C",align="center",font=("impact",50))
    time.sleep(0.2)
    t.undo()
    t.pencolor("brown")
    t.write("CO",align="center",font=("impact",50))
    time.sleep(0.2)
    t.undo()
    t.pencolor("gray")
    t.write("COD",align="center",font=("impact",50))
    time.sleep(0.2)
    t.undo()
    t.pencolor("brown")
    t.write("CODO",align="center",font=("impact",50))
    time.sleep(0.2)
    t.undo()
    t.pencolor("gray")
    t.write("CODOFF",align="center",font=("impact",50))
    time.sleep(0.2)
    t.undo()
    t.pencolor("brown")
    t.write("CODOFFEE",align="center",font=("impact",50))
    time.sleep(0.2)
    t.pu()
    t.goto(0,-40)
    t.pd()
    t.pencolor("darkblue")
    t.write("Quiz Maker",align="center",font=("Comic Sans MS",30,("bold")))
    t.pu()
    t.goto(0,-178)
    t.pd()
    t.pencolor("black")
    t.write("© 2018 Codoffee | All rights reserved.",align="center",font=("Arial",7,("bold")))
    t.pu()
    t.goto(0,-195)
    t.pd()
    t.pencolor("black")
    t.write(".تمامي حقوق اين نرم افزار محفوظ است",align="center",font=("B Tite",10))
    playsound.playsound("Codoffee Audio.mp3")
    t.pensize(1)
    file=open("db4.db")
    t_j_o=file.read()
    file.close()
    if(t_j_o=="0"):
        t.clear()
        t.title("Sign-in | ورود")
        t.pu()
        t.goto(0,-10)
        t.pd()
        t.bgcolor("#66cc66")
        t.pencolor("purple")
        t.write("Sign-in",align="center",font=("Impact",35))
        t.pu()
        t.goto(-2,-60)
        t.pd()
        t.pencolor("darkblue")
        t.write("ورود",align="center",font=("B Titr",25))
        numw=t.Turtle()
        numw.pu()
        numw.goto(-30,-138)
        numw.pd()
        numw.ht()
        numw.write("1",align="center",font=("Impact",11))
        your_name=t.textinput("Sign-in | ورود","Name and Family Name | *Enter in english only*:    \n:*نام و نام خانوادگي، *الزاما انگليسي وارد کنيد    ")
        numw.forward(10)
        numw.write("2",align="center",font=("Impact",11))
        account=t.textinput("Sign-in | ورود","Account Type (Student/Teacher):    \n:نوع حساب (دانش آموز/معلم)    ")
        numw.forward(10)
        numw.write("3",align="center",font=("Impact",11))
        if(account=="دانش آموز")or(account=="دانشاموز"):
            account="student"
        elif(account=="معلم"):
            account="teacher"
        language=t.textinput("Sign-in | ورود","Language (English/فارسي):    \n:زبان (انگليسي/فارسي)    ")
        if(language=="فارسي"):
            language="persian"
        elif(language=="انگليسي"):
            language="english"
        if(account.lower()=="student"):
            numw.forward(10)
            numw.write("4",align="center",font=("Impact",11))
            teacher_name_u=t.textinput("Sign-in | ورود","Teacher's Name | *Enter in english only*:    \n:*نام معلم، *الزاما انگليسي وارد کنيد    ")
            numw.forward(10)
            numw.write("5",align="center",font=("Impact",11))
            id_have_s=t.textinput("Sign-in | ورود","Does your teacher have CodoffeeID?(yes/no):  \n:آيا معلم شما کدفي آيدي دارد؟(بله/خير)    ")
            if(id_have_s=="yes")or(id_have_s=="بله"):
                numw.forward(10)
                numw.write("6",align="center",font=("Impact",11))
                while True:
                    teacher_id_u=t.textinput("Sign-in | ورود","Teacher's Codoffee ID | *Enter in english only*:  \n:*کدفي آيدي معلم، *الزاما انگليسي وارد کنيد    ")
                    numw.forward(10)
                    numw.write("7",align="center",font=("Impact",11))
                    try:
                        ftp=ftplib.FTP("ftpupload.net","cldff_22998458","arizamir")
                    except:
                        playsound.playsound("12.mp3")
                        exit()
                    try:
                        ftp.cwd("htdocs/"+teacher_id_u)
                        break
                    except:
                        playsound.playsound("17.mp3")
                        exit()
                file=open("db10.db",'w')
                file.write(teacher_id_u)
                file.close()
            else:
                numw.forward(10)
                numw.write("6",align="center",font=("Impact",11))
            classroom_u=t.textinput("Sign-in | ورود","Classroom | *Enter in english only*:    \n:*نام کلاس، *الزاما انگليسي وارد کنيد    ")
            if(classroom_u==""):
                classroom_u="نال"
            if(teacher_name_u==""):
                teacher_name_u="نال"
            file=open("db5.db","w")
            file.write(your_name)
            file.close()
            file=open("db6.db","w")
            file.write(account)
            file.close()
            file=open("db7.db","w")
            file.write(teacher_name_u)
            file.close()
            file=open("db8.db","w")
            file.write(classroom_u)
            file.close()
            file=open("db9.db","w")
            file.write(language)
            file.close()
        else:
            file=open("db5.db","w")
            file.write(your_name)
            file.close()
            file=open("db6.db","w")
            file.write(account)
            file.close()
            file=open("db9.db","w")
            file.write(language)
            file.close()
        numw.clear()
    elif(t_j_o!="1"):
        file=open("db4.db","r")
        salamak_m=file.readline()
        hh=file.readline()
        gghrt=file.read()
        file.close()
        file=open("db4.db","w")
        file.write(gghrt)
        file.close()
        t.title("Sending result... | ...ارسال نتيجه")
        t.clear()
        t.setup(620,510)
        t.bgcolor(bg_color)
        m.speed(0)
        m.ht()
        file=open("db4.db","r")
        ID_show=file.read()
        file.close()
        uitwqe=""
        ID_show_m=""
        for joooooapppp in range(0,len(ID_show)):
            if(ID_show[joooooapppp]=="-"):
                uitwqe=int(uitwqe)-984
                ID_show_m+=chr(uitwqe)
                uitwqe=""
            else:
                uitwqe+=ID_show[joooooapppp]
        ID_show=ID_show_m
        m.clear()
        m.pu()
        m.goto(0,15)
        m.pd()
        m.pencolor("brown")
        m.write("Sending result...",align="center",font=("Copperplate Gothic Bold",15))
        m.pu()
        m.goto(0,-15)
        m.pd()
        m.pencolor("pink")
        m.write("...ارسال نتيجه",align="center",font=("B Nazanin",15,("bold")))
        playsound.playsound("9.mp3")
        import email.mime.text
        import smtplib
        while True:
            try:        
                def send_email (admin, pwd, user, message):
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login(admin, pwd)
                    server.sendmail(admin, user, message)
                    server.close()
                msg = email.mime.text.MIMEText(ID_show, _charset="UTF-8")
                send_email('codoffee@gmail.com', 'codoffeemenallah', salamak_m, msg.as_string())
                file=open("db4.db","w")
                file.write("1")
                file.close()
                m.clear()
                m.pu()
                m.goto(0,15)
                m.pd()
                m.pencolor("brown")
                m.write("Sending finished.",align="center",font=("Copperplate Gothic Bold",15))
                m.pu()
                m.goto(0,-15)
                m.pd()
                m.pencolor("pink")
                m.write(".ارسال پايان يافت",align="center",font=("B Nazanin",15,("bold")))
                playsound.playsound("11.mp3")
                break
            except:
                t.title("Error")
                m.clear()
                m.pu()
                m.goto(0,40)
                m.pd()
                m.pencolor("darkorange")
                m.write("Sorry, The internet aren't talking\nright now. Please check connection.",align="center",font=("Copperplate Gothic Bold",15))
                m.pu()
                m.goto(0,-35)
                m.pd()
                m.pencolor("orange")
                m.write(".متاسفيم، ارتباطات درون شبکه موجود نمي باشد\n.لطفا ارتباطات را بررسي کنيد",align="center",font=("B Nazanin",15,("bold")))
                playsound.playsound("12.mp3")
    #GUI2 making:
    file=open("db6.db")
    t_or_s=file.read()
    file.close()
    #teacher:
    file=open("db9.db","r")
    language=file.read()
    file.close()
    if(language.lower()=="english"):
        if(t_or_s.lower()=="teacher"):
            m.clear()
            t.title("Codoffee Quiz Maker 1.6 | Teacher Account")
            t.setup(620,510)
            m.ht()
            m.speed(0)
            t.clear()
            t.bgcolor(bg_color)
            t.pencolor("black")
            t.fillcolor("#001a1a")
            t.pu()
            t.goto(-310,210)
            t.pd()
            t.goto(310,210)
            t.pu()
            t.goto(-310,215)
            t.pd()
            t.goto(310,215)
            t.pu()
            t.goto(-310,220)
            t.pd()
            t.begin_fill()
            t.goto(310,220)
            t.goto(310,255)
            t.goto(-310,255)
            t.goto(-310,220)
            t.end_fill()
            t.pu()
            t.goto(-310,-190)
            t.pd()
            t.goto(310,-190)
            t.pu()
            t.goto(-310,-195)
            t.pd()
            t.goto(310,-195)
            t.pu()
            t.goto(-310,-200)
            t.pd()
            t.goto(310,-200)
            t.pu()
            t.goto(-310,-205)
            t.pd()
            t.goto(310,-205)
            t.pu()
            t.goto(-310,-210)
            t.pd()
            t.begin_fill()
            t.goto(310,-210)
            t.goto(310,-255)
            t.goto(-310,-255)
            t.goto(-310,-210)
            t.end_fill()
            button1=Turtle("square")
            button1.speed(0)
            button1.pu()
            button1.goto(20,-197)
            button1.pd()
            button1.shapesize(1.6)
            try:
                button1.fillcolor("light"+b_color)
            except:
                button1.fillcolor(b_color)
            t.pu()
            t.goto(23,-242)
            t.pd()
            try:
                t.pencolor("dark"+b_color)
            except:
                t.pencolor(b_color)
            t.write("Start!",align="center",font=("Comic Sans MS",15))
            time.sleep(0.2)
            t.undo()
            t.pu()
            t.goto(33,-242)
            t.pd()
            t.write("Start!",align="center",font=("Comic Sans MS",15))
            time.sleep(0.2)
            t.undo()
            t.pu()
            t.goto(13,-242)
            t.pd()
            t.write("Start!",align="center",font=("Comic Sans MS",15))
            time.sleep(0.2)
            t.undo()
            t.pu()
            t.goto(23,-242)
            t.pd()
            t.write("Start!",align="center",font=("Comic Sans MS",15))
            button2=Turtle("square")
            button2.speed(4)
            button2.pu()
            button2.goto(-40,225)
            button2.pd()
            button2.shapesize(1.2)
            try:
                button2.fillcolor("dark"+p_color)
            except:
                try:
                    button2.fillcolor("light"+p_color)
                except:
                    button2.fillcolor(p_color)
            button2.left(360)
            t.pu()
            t.goto(-39,192)
            t.pd()
            t.pencolor(p_color)
            t.write("Personalize!",align="center",font=("Comic Sans MS",10))
            button3=Turtle("triangle")
            button3.speed(0)
            button3.pu()
            button3.goto(170,-197)
            button3.pd()
            button3.shapesize(1.5)
            button3.fillcolor("#ac3973")
            t.pu()
            t.goto(177,-236)
            t.pd()
            t.pencolor("#ac3973")
            t.write("Quizes",align="center",font=("Comic Sans MS",10))
            button4=Turtle("circle")
            button4.speed(0)
            button4.pu()
            button4.goto(-134,-197)
            button4.pd()
            button4.shapesize(1.5)
            button4.fillcolor("#666699")
            t.pu()
            t.goto(-132,-236)
            t.pd()
            t.pencolor("#666699")
            t.write("Help",align="center",font=("Comic Sans MS",10))
            button5=Turtle("triangle")
            button5.speed(0)
            button5.pu()
            button5.goto(40,222)
            button5.pd()
            button5.left(90)
            button5.shapesize(1.5)
            button5.fillcolor("lightblue")
            t.pu()
            t.goto(42,192)
            t.pd()
            t.pencolor("darkblue")
            t.write("Info",align="center",font=("Comic Sans MS",10))
            button6=Turtle()
            image = "Logo.gif"
            scr.addshape(image)
            button6.shape(image)
            button6.speed(0)
            button6.pu()
            button6.goto(95,225)
            button6.pd()
            button6.left(90)
            button6.shapesize(2)
            t.pu()
            t.goto(95,192)
            t.pd()
            t.pencolor("red")
            t.write("ID",align="center",font=("Comic Sans MS",10))
            button7=Turtle()
            image = "cloud.gif"
            scr.addshape(image)
            button7.shape(image)
            button7.speed(0)
            button7.pu()
            button7.goto(-260,-200)
            button7.pd()
            button7.left(45)
            button7.shapesize(1.3)
            try:
                file=open("db10.db","r")
                datacl=file.read()
                file.close()
                button8=Turtle()
                image = "sun.gif"
                scr.addshape(image)
                button8.shape(image)
                button8.speed(0)
                button8.pu()
                button8.goto(-235,-180)
                button8.pd()
                button8.left(45)
                button8.shapesize(1)
            except:
                pass
            t.pu()
            t.goto(-260,-235)
            t.pd()
            t.pencolor("#ffcc00")
            t.write("Cloud",align="center",font=("Comic Sans MS",11))
            if(t_v=="0"):
                m.pu()
                m.goto(0,70)
                m.pd()
                m.pencolor("brown")
                m.write("Welcome;",align="center",font=("Copperplate Gothic Bold",15))
                m.pu()
                m.goto(0,50)
                m.pd()
                m.pencolor("black")
                m.write("To the Codoffee Quiz Maker!",align="center",font=("Copperplate Gothic Bold",15))
                playsound.playsound("2.mp3")
                m.pu()
                m.goto(0,30)
                m.pd()
                m.write("Click on {Help} button for learn.",align="center",font=("Copperplate Gothic Bold",15))
                playsound.playsound("3.mp3")
                file=open("db4.db","w")
                file.write("1")
                file.close()
            #onclick buttons
            def buton1(x,y):
                m.clear()
                m.pu()
                m.goto(0,20)
                m.pd()
                m.pencolor("brown")
                m.write("Getting ready...",align="center",font=("Copperplate Gothic Bold",15))
                time.sleep(2)
                m.clear()
                m.pu()
                m.goto(0,20)
                m.pd()
                m.pencolor("darkblue")
                m.write("Please select exam's location.",align="center",font=("Copperplate Gothic Bold",15))
                name_exam_w= Tk()
                name_exam_w.withdraw()
                name_exam_w.filename=filedialog.asksaveasfilename(initialdir = "/",title = "Select exam's location.",filetypes = (("Quiz Maker Exam file","*.QME"),("all files","*.*")))
                name_exam_t=name_exam_w.filename+".QME"
                bbiu="0"
                try:
                    file=open(name_exam_t,"r")
                    file.read()
                    file.close()
                    m.clear()
                    m.pu()
                    m.goto(0,20)
                    m.pd()
                    m.pencolor("darkorange")
                    bbiu="1"
                    m.write("Sorry, you have already an exam with\nthis location.",align="center",font=("Copperplate Gothic Bold",15))
                    playsound.playsound("13.mp3")
                except:
                    m.clear()
                    m.pu()
                    m.goto(0,20)
                    m.pd()
                    m.pencolor("darkblue")
                    m.write("Please enter your e-mail address.",align="center",font=("Copperplate Gothic Bold",15))
                    mail_of_u=t.textinput("Creating Exam","Your mail: ")+"\n"
                    mail_of_u_m=""
                    for joooapp in range(0,len(mail_of_u)):
                        mail_of_u_m+=str(ord(mail_of_u[joooapp])+835)+"-"
                    m.clear()
                    m.pu()
                    m.goto(0,20)
                    m.pd()
                    m.pencolor("darkblue")
                    m.write("Please choose a password/pincode for it.",align="center",font=("Copperplate Gothic Bold",15))
                    passw_of_e="$"+t.textinput("Creating Exam","Password/Pincode: ")+"$"
                    passw_of_e_m=""
                    for jooooapp in range(0,len(passw_of_e)):
                        passw_of_e_m+=str(ord(passw_of_e[jooooapp])+835)+"-"
                    file=open(name_exam_t,"w")
                    file.write(mail_of_u_m+"\n")
                    file.close()
                if(t_j_o=="0"):
                    m.clear()
                    m.pu()
                    m.goto(0,130)
                    m.pd()
                    m.pencolor("brown")
                    m.write("Serious;",align="center",font=("Copperplate Gothic Bold",15))
                    m.pu()
                    m.goto(-50,-140)
                    m.pd()
                    m.pencolor("black")
                    m.write('''
                    In every step, you should enter a question.
                    For every question, you should enter that's
                    correct answer. If you use choice question
                    type, you have 3 step for make a question:
                    1-Designing question.
                    2-Designing choices answer for it.
                    3-Define the correct answer.
                    ** don't use {?} between question, you can
                    use it in the end of question. **
                    Type {done} or nothing instead question for
                    conserve your exam and exit from portal.
                    ''',align="center",font=("Copperplate Gothic Bold",15))
                    playsound.playsound("15.mp3")
                counter=1
                wq=t.Turtle()
                wq.ht()
                question_m=""
                while(bbiu=="0"):
                    m.clear()
                    m.pu()
                    m.goto(0,-155)
                    m.pd()
                    m.pencolor("white")
                    m.write("Type {done} for load & exit.",align="center",font=("Copperplate Gothic Bold",12))
                    m.pu()
                    m.goto(0,20)
                    m.pd()
                    m.pencolor("darkred")
                    nahaii=str(counter)
                    m.write(nahaii,align="center",font=("impact",50))
                    wq.clear()
                    wq.pu()
                    wq.goto(0,-5)
                    wq.pd()
                    wq.pencolor("darkblue")
                    lofd="Please enter the type of question num-"+str(counter) 
                    wq.write(lofd,align="center",font=("Copperplate Gothic Bold",15))
                    typeq=t.textinput(name_exam_t,"Type of question(choice{cho}/descriptive{des}): ")
                    if(typeq=="done")or(typeq=="done?")or(typeq==""):
                        break
                    wq.pu()
                    wq.goto(0,-25)
                    wq.pd()
                    wq.pencolor("darkblue")
                    lofd="Please enter the question num-"+str(counter) 
                    wq.write(lofd,align="center",font=("Copperplate Gothic Bold",15))
                    question=t.textinput(name_exam_t,"Question:                                             ")
                    if(question=="done")or(question=="done?")or(question==""):
                        break
                    choices=""
                    if(typeq=="choice")or(typeq=="cho"):
                        wq.pu()
                        wq.goto(0,-45)
                        wq.pd()
                        wq.pencolor("darkblue")
                        lofd="Please enter the choices. Use {/} or {|} for division."
                        wq.write(lofd,align="center",font=("Copperplate Gothic Bold",15))
                        choices=t.textinput(name_exam_t,"Choices of question:                                             ")
                        if(choices=="done")or(choices=="done?")or(choices==""):
                            break
                        wq.pu()
                        wq.goto(0,-65)
                        wq.pd()
                        wq.pencolor("darkblue")
                        lofd="Please enter the correct answer."
                        wq.write(lofd,align="center",font=("Copperplate Gothic Bold",15))
                        if(question[len(question)-1]=="?"):
                            question=question[:(len(question)-1)]
                        if(question[len(question)-1]=="؟"):
                            question=question[:(len(question)-1)]
                        question+=" ( "+choices+" )"
                    else:
                        wq.pu()
                        wq.goto(0,-45)
                        wq.pd()
                        wq.pencolor("darkblue")
                        lofd="Please enter the correct answer."
                        wq.write(lofd,align="center",font=("Copperplate Gothic Bold",15))
                    if("?" not in question)and(question!=""):
                        question+="?"
                    answer_of_q=t.textinput(name_exam_t,"Answer of question: ")+"!"
                    if(answer_of_q==""):
                        break
                    try:
                        file=open("db10.db","r")
                        file.read()
                        file.close()
                        wq.clear()
                        wq.pu()
                        wq.goto(0,-25)
                        wq.pd()
                        wq.pencolor("darkblue")
                        lofd="Do you want upload picture?"
                        wq.write(lofd,align="center",font=("Copperplate Gothic Bold",15))
                        pic_s=t.textinput(name_exam_t,"Upload(yes/no): ")
                        if(pic_s=="yes")or(pic_s=="y"):
                            wq.pu()
                            wq.goto(0,-45)
                            wq.pd()
                            wq.pencolor("darkblue")
                            lofd="Please select the picture."
                            wq.write(lofd,align="center",font=("Copperplate Gothic Bold",15))
                            root = Tk()
                            root.withdraw()
                            root.filename=filedialog.askopenfilename(initialdir = "/",title = "Select Picture.",filetypes = (("Graphics Interchange File","*.gif"),("Digital images","*.jpg"),("Digital images","*.jpeg"),("Portable Network Graphics","*.png"),("all files","*.*")))
                            no_address_file_name=""
                            for kt in range(0,len(root.filename)):
                                no_address_file_name+=root.filename[kt]
                                if(root.filename[kt]=="/"):
                                    no_address_file_name=""
                            question+=no_address_file_name
                            wq.pu()
                            wq.goto(0,-65)
                            wq.pd()
                            wq.pencolor("darkblue")
                            lofd="Uploading Picture to Cloud Host..."
                            wq.write(lofd,align="center",font=("Copperplate Gothic Bold",15))
                            time.sleep(1)
                            file=open("db10.db")
                            usern_cloud=file.read()
                            file.close()
                            try:
                                session=ftplib.FTP("ftpupload.net","cldff_22998458","arizamir")
                                try:
                                    file=open(root.filename,'rb')                  
                                    session.storbinary('STOR '+"htdocs/"+usern_cloud+"/QM/"+no_address_file_name,file)     
                                    file.close()                                    
                                    session.quit()
                                    wq.undo()
                                    wq.pu()
                                    wq.goto(0,-65)
                                    wq.pd()
                                    wq.pencolor("darkblue")
                                    lofd="Successfully Uploaded."
                                    wq.write(lofd,align="center",font=("Copperplate Gothic Bold",15))
                                    time.sleep(1.5)
                                except:
                                    wq.pu()
                                    wq.goto(0,-85)
                                    wq.pd()
                                    wq.pencolor("darkorange")
                                    wq.write("Sorry, password is false.",align="center",font=("Copperplate Gothic Bold",15))
                                    playsound.playsound("1.mp3")
                            except:
                                wq.clear()
                                wq.pu()
                                wq.goto(0,-65)
                                wq.pd()
                                wq.pencolor("darkorange")
                                wq.write("Sorry, The internet aren't talking right now.",align="center",font=("Copperplate Gothic Bold",15))
                                playsound.playsound("12.mp3")
                        else:
                            wq.pu()
                            wq.goto(0,-45)
                            wq.pd()
                            wq.pencolor("darkblue")
                            lofd="Upload progress canceled."
                            wq.write(lofd,align="center",font=("Copperplate Gothic Bold",15))
                            time.sleep(1.5)
                    except:
                        pass
                    question_mm=""
                    for yjru in range(0,len(question)):
                        question_mm+=question[yjru]
                        if(yjru%50==0)and(yjru!=0):
                            if(question[yjru]!=" "):
                                question_mm+="_"+"\n"
                            else:
                                question_mm+="\n"
                    question_mm+=answer_of_q+"\n"
                    for jooapp in range(0,len(question_mm)):
                        question_m+=str(ord(question_mm[jooapp])+835)+"-"
                    file=open(name_exam_t,"r")
                    befor_exam=file.read()
                    file.close()
                    befor_exam+=question_m+"\n"
                    question_m=""
                    file=open(name_exam_t,"w")
                    file.write(befor_exam)
                    file.close()
                    counter+=1
                file=open(name_exam_t,"r")
                befor_exam=file.read()
                file.close()
                befor_exam+=passw_of_e_m
                file=open(name_exam_t,"w")
                file.write(befor_exam)
                file.close()
                wq.clear()
                m.clear()
                m.pu()
                m.goto(0,20)
                m.pd()
                m.pencolor("brown")
                m.write("Exam Created Successfully!",align="center",font=("Copperplate Gothic Bold",14))
                playsound.playsound("16.mp3")
                abirang=True
                if(abirang==True):
                    try:
                        file=open("db10.db","r")
                        file.read()
                        file.close()
                        wq.clear()
                        wq.pu()
                        wq.goto(0,-45)
                        wq.pd()
                        wq.pencolor("darkblue")
                        wq.write("Do you want to upload this exam to the host?",align="center",font=("Copperplate Gothic Bold",14))
                        pic_s=t.textinput(name_exam_t,"Upload?(yes/no) ")
                        if(pic_s=="yes")or(pic_s=="y"):
                            no_address_file_name=""
                            for kt in range(0,len(name_exam_t)):
                                no_address_file_name+=name_exam_t[kt]
                                if(name_exam_t[kt]=="/"):
                                    no_address_file_name=""
                            wq.pu()
                            wq.goto(0,-65)
                            wq.pd()
                            wq.pencolor("darkblue")
                            lofd="Uploading Exam to Cloud Host..."
                            wq.write(lofd,align="center",font=("Copperplate Gothic Bold",15))
                            time.sleep(1)
                            passu_cloud=t.textinput(name_exam_t,"Cloud Password: ")
                            typeofm=t.textinput(name_exam_t,"Type of upload(Public{Pu}/Private{Pr}): ")
                            file=open("db10.db")
                            usern_cloud=file.read()
                            file.close()
                            try:
                                session=ftplib.FTP("ftpupload.net","cldff_22998458","arizamir")
                                try:
                                    if(typeofm.lower()=="pu")or(typeofm.lower()=="public"):
                                        file=open(name_exam_t,'rb')
                                        session.storlines('STOR '+"htdocs/"+usern_cloud+"/QM/"+no_address_file_name,file)     
                                        file.close()
                                    if(typeofm.lower()=="pr")or(typeofm.lower()=="private"):
                                        file=open(name_exam_t,'rb')                  
                                        session.storlines('STOR '+"htdocs/"+usern_cloud+"/"+passu_cloud+"/QM/"+no_address_file_name,file)     
                                        file.close()
                                    session.quit()
                                    wq.undo()
                                    wq.pu()
                                    wq.goto(0,-65)
                                    wq.pd()
                                    wq.pencolor("darkblue")
                                    lofd="Upload progress was successful."
                                    wq.write(lofd,align="center",font=("Copperplate Gothic Bold",15))
                                    playsound.playsound("21.mp3")
                                except:
                                    wq.undo()
                                    wq.pu()
                                    wq.goto(0,-65)
                                    wq.pd()
                                    wq.pencolor("darkorange")
                                    wq.write("Sorry, password is false.",align="center",font=("Copperplate Gothic Bold",15))
                                    playsound.playsound("1.mp3")
                            except:
                                wq.clear()
                                wq.pu()
                                wq.goto(0,-85)
                                wq.pd()
                                wq.pencolor("darkorange")
                                wq.write("Sorry, The internet aren't talking right now.",align="center",font=("Copperplate Gothic Bold",15))
                                playsound.playsound("12.mp3")
                        else:
                            wq.pu()
                            wq.goto(0,-65)
                            wq.pd()
                            wq.pencolor("darkblue")
                            lofd="Upload progress canceled."
                            wq.write(lofd,align="center",font=("Copperplate Gothic Bold",15))
                            time.sleep(1.5)
                        wq.clear()
                    except:
                        pass
            def buton2(x,y):
                os.startfile("color.pdf")
                m.clear()
                m.pu()
                m.goto(0,0)
                m.pd()
                m.pencolor("darkblue")
                m.write("Personalize",align="center",font=("Comic Sans MS",35,("bold")))
                time.sleep(4)
                m.clear()
                m.pu()
                m.goto(0,20)
                m.pd()
                m.pencolor("darkblue")
                m.write("Please enter the background color.",align="center",font=("Copperplate Gothic Bold",15))
                bg_color_u=t.textinput("Personalize","Background Color: ").lower()
                m.clear()
                m.write("Please enter the pen color.",align="center",font=("Copperplate Gothic Bold",15))
                p_color_u=t.textinput("Personalize","Pen Color: ").lower()
                m.clear()
                m.write("Please enter the button color.",align="center",font=("Copperplate Gothic Bold",15))
                b_color_u=t.textinput("Personalize","Button Color: ").lower()
                colors=["blue","green","yellow","red","black","white","gray","orange","pink","purple"]
                if(bg_color_u in colors)and(p_color_u in colors)and(b_color_u in colors):
                    file=open("db1.db","w")
                    file.write(bg_color_u)
                    file.close()
                    file=open("db2.db","w")
                    file.write(p_color_u)
                    file.close()
                    file=open("db3.db","w")
                    file.write(b_color_u)
                    file.close()
                else:
                    m.clear()
                    m.pu()
                    m.goto(0,20)
                    m.pd()
                    m.pencolor("darkorange")
                    m.write("Sorry, entered colors are not definite.",align="center",font=("Copperplate Gothic Bold",15))
                    playsound.playsound("5.mp3")
            def buton3(x,y):
                try:
                    m.clear()
                    m.pu()
                    m.goto(0,20)
                    m.pd()
                    m.pencolor("darkblue")
                    m.write("Please select the exam file.",align="center",font=("Copperplate Gothic Bold",15))
                    root = Tk()
                    root.withdraw()
                    root.filename=filedialog.askopenfilename(initialdir = "/",title = "Select exam file.",filetypes = (("Quiz Maker Exam file","*.QME"),("all files","*.*")))
                    if(".QME"not in root.filename):
                        error1()
                    file=open(root.filename)
                    salamak=file.readline()
                    exam=file.read()
                    file.close()
                    h=""
                    taghalob="0"
                    m.clear()
                    m.pu()
                    m.goto(0,20)
                    m.pd()
                    m.pencolor("darkblue")
                    m.write("Please enter the password/pincode of exam.",align="center",font=("Copperplate Gothic Bold",15))
                    passwc_of_e=t.textinput(root.filename,"Password/Pincode: ")
                    huit=0
                    jo=""
                    passwc=""
                    for jomunji in range(0,len(exam)):
                        if(exam[jomunji]=="-"):
                            jo=int(jo)-835
                            bomboli=chr(jo)
                            if(huit==1):
                                huit+=1
                            if(bomboli=="$"):
                                huit+=1
                            if(huit==2):
                                passwc+=chr(jo)
                            elif(huit==3):
                                break
                            jo=""
                        else:
                            jo+=exam[jomunji]
                    if(passwc==passwc_of_e):
                        taghalob="1"
                    else:
                        m.clear()
                        m.pu()
                        m.goto(0,20)
                        m.pd()
                        m.pencolor("darkorange")
                        m.write("Sorry, password is false.",align="center",font=("Copperplate Gothic Bold",15))
                        playsound.playsound("1.mp3")
                    if(taghalob=="1"):
                        m.clear()
                        m.pu()
                        m.goto(0,20)
                        m.pd()
                        m.pencolor("brown")
                        m.write("Quiz is starting!",align="center",font=("Copperplate Gothic Bold",15))
                        time.sleep(1.5)
                        domboli=""
                        jo=""
                        for k in range(0,len(exam)):
                            if(exam[k]=="-"):
                                jo=int(jo)-835
                                h+=chr(jo)
                                domboli=chr(jo)
                                jo=""
                            else:
                                jo+=exam[k]
                            joi=""
                            hi=""
                            if(domboli=="?")or(domboli=="؟"):
                                try:
                                    for jhk in range(k+1,len(exam)):
                                        if(exam[jhk]=="-"):
                                            joi=int(joi)-835
                                            hi+=chr(joi)
                                            if(".gif" in hi)or(".GIF" in hi)or(".png" in hi)or(".PNG" in hi)or(".jpg" in hi)or(".JPG" in hi)or(".jpeg" in hi)or(".JPEG" in hi):
                                                break
                                            joi=""
                                        else:
                                            joi+=exam[jhk]
                                    ftp=ftplib.FTP("ftpupload.net")
                                    ftp.login("cldff_22998458","arizamir")
                                    file=open("db10.db")
                                    datacl=file.read()
                                    file.close()
                                    ftp.cwd('htdocs/'+datacl+"/QM")
                                    file=open(hi,"wb")
                                    ftp.retrbinary('RETR %s' % hi, file.write)
                                    file.close()
                                    fig = plt.figure(0)
                                    fig.canvas.set_window_title('Codoffee Quiz Maker')
                                    img=mpimg.imread(hi)
                                    imgplot = plt.imshow(img)
                                    plt.title("Image of question: ")
                                    fig.show()
                                    time.sleep(0.5)
                                    os.remove(hi)
                                except:
                                    pass
                                m.clear()
                                m.pu()
                                m.goto(0,-10)
                                m.pd()
                                m.pencolor("black")
                                m.write(h,align="center",font=("Copperplate Gothic Bold",11))
                                h=""
                                student_answers_this=t.textinput(root.filename,"Please answer this question: ")
                                try:
                                    plt.close(fig)
                                except:
                                    pass
                                domboli=""
                            elif(domboli=="!"):
                                h=""
                                domboli=""
                        m.clear()
                        m.pu()
                        m.goto(0,20)
                        m.pd()
                        m.pencolor("brown")
                        m.write("Quiz finished!",align="center",font=("Copperplate Gothic Bold",15))
                        try:
                            plt.close(fig)
                        except:
                            pass
                except:
                    m.clear()
                    m.pu()
                    m.goto(0,20)
                    m.pd()
                    m.pencolor("darkorange")
                    m.write("Sorry, exam file isn't working.",align="center",font=("Copperplate Gothic Bold",15))  
                    playsound.playsound("8.mp3")
            def buton4(x,y):
                m.clear()
                m.pu()
                m.goto(0,73)
                m.pd()
                m.pencolor("brown")
                m.write("Help;",align="center",font=("Copperplate Gothic Bold",15))
                m.pu()
                m.goto(0,-40)
                m.pd()
                m.pencolor("black")
                m.write("Click on {Start!} button to make exam.\nClick on {Quizes} button to test your\nexams. Click on {Info} button to show\nthe information. You can personalize\napp with {Personalize!} button.",align="center",font=("Copperplate Gothic Bold",15))
                m.pu()
                m.goto(0,-65)
                m.pd()
                m.pencolor("darkblue")
                m.write("Press the {D} key, to learn more.",align="center",font=("Copperplate Gothic Bold",15))
                playsound.playsound("4.mp3")
            def buton5(x,y):
                m.clear()
                m.pu()
                m.goto(0,80)
                m.pd()
                m.pencolor("brown")
                m.write("Information;",align="center",font=("Copperplate Gothic Bold",15))
                m.pu()
                m.goto(0,35)
                m.pd()
                m.pencolor("black")
                m.write("Codoffee Quiz Maker V1.6\n© 2018 Codoffee | All rights reserved.",align="center",font=("Copperplate Gothic Bold",15))
                m.pu()
                m.goto(0,-60)
                m.pd()
                m.pencolor("darkblue")
                m.write("Administration Manager: Aria Izanlou\nSupervisor: Amir Hossain Safarzadeh\nGUI-Designed By Codoffee Maze-GUI\nAudio/Sound Support By Codoffee TTS/STT API",align="center",font=("Copperplate Gothic Bold",15))
            def buton6(x,y):
                m.clear()
                m.pu()
                m.goto(0,45)
                m.pd()
                m.pencolor("brown")
                m.write("ID Information;",align="center",font=("Copperplate Gothic Bold",15))
                file=open("db5.db")
                name=file.read()+" | Teacher Account\nThis program has already licensed."
                file.close()
                m.pu()
                m.goto(0,0)
                m.pd()
                m.pencolor("black")
                m.write(name,align="center",font=("Copperplate Gothic Bold",15))
                try:
                    file=open("db10.db")
                    cloudtf=file.read()
                    file.close()
                    cloudtf="Codoffee Cloud | Connected to ID: "+cloudtf
                except:
                    cloudtf="Codoffee Cloud | Not Connected."
                m.pu()
                m.goto(0,-25)
                m.pd()
                m.pencolor("black")
                m.write(cloudtf,align="center",font=("Copperplate Gothic Bold",15))
                m.pu()
                m.goto(0,-50)
                m.pd()
                m.pencolor("darkblue")
                m.write("Press the {space} key to log-out.",align="center",font=("Copperplate Gothic Bold",15))
            def buton7(x,y):
                try:
                    file=open("db10.db","r")
                    datacl=file.read()
                    file.close()
                    m.clear()
                    m.pu()
                    m.goto(0,20)
                    m.pd()
                    m.pencolor("brown")
                    m.write("Codoffee Cloud has been connected to ID:",align="center",font=("Copperplate Gothic Bold",15))
                    m.pu()
                    m.goto(0,-5)
                    m.pd()
                    m.pencolor("black")
                    m.write(datacl,align="center",font=("Copperplate Gothic Bold",15))
                except:
                    m.clear()
                    m.pu()
                    m.goto(0,20)
                    m.pd()
                    m.pencolor("brown")
                    m.write("Connecting to Codoffee Cloud...",align="center",font=("Copperplate Gothic Bold",15))
                    time.sleep(3)
                    m.clear()
                    m.pu()
                    m.goto(0,20)
                    m.pd()
                    m.pencolor("brown")
                    m.write("Sign-in to Codoffee Cloud.",align="center",font=("Copperplate Gothic Bold",15))
                    m.pu()
                    m.goto(0,-10)
                    m.pd()
                    m.pencolor("black")
                    m.write("If you don't have account, you can register on:\ncodoffeegroup.ir/cloud",align="center",font=("Copperplate Gothic Bold",11))
                    usern_cloud=t.textinput("Cloud Sign-in","Username: ")
                    passu_cloud=t.textinput("Cloud Sign-in","Password: ")
                    try:
                        m.clear()
                        m.pu()
                        m.goto(0,20)
                        m.pd()
                        m.pencolor("brown")
                        m.write("Checking your ID...",align="center",font=("Copperplate Gothic Bold",15))
                        time.sleep(3)
                        ftp=ftplib.FTP("ftpupload.net")
                        ftp.login("cldff_22998458","arizamir")
                        ftp.cwd('htdocs')
                        def directory_exists(dir):
                            dr_exits=ftp.nlst()
                            if(dir) in dr_exits:
                                return True
                            else:
                                return False
                        if directory_exists(usern_cloud) is True:
                            ftp.cwd(usern_cloud)
                            if ('QM' in ftp.nlst()):
                                pass
                            else:
                                try:
                                    ftp.mkd('QM')
                                except:
                                    pass
                            if (directory_exists(passu_cloud)) is True:
                                ftp.cwd(passu_cloud)
                                if ('QM' in ftp.nlst()):
                                    pass
                                else:
                                    try:
                                        ftp.mkd('QM')
                                    except:
                                        pass
                                m.clear()
                                m.pu()
                                m.goto(0,20)
                                m.pd()
                                m.pencolor("black")
                                m.write("Welcome ID: "+usern_cloud,align="center",font=("Copperplate Gothic Bold",15))
                                m.pu()
                                m.goto(0,-20)
                                m.pd()
                                m.pencolor("white")
                                m.write("Log-in progress was successfull.\nPlease restart Codoffee Quiz Maker.",align="center",font=("Copperplate Gothic Bold",12))
                                playsound.playsound("18.mp3")
                                file=open("db10.db","w")
                                file.write(usern_cloud)
                                file.close()
                                ftp.quit()
                            else:
                               m.clear()
                               m.pu()
                               m.goto(0,20)
                               m.pd()
                               m.pencolor("darkorange")
                               m.write("Sorry, password is false.",align="center",font=("Copperplate Gothic Bold",15))
                               playsound.playsound("1.mp3")
                               ftp.quit()
                        else:
                            m.clear()
                            m.pu()
                            m.goto(0,20)
                            m.pd()
                            m.pencolor("darkorange")
                            m.write("Sorry, there is no account with this username.",align="center",font=("Copperplate Gothic Bold",15))  
                            playsound.playsound("17.mp3")
                    except:
                        m.clear()
                        m.pu()
                        m.goto(0,20)
                        m.pd()
                        m.pencolor("darkorange")
                        m.write("Sorry, The internet aren't talking\nright now. Please check connection.",align="center",font=("Copperplate Gothic Bold",15))
                        playsound.playsound("12.mp3")
            def buton8(x,y):
                m.clear()
                m.pu()
                m.goto(0,20)
                m.pd()
                m.pencolor("brown")
                m.write("Connecting to Codoffee Cloud...",align="center",font=("Copperplate Gothic Bold",15))
                time.sleep(3)
                try:
                    file=open("db10.db","r")
                    datacl=file.read()
                    file.close()
                    ftp=ftplib.FTP("ftpupload.net")
                    m.clear()
                    m.pu()
                    m.goto(0,20)
                    m.pd()
                    m.pencolor("black")
                    m.write("Codoffee Cloud has been connected to ID: "+datacl,align="center",font=("Copperplate Gothic Bold",15))
                    m.pu()
                    m.goto(0,0)
                    m.pd()
                    m.pencolor("brown")
                    m.write("Showing up Files...",align="center",font=("Copperplate Gothic Bold",15))
                    ftp=ftplib.FTP("ftpupload.net")
                    ftp.login("cldff_22998458","arizamir")
                    prorpu=t.textinput('My Files','Type of showing(Public{Pu}/Private{Pr}): ')
                    if(prorpu.lower()=='pu' or prorpu.lower()=='public'):
                        ftp.cwd('htdocs/'+datacl+'/QM')
                        sabzaloo=ftp.nlst()
                        j=""
                        for i in range(1,len(sabzaloo)):
                            if(".QME" in sabzaloo[i]):
                                j+=sabzaloo[i]+'\n'
                        zardaloo=t.textinput("My Files",j)
                    else:
                        passu_req=t.textinput("My Files","Cloud Password: ")
                        try:
                            ftp.cwd('htdocs/'+datacl+'/'+passu_req+'/QM')
                        except:
                            m.clear()
                            m.pu()
                            m.goto(0,20)
                            m.pd()
                            m.pencolor("darkorange")
                            m.write("Sorry, password is false.",align="center",font=("Copperplate Gothic Bold",15))
                            playsound.playsound("1.mp3")
                            exit()
                        sabzaloo=ftp.nlst()
                        j=""
                        for i in range(1,len(sabzaloo)):
                            if(".QME" in sabzaloo[i]):
                                j+=sabzaloo[i]+'\n'
                        zardaloo=t.textinput("My Files",j)
                    m.clear()
                    m.pu()
                    m.goto(0,20)
                    m.pd()
                    m.pencolor("darkblue")
                    m.write("Please select download's location.",align="center",font=("Copperplate Gothic Bold",15))
                    name_exam_w= Tk()
                    name_exam_w.withdraw()
                    name_exam_w.filename=filedialog.asksaveasfilename(initialdir = "/",title = "Select download's location.",filetypes = (("Quiz Maker Exam file","*.QME"),("all files","*.*")))
                    try:
                        if(".QME"not in zardaloo):
                            zardaloo+=".QME"
                            dll=name_exam_w.filename+".QME"
                        file=open(dll,"wb")
                        ftp.retrbinary('RETR %s' % zardaloo, file.write)
                        file.close()
                        m.clear()
                        m.pu()
                        m.goto(0,20)
                        m.pd()
                        m.pencolor("brown")
                        m.write("Your file downloaded successfully.",align="center",font=("Copperplate Gothic Bold",15))
                        playsound.playsound("22.mp3")
                    except:
                        m.clear()
                        m.pu()
                        m.goto(0,20)
                        m.pd()
                        m.pencolor("darkorange")
                        m.write("Sorry, something went wrong with downloading.",align="center",font=("Copperplate Gothic Bold",15))
                        playsound.playsound("19.mp3")
                except:
                    m.clear()
                    m.pu()
                    m.goto(0,20)
                    m.pd()
                    m.pencolor("darkorange")
                    m.write("Sorry, The internet aren't talking\nright now. Please check connection.",align="center",font=("Copperplate Gothic Bold",15))
                    playsound.playsound("12.mp3")
            def key1():
                file=open("db4.db","w")
                file.write("0")
                file.close()
                os.remove("db10.db")
                m.clear()
                m.pu()
                m.goto(0,0)
                m.pd()
                m.pencolor("darkgray")
                m.write("Log-out progress was successfull.\nPlease restart Codoffee Quiz Maker.",align="center",font=("Copperplate Gothic Bold",15))
            def key2():
                os.startfile("Docs.pdf")
            m.clear()
            m.pu()
            m.goto(0,0)
            m.pd()
            m.pencolor("darkgray")
            m.write("Codoffee Quiz Maker V1.6\nTeacher Account",align="center",font=("Copperplate Gothic Bold",15))
            button1.onclick(buton1)
            button2.onclick(buton2)
            button3.onclick(buton3)
            button4.onclick(buton4)
            button5.onclick(buton5)
            button6.onclick(buton6)
            button7.onclick(buton7)
            try:
                button8.onclick(buton8)
            except:
                pass
            scr.onkey(key1,"space")
            scr.onkey(key2,"d")
            scr.listen()
            def bgback():
                while True:
                    t.bgcolor("#5c5c3d")
                    time.sleep(1)
                    t.bgcolor("#4d4d33")
                    time.sleep(1)
                    t.bgcolor("#3d3d29")
                    time.sleep(1)
                    t.bgcolor("#4d4d33")
                    time.sleep(1)
                    t.bgcolor("#5c5c3d")
                    time.sleep(1)
                    t.bgcolor("#6b6b47")
            def date_time():
                dt=t.Turtle()
                dt.speed(0)
                dt.ht()
                while True:
                    now=datetime.now()
                    now_time="%s:%s"%(now.hour,now.minute)
                    now_date="%s/%s/%s"%(now.month,now.day,now.year)
                    dt.clear()
                    dt.pu()
                    dt.goto(270,222)
                    dt.pd()
                    try:    
                        dt.pencolor("light"+p_color)
                    except:
                        dt.pencolor(p_color)
                    dt.write(now_time,align="center",font=("Bahnschrift SemiBold",17,("bold")))
                    dt.pu()
                    dt.goto(-248,222)
                    dt.pd()
                    dt.pencolor(p_color)
                    dt.write(now_date,align="center",font=("Bahnschrift SemiBold",17,("bold")))
                    time.sleep(59.9)
            thread1=Thread(target=date_time,args=[])
            thread1.start()
            thread2=Thread(target=bgback,args=[])
            thread2.start()
            t.mainloop()
        #student-English:
        elif(t_or_s.lower()=="student"):
            m.clear()
            t.title("Codoffee Quiz Maker 1.6 | Student Account")
            t.setup(620,510)
            m=t.Turtle()
            m.ht()
            m.speed(0)
            t.clear()
            if(bg_color=="#6b6b47"):
                t.bgcolor("gray")
            else:
                t.bgcolor(bg_color)
            t.pencolor("#001a00")
            t.fillcolor("#001a00")
            t.pu()
            t.goto(-310,210)
            t.pd()
            t.goto(310,210)
            t.pu()
            t.goto(-310,215)
            t.pd()
            t.goto(310,215)
            t.pu()
            t.goto(-310,220)
            t.pd()
            t.goto(310,220)
            t.pd()
            t.begin_fill()
            t.goto(310,220)
            t.goto(310,255)
            t.goto(-310,255)
            t.goto(-310,220)
            t.end_fill()
            t.pu()
            t.goto(-310,-190)
            t.pd()
            t.goto(310,-190)
            t.pu()
            t.goto(-310,-195)
            t.pd()
            t.goto(310,-195)
            t.pu()
            t.goto(-310,-200)
            t.pd()
            t.goto(310,-200)
            t.pu()
            t.goto(-310,-205)
            t.pd()
            t.goto(310,-205)
            t.pu()
            t.goto(-310,-210)
            t.pd()
            t.begin_fill()
            t.goto(310,-210)
            t.goto(310,-255)
            t.goto(-310,-255)
            t.goto(-310,-210)
            t.end_fill()
            button1=Turtle("triangle")
            button1.speed(0)
            button1.pu()
            button1.goto(15,-194)
            button1.pd()
            button1.shapesize(1.8)
            try:
                button1.fillcolor("dark"+b_color)
            except:
                button1.fillcolor(b_color)
            t.pu()
            t.goto(23,-242)
            t.pd()
            try:
                t.pencolor("light"+b_color)
            except:
                t.pencolor(b_color)
            t.write("Take!",align="center",font=("Comic Sans MS",15))
            time.sleep(0.2)
            t.undo()
            t.pu()
            t.goto(33,-242)
            t.pd()
            t.write("Take!",align="center",font=("Comic Sans MS",15))
            time.sleep(0.2)
            t.undo()
            t.pu()
            t.goto(13,-242)
            t.pd()
            t.write("Take!",align="center",font=("Comic Sans MS",15))
            time.sleep(0.2)
            t.undo()
            t.pu()
            t.goto(23,-242)
            t.pd()
            t.write("Take!",align="center",font=("Comic Sans MS",15))
            button2=Turtle("square")
            button2.speed(4)
            button2.pu()
            button2.goto(-46,225)
            button2.pd()
            button2.shapesize(1.2)
            try:
                button2.fillcolor("dark"+p_color)
            except:
                try:
                    button2.fillcolor("light"+p_color)
                except:
                    button2.fillcolor(p_color)
            button2.left(360)
            t.pu()
            t.goto(-45,191)
            t.pd()
            t.pencolor(p_color)
            t.write("Personalize!",align="center",font=("Comic Sans MS",10))
            button3=Turtle("circle")
            button3.speed(0)
            button3.pu()
            button3.goto(126,-197)
            button3.pd()
            button3.shapesize(1.5)
            button3.fillcolor("pink")
            t.pu()
            t.goto(126,-233)
            t.pd()
            t.pencolor("pink")
            t.write("Results",align="center",font=("Comic Sans MS",10))
            button4=Turtle("square")
            button4.speed(0)
            button4.pu()
            button4.goto(-100,-197)
            button4.pd()
            button4.shapesize(1.4)
            button4.fillcolor("darkorange")
            t.pu()
            t.goto(-98,-233)
            t.pd()
            t.pencolor("darkorange")
            t.write("Help",align="center",font=("Comic Sans MS",10))
            button5=Turtle("triangle")
            button5.speed(0)
            button5.pu()
            button5.goto(34,223)
            button5.pd()
            button5.left(90)
            button5.shapesize(1.5)
            button5.fillcolor("lightblue")
            t.pu()
            t.goto(36,191)
            t.pd()
            t.pencolor("darkblue")
            t.write("Info",align="center",font=("Comic Sans MS",10))
            button6=Turtle()
            image = "Logo.gif"
            scr.addshape(image)
            button6.shape(image)
            button6.speed(0)
            button6.pu()
            button6.goto(95,225)
            button6.pd()
            button6.left(90)
            button6.shapesize(2)
            t.pu()
            t.goto(-132,192)
            t.pd()
            t.pencolor("red")
            t.write("ID",align="center",font=("Comic Sans MS",10))
            try:
                file=open("db10.db","r")
                file.read()
                file.close()
                button7=Turtle("square")
                button7.speed(0)
                button7.pu()
                button7.goto(-260,-196)
                button7.pd()
                button7.left(45)
                button7.shapesize(1)
                image = "cloudl.gif"
                scr.addshape(image)
                button7.shape(image)
                t.pu()
                t.goto(-258,-235)
                t.pd()
                t.pencolor("#e6b800")
                t.write("Cloud DL",align="center",font=("Comic Sans MS",11))
            except:
                pass
            if(t_v=="0"):
                m.pu()
                m.goto(0,70)
                m.pd()
                m.pencolor("brown")
                m.write("Welcome;",align="center",font=("Copperplate Gothic Bold",15))
                m.pu()
                m.goto(0,50)
                m.pd()
                m.pencolor("black")
                m.write("To the Codoffee Quiz Maker!",align="center",font=("Copperplate Gothic Bold",15))
                playsound.playsound("2.mp3")
                m.pu()
                m.goto(0,30)
                m.pd()
                m.write("Click on {Help} button for learn.",align="center",font=("Copperplate Gothic Bold",15))
                playsound.playsound("3.mp3")
                file=open("db4.db","w")
                file.write("1")
                file.close()
            def buton1(x,y):
                try:
                    m.clear()
                    m.pu()
                    m.goto(0,20)
                    m.pd()
                    m.pencolor("darkblue")
                    m.write("Please select the exam file",align="center",font=("Copperplate Gothic Bold",15))
                    root = Tk()
                    root.withdraw()
                    root.filename=filedialog.askopenfilename(initialdir = "/",title = "Select exam file.",filetypes = (("Quiz Maker Exam file","*.QME"),("all files","*.*")))
                    samanoo=root.filename
                    if("QME"not in samanoo):
                        samanoo+='.QME'
                    file=open(samanoo)
                    salamak=file.readline()
                    exam=file.read()
                    file.close()
                    uitwq=""
                    salamak_m=""
                    for joooooapp in range(0,len(salamak)):
                        if(salamak[joooooapp]=="-"):
                            uitwq=int(uitwq)-835
                            salamak_m+=chr(uitwq)
                            uitwq=""
                        else:
                            uitwq+=salamak[joooooapp]
                    counter=0
                    taghalob="1"
                    now=datetime.now()
                    time_start="%s:%s:%s"%(now.hour,now.minute,now.second)
                    try:
                        name_answers=samanoo+"S"
                        file=open(name_answers,"r")
                        read_db_answers=file.read()
                        file.close()
                        if("Codoffee Quiz Maker" in read_db_answers)or("Codoffee Quiz Maker's Result:" in read_db_answers):
                            taghalob="0"
                            m.clear()
                            m.pu()
                            m.goto(0,20)
                            m.pd()
                            m.pencolor("darkorange")
                            m.write("Sorry, you can't answer again.",align="center",font=("Copperplate Gothic Bold",15))
                            playsound.playsound("7.mp3")
                        file=open(name_answers)
                        file.write("")
                        file.close()
                    except:
                        file=open(name_answers,"w")
                        file.write("Codoffee Quiz Maker's Result:\n\n")
                        file.close()
                    billur=0
                    if(taghalob=="1"):
                        m.clear()
                        m.pu()
                        m.goto(0,20)
                        m.pd()
                        m.pencolor("brown")
                        m.write("Quiz is starting...",align="center",font=("Copperplate Gothic Bold",15))
                        time.sleep(1.5)
                        jo=""
                        domboli=""
                        h=""
                        nahai="Codoffee Quiz Maker's Result:\n\n"
                        nahai_m=""
                        for k in range(0,len(exam)):
                            if(exam[k]=="-"):
                                jo=int(jo)-835
                                h+=chr(jo)
                                domboli=chr(jo)
                                jo=""
                            else:
                                jo+=exam[k]
                            joi=""
                            hi=""
                            if(domboli=="?")or(domboli=="؟"):
                                try:
                                    for jhk in range(k+1,len(exam)):
                                        if(exam[jhk]=="-"):
                                            joi=int(joi)-835
                                            hi+=chr(joi)
                                            if(".gif" in hi)or(".GIF" in hi)or(".png" in hi)or(".PNG" in hi)or(".jpg" in hi)or(".JPG" in hi)or(".jpeg" in hi)or(".JPEG" in hi):
                                                break
                                            joi=""
                                        else:
                                            joi+=exam[jhk]
                                    ftp=ftplib.FTP("ftpupload.net")
                                    ftp.login("cldff_22998458","arizamir")
                                    file=open("db10.db")
                                    datacl=file.read()
                                    file.close()
                                    ftp.cwd('htdocs/'+datacl+"/QM")
                                    file=open(hi,"wb")
                                    ftp.retrbinary('RETR %s' % hi, file.write)
                                    file.close()
                                    fig = plt.figure(0)
                                    fig.canvas.set_window_title('Codoffee Quiz Maker')
                                    img=mpimg.imread(hi)
                                    imgplot = plt.imshow(img)
                                    plt.title("Image of question: ")
                                    fig.show()
                                    time.sleep(0.5)
                                    os.remove(hi)
                                except:
                                    pass
                                counter+=1
                                m.clear()
                                m.pu()
                                m.goto(0,-10)
                                m.pd()
                                m.pencolor("black")
                                m.write(h,align="center",font=("Copperplate Gothic Bold",11))
                                h=""
                                student_answers_this=t.textinput(samanoo,"Please answer this question: ")
                                try:
                                    plt.close(fig)
                                except:
                                    pass
                                nahai+=str(counter)+"-"+student_answers_this+"\n"
                                domboli=""
                            if(".gif" in h)or(".GIF" in h)or(".png" in h)or(".PNG" in h)or(".jpg" in h)or(".JPG" in h)or(".jpeg" in h)or(".JPEG" in h):
                                h=""
                            if(domboli=="!"):
                                if(student_answers_this.lower()=="codoffeearizamir"):
                                    student_answers_this=h[:(len(h)-1)].lower()
                                if(h[:(len(h)-1)].lower()==student_answers_this.lower())or(h[:(len(h)-2)].lower()==student_answers_this.lower()):
                                    billur+=1
                                    nahai+=str(counter)+"-"+"Answer is right!\n"
                                    nahai_m+=str(counter)+"-"+"Answer is right!\n"
                                else:
                                    nahai+=str(counter)+"-"+"Answer is wrong!\n"
                                    nahai_m+=str(counter)+"-"+"Answer is wrong!\n"
                                h=""
                                domboli=""
                        now=datetime.now()
                        time_tamam="%s:%s:%s"%(now.hour,now.minute,now.second)
                        file=open(name_answers,"r")
                        student_answers=file.read()
                        file.close()
                        score_of_u="\nScore: "+str(billur)+" of "+str(counter)
                        nahai+="\nStart time: "+time_start+"\nOver time: "+time_tamam+score_of_u+"\n\nCodoffee Quiz Maker"
                        nahai_m+="\nStart time: "+time_start+"\nOver time: "+time_tamam+score_of_u+"\n\nCodoffee Quiz Maker"
                        file=open(name_answers,"w")
                        file.write(nahai_m)
                        file.close()
                        m.clear()
                        m.pu()
                        m.goto(0,20)
                        m.pd()
                        m.pencolor("brown")
                        m.write("Quiz finished!",align="center",font=("Copperplate Gothic Bold",15))
                        time.sleep(1.5)
                        try:
                            plt.close(fig)
                        except:
                            pass
                        file=open("db5.db")
                        n_student=file.read()
                        file.close()
                        file=open("db7.db")
                        t_student=file.read()
                        file.close()
                        file=open("db8.db")
                        c_student=file.read()
                        file.close()
                        ID_show=n_student+", student of "+t_student+" | Class: "+c_student
                        no_address_file_name=""
                        for kt in range(0,len(samanoo)):
                            no_address_file_name+=samanoo[kt]
                            if(samanoo[kt]=="/"):
                                no_address_file_name=""
                        ID_show+=" - "+no_address_file_name
                        ID_show+="\n\n"+nahai
                        ID_show_m=""
                        for joooappuhht in range(0,len(ID_show)):
                            ID_show_m+=str(ord(ID_show[joooappuhht])+984)+"-"
                        file=open("db4.db","w")
                        file.write(salamak_m+"\n"+ID_show_m)
                        file.close()
                        m.clear()
                        m.pu()
                        m.goto(0,20)
                        m.pd()
                        m.pencolor("brown")
                        m.write("Sending result...",align="center",font=("Copperplate Gothic Bold",15))
                        playsound.playsound("9.mp3")
                        import email.mime.text
                        import smtplib
                        while True:
                            try:        
                                def send_email (admin, pwd, user, message):
                                    server = smtplib.SMTP('smtp.gmail.com', 587)
                                    server.ehlo()
                                    server.starttls()
                                    server.login(admin, pwd)
                                    server.sendmail(admin, user, message)
                                    server.close()
                                msg = email.mime.text.MIMEText(ID_show, _charset="UTF-8")
                                send_email('codoffee@gmail.com', 'codoffeemenallah', salamak_m, msg.as_string())
                                file=open("db4.db","w")
                                file.write("1")
                                file.close()
                                m.clear()
                                m.pu()
                                m.goto(0,20)
                                m.pd()
                                m.pencolor("brown")
                                m.write("Sending finished.",align="center",font=("Copperplate Gothic Bold",15))
                                playsound.playsound("11.mp3")
                                break
                            except:
                                m.clear()
                                m.pu()
                                m.goto(0,20)
                                m.pd()
                                m.pencolor("darkorange")
                                m.write("Sorry, The internet aren't talking\nright now. Please check connection.",align="center",font=("Copperplate Gothic Bold",15))
                                playsound.playsound("12.mp3")
                except:
                    m.clear()
                    m.pu()
                    m.goto(0,20)
                    m.pd()
                    m.pencolor("darkorange")
                    m.write("Sorry, exam file isn't working.",align="center",font=("Copperplate Gothic Bold",15))  
                    playsound.playsound("8.mp3")
            def buton2(x,y):
                os.startfile("color.pdf")
                m.clear()
                m.pu()
                m.goto(0,0)
                m.pd()
                m.pencolor("darkblue")
                m.write("Personalize",align="center",font=("Comic Sans MS",35,("bold")))
                time.sleep(4)
                m.clear()
                m.pu()
                m.goto(0,20)
                m.pd()
                m.pencolor("darkblue")
                m.write("Please enter the background color.",align="center",font=("Copperplate Gothic Bold",15))
                bg_color_u=t.textinput("Personalize","Background Color: ").lower()
                m.clear()
                m.write("Please enter the pen color.",align="center",font=("Copperplate Gothic Bold",15))
                p_color_u=t.textinput("Personalize","Pen Color: ").lower()
                m.clear()
                m.write("Please enter the button color.",align="center",font=("Copperplate Gothic Bold",15))
                b_color_u=t.textinput("Personalize","Button Color: ").lower()
                colors=["blue","green","yellow","red","black","white","gray","orange","pink","purple"]
                if(bg_color_u in colors)and(p_color_u in colors)and(b_color_u in colors):
                    file=open("db1.db","w")
                    file.write(bg_color_u)
                    file.close()
                    file=open("db2.db","w")
                    file.write(p_color_u)
                    file.close()
                    file=open("db3.db","w")
                    file.write(b_color_u)
                    file.close()
                else:
                    m.clear()
                    m.pu()
                    m.goto(0,20)
                    m.pd()
                    m.pencolor("darkorange")
                    m.write("Sorry, entered colors are not definite.",align="center",font=("Copperplate Gothic Bold",15))
                    playsound.playsound("5.mp3")
            def buton3(x,y):
                m.clear()
                m.pu()
                m.goto(0,20)
                m.pd()
                m.pencolor("darkblue")
                m.write("Please select exam file, for see result.",align="center",font=("Copperplate Gothic Bold",15))
                root = Tk()
                root.withdraw()
                root.filename=filedialog.askopenfilename(initialdir = "/",title = "Select exam file, for see result.",filetypes = (("Quiz Maker Exam file","*.QME"),("all files","*.*")))+"S"
                try:
                    file=open(root.filename,"r")
                    rootina=file.readline()
                    rootina=file.readline()
                    while True:
                        rootina=file.readline()
                        if(rootina==""):
                            break
                        m.clear()
                        m.pu()
                        m.goto(0,20)
                        m.pd()
                        m.pencolor("brown")
                        if("answer is right!"in rootina.lower()):
                            rootina="Answer of question num-"+rootina[0]+" is right!"
                            m.write(rootina,align="center",font=("Copperplate Gothic Bold",15))
                        if("answer is wrong!"in rootina.lower()):
                            rootina="Answer of question num-"+rootina[0]+" is wrong!"
                            m.write(rootina,align="center",font=("Copperplate Gothic Bold",15))
                        if(rootina.lower()=="codoffee quiz maker"):
                            m.pencolor("darkgray")
                            m.write("Codoffee Quiz Maker",align="center",font=("Copperplate Gothic Bold",15))
                        if("Start time:"in rootina)or("Over time:"in rootina)or("Score:"in rootina):
                            m.pencolor("green")
                            m.write(rootina,align="center",font=("Copperplate Gothic Bold",15))
                        time.sleep(1)
                    file.close()
                except:
                    m.clear()
                    m.pu()
                    m.goto(0,20)
                    m.pd()
                    m.pencolor("darkorange")
                    m.write("Sorry, results dosen't exist.",align="center",font=("Copperplate Gothic Bold",15)) 
                    playsound.playsound("10.mp3")
            def buton4(x,y):
                m.clear()
                m.pu()
                m.goto(0,100)
                m.pd()
                m.pencolor("brown")
                m.write("Help;",align="center",font=("Copperplate Gothic Bold",15))
                m.pu()
                m.goto(0,-60)
                m.pd()
                m.pencolor("black")
                m.write("Click on {Take!} button to take exam. We\nwill send your exam's results for your\nteacher. you can see your results with\nclicking on {Results} button. Click on\n{Info} button to show the Information.\nYou can personalize application using \n{Personalize!} button.",align="center",font=("Copperplate Gothic Bold",15))
                m.pu()
                m.goto(0,-85)
                m.pd()
                m.pencolor("darkblue")
                m.write("Press the {D} key, to learn more.",align="center",font=("Copperplate Gothic Bold",15))
                playsound.playsound("6.mp3")
            def buton5(x,y):
                m.clear()
                m.pu()
                m.goto(0,80)
                m.pd()
                m.pencolor("brown")
                m.write("Information;",align="center",font=("Copperplate Gothic Bold",15))
                m.pu()
                m.goto(0,35)
                m.pd()
                m.pencolor("black")
                m.write("Codoffee Quiz Maker V1.6\n© 2018 Codoffee | All rights reserved.",align="center",font=("Copperplate Gothic Bold",15))
                m.pu()
                m.goto(0,-60)
                m.pd()
                m.pencolor("darkblue")
                m.write("Administration Manager: Aria Izanlou\nSupervisor: Amir Hossain Safarzadeh\nGUI-Designed By Codoffee Maze-GUI\nAudio/Sound Support By Codoffee TTS/STT API",align="center",font=("Copperplate Gothic Bold",15))
                m.pu()
                m.goto(0,-85)
                m.pd()
                m.pencolor("brown")
                m.write("Press the {space} key to log-out.",align="center",font=("Copperplate Gothic Bold",15))
            def buton6(x,y):
                m.clear()
                m.pu()
                m.goto(0,45)
                m.pd()
                m.pencolor("brown")
                m.write("ID Information;",align="center",font=("Copperplate Gothic Bold",15))
                file=open("db5.db")
                name=file.read()+" | Student Account\nThis program has already licensed."
                file.close()
                m.pu()
                m.goto(0,0)
                m.pd()
                m.pencolor("black")
                m.write(name,align="center",font=("Copperplate Gothic Bold",15))
                try:
                    file=open("db10.db")
                    cloudtf=file.read()
                    file.close()
                    cloudtf="Codoffee Cloud | Connected to ID: "+cloudtf
                except:
                    cloudtf="Codoffee Cloud | Not Connected."
                m.pu()
                m.goto(0,-25)
                m.pd()
                m.pencolor("black")
                m.write(cloudtf,align="center",font=("Copperplate Gothic Bold",15))
                m.pu()
                m.goto(0,-45)
                m.pd()
                file=open("db5.db")
                n_student=file.read()
                file.close()
                file=open("db7.db")
                t_student=file.read()
                file.close()
                file=open("db8.db")
                c_student=file.read()
                file.close()
                ID_show=n_student+", student of "+t_student+" | Classroom: "+c_student
                m.pencolor("darkblue")
                m.write(ID_show,align="center",font=("Copperplate Gothic Bold",13))
            def buton7(x,y):
                m.clear()
                m.pu()
                m.goto(0,20)
                m.pd()
                m.pencolor("brown")
                m.write("Connecting to Codoffee Cloud...",align="center",font=("Copperplate Gothic Bold",15))
                time.sleep(3)
                try:
                    file=open("db10.db","r")
                    datacl=file.read()
                    file.close()
                    ftp=ftplib.FTP("ftpupload.net")
                    m.clear()
                    m.pu()
                    m.goto(0,20)
                    m.pd()
                    m.pencolor("black")
                    m.write("Codoffee Cloud has been connected to ID: "+datacl,align="center",font=("Copperplate Gothic Bold",15))
                    m.pu()
                    m.goto(0,0)
                    m.pd()
                    m.pencolor("brown")
                    m.write("Showing up Files...",align="center",font=("Copperplate Gothic Bold",15))
                    ftp=ftplib.FTP("ftpupload.net")
                    ftp.login("cldff_22998458","arizamir")
                    prorpu=t.textinput('Files','Type of showing(Public{Pu}/Private{Pr}): ')
                    if(prorpu.lower()=='pu' or prorpu.lower()=='public'):
                        ftp.cwd('htdocs/'+datacl+'/QM')
                        sabzaloo=ftp.nlst()
                        j=""
                        for i in range(1,len(sabzaloo)):
                            if(".QME" in sabzaloo[i]):
                                j+=sabzaloo[i]+'\n'
                        zardaloo=t.textinput("Files",j)
                    else:
                        passu_req=t.textinput("Files","Cloud Password: ")
                        try:
                            ftp.cwd('htdocs/'+datacl+'/'+passu_req+'/QM')
                        except:
                            m.clear()
                            m.pu()
                            m.goto(0,20)
                            m.pd()
                            m.pencolor("darkorange")
                            m.write("Sorry, password is false.",align="center",font=("Copperplate Gothic Bold",15))
                            playsound.playsound("1.mp3")
                            exit()
                        sabzaloo=ftp.nlst()
                        j=""
                        for i in range(1,len(sabzaloo)):
                            if(".QME" in sabzaloo):
                                j+=sabzaloo[i]+'\n'
                        zardaloo=t.textinput("Files",j)
                    m.clear()
                    m.pu()
                    m.goto(0,20)
                    m.pd()
                    m.pencolor("darkblue")
                    m.write("Please select download's location.",align="center",font=("Copperplate Gothic Bold",15))
                    name_exam_w= Tk()
                    name_exam_w.withdraw()
                    name_exam_w.filename=filedialog.asksaveasfilename(initialdir = "/",title = "Select download's location.",filetypes = (("Quiz Maker Exam file","*.QME"),("all files","*.*")))
                    try:
                        if(".QME"not in zardaloo):
                            zardaloo+=".QME"
                        dll=name_exam_w.filename+".QME"
                        file=open(dll,"wb")
                        ftp.retrbinary('RETR %s' % zardaloo, file.write)
                        file.close()
                        m.clear()
                        m.pu()
                        m.goto(0,20)
                        m.pd()
                        m.pencolor("brown")
                        m.write("File downloaded successfully.",align="center",font=("Copperplate Gothic Bold",15))
                        playsound.playsound("23.mp3")
                    except:
                        m.clear()
                        m.pu()
                        m.goto(0,20)
                        m.pd()
                        m.pencolor("darkorange")
                        m.write("Sorry, something went wrong with downloading.",align="center",font=("Copperplate Gothic Bold",15))
                        playsound.playsound("19.mp3")
                except:
                    m.clear()
                    m.pu()
                    m.goto(0,20)
                    m.pd()
                    m.pencolor("darkorange")
                    m.write("Sorry, The internet aren't talking\nright now. Please check connection.",align="center",font=("Copperplate Gothic Bold",15))
                    playsound.playsound("12.mp3")
            def key1():
                file=open("db4.db","w")
                file.write("0")
                file.close()
                m.clear()
                m.pu()
                m.goto(0,0)
                m.pd()
                m.pencolor("darkgray")
                m.write("Log-out progress was successfull.\nPlease restart Codoffee Quiz Maker.",align="center",font=("Copperplate Gothic Bold",15))
            def key2():
                os.startfile("Docs.pdf")
            m.clear()
            m.pu()
            m.goto(0,0)
            m.pd()
            m.pencolor("darkgray")
            m.write("Codoffee Quiz Maker V1.6\nStudent Account",align="center",font=("Copperplate Gothic Bold",15))
            button1.onclick(buton1)
            button2.onclick(buton2)
            button3.onclick(buton3)
            button4.onclick(buton4)
            button5.onclick(buton5)
            button6.onclick(buton6)
            try:
                button7.onclick(buton7)
            except:
                pass
            scr.onkey(key1,"space")
            scr.onkey(key2,"d")
            scr.listen()
            def bgback():
                while True:
                    t.bgcolor("#737373")
                    time.sleep(1)
                    t.bgcolor("#666666")
                    time.sleep(1)
                    t.bgcolor("#595959")
                    time.sleep(1)
                    t.bgcolor("#666666")
                    time.sleep(1)
                    t.bgcolor("#737373")
                    time.sleep(1)
                    t.bgcolor("#808080")
            def date_time():
                dt=t.Turtle()
                dt.speed(0)
                dt.ht()
                while True:
                    now=datetime.now()
                    now_time="%s:%s"%(now.hour,now.minute)
                    now_date="%s/%s/%s"%(now.month,now.day,now.year)
                    dt.clear()
                    dt.pu()
                    dt.goto(270,222)
                    dt.pd()
                    try:    
                        dt.pencolor("light"+p_color)
                    except:
                        dt.pencolor(p_color)
                    dt.write(now_time,align="center",font=("Bahnschrift SemiBold",17,("bold")))
                    dt.pu()
                    dt.goto(-248,222)
                    dt.pd()
                    dt.pencolor(p_color)
                    dt.write(now_date,align="center",font=("Bahnschrift SemiBold",17,("bold")))
                    time.sleep(59.9)
            thread1=Thread(target=date_time,args=[])
            thread1.start()
            thread2=Thread(target=bgback,args=[])
            thread2.start()
            t.mainloop()
    #language: farsi:
    else:
        #teacher-farsi:
        if(t_or_s.lower()=="teacher"):
            m.clear()
            t.setup(620,510)
            t.title("آزمون ساز کدفي 1.6 | حساب معلم")
            m.ht()
            m.speed(0)
            t.clear()
            t.bgcolor(bg_color)
            t.pencolor("black")
            t.fillcolor("#001a1a")
            t.pu()
            t.goto(-310,210)
            t.pd()
            t.goto(310,210)
            t.pu()
            t.goto(-310,215)
            t.pd()
            t.goto(310,215)
            t.pu()
            t.goto(-310,220)
            t.pd()
            t.begin_fill()
            t.goto(310,220)
            t.goto(310,255)
            t.goto(-310,255)
            t.goto(-310,220)
            t.end_fill()
            t.pu()
            t.goto(-310,-190)
            t.pd()
            t.goto(310,-190)
            t.pu()
            t.goto(-310,-195)
            t.pd()
            t.goto(310,-195)
            t.pu()
            t.goto(-310,-200)
            t.pd()
            t.goto(310,-200)
            t.pu()
            t.goto(-310,-205)
            t.pd()
            t.goto(310,-205)
            t.pu()
            t.goto(-310,-210)
            t.pd()
            t.begin_fill()
            t.goto(310,-210)
            t.goto(310,-255)
            t.goto(-310,-255)
            t.goto(-310,-210)
            t.end_fill()
            button1=Turtle("square")
            button1.speed(0)
            button1.pu()
            button1.goto(0,-194)
            button1.pd()
            button1.shapesize(1.8)
            try:
                button1.fillcolor("light"+b_color)
            except:
                button1.fillcolor(b_color)
            t.pu()
            t.goto(3,-242)
            t.pd()
            try:
                t.pencolor("dark"+b_color)
            except:
                t.pencolor(b_color)
            t.write("شروع",align="center",font=("B Titr",15))
            time.sleep(0.2)
            t.undo()
            t.pu()
            t.goto(13,-242)
            t.pd()
            t.write("شروع",align="center",font=("B Titr",15))
            time.sleep(0.2)
            t.undo()
            t.pu()
            t.goto(-7,-242)
            t.pd()
            t.write("شروع",align="center",font=("B Titr",15))
            time.sleep(0.2)
            t.undo()
            t.pu()
            t.goto(3,-242)
            t.pd()
            t.write("شروع",align="center",font=("B Titr",15))
            button2=Turtle("square")
            button2.speed(4)
            button2.pu()
            button2.goto(-40,225)
            button2.pd()
            button2.shapesize(1.2)
            try:
                button2.fillcolor("dark"+p_color)
            except:
                try:
                    button2.fillcolor("light"+p_color)
                except:
                    button2.fillcolor(p_color)
            button2.left(360)
            t.pu()
            t.goto(-39,191)
            t.pd()
            t.pencolor(p_color)
            t.write("شخصي سازي",align="center",font=("B Titr",10))
            button3=Turtle("triangle")
            button3.speed(0)
            button3.pu()
            button3.goto(150,-197)
            button3.pd()
            button3.shapesize(1.5)
            button3.fillcolor("#ac3973")
            t.pu()
            t.goto(157,-236)
            t.pd()
            t.pencolor("#ac3973")
            t.write("آزمون ها",align="center",font=("B Titr",10))
            button4=Turtle("circle")
            button4.speed(0)
            button4.pu()
            button4.goto(-154,-197)
            button4.pd()
            button4.shapesize(1.5)
            button4.fillcolor("#666699")
            t.pu()
            t.goto(-152,-236)
            t.pd()
            t.pencolor("#666699")
            t.write("راهنما",align="center",font=("B Titr",10))
            button5=Turtle("triangle")
            button5.speed(0)
            button5.pu()
            button5.goto(40,222)
            button5.pd()
            button5.left(90)
            button5.shapesize(1.5)
            button5.fillcolor("lightblue")
            t.pu()
            t.goto(42,191)
            t.pd()
            t.pencolor("darkblue")
            t.write("اطلاعات",align="center",font=("B Titr",10))
            button6=Turtle()
            image = "Logo.gif"
            scr.addshape(image)
            button6.shape(image)
            button6.speed(0)
            button6.pu()
            button6.goto(95,225)
            button6.pd()
            button6.left(90)
            button6.shapesize(2)
            t.pu()
            t.goto(97,192)
            t.pd()
            t.pencolor("red")
            t.write("هويت",align="center",font=("B Titr",10))
            button7=Turtle()
            image = "cloud.gif"
            scr.addshape(image)
            button7.shape(image)
            button7.speed(0)
            button7.pu()
            button7.goto(-260,-200)
            button7.pd()
            button7.left(45)
            button7.shapesize(1.3)
            try:
                file=open("db10.db","r")
                datacl=file.read()
                file.close()
                button8=Turtle()
                image="sun.gif"
                scr.addshape(image)
                button8.shape(image)
                button8.speed(0)
                button8.pu()
                button8.goto(-235,-180)
                button8.pd()
                button8.left(45)
                button8.shapesize(1)
            except:
                pass
            t.pu()
            t.goto(-260,-235)
            t.pd()
            t.pencolor("#ffcc00")
            t.write("فضاي ابري",align="center",font=("B Nazanin",11))
            if(t_v=="0"):
                m.pu()
                m.goto(0,75)
                m.pd()
                m.pencolor("brown")
                m.write("،خوش آمديد",align="center",font=("B Nazanin",15,("bold")))
                m.pu()
                m.goto(0,52)
                m.pd()
                m.pencolor("black")
                m.write("به آزمون ساز کدفي",align="center",font=("B Nazanin",13,("bold")))
                m.pu()
                m.goto(0,26)
                m.pd()
                m.write(".براي يادگيري بروي {راهنما} کليک کنيد",align="center",font=("B Nazanin",13,("bold")))
                file=open("db4.db","w")
                file.write("1")
                file.close()
                time.sleep(3)
            #onclick buttons
            def buton1(x,y):
                m.clear()
                m.pu()
                m.goto(0,20)
                m.pd()
                m.pencolor("brown")
                m.write("...آماده سازي",align="center",font=("B Nazanin",15,("bold")))
                time.sleep(2)
                m.clear()
                m.pu()
                m.goto(0,20)
                m.pd()
                m.pencolor("darkblue")
                m.write(".لطفا نشاني آزمون را مشخص کنيد",align="center",font=("B Nazanin",15,("bold")))
                name_exam_w= Tk()
                name_exam_w.withdraw()
                name_exam_w.filename=filedialog.asksaveasfilename(initialdir = "/",title = ".نشاني آزمون را مشخص کنيد",filetypes = (("Quiz Maker Exam file","*.QME"),("all files","*.*")))
                name_exam_t=name_exam_w.filename+".QME"
                bbiu="0"
                try:
                    file=open(name_exam_t,"r")
                    file.read()
                    file.close()
                    m.clear()
                    m.pu()
                    m.goto(0,20)
                    m.pd()
                    m.pencolor("darkorange")
                    bbiu="1"
                    m.write(".متاسفيم، شما هم اکنون آزموني با اين نشاني داريد",align="center",font=("B Nazanin",15,("bold")))
                except:
                    m.clear()
                    m.pu()
                    m.goto(0,20)
                    m.pd()
                    m.pencolor("darkblue")
                    m.write(".لطفا آدرس پست الکترونيک خود را وارد کنيد",align="center",font=("B Nazanin",15,("bold")))
                    mail_of_u=t.textinput("ساخت آزمون","                       :آدرس پست الکترونيک")+"\n"
                    mail_of_u_m=""
                    for joooapp in range(0,len(mail_of_u)):
                        mail_of_u_m+=str(ord(mail_of_u[joooapp])+835)+"-"
                    m.clear()
                    m.pu()
                    m.goto(0,20)
                    m.pd()
                    m.pencolor("darkblue")
                    m.write(".لطفا براي آزمون رمز انتخاب کنيد",align="center",font=("B Nazanin",15,("bold")))
                    passw_of_e="$"+t.textinput("ساخت آزمون","                                      :رمز")+"$"
                    passw_of_e_m=""
                    for jooooapp in range(0,len(passw_of_e)):
                        passw_of_e_m+=str(ord(passw_of_e[jooooapp])+835)+"-"
                    file=open(name_exam_t,"w")
                    file.write(mail_of_u_m+"\n")
                    file.close()
                if(t_j_o=="0"):
                    m.clear()
                    m.pu()
                    m.goto(0,60)
                    m.pd()
                    m.pencolor("brown")
                    m.write("،اخطار",align="center",font=("B Nazanin",15,("bold")))
                    m.pu()
                    m.goto(-50,-40)
                    m.pd()
                    m.pencolor("black")
                    m.write('''
                    ** شما به هيچ عنوان نبايد علامت {؟} را در بين سوالتان به
                    کار ببريد. شما مي توانيد از اين علامت در پايان سوالتان استفاده
                    .کنيد. ** براي خروج و ثبت آزمون عبارت {تمام} را وارد کنيد
                    '''
                    ,align="center",font=("B Nazanin",13,("bold")))
                    time.sleep(5)
                counter=1
                wq=t.Turtle()
                wq.ht()
                question_m=""
                while(bbiu=="0"):
                    m.clear()
                    m.pu()
                    m.goto(0,-155)
                    m.pd()
                    m.pencolor("white")
                    m.write(".براي ذخيره عبارت {تمام} را وارد کنيد",align="center",font=("B Nazanin",13,("bold")))
                    m.pu()
                    m.goto(0,20)
                    m.pd()
                    m.pencolor("darkred")
                    nahaii=str(counter)
                    m.write(nahaii,align="center",font=("B Titr",50))
                    wq.clear()
                    wq.pu()
                    wq.goto(0,-5)
                    wq.pd()
                    wq.pencolor("darkblue")
                    lofd=".لطفا نوع سوال "+nahaii+" را وارد کنيد"
                    wq.write(lofd,align="center",font=("B Nazanin",12))       
                    typeq=t.textinput(name_exam_t,"                     :نوع سوال(تشريحي/گزينه اي)")
                    if(typeq=="تمام")or(typeq=="تمام؟")or(typeq==""):
                        break
                    wq.pu()
                    wq.goto(0,-25)
                    wq.pd()
                    wq.pencolor("darkblue")
                    lofd=".لطفا سوال "+nahaii+" را وارد کنيد"
                    wq.write(lofd,align="center",font=("B Nazanin",12))
                    question=t.textinput(name_exam_t,"                                         :سوال")
                    if(question=="تمام")or(question=="تمام؟")or(question==""):
                        break
                    choices=""
                    if(typeq=="گزينه")or(typeq=="گزينه اي"):
                        wq.pu()
                        wq.goto(0,-45)
                        wq.pd()
                        wq.pencolor("darkblue")
                        lofd=".لطفا گزينه ها را وارد کنيد. از {/} براي جداسازي استفاده کنيد" 
                        wq.write(lofd,align="center",font=("B Nazanin",12))
                        choices=t.textinput(name_exam_t,"                                      :گزينه هاي سوال")
                        if(choices=="تمام")or(choices=="تمام؟")or(choices==""):
                            break
                        wq.pu()
                        wq.goto(0,-65)
                        wq.pd()
                        wq.pencolor("darkblue")
                        lofd=".لطفا پاسخ صحيح را وارد کنيد"
                        wq.write(lofd,align="center",font=("B Nazanin",12))
                        if(question[len(question)-1]=="?"):
                            question=question[:(len(question)-1)]
                        if(question[len(question)-1]=="؟"):
                            question=question[:(len(question)-1)]
                        question+=" ( "+choices+" )"
                    else:
                        wq.pu()
                        wq.goto(0,-45)
                        wq.pd()
                        wq.pencolor("darkblue")
                        lofd=".لطفا پاسخ صحيح اين سوال را وارد کنيد"
                        wq.write(lofd,align="center",font=("B Nazanin",12))
                    if("؟" not in question)and(question!=""):
                        question+="؟"
                    answer_of_q=t.textinput(name_exam_t,"                                :جواب سوال")+"!"                                                                 
                    try:
                        file=open("db10.db","r")
                        file.read()
                        file.close()
                        wq.clear()
                        wq.pu()
                        wq.goto(0,-25)
                        wq.pd()
                        wq.pencolor("darkblue")
                        lofd="آيا شما مي خواهيد عکسي بارگذاري کنيد؟"
                        wq.write(lofd,align="center",font=("B Nazanin",12))
                        pic_s=t.textinput(name_exam_t,"                                  :بارگذاري(بله/خير)")
                        if(pic_s=="بله"):
                            wq.pu()
                            wq.goto(0,-45)
                            wq.pd()
                            wq.pencolor("darkblue")
                            lofd=".لطفا عکس را انتخاب کنيد"
                            wq.write(lofd,align="center",font=("B Nazanin",12))
                            root = Tk()
                            root.withdraw()
                            root.filename=filedialog.askopenfilename(initialdir = "/",title = ".عکس را انتخاب کنيد",filetypes = ((("Graphics Interchange File","*.gif"),("Digital images","*.jpg"),("Digital images","*.jpeg"),("Portable Network Graphics","*.png"),("all files","*.*"))))
                            no_address_file_name=""
                            for kt in range(0,len(root.filename)):
                                no_address_file_name+=root.filename[kt]
                                if(root.filename[kt]=="/"):
                                    no_address_file_name=""
                            question+=no_address_file_name
                            wq.pu()
                            wq.goto(0,-65)
                            wq.pd()
                            wq.pencolor("darkblue")
                            lofd="...در حال بارگذاري فايل"
                            wq.write(lofd,align="center",font=("B Nazanin",12))
                            time.sleep(1)
                            file=open("db10.db")
                            usern_cloud=file.read()
                            file.close()
                            try:
                                session=ftplib.FTP("ftpupload.net","cldff_22998458","arizamir")
                                file=open(root.filename,'rb')                  
                                session.storbinary('STOR '+"htdocs/"+usern_cloud+"/QM/"+no_address_file_name,file)     
                                file.close()                                    
                                session.quit()
                                wq.undo()
                                wq.pu()
                                wq.goto(0,-65)
                                wq.pd()
                                wq.pencolor("darkblue")
                                lofd=".بارگذاري با موفقيت انجام شد"
                                wq.write(lofd,align="center",font=("B Nazanin",12))
                                time.sleep(1.5)
                            except:
                                wq.clear()
                                wq.pu()
                                wq.goto(0,-65)
                                wq.pd()
                                wq.pencolor("darkorange")
                                wq.write(".متاسفيم، ارتباطات درون شبکه موجود نمي باشد",align="center",font=("B Nazanin",12))
                                time.sleep(1.5)
                        else:
                            wq.pu()
                            wq.goto(0,-45)
                            wq.pd()
                            wq.pencolor("darkblue")
                            lofd=".بارگذاري لغو شد"
                            wq.write(lofd,align="center",font=("B Nazanin",12))
                            time.sleep(1.5)
                    except:
                        pass
                    question_mm=""
                    for yjru in range(0,len(question)):
                        question_mm+=question[yjru]
                        if(yjru%60==0)and(yjru!=0):
                            question_mm+="\n"
                    question_mm+=answer_of_q+"\n"
                    for jooapp in range(0,len(question_mm)):
                        question_m+=str(ord(question_mm[jooapp])+835)+"-"
                    file=open(name_exam_t,"r")
                    befor_exam=file.read()
                    file.close()
                    befor_exam+=question_m+"\n"
                    question_m=""
                    file=open(name_exam_t,"w")
                    file.write(befor_exam)
                    file.close()
                    counter+=1
                file=open(name_exam_t,"r")
                befor_exam=file.read()
                file.close()
                befor_exam+=passw_of_e_m
                file=open(name_exam_t,"w")
                file.write(befor_exam)
                file.close()
                wq.clear()
                m.clear()
                m.pu()
                m.goto(0,20)
                m.pd()
                m.pencolor("brown")
                m.write(".آزمون با موفقيت ساخته شد",align="center",font=("B Nazanin",15,("bold")))
                abirang=True
                if(abirang==True):
                    try:
                        file=open("db10.db","r")
                        file.read()
                        file.close()
                        wq.clear()
                        wq.pu()
                        wq.goto(0,-45)
                        wq.pd()
                        wq.pencolor("darkblue")
                        wq.write("آيا مايل به بارگذاري اين آزمون در فضاي ابري هستيد؟",align="center",font=("B Nazanin",12))
                        pic_s=t.textinput(name_exam_t,"                                 :آپلود؟(بله/خير)")
                        if(pic_s=="بله"):
                            no_address_file_name=""
                            for kt in range(0,len(name_exam_t)):
                                no_address_file_name+=name_exam_t[kt]
                                if(name_exam_t[kt]=="/"):
                                    no_address_file_name=""
                            wq.pu()
                            wq.goto(0,-65)
                            wq.pd()
                            wq.pencolor("darkblue")
                            lofd="...در حال بارگذاري آزمون"
                            wq.write(lofd,align="center",font=("B Nazanin",12))
                            time.sleep(1)
                            passu_cloud=t.textinput(name_exam_t,"                                :رمز فضاي ابري")
                            typeofm=t.textinput(name_exam_t,"                                 :نوع بارگذاري(خصوصي/عمومي)")
                            file=open("db10.db")
                            usern_cloud=file.read()
                            file.close()
                            try:
                                session=ftplib.FTP("ftpupload.net","cldff_22998458","arizamir")
                                try:
                                    if(typeofm.lower()=="عمومي"):
                                        file=open(name_exam_t,'rb')
                                        session.storlines('STOR '+"htdocs/"+usern_cloud+"/QM/"+no_address_file_name,file)     
                                        file.close()
                                    if(typeofm.lower()=="خصوصي"):
                                        file=open(name_exam_t,'rb')                  
                                        session.storlines('STOR '+"htdocs/"+usern_cloud+"/"+passu_cloud+"/QM/"+no_address_file_name,file)     
                                        file.close()
                                    session.quit()
                                    wq.undo()
                                    wq.pu()
                                    wq.goto(0,-65)
                                    wq.pd()
                                    wq.pencolor("darkblue")
                                    lofd=".بارگذاري با موفقيت انجام شد"
                                    wq.write(lofd,align="center",font=("B Nazanin",12))
                                    time.sleep(1.5)
                                except:
                                    wq.undo()
                                    wq.pu()
                                    wq.goto(0,-65)
                                    wq.pd()
                                    wq.pencolor("darkorange")
                                    wq.write(".متاسفيم، رمز اشتباه است",align="center",font=("B Nazanin",12))
                                    time.sleep(1.5)
                            except:
                                wq.clear()
                                wq.pu()
                                wq.goto(0,-85)
                                wq.pd()
                                wq.pencolor("darkorange")
                                wq.write(".متاسفيم، ارتباطات درون شبکه موجود نمي باشد",align="center",font=("B Nazanin",12))
                                time.sleep(1.5)
                        else:
                            wq.pu()
                            wq.goto(0,-65)
                            wq.pd()
                            wq.pencolor("darkblue")
                            lofd=".بارگذاري لغو شد"
                            wq.write(lofd,align="center",font=("B Nazanin",12))
                            time.sleep(1.5)
                        wq.clear()
                    except:
                        pass
            def buton2(x,y):
                os.startfile("color.pdf")
                m.clear()
                m.pu()
                m.goto(0,0)
                m.pd()
                m.pencolor("darkblue")
                m.write("شخصي سازي",align="center",font=("B Titr",35))
                time.sleep(4)
                m.clear()
                m.pu()
                m.goto(0,20)
                m.pd()
                m.pencolor("darkblue")
                m.write(".لطفا رنگ پس زمينه را وارد کنيد",align="center",font=("B Nazanin",15,("bold")))
                bg_color_u=t.textinput("شخصي سازي","                :رنگ پس زمينه، الزاما انگليسي").lower()
                m.clear()
                m.write(".لطفا رنگ مداد را انتخاب کنيد",align="center",font=("B Nazanin",15,("bold")))
                p_color_u=t.textinput("شخصي سازي","                   :رنگ مداد، الزاما انگليسي").lower()
                m.clear()
                m.write(".لطفا رنگ دکمه را انتخاب کنيد",align="center",font=("B Nazanin",15,("bold")))
                b_color_u=t.textinput("شخصي سازي","                   :رنگ دکمه، الزاما انگليسي").lower()
                colors=["blue","green","yellow","red","black","white","gray","orange","pink","purple"]
                if(bg_color_u in colors)and(p_color_u in colors)and(b_color_u in colors):
                    file=open("db1.db","w")
                    file.write(bg_color_u)
                    file.close()
                    file=open("db2.db","w")
                    file.write(p_color_u)
                    file.close()
                    file=open("db3.db","w")
                    file.write(b_color_u)
                    file.close()
                else:
                    m.clear()
                    m.pu()
                    m.goto(0,20)
                    m.pd()
                    m.pencolor("darkorange")
                    m.write(".متاسفيم، رنگ هاي وارد شده مشخص شده نيستند",align="center",font=("B Nazanin",15,("bold")))
            def buton3(x,y):
                try:
                    m.clear()
                    m.pu()
                    m.goto(0,20)
                    m.pd()
                    m.pencolor("darkblue")
                    m.write(".لطفا آزمون مورد نظر را انتخاب کنيد",align="center",font=("B Nazanin",15,("bold")))
                    root = Tk()
                    root.withdraw()
                    root.filename=filedialog.askopenfilename(initialdir = "/",title = ".آزمون را انتخاب کنيد",filetypes = (("Quiz Maker Exam file","*.QME"),("all files","*.*")))
                    if(".QME"not in root.filename):
                        error1()
                    file=open(root.filename)
                    salamak=file.readline()
                    exam=file.read()
                    file.close()
                    h=""
                    taghalob="0"
                    m.clear()
                    m.pu()
                    m.goto(0,20)
                    m.pd()
                    m.pencolor("darkblue")
                    m.write(".لطفا رمز را وارد کنيد",align="center",font=("B Nazanin",15,("bold")))
                    passwc_of_e=t.textinput(root.filename,"                                        :رمز")
                    huit=0
                    jo=""
                    passwc=""
                    for jomunji in range(0,len(exam)):
                        if(exam[jomunji]=="-"):
                            jo=int(jo)-835
                            bomboli=chr(jo)
                            if(huit==1):
                                huit+=1
                            if(bomboli=="$"):
                                huit+=1
                            if(huit==2):
                                passwc+=chr(jo)
                            elif(huit==3):
                                break
                            jo=""
                        else:
                            jo+=exam[jomunji]
                    if(passwc==passwc_of_e):
                        taghalob="1"
                    else:
                        m.clear()
                        m.pu()
                        m.goto(0,20)
                        m.pd()
                        m.pencolor("darkorange")
                        m.write(".متاسفيم، رمز اشتباه مي باشد",align="center",font=("B Nazanin",15,("bold")))
                    if(taghalob=="1"):
                        m.clear()
                        m.pu()
                        m.goto(0,20)
                        m.pd()
                        m.pencolor("brown")
                        m.write("...آزمون در حال شروع شدن است",align="center",font=("B Nazanin",15,("bold")))
                        time.sleep(1.5)
                        domboli=""
                        jo=""
                        for k in range(0,len(exam)):
                            if(exam[k]=="-"):
                                jo=int(jo)-835
                                h+=chr(jo)
                                domboli=chr(jo)
                                jo=""
                            else:
                                jo+=exam[k]
                            joi=""
                            hi=""
                            if(domboli=="?")or(domboli=="؟"):
                                try:
                                    for jhk in range(k+1,len(exam)):
                                        if(exam[jhk]=="-"):
                                            joi=int(joi)-835
                                            hi+=chr(joi)
                                            if(".gif" in hi)or(".GIF" in hi)or(".png" in hi)or(".PNG" in hi)or(".jpg" in hi)or(".JPG" in hi)or(".jpeg" in hi)or(".JPEG" in hi):
                                                break
                                            joi=""
                                        else:
                                            joi+=exam[jhk]
                                    ftp=ftplib.FTP("ftpupload.net")
                                    ftp.login("cldff_22998458","arizamir")
                                    file=open("db10.db")
                                    datacl=file.read()
                                    file.close()
                                    ftp.cwd('htdocs/'+datacl+"/QM")
                                    file=open(hi,"wb")
                                    ftp.retrbinary('RETR %s' % hi, file.write)
                                    file.close()
                                    fig = plt.figure(0)
                                    fig.canvas.set_window_title('آزمون ساز کدفي | عکس سوال')
                                    img=mpimg.imread(hi)
                                    imgplot = plt.imshow(img)
                                    fig.show()
                                    time.sleep(0.5)
                                    os.remove(hi)
                                except:
                                    pass
                                m.clear()
                                m.pu()
                                m.goto(0,-10)
                                m.pd()
                                m.pencolor("black")
                                m.write(h,align="center",font=("B Nazanin",12,("bold")))
                                h=""
                                student_answers_this=t.textinput(root.filename,"                       :لطفا سوال را پاسخ دهيد")
                                try:
                                    plt.close(fig)
                                except:
                                    pass
                                domboli=""
                            elif(domboli=="!"):
                                h=""
                                domboli=""
                        m.clear()
                        m.pu()
                        m.goto(0,20)
                        m.pd()
                        m.pencolor("brown")
                        m.write(".آزمون پايان يافت",align="center",font=("B Nazanin",15,("bold")))
                        try:
                            plt.close(fig)
                        except:
                            pass
                except:
                    m.clear()
                    m.pu()
                    m.goto(0,20)
                    m.pd()
                    m.pencolor("darkorange")
                    m.write(".متاسفيم، آزمون کار نمي کند",align="center",font=("B Nazanin",15,("bold")))  
            def buton4(x,y):
                m.clear()
                m.pu()
                m.goto(0,70)
                m.pd()
                m.pencolor("brown")
                m.write("،راهنما",align="center",font=("B Nazanin",15,("bold")))
                m.pu()
                m.goto(0,-35)
                m.pd()
                m.pencolor("black")
                m.write(".براي ساخت آزمون بروي {شروع} کليک کنيد\n.براي آزمايش آزمون هايتان بروي {آزمون ها} کليک کنيد\n.براي نمايش اطلاعات بروي {اطلاعات} کليک کنيد\n.شما مي توانيد با استفاده از {شخصي سازي} نرم افزار خود را شخصي سازي کنيد",align="center",font=("B Nazanin",13,("bold")))
                m.pu()
                m.goto(0,-65)
                m.pd()
                m.pencolor("darkblue")
                m.write(".کليد {ي} را فشار دهيد تا جزييات بيشتري ببينيد",align="center",font=("B Nazanin",13,("bold")))
            def buton5(x,y):
                m.clear()
                m.pu()
                m.goto(0,95)
                m.pd()
                m.pencolor("brown")
                m.write("،اطلاعات",align="center",font=("B Nazanin",15,("bold")))
                m.pu()
                m.goto(0,40)
                m.pd()
                m.pencolor("black")
                m.write("آزمون ساز کدفي 1.6\n© 2018 تمامي حقوق محفوظ است. | کدفي",align="center",font=("B Nazanin",15))
                m.pu()
                m.goto(0,-75)
                m.pd()
                m.pencolor("darkblue")
                m.write("مدير اجرايي : آريا ايزانلو\nمدير گروه : اميرحسين صفرزاده\nرابط کاربري - طراحي شده توسط کدفي\nصداپردازي - حمايت شده توسط کدفي",align="center",font=("B Nazanin",15))
            def buton6(x,y):
                m.clear()
                m.pu()
                m.goto(0,35)
                m.pd()
                m.pencolor("brown")
                m.write("،اطلاعات هويت",align="center",font=("B Nazanin",15,("bold")))
                file=open("db5.db")
                name="حساب معلم | "+file.read()
                file.close()
                m.pu()
                m.goto(0,10)
                m.pd()
                m.pencolor("black")
                m.write(name,align="center",font=("B Nazanin",13,("bold")))
                try:
                    file=open("db10.db")
                    cloudtf=file.read()
                    file.close()
                    cloudtf=cloudtf+" :فضاي ابري | متصل به آيدي"
                except:
                    cloudtf=".فضاي ابري | متصل نيست"
                m.pu()
                m.goto(0,-18)
                m.pd()
                m.pencolor("black")
                m.write(cloudtf,align="center",font=("B Nazanin",13,("bold")))
                m.pu()
                m.goto(0,-47)
                m.pd()
                m.pencolor("darkblue")
                m.write(".کليد {فاصله} را فشار دهيد تا از حساب خارج شويد",align="center",font=("B Nazanin",13,("bold")))
            def buton7(x,y):
                try:
                    file=open("db10.db","r")
                    datacl=file.read()
                    file.close()
                    m.clear()
                    m.pu()
                    m.goto(0,20)
                    m.pd()
                    m.pencolor("brown")
                    m.write(" :فضاي ابري در حال حاضر متصل است به آيدي",align="center",font=("B Nazanin",15,("bold")))
                    m.pu()
                    m.goto(0,-5)
                    m.pd()
                    m.pencolor("black")
                    m.write(datacl,align="center",font=("B Nazanin",15,("bold")))
                except:
                    m.clear()
                    m.pu()
                    m.goto(0,20)
                    m.pd()
                    m.pencolor("brown")
                    m.write("...در حال اتصال به فضاي ابري",align="center",font=("B Nazanin",15,("bold")))
                    time.sleep(3)
                    m.clear()
                    m.pu()
                    m.goto(0,20)
                    m.pd()
                    m.pencolor("brown")
                    m.write("ورود به فضاي ابري",align="center",font=("B Nazanin",15,("bold")))
                    m.pu()
                    m.goto(0,-30)
                    m.pd()
                    m.pencolor("black")
                    m.write("اگر شما حساب نداريد، مي توانيد از\n.حساب بسازيد codoffeegroup.ir/cloud طريق",align="center",font=("B Nazanin",12,("bold")))
                    usern_cloud=t.textinput("ورود به فضاي ابري","                                   :آيدي فضاي ابري")
                    passu_cloud=t.textinput("ورود به فضاي ابري","                                   :رمز فضاي ابري")
                    try:
                        m.clear()
                        m.pu()
                        m.goto(0,20)
                        m.pd()
                        m.pencolor("brown")
                        m.write("...در حال بررسي حساب شما",align="center",font=("B Nazanin",15,("bold")))
                        time.sleep(3)
                        ftp=ftplib.FTP("ftpupload.net")
                        ftp.login("cldff_22998458","arizamir")
                        ftp.cwd('htdocs')
                        def directory_exists(dir):
                            dr_exits=ftp.nlst()
                            if(dir) in dr_exits:
                                return True
                            else:
                                return False
                        if directory_exists(usern_cloud) is True:
                            ftp.cwd(usern_cloud)
                            if ('QM' in ftp.nlst()):
                                pass
                            else:
                                try:
                                    ftp.mkd('QM')
                                except:
                                    pass
                            if (directory_exists(passu_cloud)) is True:
                                ftp.cwd(passu_cloud)
                                if ('QM' in ftp.nlst()):
                                    pass
                                else:
                                    try:
                                        ftp.mkd('QM')
                                    except:
                                        pass
                                m.clear()
                                m.pu()
                                m.goto(0,20)
                                m.pd()
                                m.pencolor("black")
                                m.write(usern_cloud+" :خوش آمديد آيدي",align="center",font=("B Nazanin",15,("bold")))
                                m.pu()
                                m.goto(0,-30)
                                m.pd()
                                m.pencolor("white")
                                m.write(".ورود به حساب با موفقيت انجام شد\n.لطفا نرم افزار را دوباره اجرا کنيد",align="center",font=("B Nazanin",12,("bold")))
                                file=open("db10.db","w")
                                file.write(usern_cloud)
                                file.close()
                                ftp.quit()
                            else:
                               m.clear()
                               m.pu()
                               m.goto(0,20)
                               m.pd()
                               m.pencolor("darkorange")
                               m.write("متاسفيم، رمز اشتباه است",align="center",font=("B Nazanin",15,("bold")))
                               ftp.quit()
                        else:
                            m.clear()
                            m.pu()
                            m.goto(0,20)
                            m.pd()
                            m.pencolor("darkorange")
                            m.write(".متاسفيم، حسابي با اين آيدي وجود ندارد",align="center",font=("B Nazanin",15,("bold")))
                    except:
                        m.clear()
                        m.pu()
                        m.goto(0,20)
                        m.pd()
                        m.pencolor("darkorange")
                        m.write(".متاسفيم، ارتباطات درون شبکه موجود نمي باشد\n.لطفا ارتباطات را بررسي کنيد",align="center",font=("B Nazanin",15,("bold")))
            def buton8(x,y):    
                m.clear()
                m.pu()
                m.goto(0,20)
                m.pd()
                m.pencolor("brown")
                m.write("...در حال اتصال به فضاي ابري",align="center",font=("B Nazanin",15,("bold")))
                time.sleep(3)
                try:
                    file=open("db10.db","r")
                    datacl=file.read()
                    file.close()
                    m.clear()
                    m.pu()
                    m.goto(0,20)
                    m.pd()
                    m.pencolor("black")
                    m.write(datacl+" :فضاي ابري در حال حاضر متصل است به آيدي",align="center",font=("B Nazanin",15,("bold")))
                    m.pu()
                    m.goto(0,-5)
                    m.pd()
                    m.pencolor("brown")
                    m.write("...نمايش فايل هاي شما",align="center",font=("B Nazanin",15,("bold")))
                    ftp=ftplib.FTP("ftpupload.net")
                    ftp.login("cldff_22998458","arizamir")
                    prorpu=t.textinput('فايل هاي من','                               :نوع نمايش(عمومي/خصوصي)')
                    if(prorpu=="عمومي"):
                        ftp.cwd('htdocs/'+datacl+'/QM')
                        sabzaloo=ftp.nlst()
                        j=""
                        for i in range(1,len(sabzaloo)):
                            if(".QME" in sabzaloo[i]):
                                j+=sabzaloo[i]+'\n'
                        zardaloo=t.textinput("فايل هاي من",j)
                    else:
                        passu_req=t.textinput("فايل هاي من","                                   :رمز فضاي ابري")
                        try:
                            ftp.cwd('htdocs/'+datacl+'/'+passu_req+'/QM')
                        except:
                            m.clear()
                            m.pu()
                            m.goto(0,20)
                            m.pd()
                            m.pencolor("darkorange")
                            m.write(".متاسفيم رمز اشتباه است",align="center",font=("B Nazanin",15,("bold")))
                            time.sleep(1.5)
                            exit()
                        sabzaloo=ftp.nlst()
                        j=""
                        for i in range(1,len(sabzaloo)):
                            if(".QME" in sabzaloo[i]):
                                j+=sabzaloo[i]+'\n'
                        zardaloo=t.textinput("My Files",j)
                    m.clear()
                    m.pu()
                    m.goto(0,20)
                    m.pd()
                    m.pencolor("darkblue")
                    m.write(".لطفا محل دريافت فايل را انتخاب کنيد",align="center",font=("B Nazanin",15,("bold")))
                    name_exam_w= Tk()
                    name_exam_w.withdraw()
                    name_exam_w.filename=filedialog.asksaveasfilename(initialdir = "/",title = ".محل دريافت را انتخاب کنيد",filetypes = (("Quiz Maker Exam file","*.QME"),("all files","*.*")))
                    try:
                        if(".QME"not in zardaloo):
                            zardaloo+=".QME"
                        dll=name_exam_w.filename+".QME"
                        file=open(dll,"wb")
                        ftp.retrbinary('RETR %s' % zardaloo, file.write)
                        file.close()
                        m.clear()
                        m.pu()
                        m.goto(0,20)
                        m.pd()
                        m.pencolor("brown")
                        m.write(".فايل شما با موفقيت دريافت شد",align="center",font=("B Nazanin",15,("bold")))
                    except:
                        m.clear()
                        m.pu()
                        m.goto(0,20)
                        m.pd()
                        m.pencolor("darkorange")
                        m.write(".متاسفيم، مشکلي در دريافت فايل رخ داده است",align="center",font=("B Nazanin",15,("bold")))
                except:
                    m.clear()
                    m.pu()
                    m.goto(0,20)
                    m.pd()
                    m.pencolor("darkorange")
                    m.write(".متاسفيم، ارتباطات درون شبکه موجود نمي باشد\n.لطفا ارتباطات را بررسي کنيد",align="center",font=("B Nazanin",15,("bold")))          
            def key1():
                file=open("db4.db","w")
                file.write("0")
                file.close()
                m.clear()
                m.pu()
                m.goto(0,0)
                m.pd()
                m.pencolor("darkgray")
                m.write(".خروج از حساب با موفقيت انجام شد\n.لطفا نرم افزار را دوباره اجرا کنيد",align="center",font=("B Nazanin",15,("bold")))
            def key2():
                os.startfile("Docs.pdf")
            m.clear()
            m.pu()
            m.goto(0,0)
            m.pd()
            m.pencolor("darkgray")
            m.write("آزمون ساز کدفي\nحساب معلم",align="center",font=("B Titr",15))
            button1.onclick(buton1)
            button2.onclick(buton2)
            button3.onclick(buton3)
            button4.onclick(buton4)
            button5.onclick(buton5)
            button6.onclick(buton6)
            button7.onclick(buton7)
            try:
                button8.onclick(buton8)
            except:
                pass            
            scr.onkey(key1,"space")
            scr.onkey(key2,"d")
            scr.listen()
            def bgback():
                while True:
                    t.bgcolor("#5c5c3d")
                    time.sleep(1)
                    t.bgcolor("#4d4d33")
                    time.sleep(1)
                    t.bgcolor("#3d3d29")
                    time.sleep(1)
                    t.bgcolor("#4d4d33")
                    time.sleep(1)
                    t.bgcolor("#5c5c3d")
                    time.sleep(1)
                    t.bgcolor("#6b6b47")
            def date_time():
                dt=t.Turtle()
                dt.speed(0)
                jdatetime.set_locale('fa_IR')
                while True:
                    dt.ht()
                    now=datetime.now()
                    now_date=jdatetime.datetime.now().strftime("%d/%m/%Y")
                    now_time=jdatetime.datetime.now().strftime("%H:%M")
                    dt.clear()
                    dt.pu()
                    dt.goto(270,218)
                    dt.pd()
                    dt.pencolor(p_color)
                    dt.write(now_time,align="center",font=("B Titr",15))
                    dt.pu()
                    dt.goto(-250,218)
                    dt.pd()
                    dt.write(now_date,align="center",font=("B Titr",15))
                    time.sleep(59.9)
            thread1=Thread(target=date_time,args=[])
            thread1.start()
            thread2=Thread(target=bgback,args=[])
            thread2.start()
            t.mainloop()
        #student-farsi:
        elif(t_or_s.lower()=="student"):
            m.clear()
            t.setup(620,510)
            t.title("آزمون ساز کدفي 1.6 | حساب دانش آموز")
            m=t.Turtle()
            m.ht()
            m.speed(0)
            t.clear()
            if(bg_color=="#6b6b47"):
                t.bgcolor("gray")
            else:
                t.bgcolor(bg_color)
            t.pencolor("#001a00")
            t.fillcolor("#001a00")
            t.pu()
            t.goto(-310,210)
            t.pd()
            t.goto(310,210)
            t.pu()
            t.goto(-310,215)
            t.pd()
            t.goto(310,215)
            t.pu()
            t.goto(-310,220)
            t.pd()
            t.goto(310,220)
            t.pd()
            t.begin_fill()
            t.goto(310,220)
            t.goto(310,255)
            t.goto(-310,255)
            t.goto(-310,220)
            t.end_fill()
            t.pu()
            t.goto(-310,-190)
            t.pd()
            t.goto(310,-190)
            t.pu()
            t.goto(-310,-195)
            t.pd()
            t.goto(310,-195)
            t.pu()
            t.goto(-310,-200)
            t.pd()
            t.goto(310,-200)
            t.pu()
            t.goto(-310,-205)
            t.pd()
            t.goto(310,-205)
            t.pu()
            t.goto(-310,-210)
            t.pd()
            t.begin_fill()
            t.goto(310,-210)
            t.goto(310,-255)
            t.goto(-310,-255)
            t.goto(-310,-210)
            t.end_fill()
            button1=Turtle("triangle")
            button1.speed(0)
            button1.pu()
            button1.goto(-3,-194)
            button1.pd()
            button1.shapesize(1.8)
            try:
                button1.fillcolor("dark"+b_color)
            except:
                button1.fillcolor(b_color)
            t.pu()
            t.goto(3,-242)
            t.pd()
            try:
                t.pencolor("light"+b_color)
            except:
                t.pencolor(b_color)
            t.write("شروع",align="center",font=("B Titr",15))
            time.sleep(0.2)
            t.undo()
            t.pu()
            t.goto(13,-242)
            t.pd()
            t.write("شروع",align="center",font=("B Titr",15))
            time.sleep(0.2)
            t.undo()
            t.pu()
            t.goto(-7,-242)
            t.pd()
            t.write("شروع",align="center",font=("B Titr",15))
            time.sleep(0.2)
            t.undo()
            t.pu()
            t.goto(3,-242)
            t.pd()
            t.write("شروع",align="center",font=("B Titr",15))
            button2=Turtle("square")
            button2.speed(4)
            button2.pu()
            button2.goto(-46,225)
            button2.pd()
            button2.shapesize(1.2)
            try:
                button2.fillcolor("dark"+p_color)
            except:
                try:
                    button2.fillcolor("light"+p_color)
                except:
                    button2.fillcolor(p_color)
            button2.left(360)
            t.pu()
            t.goto(-45,191)
            t.pd()
            t.pencolor(p_color)
            t.write("شخصي سازي",align="center",font=("B Titr",10))
            button3=Turtle("circle")
            button3.speed(0)
            button3.pu()
            button3.goto(116,-197)
            button3.pd()
            button3.shapesize(1.5)
            button3.fillcolor("pink")
            t.pu()
            t.goto(116,-233)
            t.pd()
            t.pencolor("pink")
            t.write("نتايج",align="center",font=("B Titr",10))
            button4=Turtle("square")
            button4.speed(0)
            button4.pu()
            button4.goto(-120,-197)
            button4.pd()
            button4.shapesize(1.4)
            button4.fillcolor("darkorange")
            t.pu()
            t.goto(-118,-233)
            t.pd()
            t.pencolor("darkorange")
            t.write("راهنما",align="center",font=("B Titr",10))
            button5=Turtle("triangle")
            button5.speed(0)
            button5.pu()
            button5.goto(34,222)
            button5.pd()
            button5.left(90)
            button5.shapesize(1.5)
            button5.fillcolor("lightblue")
            t.pu()
            t.goto(36,191)
            t.pd()
            t.pencolor("darkblue")
            t.write("اطلاعات",align="center",font=("B Titr",10))
            button6=Turtle()
            image = "Logo.gif"
            scr.addshape(image)
            button6.shape(image)
            button6.speed(0)
            button6.pu()
            button6.goto(95,225)
            button6.pd()
            button6.left(90)
            button6.shapesize(2)
            t.pu()
            t.goto(96,192)
            t.pd()
            t.pencolor("red")
            t.write("هويت",align="center",font=("B Titr",10))
            try:
                file=open("db10.db","r")
                file.read()
                file.close()
                button7=Turtle("square")
                button7.speed(0)
                button7.pu()
                button7.goto(-260,-196)
                button7.pd()
                button7.left(45)
                button7.shapesize(1)
                image = "cloudl.gif"
                scr.addshape(image)
                button7.shape(image)
                t.pu()
                t.goto(-258,-235)
                t.pd()
                t.pencolor("#e6b800")
                t.write("فضاي ابري",align="center",font=("B Nazanin",11))
            except:
                pass
            if(t_v=="0"):
                m.pu()
                m.goto(0,75)
                m.pd()
                m.pencolor("brown")
                m.write("،خوش آمديد",align="center",font=("B Nazanin",15,("bold")))
                m.pu()
                m.goto(0,52)
                m.pd()
                m.pencolor("black")
                m.write("به آزمون ساز کدفي",align="center",font=("B Nazanin",13,("bold")))
                m.pu()
                m.goto(0,26)
                m.pd()
                m.write(".براي يادگيري بروي {راهنما} کليک کنيد",align="center",font=("B Nazanin",13,("bold")))
                file=open("db4.db","w")
                file.write("1")
                file.close()
                time.sleep(3)
            def buton1(x,y):
                try:
                    m.clear()
                    m.pu()
                    m.goto(0,20)
                    m.pd()
                    m.pencolor("darkblue")
                    m.write(".لطفا آزمون مورد نظر را انتخاب کنيد",align="center",font=("B Nazanin",15,("bold")))
                    root = Tk()
                    root.withdraw()
                    root.filename=filedialog.askopenfilename(initialdir = "/",title = ".آزمون را انتخاب کنيد",filetypes = (("Quiz Maker Exam file","*.QME"),("all files","*.*")))
                    if(".QME"not in root.filename):
                        error1()
                    import smtplib
                    file=open(root.filename)
                    salamak=file.readline()
                    exam=file.read()
                    file.close()
                    uitwq=""
                    salamak_m=""
                    for joooooapp in range(0,len(salamak)):
                        if(salamak[joooooapp]=="-"):
                            uitwq=int(uitwq)-835
                            salamak_m+=chr(uitwq)
                            uitwq=""
                        else:
                            uitwq+=salamak[joooooapp]
                    counter=0
                    taghalob="1"
                    now=datetime.now()
                    time_start="%s:%s:%s"%(now.hour,now.minute,now.second)
                    try:
                        name_answers=root.filename+"S"
                        file=open(name_answers,"r")
                        read_db_answers=file.read()
                        file.close()
                        if("Codoffee Quiz Maker" in read_db_answers)or("Codoffee Quiz Maker's Result:" in read_db_answers):
                            taghalob="0"
                            m.clear()
                            m.pu()
                            m.goto(0,20)
                            m.pd()
                            m.pencolor("darkorange")
                            m.write(".متاسفيم، شما نمي توانيد دوباره پاسخ دهيد",align="center",font=("B Nazanin",15,("bold")))
                        file=open(name_answers)
                        file.write("")
                        file.close()
                    except:
                        file=open(name_answers,"w")
                        file.write("Codoffee Quiz Maker's Result:\n\n")
                        file.close()
                    billur=0
                    if(taghalob=="1"):
                        m.clear()
                        m.pu()
                        m.goto(0,20)
                        m.pd()
                        m.pencolor("brown")
                        m.write("...آزمون در حال شروع شدن است",align="center",font=("B Nazanin",15,("bold")))
                        time.sleep(1.5)
                        jo=""
                        domboli=""
                        h=""
                        nahai=":نتايج آزمون ساز کدفي\n\n"
                        nahai_m=""
                        for k in range(0,len(exam)):
                            if(exam[k]=="-"):
                                jo=int(jo)-835
                                h+=chr(jo)
                                domboli=chr(jo)
                                jo=""
                            else:
                                jo+=exam[k]
                            joi=""
                            hi=""
                            if(domboli=="?")or(domboli=="؟"):
                                try:
                                    for jhk in range(k+1,len(exam)):
                                        if(exam[jhk]=="-"):
                                            joi=int(joi)-835
                                            hi+=chr(joi)
                                            if(".gif" in hi)or(".GIF" in hi)or(".png" in hi)or(".PNG" in hi)or(".jpg" in hi)or(".JPG" in hi)or(".jpeg" in hi)or(".JPEG" in hi):
                                                break
                                            joi=""
                                        else:
                                            joi+=exam[jhk]
                                    ftp=ftplib.FTP("ftpupload.net")
                                    ftp.login("cldff_22998458","arizamir")
                                    file=open("db10.db")
                                    datacl=file.read()
                                    file.close()
                                    ftp.cwd('htdocs/'+datacl+"/QM")
                                    file=open(hi,"wb")
                                    ftp.retrbinary('RETR %s' % hi, file.write)
                                    file.close()
                                    fig = plt.figure(0)
                                    fig.canvas.set_window_title('آزمون ساز کدفي | عکس سوال')
                                    img=mpimg.imread(hi)
                                    imgplot = plt.imshow(img)
                                    fig.show()
                                    time.sleep(0.5)
                                    os.remove(hi)
                                except:
                                    pass
                                counter+=1
                                m.clear()
                                m.pu()
                                m.goto(0,-10)
                                m.pd()
                                m.pencolor("black")
                                m.write(h,align="center",font=("B Nazanin",12,("bold")))
                                h=""
                                student_answers_this=t.textinput(root.filename,"                       :لطفا سوال را پاسخ دهيد")
                                try:
                                    plt.close(fig)
                                except:
                                    pass
                                nahai+=str(counter)+"-"+student_answers_this+"\n"
                                domboli=""
                            if(".gif" in h)or(".GIF" in h)or(".png" in h)or(".PNG" in h)or(".jpg" in h)or(".JPG" in h)or(".jpeg" in h)or(".JPEG" in h):
                                h=""
                            elif(domboli=="!"):
                                if(h[:(len(h)-1)].lower()==student_answers_this.lower())or(h[:(len(h)-2)].lower()==student_answers_this.lower()):
                                    billur+=1
                                    nahai+=str(counter)+"-"+"پاسخ صحيح است!\n"
                                    nahai_m+=str(counter)+"-"+"Answer is right!\n"
                                else:
                                    nahai+=str(counter)+"-"+"پاسخ غلط است!\n"
                                    nahai_m+=str(counter)+"-"+"Answer is wrong!\n"
                                h=""
                                domboli=""
                        now=datetime.now()
                        file=open(name_answers,"r")
                        now_answers=file.read()
                        file.close()
                        time_tamam="%s:%s:%s"%(now.hour,now.minute,now.second)
                        score_of_u="\nنمره: "+str(billur)+" از "+str(counter)
                        nahai+="\nزمان شروع: "+time_start+"\nزمان پايان: "+time_tamam+score_of_u+"\n\nآزمون ساز کدفي"
                        score_of_u="\nscore: "+str(counter)+" of "+str(billur)
                        nahai_m+="\nStart time: "+time_start+"\nOver time: "+time_tamam+score_of_u+"\n\nCodoffee Quiz Maker"
                        file=open(name_answers,"w")
                        file.write(nahai_m)
                        file.close()
                        m.clear()
                        m.pu()
                        m.goto(0,20)
                        m.pd()
                        m.pencolor("brown")
                        m.write(".آزمون پايان يافت",align="center",font=("B Nazanin",15,("bold")))
                        try:
                            plt.close(fig)
                        except:
                            pass
                        time.sleep(1.5)
                        file=open("db5.db")
                        n_student=file.read()
                        file.close()
                        file=open("db7.db")
                        t_student=file.read()
                        file.close()
                        file=open("db8.db")
                        c_student=file.read()
                        file.close()
                        ID_show=n_student+", "+c_student
                        no_address_file_name=""
                        for kt in range(0,len(root.filename)):
                            no_address_file_name+=root.filename[kt]
                            if(root.filename[kt]=="/"):
                                no_address_file_name=""
                        ID_show+=" - "+no_address_file_name+" "
                        ID_show+="\n\n"+nahai
                        ID_show_m=""
                        for joooappuhht in range(0,len(ID_show)):
                            ID_show_m+=str(ord(ID_show[joooappuhht])+984)+"-"
                        file=open("db4.db","w")
                        file.write(salamak_m+"\n"+ID_show_m)
                        file.close()
                        m.clear()
                        m.pu()
                        m.goto(0,20)
                        m.pd()
                        m.pencolor("brown")
                        m.write("...ارسال نتيجه",align="center",font=("B Nazanin",15,("bold")))
                        time.sleep(2)
                        import email.mime.text
                        import smtplib
                        while True:
                            try:        
                                def send_email (admin, pwd, user, message):
                                    server = smtplib.SMTP('smtp.gmail.com', 587)
                                    server.ehlo()
                                    server.starttls()
                                    server.login(admin, pwd)
                                    server.sendmail(admin, user, message)
                                    server.close()
                                msg = email.mime.text.MIMEText(ID_show, _charset="UTF-8")
                                send_email('codoffee@gmail.com', 'codoffeemenallah', salamak_m, msg.as_string())
                                file=open("db4.db","w")
                                file.write("1")
                                file.close()
                                m.clear()
                                m.pu()
                                m.goto(0,20)
                                m.pd()
                                m.pencolor("brown")
                                m.write(".ارسال پايان يافت",align="center",font=("B Nazanin",15,("bold")))
                                break
                            except:
                                m.clear()
                                m.pu()
                                m.goto(0,20)
                                m.pd()
                                m.pencolor("darkorange")
                                m.write(".متاسفيم، ارتباطات درون شبکه موجود نمي باشد\n.لطفا ارتباطات را بررسي کنيد",align="center",font=("B Nazanin",15,("bold")))
                                time.sleep(3)
                except:
                    m.clear()
                    m.pu()
                    m.goto(0,20)
                    m.pd()
                    m.pencolor("darkorange")
                    m.write(".متاسفيم، آزمون کار نمي کند",align="center",font=("B Nazanin",15,("bold")))  
            def buton2(x,y):
                os.startfile("color.pdf")
                m.clear()
                m.pu()
                m.goto(0,0)
                m.pd()
                m.pencolor("darkblue")
                m.write("شخصي سازي",align="center",font=("B Titr",35))
                time.sleep(4)
                m.clear()
                m.pu()
                m.goto(0,20)
                m.pd()
                m.pencolor("darkblue")
                m.write(".لطفا رنگ پس زمينه را وارد کنيد",align="center",font=("B Nazanin",15,("bold")))
                bg_color_u=t.textinput("شخصي سازي","                :رنگ پس زمينه، الزاما انگليسي").lower()
                m.clear()
                m.write(".لطفا رنگ مداد را انتخاب کنيد",align="center",font=("B Nazanin",15,("bold")))
                p_color_u=t.textinput("شخصي سازي","                   :رنگ مداد، الزاما انگليسي").lower()
                m.clear()
                m.write(".لطفا رنگ دکمه را انتخاب کنيد",align="center",font=("B Nazanin",15,("bold")))
                b_color_u=t.textinput("شخصي سازي","                   :رنگ دکمه، الزاما انگليسي").lower()
                colors=["blue","green","yellow","red","black","white","gray","orange","pink","purple"]
                if(bg_color_u in colors)and(p_color_u in colors)and(b_color_u in colors):
                    file=open("db1.db","w")
                    file.write(bg_color_u)
                    file.close()
                    file=open("db2.db","w")
                    file.write(p_color_u)
                    file.close()
                    file=open("db3.db","w")
                    file.write(b_color_u)
                    file.close()
                else:
                    m.clear()
                    m.pu()
                    m.goto(0,20)
                    m.pd()
                    m.pencolor("darkorange")
                    m.write(".متاسفيم، رنگ هاي وارد شده مشخص شده نيستند",align="center",font=("B Nazanin",15,("bold")))
            def buton3(x,y):
                m.clear()
                m.pu()
                m.goto(0,20)
                m.pd()
                m.pencolor("darkblue")
                m.write(".براي ديدن نتيجه، لطفا آزمون مورد نظر را انتخاب کنيد",align="center",font=("B Nazanin",15,("bold")))
                root = Tk()
                root.withdraw()
                root.filename=filedialog.askopenfilename(initialdir = "/",title = ".براي ديدن نتيجه، آزمون را انتخاب کنيد",filetypes = (("Quiz Maker Exam file","*.QME"),("all files","*.*")))+"S"
                try:
                    file=open(root.filename,"r")
                    while True:
                        rootina=file.readline()
                        if(rootina==""):
                            break
                        m.clear()
                        m.pu()
                        m.goto(0,10)
                        m.pd()
                        m.pencolor("brown")
                        if("Answer is right!"in rootina):
                            rootina=".پاسخ سوال "+rootina[0]+" صحيح است"
                            m.write(rootina,align="center",font=("B Titr",16))
                        if("Answer is wrong!"in rootina):
                            rootina=".پاسخ سوال "+rootina[0]+" غلط است"
                            m.write(rootina,align="center",font=("B Titr",16))
                        if(rootina.lower()=="codoffee quiz maker"):
                            m.pencolor("darkgray")
                            m.write("آزمون ساز کدفي",align="center",font=("B Titr",16,("bold")))
                        if("Start time:"in rootina)or("Over time:"in rootina)or("Score:"in rootina):
                            m.pencolor("green")
                            m.write(rootina,align="center",font=("B Nazanin",16))
                        time.sleep(1)
                    file.close()
                except:
                    m.clear()
                    m.pu()
                    m.goto(0,20)
                    m.pd()
                    m.pencolor("darkorange")
                    m.write(".متاسفيم، نتايج موجود نمي باشند",align="center",font=("B Nazanin",15,("bold"))) 
            def buton4(x,y):
                m.clear()
                m.pu()
                m.goto(0,85)
                m.pd()
                m.pencolor("brown")
                m.write("،راهنما",align="center",font=("B Nazanin",15,("bold")))
                m.pu()
                m.goto(0,-47)
                m.pd()
                m.pencolor("black")
                m.write(".براي آزمون دادن بروي {شروع} کليک کنيد\n.ما نتايج آزمون هاي شما را براي معلمتان ارسال ميکنيم\n.شما مي توانيد با {نتايج}، نتايج آزمون هاي خود را ببينيد\n.براي نمايش اطلاعات بروي {اطلاعات} کليک کنيد\n.شما مي توانيد با استفاده از {شخصي سازي} نرم افزار خود را شخصي سازي کنيد",align="center",font=("B Nazanin",13,("bold")))
                m.pu()
                m.goto(0,-75)
                m.pd()
                m.pencolor("darkblue")
                m.write(".کليد {ي} را فشار دهيد تا جزييات بيشتري ببينيد",align="center",font=("B Nazanin",13,("bold")))
            def buton5(x,y):
                m.clear()
                m.pu()
                m.goto(0,110)
                m.pd()
                m.pencolor("brown")
                m.write("،اطلاعات",align="center",font=("B Nazanin",15,("bold")))
                m.pu()
                m.goto(0,55)
                m.pd()
                m.pencolor("black")
                m.write("آزمون ساز کدفي 1.4\n© 2018 تمامي حقوق محفوظ است. | کدفي",align="center",font=("B Nazanin",15))
                m.pu()
                m.goto(0,-60)
                m.pd()
                m.pencolor("darkblue")
                m.write("مدير اجرايي : آريا ايزانلو\nمدير گروه : اميرحسين صفرزاده\nرابط کاربري - طراحي شده توسط لوگوفي\nصداپردازي - حمايت شده توسط کدفي",align="center",font=("B Nazanin",15))
                m.pu()
                m.goto(0,-85)
                m.pd()
                m.pencolor("brown")
                m.write(".کليد {فاصله} را فشار دهيد تا از حساب خارج شويد",align="center",font=("B Nazanin",13,("bold")))
            def buton6(x,y):
                m.clear()
                m.pu()
                m.goto(0,35)
                m.pd()
                m.pencolor("brown")
                m.write("،اطلاعات هويت",align="center",font=("B Nazanin",15,("bold")))
                file=open("db5.db")
                name="حساب دانش آموز | "+file.read()
                file.close()
                m.pu()
                m.goto(0,10)
                m.pd()
                m.pencolor("darkblue")
                m.write(name,align="center",font=("B Nazanin",13,("bold")))
                try:
                    file=open("db10.db")
                    cloudtf=file.read()
                    file.close()
                    cloudtf=cloudtf+" :فضاي ابري | متصل به آيدي"
                except:
                    cloudtf=".فضاي ابري | متصل نيست"
                m.pu()
                m.goto(0,-18)
                m.pd()
                m.pencolor("black")
                m.write(cloudtf,align="center",font=("B Nazanin",13,("bold")))
                m.pu()
                m.goto(0,-50)
                m.pd()
                file=open("db5.db")
                n_student=file.read()
                file.close()
                file=open("db7.db")
                t_student=file.read()
                file.close()
                file=open("db8.db")
                c_student=file.read()
                file.close()
                ID_show=c_student+" :کلاس | "+t_student+" دانش آموز ،"+n_student
                m.pencolor("black")
                m.write(ID_show,align="center",font=("B Nazanin",13))
            def buton7(x,y):
                m.clear()
                m.pu()
                m.goto(0,20)
                m.pd()
                m.pencolor("brown")
                m.write("...در حال اتصال به فضاي ابري",align="center",font=("B Nazanin",15,("bold")))
                time.sleep(3)
                try:
                    file=open("db10.db","r")
                    datacl=file.read()
                    file.close()
                    ftp=ftplib.FTP("ftpupload.net")
                    m.clear()
                    m.pu()
                    m.goto(0,20)
                    m.pd()
                    m.pencolor("black")
                    m.write(datacl+" :فضاي ابري در حال حاضر متصل است به آيدي",align="center",font=("B Nazanin",15,("bold")))
                    m.pu()
                    m.goto(0,-5)
                    m.pd()
                    m.pencolor("brown")
                    m.write("...در حال نمايش فايل ها",align="center",font=("B Nazanin",15,("bold")))
                    ftp=ftplib.FTP("ftpupload.net")
                    ftp.login("cldff_22998458","arizamir")
                    prorpu=t.textinput('فايل ها','                          :نوع نمايش(عمومي/خصوصي)')
                    if(prorpu=="عمومي"):
                        ftp.cwd('htdocs/'+datacl+'/QM')
                        sabzaloo=ftp.nlst()
                        j=""
                        for i in range(1,len(sabzaloo)):
                            if(".QME" in sabzaloo[i]):
                                j+=sabzaloo[i]+'\n'
                        zardaloo=t.textinput("فايل ها",j)
                    else:
                        passu_req=t.textinput("فايل ها","                           :رمز فضاي ابري")
                        try:
                            ftp.cwd('htdocs/'+datacl+'/'+passu_req+'/QM')
                        except:
                            m.clear()
                            m.pu()
                            m.goto(0,20)
                            m.pd()
                            m.pencolor("darkorange")
                            m.write(".متاسفيم، رمز اشتباه است",align="center",font=("B Nazanin",15,("bold")))
                            time.sleep(1.5)
                            exit()
                        sabzaloo=ftp.nlst()
                        j=""
                        for i in range(1,len(sabzaloo)):
                            if(".QME" in sabzaloo[i]):
                                j+=sabzaloo[i]+'\n'
                        zardaloo=t.textinput("فايل ها",j)
                    m.clear()
                    m.pu()
                    m.goto(0,20)
                    m.pd()
                    m.pencolor("darkblue")
                    m.write(".لطفا نشاني دريافت فايل را انتخاب کنيد",align="center",font=("B Nazanin",15,("bold")))
                    name_exam_w= Tk()
                    name_exam_w.withdraw()
                    name_exam_w.filename=filedialog.asksaveasfilename(initialdir = "/",title = ".نشاني دريافت فايل را انتخاب کنيد",filetypes = (("Quiz Maker Exam file","*.QME"),("all files","*.*")))
                    try:
                        if(".QME"not in zardaloo):
                            zardaloo+=".QME"
                        dll=name_exam_w.filename+".QME"
                        file=open(dll,"wb")
                        ftp.retrbinary('RETR %s' % zardaloo, file.write)
                        file.close()
                        m.clear()
                        m.pu()
                        m.goto(0,20)
                        m.pd()
                        m.pencolor("brown")
                        m.write(".فايل با موفقيت دريافت شد",align="center",font=("B Nazanin",13,("bold")))
                    except:
                        m.clear()
                        m.pu()
                        m.goto(0,20)
                        m.pd()
                        m.pencolor("darkorange")
                        m.write(".متاسفيم، مشکلي در دريافت فايل رخ داده است",align="center",font=("B Nazanin",15,("bold")))
                except:
                    m.clear()
                    m.pu()
                    m.goto(0,20)
                    m.pd()
                    m.pencolor("darkorange")
                    m.write(".متاسفيم، ارتباطات درون شبکه موجود نمي باشد\n.لطفا ارتباطات را بررسي کنيد",align="center",font=("B Nazanin",15,("bold")))          
            def key1():
                file=open("db4.db","w")
                file.write("0")
                file.close()
                m.clear()
                m.pu()
                m.goto(0,0)
                m.pd()
                m.pencolor("darkgray")
                m.write(".خروج از حساب با موفقيت انجام شد\n.لطفا نرم افزار را دوباره اجرا کنيد",align="center",font=("B Nazanin",15,("bold")))
            def key2():
                os.startfile("Docs.pdf")
            m.clear()
            m.pu()
            m.goto(0,0)
            m.pd()
            m.pencolor("darkgray")
            m.write("آزمون ساز کدفي\nحساب دانش آموز",align="center",font=("B Titr",15))
            button1.onclick(buton1)
            button2.onclick(buton2)
            button3.onclick(buton3)
            button4.onclick(buton4)
            button5.onclick(buton5)
            button6.onclick(buton6)
            try:
                button7.onclick(buton7)
            except:
                pass
            scr.onkey(key1,"space")
            scr.onkey(key2,"d")
            scr.listen()
            def bgback():
                while True:
                    t.bgcolor("#737373")
                    time.sleep(1)
                    t.bgcolor("#666666")
                    time.sleep(1)
                    t.bgcolor("#595959")
                    time.sleep(1)
                    t.bgcolor("#666666")
                    time.sleep(1)
                    t.bgcolor("#737373")
                    time.sleep(1)
                    t.bgcolor("#808080")
            def date_time():
                dt=t.Turtle()
                dt.speed(0)
                jdatetime.set_locale('fa_IR')
                while True:
                    dt.ht()
                    now=datetime.now()
                    now_date=jdatetime.datetime.now().strftime("%d/%m/%Y")
                    now_time=jdatetime.datetime.now().strftime("%H:%M")
                    dt.clear()
                    dt.pu()
                    dt.goto(270,218)
                    dt.pd()
                    try:
                        dt.pencolor("light"+p_color)
                    except:
                        dt.pencolor(p_color)
                    dt.write(now_time,align="center",font=("B Titr",15))
                    dt.pu()
                    dt.goto(-250,218)
                    dt.pd()
                    dt.write(now_date,align="center",font=("B Titr",15))
                    time.sleep(59.9)
            thread1=Thread(target=date_time,args=[])
            thread1.start()
            thread2=Thread(target=bgback,args=[])
            thread2.start()
            t.mainloop()
except:
    scr.reset()
    try:
        button1.ht()
        button2.ht()
        button3.ht()
        button4.ht()
        button5.ht()
        button6.ht()
    except:
        pass
    try:
        button7.ht()
    except:
        pass
    try:
        button8.ht()
    except:
        pass
    m.ht()
    t.ht()
    dcw.ht()
    t.bgcolor("gray")
    t.clear()
    t.pencolor("brown")
    t.pu()
    t.goto(0,0)
    t.pd()
    t.write("Error",align="center",font=("Arial",25,("bold")))
    time.sleep(2)
    t.clear()
    t.pencolor("pink")
    t.pu()
    t.goto(0,0)
    t.pd()
    t.write("خطا",align="center",font=("B Titr",25,("bold")))
    playsound.playsound("14.mp3")
#End, Total codes: 3950 line:----------------------------------------------------Codoffee Quiz Maker V1.6--------------------------------------------------------------
#Thanks from:
    #Mr.Izanlou-CodoffeeManager
    #Mr.Safarzadeh-CodoffeeManager
    #Logoffee-Startup==ForDesigningGUI
    #Proudly-PoweredBy-PythonTkinter-C++/C-PL
