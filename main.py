from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Dynamic Face Detection")
root.geometry("800x400")
root.resizable(False,False)
root.configure(background='#EEEEE8')

img1 = PhotoImage(file="B1.png")
img2 = PhotoImage(file="B2.png")


L1 = Label(root,text="FACE IMAGE", font="Ubuntu 18")
L1.place(x=225,y=45)

I1 = Entry(root,width=80,borderwidth=15,background="#EEEEC5")
I1.place(x=50,y=80)
L2 = Label(root,text="VIDEO", font="Ubuntu 18")
L2.place(x=250,y=135)

I2 = Entry(root,width=80,borderwidth=15,background="#EEEEC5")
I2.place(x=50,y=170)

B1 = Button(root,image=img1,borderwidth=0)
B1.place(x=70,y=280)

B2 = Button(root,image=img2,borderwidth=0)
B2.place(x=380,y=280)

L3 = Label(root,text="HSA Soft Limited",font="Sansation 10",fg="grey")
L3.place(x=600,y=375)
def openpng():
    pngName = filedialog.askopenfilename(initialdir="/",title="Select The Image",filetypes=(("jpeg","*.jpeg"),("jpg","*jpg"),("png","*png")))
    
def openmkv():
    vidName = filedialog.askopenfilename(initialdir="/",title="Select The Video",filetypes=(("mkv","*.mkv"),("mp4","*.mp4")))
    
B3 = Button(root,text="TARGET IMAGE",width=9,padx=20,pady=10,command= lambda:openpng(),bg="Green",font="Bold")
B3.place(x=590,y=80)

B4 = Button(root,text="THE VIDEO",width=9,padx=20,pady=10,command= lambda:openmkv(),bg="Green",font="Bold")
B4.place(x=590,y=160)




root.mainloop()