from os import times
import os
import tkinter
from tkinter import Pack, font
from tkinter.constants import BOTTOM, CENTER, LEFT, RIGHT, TOP
import time
import cv2
from PIL import Image, ImageTk
from face_recognition.api import face_distance
import numpy as np
import face_recognition
import pandas as pd
import datetime
import ctypes
######################## Follwonig code for the rasperry pi Distance sensor ############################################# 
import RPi.GPIO as GPIO   


GPIO.setmode(GPIO.BCM)
 

GPIO_TRIGGER = 18
GPIO_ECHO = 24
 

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
   
    GPIO.output(GPIO_TRIGGER, True)
 
    
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
   
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
   
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
   
    TimeElapsed = StopTime - StartTime
    
    distance = (TimeElapsed * 34300) / 2
 
    return distance

########################## End of Distance Function declaration#################################
while True:

    pic_taking=1
    acc_name_text=""
    alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
    cap= cv2.VideoCapture(0)



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


    def checkin():
        
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
        tkinter.Button(Entry,text='Enter',font="Times 20 bold",command=Use_Cell).place(x=600,y=700)
        
        
        
        

        Entry.mainloop()

    

    def Creat_acc_photo():
        global acc_pic
        global label
        global cap
        global acc_name_text
        acc_pic=tkinter.Tk()
        label =tkinter.Label(acc_pic)
        label.pack(side=LEFT)
        acc_pic.title("Inabayama")
        acc_pic.attributes('-fullscreen',True)
        tkinter.Button(acc_pic,text="Cancel",command=return_welcome2).place(x=1400, y=750)
        while True:
            dist = distance()
            if dist>30 and dist<50:
                break
            ctypes.windll.user32.MessageBoxW(0, "Please move into the footpoint", "Out of range detected", 1)
          #makes the window fullscreen
        tkinter.Label(acc_pic,text=f'{acc_name_text}',font="Times 16 bold",height=13).pack(side=TOP)
        #tkinter.Button(text="Camera On",font="Times 16 bold",command=tk_pic.video).place(x=700, y=500)
        tkinter.Button(acc_pic,text="Take picture",font="Times 16 bold",command=take_photo).place(x=700, y=600)
        
        show_frames()
        
        acc_pic.mainloop()

    def show_frames():
        if pic_taking==1:
            # Get the latest frame and convert into Image
            cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
            img = Image.fromarray(cv2image)
            # Convert image to PhotoImage
            imgtk = ImageTk.PhotoImage(image = img)
            label.imgtk = imgtk
            label.configure(image=imgtk)
            # Repeat after an interval to capture continiously

            label.after(20, show_frames)   

    def discard_photo():
        acc_pic.destroy()
        global pic_taking
        pic_taking=1
        #show_frames()
        Creat_acc_photo()

    def take_photo():
        global pic_taking
        pic_taking=0
        global frame
        ret, frame = cap.read()
        print (ret)
        tkinter.Button(acc_pic,text="Discard photo",font="Times 16 bold",command=discard_photo).place(x=900, y=600)
        tkinter.Button(acc_pic,text="Done",font="Times 16 bold",command=save_pic).place(x=1100, y=600)


    def save_pic():
        cv2.imwrite(f'photos\{acc_name_text}.png', frame)
        now = datetime.datetime.now()
        #os.system("gui.py")
        df = pd.read_csv('data.csv')
        print(df.to_string())
        data = pd.DataFrame([[acc_name_text,str(now),str(now),"NA"]])
        data.to_csv('data.csv', mode='a', index=False, header=False)
        acc_pic.destroy()
        # releasing the webcam

        #cap.release()
        # displaying image

        #cv2.imshow("my image", frame)
        #cv2.imwrite('photos\opencv1.png', frame)
        # stopping the output

        #cv2.waitKey()

        # releasing all windows

        #cv2.destroyAllWindows()
    
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
        import pandas as pd
        df = pd.read_csv('data.csv')

        exists = acc_name_text in df["Name"].values
        if exists:
              
            ctypes.windll.user32.MessageBoxW(0, "Close this window box and renter the modiifed name", "Name already exist", 1)
        else: 
            Entry.destroy()
            Creat_acc_photo()
        
        
        #tk_pic.video()

    def return_welcome2():
        acc_pic.destroy()
    


    def return_welcome():
        Entry.destroy()
    





    def Use_Cell():
        data = pd.read_csv('data.csv',index_col='Name')

        df = pd.read_csv('data.csv')

        exists = acc_name_text in df["Name"].values
        if not exists:  
            ctypes.windll.user32.MessageBoxW(0, "Close the window and retry. If the issue persist contact the technical support", "Name not registered", 1)
        else: 
            is_face=[]
            cell=0
            Entry.destroy()
            global use_cell
            use_cell=tkinter.Tk()
            use_cell.title("Inabayama")
            use_cell.attributes('-fullscreen',True)  #makes the window fullscreen
            tkinter.Button(text="Cancel",command=use_cell.destroy).place(x=1400, y=750)
            
            for i in range(5):
                time.sleep(0.5)
                ret, frame = cap.read()
                #print (ret)

                # releasing the webcam

                
                cv2.imwrite(f'photos\opencv{i}.png', frame)
            actimage = face_recognition.load_image_file(f'photos\{acc_name_text}.png')
            actimage = cv2.cvtColor(actimage,cv2.COLOR_BGR2RGB)
            faceLoc = face_recognition.face_locations(actimage)[0]
            encodeact = face_recognition.face_encodings(actimage)[0]
            cv2.rectangle(actimage,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(200,1000,200),2)
            for j in range(5):
                
                test = face_recognition.load_image_file(f'photos\opencv{j}.png')
                test = cv2.cvtColor(test,cv2.COLOR_BGR2RGB)
                try:
                    faceLoctest = face_recognition.face_locations(test)[0]
                    encodetest = face_recognition.face_encodings(test)[0]
                    
                    #cv2.rectangle(test,(faj,ceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(200,1000,200),2)
                    results = face_recognition.compare_faces([encodeact],encodetest)
                    is_face.append(results)
                    cell+=results[0]
                except:
                    ctypes.windll.user32.MessageBoxW(0, "We couldn't find any face in the takes.\n Please redo the proccess\n if problem persists contact technical support", "Face not found", 1)
                    break
            if cell>3:
                now = datetime.datetime.now()
                data.loc[f'{acc_name_text}','last used']=str(now)
                data.to_csv('data.csv')
                tkinter.Button(text="Get Cell",command=get_cell_sto).place(x=800, y=750)
                tkinter.Button(text="Desolve Account",command=desolve_acc).place(x=600, y=750)
                
                


            
            print(is_face)


        



        use_cell.mainloop()



    def get_cell_sto():
        df = pd.read_csv('data.csv')
        da=df[df["Name"]==acc_name_text]
        row=da['row']
        col=da['col']
        DIR =20
        STEP= 21
        CW = 1
        CCW =0
        SPR =48

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(DIR,GPIO.OUT)
        GPIO.setup(STEP,GPIO.OUT)
        GPIO.output(DIR,CW)

        step_count = SPR
        delay = 0.0208

        for x in range(step_count/360*25.71*col):
            GPIO.output(STEP,GPIO.HIGH)
            time.sleep(delay)
            GPIO.output(STEP,GPIO.LOW)
            time.sleep(delay)

        ARD1=25
        ARD2=22
        ARD3=27
        ARD4=26

        GPIO.setup(ARD1,GPIO.OUT)
        GPIO.setup(ARD2,GPIO.OUT)
        GPIO.setup(ARD3,GPIO.OUT)
        GPIO.setup(ARD4,GPIO.OUT)

        # GPIO.output(ARD1,1)
        # GPIO.output(ARD2,0)
        # GPIO.output(ARD3,0)

        # time.sleep(1)

        col_la=bin(row)

        GPIO.output(ARD1,int(col_la[3]))
        GPIO.output(ARD2,int(col_la[2]))
        GPIO.output(ARD3,int(col_la[1]))
        GPIO.output(ARD4,int(col_la[0]))
        time.sleep(21+10*row)


        for x in range(step_count/360*25.71*col):
            GPIO.output(STEP,GPIO.LOW)
            time.sleep(delay)
            GPIO.output(STEP,GPIO.HIGH)
            time.sleep(delay)



        # time.sleep(10)

        # GPIO.output(ARD1,0)
        # GPIO.output(ARD2,1)
        # GPIO.output(ARD3,0)

        # time.sleep(1)
        # time.sleep(10)

        # GPIO.output(ARD1,0)
        # GPIO.output(ARD2,0)
        # GPIO.output(ARD3,1)
        tkinter.Button(use_cell,text="Return cell",command=return_cell).place(x=600, y=750)


    def return_cell():
        df = pd.read_csv('data.csv')
        da=df[df["Name"]==acc_name_text]
        row=da['row']
        col=da['col']
        DIR =20
        STEP= 21
        CW = 1
        CCW =0
        SPR =48

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(DIR,GPIO.OUT)
        GPIO.setup(STEP,GPIO.OUT)
        GPIO.output(DIR,CW)

        step_count = SPR
        delay = 0.0208

        

        ARD1=25
        ARD2=22
        ARD3=27
        ARD4=26

        GPIO.setup(ARD1,GPIO.OUT)
        GPIO.setup(ARD2,GPIO.OUT)
        GPIO.setup(ARD3,GPIO.OUT)
        GPIO.setup(ARD4,GPIO.OUT)

        # GPIO.output(ARD1,1)
        # GPIO.output(ARD2,0)
        # GPIO.output(ARD3,0)

        # time.sleep(1)

        col_la=bin(row)

        GPIO.output(ARD1,int(col_la[3]))
        GPIO.output(ARD2,int(col_la[2]))
        GPIO.output(ARD3,int(col_la[1]))
        GPIO.output(ARD4,int(col_la[0]))
        time.sleep(21+10*row)

        for x in range(step_count/360*25.71*col):
            GPIO.output(STEP,GPIO.HIGH)
            time.sleep(delay)
            GPIO.output(STEP,GPIO.LOW)
            time.sleep(delay)

        time.sleep(60)

        for x in range(step_count/360*25.71*col):
            GPIO.output(STEP,GPIO.LOW)
            time.sleep(delay)
            GPIO.output(STEP,GPIO.HIGH)
            time.sleep(delay)

        








    def desolve_acc():
        now = datetime.datetime.now()
        data = pd.read_csv('data.csv',index_col='Name')
        data.loc[f'{acc_name_text}','canceled time']=str(now)
        data.to_csv('data.csv')
        use_cell.destroy()

    def Welcome():    
        global welcome                                                              #Welcome window
        welcome = tkinter.Tk() #Welcome window
        welcome.title("Inabayama")
        welcome.attributes('-fullscreen',True)  #makes the window fullscreen
        load= Image.open("Icon.png")
        load= load.resize((500,500), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        
        tkinter.Label(welcome, image=render).place(x=100,y=100)
        
        tkinter.Label(welcome, text = "Welcome to Inabayama",justify=CENTER,font="times 35 bold",fg="grey",height=12).pack() #Welcome Text
        tkinter.Button(welcome,text="Creat Account",foreground="grey",font="Times 16 bold",command=Creat_acc).pack(ipadx=10,ipady=10) #Button to go to creat account window
        tkinter.Button(welcome,text="Use Cell",foreground="grey",font="Times 16 bold",command=checkin).pack(ipadx=10,ipady=10) #Button to go to creat account window
        #tkinter.Button(text="Cancel",foreground="grey",font="Times 14 bold",command=welcome.destroy).place(x=1400, y=750) #button  for cancel the functions





        welcome.mainloop()

    # wait = tkinter.Tk() #Welcome window
    # wait.title("Inabayama")
    # wait.attributes('-fullscreen',True)  #makes the window fullscreen
    # tkinter.Label(wait, text = "Wait program is loading",justify=CENTER,font="times 45 bold",fg="grey",height=12).pack()
    # time.sleep(3)
    Welcome()




