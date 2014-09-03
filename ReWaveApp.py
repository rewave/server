from time import *
from threading import Thread
from Tkinter import *

global New_Signal
New_Signal=0
global Bluetooth_Connection
Bluetooth_Connection=True

def ConnectBluetooth():
    #Code For Connecting To Bluetooth
    global Bluetooth_Connection
    Bluetooth_Connection=True
def DisconnectBluetooth():
    #Code For Disconnecting
    global Bluetooth_Connection
    Bluetooth_Connection=not Bluetooth_Connection
    
def Label1():
    Lab1=Label(Main,text="Disconnected!!!",fg="black",font=('Calibri',12,'bold'),bg="deep sky blue")
    Lab1.place(x=5,y=35,width=250)
    while True:
        if Bluetooth_Connection==True and New_Signal==0:
            Lab1.config(text="Connected")
        elif Bluetooth_Connection==True and New_Signal!=0:
            Lab1.config(text="Listening")
        elif Bluetooth_Connection==False:
            Lab1.config(text="Disconnected")
    sleep(2000)


def Button1():
    while True:
        global Bluetooth_Connection
        global B1
        if Bluetooth_Connection==True:
            B1.config(text='Disconnect',command=DisconnectBluetooth)
        elif Bluetooth_Connection==False:
            B1.config(text='Connect',command=ConnectBluetooth)
            
        
def Func():
    while True:
        if Current_Signal != New_Signal:
	    #Read The Input Signal
            if New_Signal==Right:
		#What To Do In Case Right
            elif New_Signal==Left:
                #Left
            Current_Signal=New_Signal


def GettingStarted():
    pass
def Help():
    pass
def Feedback():
    pass

Main=Tk()
Main.title("ReWave App")
Main.geometry(newGeometry='400x150')
Main.resizable(0,0)
Main.overrideredirect(1)
fr=Frame(Main,bg='white',height=150,width=400)
fr.pack()
C1=Canvas(Main,bg="snow",height=30,width=400)
C1.place(x=0,y=0)
circle1=C1.create_oval(10,10,20,20,fill='red',width=0)
circle2=C1.create_oval(25,10,35,20,fill='blue',width=0)
Lab2=Label(Main,text="ReWave App",fg="red",font=('Calibri',12,'bold'),bg="deep sky blue")
Lab2.place(x=150,y=5)
C2=Canvas(Main,bg="deep sky blue", height=30, width=250)
C2.place(x=0,y=30)
Thread(target=Label1).start()
C3=Canvas(Main,bg="coral",height=30,width=150)
C3.place(x=250,y=30)
B1=Button(text='Connect',command=ConnectBluetooth,fg="black",font=("Calibri",12,'bold'),bg="coral",border=0,activebackground='red')
B1.place(x=250,y=31,width=150)
Thread(target=Button1).start()
C4=Canvas(Main,bg="lavender",height=60,width=400)
C4.place(x=0,y=60)
#Im1=Label(Main,ImageTk,PhotoImage(Image.open('pic.gif')))
C5=Canvas(Main,bg='snow',height=30,width=400)
C5.place(x=0,y=120)
B2=Button(text="Getting Started",wraplength=50,command=GettingStarted, bd=0, bg="snow",fg="deep sky blue",activebackground="snow",font=('Calibri',8),justify='center')
B2.place(x=10,y=120)
B3=Button(text="Help",wraplength=50,command=Help, bd=0, bg="snow",fg="deep sky blue",activebackground="snow",font=('Calibri',8),justify='center')
B3.place(x=280,y=125,height=20,width=40)
B4=Button(text="Feedback",wraplength=50,command=Feedback, bd=0, bg="snow",fg="deep sky blue",activebackground="snow",font=('Calibri',8),justify='center')
B4.place(x=330,y=125,height=20,width=50)

Main.mainloop()
