from os import times
import tkinter
from tkinter import Pack, font
from tkinter.constants import BOTTOM, CENTER, LEFT, RIGHT, TOP
import take_picture as tk_pic
import time
import cv2
from PIL import Image, ImageTk
from face_recognition.api import face_distance
import numpy as np
import face_recognition



acc_name_text=""
alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']




def Creat_acc():
    
    welcome.destroy() 
    global Entry
    global acc_name_text
    acc_name_text=""
    Entry=tkinter.Tk()
    Entry.title("Inabayama")
    Entry.attributes('-fullscreen',True)  #makes the window fullscreen
    tkinter.Button(text="Cancel",command=return_welcome).place(x=1400, y=750)
    tkinter.Label(Entry,text="Enter your name",font="Times 16 bold",height=13).pack(side=TOP)
    
    global name
    name = tkinter.Label(Entry,text=f"{acc_name_text}",font="Times 16 bold",height=13)
    name.place(x=700,y=200)
    
    i=0
    tkinter.Button(Entry,text=f'{alp[i]}',font="Times 16 bold",command=add_a).place(x=200+40*i,y=500)
    i+=1
    tkinter.Button(Entry,text=f'{alp[i]}',font="Times 16 bold",command=add_b).place(x=200+40*i,y=500)
    i+=1
    tkinter.Button(Entry,text=f'{alp[i]}',font="Times 16 bold",command=add_c).place(x=200+40*i,y=500)
    i+=1
    tkinter.Button(Entry,text=f'{alp[i]}',font="Times 16 bold",command=add_d).place(x=200+40*i,y=500)
    i+=1
    tkinter.Button(Entry,text=f'{alp[i]}',font="Times 16 bold",command=add_e).place(x=200+40*i,y=500)
    i+=1
    tkinter.Button(Entry,text=f'{alp[i]}',font="Times 16 bold",command=add_f).place(x=200+40*i,y=500)
    i+=1
    tkinter.Button(Entry,text=f'{alp[i]}',font="Times 16 bold",command=add_g).place(x=200+40*i,y=500)
    i+=1
    tkinter.Button(Entry,text=f'{alp[i]}',font="Times 16 bold",command=add_h).place(x=200+40*i,y=500)
    i+=1
    tkinter.Button(Entry,text=f'{alp[i]}',font="Times 16 bold",command=add_i).place(x=200+40*i,y=500)
    i+=1
    tkinter.Button(Entry,text=f'{alp[i]}',font="Times 16 bold",command=add_j).place(x=200+40*i,y=500)
    i+=1
    tkinter.Button(Entry,text=f'{alp[i]}',font="Times 16 bold",command=add_k).place(x=200+40*i,y=500)
    i+=1
    tkinter.Button(Entry,text=f'{alp[i]}',font="Times 16 bold",command=add_l).place(x=200+40*i,y=500)
    i+=1
    tkinter.Button(Entry,text=f'{alp[i]}',font="Times 16 bold",command=add_m).place(x=200+40*i,y=500)
    i+=1
    tkinter.Button(Entry,text=f'{alp[i]}',font="Times 16 bold",command=add_n).place(x=200+40*i,y=500)
    i+=1
    tkinter.Button(Entry,text=f'{alp[i]}',font="Times 16 bold",command=add_o).place(x=200+40*i,y=500)
    i+=1
    tkinter.Button(Entry,text=f'{alp[i]}',font="Times 16 bold",command=add_p).place(x=200+40*i,y=500)
    i+=1
    tkinter.Button(Entry,text=f'{alp[i]}',font="Times 16 bold",command=add_q).place(x=200+40*i,y=500)
    i+=1
    tkinter.Button(Entry,text=f'{alp[i]}',font="Times 16 bold",command=add_r).place(x=200+40*i,y=500)
    i+=1
    tkinter.Button(Entry,text=f'{alp[i]}',font="Times 16 bold",command=add_s).place(x=200+40*i,y=500)
    i+=1
    tkinter.Button(Entry,text=f'{alp[i]}',font="Times 16 bold",command=add_t).place(x=200+40*i,y=500)
    i+=1
    tkinter.Button(Entry,text=f'{alp[i]}',font="Times 16 bold",command=add_u).place(x=200+40*i,y=500)
    i+=1
    tkinter.Button(Entry,text=f'{alp[i]}',font="Times 16 bold",command=add_v).place(x=200+40*i,y=500)
    i+=1
    tkinter.Button(Entry,text=f'{alp[i]}',font="Times 16 bold",command=add_w).place(x=200+40*i,y=500)
    i+=1
    tkinter.Button(Entry,text=f'{alp[i]}',font="Times 16 bold",command=add_x).place(x=200+40*i,y=500)
    i+=1
    tkinter.Button(Entry,text=f'{alp[i]}',font="Times 16 bold",command=add_y).place(x=200+40*i,y=500)
    i+=1
    tkinter.Button(Entry,text=f'{alp[i]}',font="Times 16 bold",command=add_z).place(x=200+40*i,y=500)
    i+=1
    tkinter.Button(Entry,text=f'{alp[i]}',font="Times 16 bold",command=add_0).place(x=500+40*(i-24),y=600)
    i+=1
    tkinter.Button(Entry,text=f'{alp[i]}',font="Times 16 bold",command=add_1).place(x=500+40*(i-24),y=600)
    i+=1
    tkinter.Button(Entry,text=f'{alp[i]}',font="Times 16 bold",command=add_2).place(x=500+40*(i-24),y=600)
    i+=1
    tkinter.Button(Entry,text=f'{alp[i]}',font="Times 16 bold",command=add_3).place(x=500+40*(i-24),y=600)
    i+=1
    tkinter.Button(Entry,text=f'{alp[i]}',font="Times 16 bold",command=add_4).place(x=500+40*(i-24),y=600)
    i+=1
    tkinter.Button(Entry,text=f'{alp[i]}',font="Times 16 bold",command=add_5).place(x=500+40*(i-24),y=600)
    i+=1
    tkinter.Button(Entry,text=f'{alp[i]}',font="Times 16 bold",command=add_6).place(x=500+40*(i-24),y=600)
    i+=1
    tkinter.Button(Entry,text=f'{alp[i]}',font="Times 16 bold",command=add_7).place(x=500+40*(i-24),y=600)
    i+=1
    tkinter.Button(Entry,text=f'{alp[i]}',font="Times 16 bold",command=add_8).place(x=500+40*(i-24),y=600)
    i+=1
    tkinter.Button(Entry,text=f'{alp[i]}',font="Times 16 bold",command=add_9).place(x=500+40*(i-24),y=600)
    i+=1
    tkinter.Button(Entry,text=' ',font="Times 16 bold",command=add_space).place(x=200+40*26,y=500)
    i+=1
    tkinter.Button(Entry,text='Delete',font="Times 16 bold",command=add_Delete).place(x=200+40*i,y=500)
    tkinter.Button(Entry,text='Clear',font="Times 20 bold",command=add_clear).place(x=800,y=700)
    tkinter.Button(Entry,text='Enter',font="Times 20 bold",command=add_enter).place(x=600,y=700)
    
    
    
    

    Entry.mainloop()



def Creat_acc_photo():
    global acc_pic
    global label
    global cap
    global acc_name_text
    acc_pic=tkinter.Tk()
    label =tkinter.Label(acc_pic)
    label.pack()
    cap= cv2.VideoCapture(0)
    acc_pic.title("Inabayama")
    acc_pic.attributes('-fullscreen',True)  #makes the window fullscreen
    tkinter.Button(text="Cancel",command=return_welcome2).place(x=1400, y=750)
    tkinter.Label(acc_pic,text=f'{acc_name_text}',font="Times 16 bold",height=13).pack(side=TOP)
    tkinter.Button(text="Camera On",font="Times 16 bold",command=tk_pic.video).place(x=700, y=500)
    tkinter.Button(text="Take picture",font="Times 16 bold",command=tk_pic.take_photo).place(x=700, y=600)
    show_frames()
    
    acc_pic.mainloop()

def show_frames():
   # Get the latest frame and convert into Image
   cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
   img = Image.fromarray(cv2image)
   # Convert image to PhotoImage
   imgtk = ImageTk.PhotoImage(image = img)
   label.imgtk = imgtk
   label.configure(image=imgtk)
   # Repeat after an interval to capture continiously
   label.after(20, show_frames)   
  
def add_a():
    global acc_name_text
    name.config(text=acc_name_text+"a")
    acc_name_text+="a" 

def add_b():
    global acc_name_text
    name.config(text=acc_name_text+"b")
    acc_name_text+="b" 

def add_c():
    global acc_name_text
    name.config(text=acc_name_text+"c")
    acc_name_text+="c" 

def add_d():
    global acc_name_text
    name.config(text=acc_name_text+"d")
    acc_name_text+="d" 

def add_e():
    global acc_name_text
    name.config(text=acc_name_text+"e")
    acc_name_text+="e"

def add_f():
    global acc_name_text
    name.config(text=acc_name_text+"f")
    acc_name_text+="f" 

def add_g():
    global acc_name_text
    name.config(text=acc_name_text+"g")
    acc_name_text+="g" 

def add_h():
    global acc_name_text
    name.config(text=acc_name_text+"h")
    acc_name_text+="h"

def add_i():
    global acc_name_text
    name.config(text=acc_name_text+"i")
    acc_name_text+="i" 

def add_j():
    global acc_name_text
    name.config(text=acc_name_text+"j")
    acc_name_text+="j" 

def add_k():
    global acc_name_text
    name.config(text=acc_name_text+"k")
    acc_name_text+="k" 

def add_l():
    global acc_name_text
    name.config(text=acc_name_text+"l")
    acc_name_text+="l" 

def add_m():
    global acc_name_text
    name.config(text=acc_name_text+"m")
    acc_name_text+="m" 

def add_n():
    global acc_name_text
    name.config(text=acc_name_text+"n")
    acc_name_text+="n" 

def add_o():
    global acc_name_text
    name.config(text=acc_name_text+"o")
    acc_name_text+="o" 

def add_p():
    global acc_name_text
    name.config(text=acc_name_text+"p")
    acc_name_text+="p" 

def add_q():
    global acc_name_text
    name.config(text=acc_name_text+"q")
    acc_name_text+="q" 

def add_r():
    global acc_name_text
    name.config(text=acc_name_text+"r")
    acc_name_text+="r" 

def add_s():
    global acc_name_text
    name.config(text=acc_name_text+"s")
    acc_name_text+="s" 

def add_t():
    global acc_name_text
    name.config(text=acc_name_text+"t")
    acc_name_text+="t" 
def add_u():
    global acc_name_text
    name.config(text=acc_name_text+"u")
    acc_name_text+="u" 

def add_v():
    global acc_name_text
    name.config(text=acc_name_text+"v")
    acc_name_text+="v" 


def add_w():
    global acc_name_text
    name.config(text=acc_name_text+"w")
    acc_name_text+="w" 

def add_x():
    global acc_name_text
    name.config(text=acc_name_text+"x")
    acc_name_text+="x" 

def add_y():
    global acc_name_text
    name.config(text=acc_name_text+"y")
    acc_name_text+="y" 

def add_z():
    global acc_name_text
    name.config(text=acc_name_text+"z")
    acc_name_text+="z" 

def add_0():
    global acc_name_text
    name.config(text=acc_name_text+"0")
    acc_name_text+="0" 

def add_1():
    global acc_name_text
    name.config(text=acc_name_text+"1")
    acc_name_text+="1" 

def add_2():
    global acc_name_text
    name.config(text=acc_name_text+"2")
    acc_name_text+="2" 

def add_3():
    global acc_name_text
    name.config(text=acc_name_text+"3")
    acc_name_text+="3"

def add_4():
    global acc_name_text
    name.config(text=acc_name_text+"4")
    acc_name_text+="4" 

def add_5():
    global acc_name_text
    name.config(text=acc_name_text+"5")
    acc_name_text+="5" 

def add_6():
    global acc_name_text
    name.config(text=acc_name_text+"6")
    acc_name_text+="6" 

def add_7():
    global acc_name_text
    name.config(text=acc_name_text+"7")
    acc_name_text+="7" 

def add_8():
    global acc_name_text
    name.config(text=acc_name_text+"8")
    acc_name_text+="8"

def add_9():
    global acc_name_text
    name.config(text=acc_name_text+"9")
    acc_name_text+="9"  

def add_space():
    global acc_name_text
    name.config(text=acc_name_text+" ")
    acc_name_text+=" " 


def add_Delete():
    global acc_name_text
    name.config(text=acc_name_text[:-1])
    acc_name_text=acc_name_text[:-1]

def add_clear():
    global acc_name_text
    name.config(text="")
    acc_name_text=""

def add_enter():
    
    Entry.destroy()
    Creat_acc_photo()
    
    
    #tk_pic.video()

def return_welcome2():
    acc_pic.destroy()
    Welcome()


def return_welcome():
    Entry.destroy()
    Welcome()





def Use_Cell():
    welcome.destroy()
    global use_cell
    use_cell=tkinter.Tk()
    use_cell.title("Inabayama")
    use_cell.attributes('-fullscreen',True)  #makes the window fullscreen
    tkinter.Button(text="Cancel",command=use_cell.destroy).place(x=1400, y=750)



    use_cell.mainloop()

def Welcome():    
    global welcome                                                              #Welcome window
    welcome = tkinter.Tk() #Welcome window
    welcome.title("Inabayama")
    welcome.attributes('-fullscreen',True)  #makes the window fullscreen
    tkinter.Label(welcome, text = "Welcome to Inabayama",justify=CENTER,font="times 35 bold",fg="grey",height=12).pack() #Welcome Text
    tkinter.Button(text="Creat Account",foreground="grey",font="Times 16 bold",command=Creat_acc).pack(ipadx=10,ipady=10) #Button to go to creat account window
    tkinter.Button(text="Use Cell",foreground="grey",font="Times 16 bold",command=Use_Cell).pack(ipadx=10,ipady=10) #Button to go to creat account window
    #tkinter.Button(text="Cancel",foreground="grey",font="Times 14 bold",command=welcome.destroy).place(x=1400, y=750) #button  for cancel the functions





    welcome.mainloop()

Welcome()




