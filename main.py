from tkinter import *
from tkinter import filedialog
import threading
import webbrowser
import engine

root = Tk()
root.title("Dynamic Face Detection")
root.geometry("720x400")
root.resizable(False,False)
root.configure(background='#EEEEE8')

img1 = PhotoImage(file="IconImg/B1.png")
img2 = PhotoImage(file="IconImg/B2.png")
img3 = PhotoImage(file="IconImg/B3.png")
img4 = PhotoImage(file="IconImg/B4.png")
img5 = PhotoImage(file="IconImg/clogo.png")
img6 = PhotoImage(file="IconImg/B3_.png")
img7 = PhotoImage(file="IconImg/B4_.png")
img8 = PhotoImage(file="IconImg/B1_.png")
img9 = PhotoImage(file="IconImg/B2_.png")
img10 = PhotoImage(file="IconImg/head.png")
img11 = PhotoImage(file="IconImg/B5.png")
img12 = PhotoImage(file="IconImg/B5_.png")

Olink = "https://stackoverflow.com/"

L1 = Label(root,text="FACE IMAGE", font="Ubuntu 15")
L1.place(x=235,y=45)

I1 = Entry(root,width=80,borderwidth=2,background="#EEEEC5")
I1.place(x=50,y=80)
L2 = Label(root,text="VIDEO", font="Ubuntu 15",padx=2)
L2.place(x=260,y=135)

I2 = Entry(root,width=80,borderwidth=2,background="#EEEEC5")
I2.place(x=50,y=170)

#Backend Fucntion
def backend():
    engine.Frames(I2.get(),I1.get())

#Start Button Function
def start():
    P1 = threading.Thread(target=backend())
    P1.setDaemon=True
    P1.start()
    P1.join()

B1 = Button(root,image=img1,borderwidth=0,command=start)
B1.place(x=110,y=260)
def Enter3(e):
    B1.place(x=109,y=259)

    B1.config(image=img8)
def Leave3(e):
    B1.place(x=110,y=260)
    B1.config(image=img1)

B1.bind("<Enter>",Enter3)
B1.bind("<Leave>",Leave3)

B2 = Button(root,image=img2,borderwidth=0)
B2.place(x=380,y=260)
def Enter4(e):
    B2.place(x=379,y=259)

    B2.config(image=img9)
def Leave4(e):
    B2.place(x=380,y=260)
    B2.config(image=img2)

B2.bind("<Enter>",Enter4)
B2.bind("<Leave>",Leave4)

L3 = Label(root,text="HSA Soft Limited",font="Sansation 10",fg="grey")
L3.place(x=600,y=375)
L4 = Label(root,image=img5,bg="#EEEEE8")
L4.place(x=620,y=300)
def openpng():
    global pngName
    pngName = filedialog.askopenfilename(initialdir="/Desktop",title="Select The Image",filetypes=(("jpg","*.jpg"),("jpeg","*.jpeg"),("png","*.png")))
    print(pngName)
    I1.delete(0,END)
    I1.insert(0,pngName)

vidName = ""    
def openmkv():
    global vidName
    vidName = filedialog.askopenfilename(initialdir="/Desktop",title="Select The Video",filetypes=(("mp4","*.mp4"),("mkv","*.mkv")))
    print(vidName)
    I2.delete(0,END)
    I2.insert(0,vidName)

B3 = Button(root,image=img3,borderwidth=0,command= lambda:openpng())
B3.place(x=540,y=75)
def Enter1(e):
    B3.place(x=539,y=73.5)

    B3.config(image=img6)
def Leave1(e):
    B3.place(x=540,y=75)
    B3.config(image=img3)

B3.bind("<Enter>",Enter1)
B3.bind("<Leave>",Leave1)

B4 = Button(root,image=img4,borderwidth=0,command= lambda:openmkv())
B4.place(x=540,y=165)

def Enter2(e):
    B4.place(x=539,y=163.5)
    B4.config(image=img7)

def Leave2(e):
    B4.place(x=540,y=165)
    B4.config(image=img4)

B4.bind("<Enter>",Enter2)
B4.bind("<Leave>",Leave2)

L5 = Label(root,image=img10)
L5.place(x=15,y=378)

def link():
    webbrowser.open_new(Olink)
B5 = Button(root,image=img11,borderwidth=0,command=link)
B5.place(x=630,y=8)

def Enter5(e):

    B5.config(image=img12)

def Leave5(e):
    B5.config(image=img11)

B5.bind("<Enter>",Enter5)
B5.bind("<Leave>",Leave5)


root.mainloop()