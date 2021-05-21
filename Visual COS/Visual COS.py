import os
import playsound
import time
import datetime
import turtle as t
from turtle import Turtle, mainloop
from threading import Thread
from datetime import datetime
t.setup(1366,768)
t.title("Visual - CodoffeeOS :: Codoffee Quiz Maker V1.6 :: Best Projects Celebration")
t.bgcolor("lightyellow")
t.speed(0)
t.ht()
def date_time():
    dt=t.Turtle()
    dt.speed(0)
    dt.ht()
    while True:
        now=datetime.now()
        now_time="%s:%s:%s"%(now.hour,now.minute,now.second)
        now_date="%s/%s/%s"%(now.month,now.day,now.year)
        dt.clear()
        dt.pu()
        dt.goto(600,300)
        dt.pd()
        try:
            dt.pencolor("black")
        except:
            dt.pencolor("black")
        dt.write(now_time,align="center",font=("Agency FB",20,("bold")))
        dt.pu()
        dt.goto(-600,300)
        dt.pd()
        dt.pencolor("darkblue")
        dt.write(now_date,align="center",font=("Agency FB",20,("bold")))
        time.sleep(0.9)
thread1=Thread(target=date_time,args=[])
thread1.start()
t.pu()
t.goto(0,200)
t.pd()
t.pencolor("brown")
t.write("Codoffee Quiz Maker",align="center",font=("Impact",60))
t.pu()
t.goto(0,100)
t.pd()
t.pencolor("darkblue")
t.write("آزمون ساز ايمن کدفي",align="center",font=("B Titr",35,("bold")))
t.pu()
t.goto(0,40)
t.pd()
t.pencolor("black")
t.write("نمايشگاه آثار برتر پژوهشي - سال تحصيلي 96-97",align="center",font=("B Nazanin",30,("bold")))
t.pu()
t.goto(0,-35)
t.pd()
t.pencolor("darkorange")
t.write("اعضاي گروه : آريا ايزانلو(مدير گروه) ، اميرحسين صفرزاده(مدير برنامه نويسان)",align="center",font=("B Nazanin",25,("bold")))
#button1:
button1=Turtle("triangle")
button1.speed(0)
button1.pu()
button1.goto(0,-150)
button1.pd()
button1.shapesize(4)
button1.fillcolor("blue")
t.pu()
t.goto(0,-235)
t.pd()
t.pencolor("blue")
t.write("شروع نرم افزار",align="center",font=("B Nazanin",20,("bold")))
#button2:
button2=Turtle("square")
button2.speed(0)
button2.pu()
button2.goto(300,-150)
button2.pd()
button2.shapesize(3)
button2.fillcolor("green")
t.pu()
t.goto(300,-235)
t.pd()
t.pencolor("green")
t.write("تازه سازي",align="center",font=("B Nazanin",20,("bold")))
#button3:
button3=Turtle("circle")
button3.speed(0)
button3.pu()
button3.goto(-300,-150)
button3.pd()
button3.shapesize(3)
button3.fillcolor("red")
t.pu()
t.goto(-300,-235)
t.pd()
t.pencolor("red")
t.write("راهنما",align="center",font=("B Nazanin",20,("bold")))
#onclicks:
def buton1(x,y):
    try:
        os.remove("C://Users//Arizlo Atom//Desktop//آزمون.QMES")
    except:
        pass
    os.startfile("Quiz Maker.py")
def buton2(x,y):
    file=open("db4.db","w")
    file.write("0")
    file.close()
    try:
        os.remove("db10.db")
    except:
        pass
    try:
        os.remove("C://Users//Arizlo Atom//Desktop//آزمون.QMES")
    except:
        pass
def buton3(x,y):
    os.startfile("Docs.pdf")
button1.onclick(buton1)
button2.onclick(buton2)
button3.onclick(buton3)
t.mainloop()
#End - Visual Codoffee OS ----------------------------------------------
