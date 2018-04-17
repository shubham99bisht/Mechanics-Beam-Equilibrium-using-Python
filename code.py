from tkinter import *
import math
import numpy as np
from PIL import Image,ImageTk

#variable declaration
#variables for type 1 
sgmx, sgmy, sgmm=0,0,0
#variables for type 3
sy,sm=0,0
#variables for type 4
sy4,sam4=0,0
#variables for overhanging
yovr,movr=0,0
#variables for type 5
x5,y5,m5=0,0,0
#variables for type 6
x6,y6,m6=0,0,0


#main class. it loads all the pages and is responsible for showing the current frame on screen.
class mechproj(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)
        container.pack(side=TOP, fill=BOTH, expand=1)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        #F is a tuple(unchangable array) which contains list of all the class that this program has.
        for F in (WelcomePage,RDme,InputPage,SimSupp,ST1,ST2,ST3,ST4,ST5,ST6,S5,ADDXst1, ADDYst1, ADDOBst1, ADDUDLst1,ADDUDLst3, ADDYst3, ADDYst4, ADDUDLst4,OvrHng,ADDYovr,ADDUDLovr,ADDXst5, ADDYst5, ADDOBst5, ADDUDLst5,ADDXst6, ADDYst6, ADDOBst6, ADDUDLst6):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky=N + S + E + W)
        self.show_frame(WelcomePage)
    #this function takes a Page name as parameter (named as 'cont') and displays it on top, hiding other pages behind.
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        
#Welcome page class, first page to get loaded 
class WelcomePage(Frame):
 def __init__(self,parent,controller) :
  Frame.__init__(self,parent)
  #For showing logo on top, "sticky=N" means stick this label to north(top).
  lo=Label(self, text="MECHwithTECH", font=("Berlin Sans FB",40))
  lo.place(relx=0.5, rely=0.1, anchor=CENTER)

  #button for "Read Me" on this page and the next line specifies its position on page.
  #controller.showFrame() calls the show frame function defined in class mechproj with input parameter of the page name to be opened.
  home = ImageTk.PhotoImage(Image.open("ead.png"))
  b2 = Button(self, image=home, command=lambda: controller.show_frame(RDme))
  b2.image = home
  b2.place(relx=0.25, rely=0.65, anchor=CENTER)

  home = ImageTk.PhotoImage(Image.open("home.png"))
  b2 = Button(self, image=home, command=lambda: controller.show_frame(RDme))
  b2.image = home
  b2.place(relx=0.5, rely=0.4, anchor=CENTER)

  #Labels are used for showing text content on page.
  t1=Label(self, text="NOTE: Please read READ-ME for input details and to know about assumptions\nthe creator of this app has taken!")
  t1.place(relx=0.5, rely=0.8, anchor=CENTER)

  #button for "Start Now" on this page and the next line specifies its position on page.
  #controller.showFrame() calls the show frame function defined in class mechproj with input parameter of the page name to be opened.

  home = ImageTk.PhotoImage(Image.open("start.jpg"))
  b2 = Button(self, image=home, command=lambda: controller.show_frame(InputPage))
  b2.image = home
  b2.place(relx=0.75, rely=0.65, anchor=CENTER)


  #Labels are used for showing text content on page.
  l=Label(self, text="Made by Shubham Bisht",font=("",10,"bold"))
  l.place(relx=0.99, rely=0.99, anchor=SE)

class InputPage(Frame):
 def __init__(self, parent, controller):
  Frame.__init__(self, parent)
  #all globally declared variables must be declared as global before they can be used inside a function.
  global sgmx, sgmy, sgmm,sy,sm,sy4,sam4,yovr,movr
  #initilizing those global variables to 0.
  sgmx, sgmy, sgmm, sy, sm, sy4, sam4, yovr, movr = 0, 0, 0, 0, 0, 0, 0, 0, 0
  
  #For showing logo on top, "sticky=N" means stick this label to north(top).
  lo = Label(self, text="MECHwithTECH", font=("Berlin Sans FB", 40 ))
  lo.place(relx=0.5, rely=0.1, anchor=CENTER)

  #Labels are used for showing text content on page.
  l1=Label(self, text="Choose the beam type:", font=("times",30,"bold"))
  l1.place(relx=0.5, rely=0.3, anchor=CENTER)

  #button for "Simple supp" option on this page, command opens the Simsupp class(simple support) when this button is clicked.
  home = ImageTk.PhotoImage(Image.open("p1.jpg"))
  b2 = Label(self, image=home)
  b2.image = home
  b2.place(relx=0.33333, rely=0.5, anchor=CENTER)
  b2=Button(self,width=20, text="SIMPLE SUPPORTED",font=("times",25,"bold"), command=lambda: controller.show_frame(SimSupp))
  b2.place(relx=0.33333, rely=0.6, anchor=CENTER)

  #button for "over-hanging" option on this page, command opens the Ovrhng class (overhanging) when this button is clicked.
  home = ImageTk.PhotoImage(Image.open("p2.jpg"))
  b2 = Label(self, image=home)
  b2.image = home
  b2.place(relx=0.66666, rely=0.5, anchor=CENTER)
  b2=Button(self,width=20, text="OVER-HANGING",font=("times",25,"bold"), command=lambda: controller.show_frame(OvrHng))
  b2.place(relx=0.66666, rely=0.6, anchor=CENTER)

#class for simple supported beam type of problems
class SimSupp(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        #For showing logo on top, "sticky=N" means stick this label to north(top).
        lo = Label(self, text="MECHwithTECH", font=("Berlin Sans FB", 40 ))
        lo.place(relx=0.5, rely=0.1, anchor=CENTER)

        l1 = Label(self, text="Choose the Problem Type:", font=("times", 40, "bold"))
        l1.place(relx=0.5, rely=0.2, anchor=CENTER)

        #five buttons for showing different options for problem types on this page.
        #when any of these buttons is clicked, show frame is called respective page gets displayed.
        b1=Button(self,width=60,text="""TYPE I: To find: Reaction forces at two support points      .
             Given: Load and their Positions on Beam.""",justify=LEFT,command=lambda: controller.show_frame(ST1),font=(30))
        b1.place(relx=0.5, rely=0.4, anchor=CENTER)

        b2=Button(self,width=60, text="""TYPE II: To find: Max load and its position                          .
              Given: Reactions forces and Length of Beam.""",justify=LEFT,command=lambda: controller.show_frame(ST2),font=(30))
        b2.place(relx=0.5, rely=0.5, anchor=CENTER)

        b3=Button(self,width=60, text="""TYPE III: To find: One reaction force and Position of Load.
                Given: One reaction force and Load.""",justify=LEFT,command=lambda: controller.show_frame(ST3),font=(30))
        b3.place(relx=0.5, rely=0.6, anchor=CENTER)

        b4=Button(self,width=60, text="""TYPE IV: To find: Load and its Position                              .
                Given: Both Reaction forces are equal.""",justify=LEFT,command=lambda: controller.show_frame(ST4),font=(30))
        b4.place(relx=0.5, rely=0.7, anchor=CENTER)

        b5= Button(self, width=60,text="""TYPE V: To find: Reaction forces at two support points     .
                Given: One of the Supports is inclined.""",justify=LEFT,command=lambda: controller.show_frame(S5),font=(30))
        b5.place(relx=0.5, rely=0.8, anchor=CENTER)
class ST1(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        #For showing logo on top, "sticky=N" means stick this label to north(top).
        lo = Label(self, text="MECHwithTECH", font=("Berlin Sans FB", 40 ))
        lo.place(relx=0.5, rely=0.1, anchor=CENTER)
        
        #Label for asking user to input length of beam
        l1=Label(self,text="Length of Beam:", font=(15))
        l1.place(relx=0.4, rely=0.3, anchor=CENTER)
        #Entry widget infront of above label to take input length from user.
        self.e1=Entry(self)
        self.e1.place(relx=0.6, rely=0.3, anchor=CENTER)
        
        #four buttons below are used for adding different forces on the beam.
        #each button calls a different class using showFrame() to perform the respective function

        b1=Button(self, text="Add Force along Y-axis",font=(15), width=25, command=lambda :controller.show_frame(ADDYst1))
        b1.place(relx=0.4, rely=0.4, anchor=CENTER)

        b2 = Button(self, text="Add Force along X-axis",font=(15),width=25, command=lambda :controller.show_frame(ADDXst1))
        b2.place(relx=0.6, rely=0.4, anchor=CENTER)

        b3 = Button(self, text="Add Oblique Force",font=(15),width=25, command=lambda :controller.show_frame(ADDOBst1))
        b3.place(relx=0.4, rely=0.5, anchor=CENTER)

        b4 = Button(self, text="Add Uniformly Distributed Load",font=(15),width=25, command=lambda :controller.show_frame(ADDUDLst1))
        b4.place(relx=0.6, rely=0.5, anchor=CENTER)


        #this button calls the sol() function defined just below, to calculate and display the solution.
        b6=Button(self, text="Solve!",font=(30), command=lambda : sol())
        b6.place(relx=0.4, rely=0.7, anchor=CENTER)
        #this button calls the newp() function defined just below, to re-initialize all variables to 0 and start a new problem.
        b7=Button(self, text="New Problem", font=(30),command=lambda :newp())
        b7.place(relx=0.6, rely=0.7, anchor=CENTER)

        def sol():
            #global variables re-declared
            global sgmm,sgmx,sgmy
            
            #Taking input from self.e1 entry widget defined above using .get() converting it to float
            #and storing the value in a new variable named as "len"
            len=float(self.e1.get())
            
            # rax is the only force acting along x direction, since at B there is a roller support, which will always be
            #perpendicularly upwards. so, rax= negative of sigma X.
            rax=(-1*sgmx)
            
            #sgmm is moment of all forces(expect support reactions) about point A (left end).
            #using 'sigma moment=0' reaction at B is equal to sgmm divided by distance of B from A i.e. length of beam.
            rb=(sgmm)/len
            
            #using 'sigma Y=0', we know value of reaction at right end, therefore reaction at left end = (sigma y)-ra
            ray=sgmy-rb
            if rax==0:
                #if there is no force about x axis rax=0, therefore ra=ray.
                ra=ray
                #rounding the solution to 2 decimal places.
                ra=round(ra,2)
                rb = round(rb, 2)
                #creating a new label for showing the solution.
                self.An = Label(self, text="""The solution is :\n\n Reaction at A={} N\n Reaction at B={} N
                
                
                NOTE: Human takes about 10 mins to solve such problems and computer completed it in about 0.1 secs!""".format(ra,rb), font=(30))
                self.An.place(relx=0.5, rely=0.9, anchor=CENTER)
            else:
                #if rax not equal to zero, then angle of their resultant is calculated. 
                th=math.atan(abs(ray)/abs(rax))
                th=math.degrees(th)
                if rax>=0 and ray>=0:
                    th=th
                elif rax<0 and ray>0:
                    th=th+90
                elif rax<0 and ray<=0:
                    th+=180
                else:
                    th+=270
                #calculating resultant of rax and ray.
                ra = math.sqrt(rax ** 2 + ray ** 2)
                #creating a new label for showing the solution.
                self.An = Label(self, text="""The solution is :\n\n Reaction at A={} N, inclined at {} degrees to +X-axis\n Reaction at B={} N
                
                \nNOTE: Human takes about 10 mins to solve such problems and computer completed it in about 0.1 secs!""".format(ra,th,rb),font=(30))
                self.An.place(relx=0.5, rely=0.9, anchor=CENTER)

        def newp():
            #this function is for re-initializing all variables used to solve the above problem to 0 and starting a new problem.
            global sgmm, sgmx, sgmy
            sgmm, sgmx, sgmy=0,0,0
            # .destory() is used to remove the previous solution from the page.(Remember we created a new label for showing solution).
            self.An.destroy()
            self.e1.delete(0, 'end')
            controller.show_frame(InputPage)
class ADDXst1(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        #For showing logo on top, "sticky=N" means stick this label to north(top).
        lo = Label(self, text="MECHwithTECH", font=("Berlin Sans FB", 40 ))
        lo.place(relx=0.5, rely=0.1, anchor=CENTER)

        #Label asking for magnitude of force from user.
        l1 = Label(self, text="Magnitude:", font=(15))
        l1.place(relx=0.4, rely=0.3, anchor=CENTER)
        #entry widget against that label to take input.
        self.e1 = Entry(self)
        self.e1.place(relx=0.6, rely=0.3, anchor=CENTER)

        v = DoubleVar()
        #Label asking for magnitude of force from user.
        l2 = Label(self, text="Direction : ", font=(15))
        l2.place(relx=0.4, rely=0.4, anchor=CENTER)
        #radio buttons for two options to be chosen, left or right.
        self.E2 = Radiobutton(self, text="Towards Left", variable=v, value="-1", font=(15))
        self.E2.place(relx=0.55, rely=0.4, anchor=W)
        self.E4 = Radiobutton(self, text="Towards Right", variable=v, value="1", font=(15))
        self.E4.place(relx=0.55, rely=0.45, anchor=W)

        #submit button to call the sub() function.
        b = Button(self, text="Submit",font=(15), command=lambda :sub())
        b.place(relx=0.5, rely=0.6, anchor=CENTER)
        
        #this function takes the input and again opens the previous page (ST1) from where the add force button was clicked.
        def sub():
            global sgmx
            #mag is storing the magnitude of force that users enters in e1 Entry widget.
            mag=float(self.e1.get())
            #storing value of force in sgmx (sigma x).
            sgmx+=mag*v.get()
            self.e1.delete(0, 'end')
            #calling back the previous page.
            controller.show_frame(ST1)
class ADDYst1(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        #For showing logo on top, "sticky=N" means stick this label to north(top).
        lo = Label(self, text="MECHwithTECH", font=("Berlin Sans FB", 40 ))
        lo.place(relx=0.5, rely=0.1, anchor=CENTER)

        l1 = Label(self, text="Magnitude:",font=(15))
        l1.place(relx=0.4, rely=0.3, anchor=CENTER)
        self.e1 = Entry(self)
        self.e1.place(relx=0.6, rely=0.3, anchor=CENTER)

        l2 = Label(self, text="Position (from left end):",font=(15))
        l2.place(relx=0.4, rely=0.4, anchor=CENTER)
        self.e2 = Entry(self)
        self.e2.place(relx=0.6, rely=0.4, anchor=CENTER)

        v = DoubleVar()
        l2 = Label(self, text="Direction : ",font=(15))
        l2.place(relx=0.4, rely=0.5, anchor=CENTER)
        self.E2 = Radiobutton(self, text="Upwards",font=(15), variable=v, value="-1")
        self.E2.place(relx=0.55, rely=0.5, anchor=W)
        self.E4 = Radiobutton(self, text="Downwards",font=(15), variable=v, value="1")
        self.E4.place(relx=0.55, rely=0.55, anchor=W)

        b = Button(self, text="Submit", command=lambda :clr(),font=(15))
        b.place(relx=0.5, rely=0.6, anchor=CENTER)

        def clr():
            global sgmy
            global sgmm
            #taking magnitude and position from Entry widgets.
            pos=float(self.e2.get())
            mag=float(self.e1.get())
            #clearing the Entry widget for next input.
            self.e2.delete(0,"end")
            self.e1.delete(0, "end")
            #storing magnitude multiplied by direction in sigma Y.
            sgmy+=mag*v.get()
            #calculating and storing moment in sgmm
            sgmm+=(mag*pos*v.get())
            #calling back ST1
            controller.show_frame(ST1)
class ADDUDLst1(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        #For showing logo on top, "sticky=N" means stick this label to north(top).
        lo = Label(self, text="MECHwithTECH", font=("Berlin Sans FB", 40 ))
        lo.place(relx=0.5, rely=0.1, anchor=CENTER)
        #this class is for taking a UDL force as input.
        #so, below are labels and entry widgets for taking input from user.

        l1 = Label(self, text="Magnitude:",font=(15))
        l1.place(relx=0.4, rely=0.3, anchor=CENTER)
        self.e1 = Entry(self)
        self.e1.place(relx=0.6, rely=0.3, anchor=CENTER)

        l2 = Label(self, text="Position (Of starting point from left end):",font=(15))
        l2.place(relx=0.4, rely=0.4, anchor=CENTER)
        self.e2 = Entry(self)
        self.e2.place(relx=0.6, rely=0.4, anchor=CENTER)

        l3 = Label(self, text="Length of UDL:",font=(15))
        l3.place(relx=0.4, rely=0.5, anchor=CENTER)
        self.e3 = Entry(self)
        self.e3.place(relx=0.6, rely=0.5, anchor=CENTER)

        v = DoubleVar()
        l2 = Label(self, text="Direction : ",font=(15))
        l2.place(relx=0.4, rely=0.6, anchor=CENTER)
        self.E2 = Radiobutton(self, text="Upwards", variable=v, value="-1",font=(15))
        self.E2.place(relx=0.55, rely=0.6, anchor=W)
        self.E4 = Radiobutton(self, text="Downwards", variable=v, value="1",font=(15))
        self.E4.place(relx=0.55, rely=0.65, anchor=W)
        
        #button to call clr() function defined below, when submit button is clicked.
        b = Button(self, text="Submit", command=lambda :clr(),font=(15))
        b.place(relx=0.5, rely=0.7, anchor=CENTER)

        def clr():
            global sgmy
            global sgmm
            #taking values of magnitude and position and storing in mag, pos variables.
            mag=float(self.e3.get())*float(self.e1.get())*v.get()
            pos=float(self.e2.get())+float(self.e3.get())/2
            #adding value of force to sigma y and moment to sigma M
            sgmy+=mag
            sgmm+=(mag*pos)
            self.e1.delete(0,"end")
            self.e2.delete(0, "end")
            self.e3.delete(0, "end")
            controller.show_frame(ST1)
class ADDOBst1(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        #For showing logo on top, "sticky=N" means stick this label to north(top).
        lo = Label(self, text="MECHwithTECH", font=("Berlin Sans FB", 40 ))
        lo.place(relx=0.5, rely=0.1, anchor=CENTER)

        l1 = Label(self, text="Magnitude:",font=(15))
        l1.place(relx=0.4, rely=0.3, anchor=CENTER)
        self.e1 = Entry(self)
        self.e1.place(relx=0.6, rely=0.3, anchor=CENTER)

        l2 = Label(self, text="Position (Of starting point from left end):", font=(15))
        l2.place(relx=0.4, rely=0.4, anchor=CENTER)
        self.e2 = Entry(self)
        self.e2.place(relx=0.6, rely=0.4, anchor=CENTER)

        l3 = Label(self, text="Angle with positive X axis (0-360 degrees):",font=(15))
        l3.place(relx=0.4,rely=0.5,anchor=CENTER)
        self.e3 = Entry(self)
        self.e3.place(relx=0.6,rely=0.5,anchor=CENTER)

        b = Button(self, text="Submit", command=lambda :clr(),font=(15))
        b.place(relx=0.5, rely=0.6, anchor=CENTER)
# the function below this line, takes oblique values
        def clr():
            global sgmx
            global sgmy
            global sgmm
            a=float(self.e3.get())
            mag=float(self.e1.get())
            fx, fy=0,0
            if 0<=a<90 or a==360:
                fx=mag*math.cos(math.radians(a))
                fy = mag * math.sin(math.radians(a))
                fy*=(-1)
            elif 90<a<180:
                a%=90
                fx = mag * math.sin(math.radians(a))
                fy = mag * math.cos(math.radians(a))
                fx*=(-1)
                fy *= (-1)
            elif 180<a<270:
                a%=90
                fx = mag*math.cos(math.radians(a))
                fy = mag * math.sin(math.radians(a))
                fx*=(-1)
            elif 270<a<=360:
                a%=90
                fx = mag * math.sin(math.radians(a))
                fy = mag * math.cos(math.radians(a))
            elif a==90:
                fx=0
                fy=(-1*mag)
            elif a==180:
                fx=(-1*mag)
                fy=0
            elif a==270:
                fx=0
                fy=mag
            sgmy+=fy
            sgmx+=fx
            sgmm+=fy*float(self.e2.get())
            controller.show_frame(ST1)
class ST2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        lo = Label(self, text="MECHwithTECH", font=("Berlin Sans FB", 40 ))
        lo.place(relx=0.5, rely=0.1, anchor=CENTER)

        l1=Label(self, text="Reaction force at left end (Ra):",font=(15))
        l1.place(relx=0.4, rely=0.3, anchor=CENTER)
        self.e1=Entry(self)
        self.e1.place(relx=0.6, rely=0.3, anchor=CENTER)

        l2=Label(self, text="Reaction force at right end (Rb):",font=(15))
        l2.place(relx=0.4, rely=0.4, anchor=CENTER)
        self.e2=Entry(self)
        self.e2.place(relx=0.6, rely=0.4, anchor=CENTER)

        l3=Label(self, text="Length of Beam:",font=(15))
        l3.place(relx=0.4, rely=0.5, anchor=CENTER)
        self.e3=Entry(self)
        self.e3.place(relx=0.6, rely=0.5, anchor=CENTER)

        b1=Button(self, text="Solve!", command= lambda : sol(),font=(15))
        b1.place(relx=0.4, rely=0.6, anchor=CENTER)

        b7 = Button(self, text="New Problem", command=lambda: newp(),font=(15))
        b7.place(relx=0.6, rely=0.6, anchor=CENTER)

        def sol():
            ra=float(self.e1.get())
            rb=float(self.e2.get())
            l=float(self.e3.get())
            w=ra+rb
            p=rb*l/w
            self.An = Label(self, text="""The solution is :\n\n Max Load = {} N\n Position of load from left end = {} m
            
            \nNOTE: Human takes about 10 mins to solve such problems and computer completed it in about 0.1 secs!""".format(w,p),font=(15))
            self.An.place(relx=0.5, rely=0.8, anchor=CENTER)

        def newp():
            self.An.destroy()
            self.e1.delete(0, 'end')
            self.e2.delete(0, 'end')
            self.e3.delete(0, 'end')
            controller.show_frame(InputPage)
class ST3(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        lo = Label(self, text="MECHwithTECH", font=("Berlin Sans FB", 40 ))
        lo.place(relx=0.5, rely=0.1, anchor=CENTER)

        l1 = Label(self, text="Reaction force at left end (Ra):",font=(15))
        l1.place(relx=0.4, rely=0.3, anchor=CENTER)
        self.e1 = Entry(self)
        self.e1.place(relx=0.6, rely=0.3, anchor=CENTER)

        l2 = Label(self, text="Load Weight:",font=(15))
        l2.place(relx=0.4, rely=0.4, anchor=CENTER)
        self.e2 = Entry(self)
        self.e2.place(relx=0.6, rely=0.4, anchor=CENTER)

        l3 = Label(self, text="Beam Length:",font=(15))
        l3.place(relx=0.4, rely=0.5, anchor=CENTER)
        self.e3 = Entry(self)
        self.e3.place(relx=0.6, rely=0.5, anchor=CENTER)

        b1 = Button(self, text="Add Force along Y-axis", width=20, command=lambda: controller.show_frame(ADDYst3),font=(15))
        b1.place(relx=0.4, rely=0.6, anchor=CENTER)

        b4 = Button(self, text="Add Uniformly Distributed Load",command=lambda: controller.show_frame(ADDUDLst3),font=(15))
        b4.place(relx=0.6, rely=0.6, anchor=CENTER)

        b1 = Button(self, text="Solve!", command=lambda :sol(),font=(15))
        b1.place(relx=0.4, rely=0.7, anchor=CENTER)

        b7 = Button(self, text="New Problem", command=lambda: newp(),font=(15))
        b7.place(relx=0.6, rely=0.7, anchor=CENTER)

        def sol():
            global sy
            global sm
            ra=float(self.e1.get())
            w=float(self.e2.get())
            l=float(self.e3.get())
            rb=sy+w-ra
            p=(rb*l-sm)/w
            self.An = Label(self,text="""The solution is :\n Reaction at B = {} N\n Position of load from left end = {} m
                                      
            \nNOTE: Human takes about 10 mins to solve such problems and computer completed it in about 0.1 secs!""".format(rb, p),font=(15))
            self.An.place(relx=0.5, rely=0.9, anchor=CENTER)
        def newp():
            global sm,sy
            sm,sy=0,0
            self.An.destroy()
            self.e1.delete(0, 'end')
            self.e2.delete(0, 'end')
            self.e3.delete(0, 'end')
            controller.show_frame(InputPage)
class ADDYst3(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        lo = Label(self, text="MECHwithTECH", font=("Berlin Sans FB", 40 ))
        lo.place(relx=0.5, rely=0.1, anchor=CENTER)

        l1 = Label(self, text="Magnitude:",font=(15))
        l1.place(relx=0.4, rely=0.3, anchor=CENTER)
        self.e1 = Entry(self)
        self.e1.place(relx=0.6, rely=0.3, anchor=CENTER)

        l2 = Label(self, text="Position (from left end):",font=(15))
        l2.place(relx=0.4, rely=0.4, anchor=CENTER)
        self.e2 = Entry(self)
        self.e2.place(relx=0.6, rely=0.4, anchor=CENTER)

        v = DoubleVar()
        l2 = Label(self, text="DIRECTION : ",font=(15))
        l2.place(relx=0.4, rely=0.5, anchor=CENTER)
        self.E2 = Radiobutton(self, text="Upwards", variable=v, value="1",font=(15))
        self.E2.place(relx=0.55, rely=0.5, anchor=W)
        self.E4 = Radiobutton(self, text="Downwards", variable=v, value="-1",font=(15))
        self.E4.place(relx=0.55, rely=0.55, anchor=W)

        b = Button(self, text="Submit", command=lambda :clr(),font=(15))
        b.place(relx=0.5, rely=0.6, anchor=CENTER)

        def clr():
            #clear everything to blank
            global sy
            global sm
            pos=float(self.e2.get())
            mag=float(self.e1.get())
            self.e2.delete(0,"end")
            self.e1.delete(0, "end")
            sy+=mag
            sm+=mag*pos
            controller.show_frame(ST3)
class ADDUDLst3(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        lo = Label(self, text="MECHwithTECH", font=("Berlin Sans FB", 40 ))
        lo.place(relx=0.5, rely=0.1, anchor=CENTER)

        l1 = Label(self, text="Magnitude:")
        l1.place(relx=0.4, rely=0.3, anchor=CENTER)
        self.e1 = Entry(self)
        self.e1.place(relx=0.6, rely=0.3, anchor=CENTER)

        l2 = Label(self, text="Position (Of starting point from left end):")
        l2.place(relx=0.4, rely=0.4, anchor=CENTER)
        self.e2 = Entry(self)
        self.e2.place(relx=0.6, rely=0.4, anchor=CENTER)

        l3 = Label(self, text="Length of UDL:")
        l3.place(relx=0.4, rely=0.5, anchor=CENTER)
        self.e3 = Entry(self)
        self.e3.place(relx=0.6, rely=0.5, anchor=CENTER)

        v = DoubleVar()
        l2 = Label(self, text="DIRECTION : ")
        l2.place(relx=0.4, rely=0.6, anchor=CENTER)
        self.E2 = Radiobutton(self, text="Upwards", variable=v, value="1")
        self.E2.place(relx=0.55, rely=0.6, anchor=W)
        self.E4 = Radiobutton(self, text="Downwards", variable=v, value="-1")
        self.E4.place(relx=0.55, rely=0.65, anchor=W)

        b = Button(self, text="Submit", command=lambda :clr())
        b.place(relx=0.5, rely=0.7, anchor=CENTER)

        def clr():
            global sy
            global sm
            mag=float(self.e3.get())*float(self.e1.get())
            pos=float(self.e2.get())+float(self.e3.get())/2
            sy+=mag
            sm+=mag*pos
            self.e1.delete(0,"end")
            self.e2.delete(0, "end")
            self.e3.delete(0, "end")
            controller.show_frame(ST3)
class ST4(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        global lst4
        lo = Label(self, text="MECHwithTECH", font=("Berlin Sans FB", 40 ))
        lo.place(relx=0.5, rely=0.1, anchor=CENTER)

        l1 = Label(self, text="Length of Beam:",font=(15))
        l1.place(relx=0.4, rely=0.3, anchor=CENTER)
        self.e1 = Entry(self)
        self.e1.place(relx=0.6, rely=0.3, anchor=CENTER)
        lst4=self.e1.get()

        l2 = Label(self, text="Position of Load:",font=(15))
        l2.place(relx=0.4, rely=0.4, anchor=CENTER)
        self.e2 = Entry(self)
        self.e2.place(relx=0.6, rely=0.4, anchor=CENTER)
        lst4 = self.e1.get()

        b1 = Button(self, text="Add Force along Y-axis", command=lambda : controller.show_frame(ADDYst4),font=(15))
        b1.place(relx=0.4, rely=0.5, anchor=CENTER)

        b4 = Button(self, text="Add Uniformly Distributed Load", command=lambda : controller.show_frame(ADDUDLst4),font=(15))
        b4.place(relx=0.6, rely=0.5, anchor=CENTER)

        b5 = Button(self, text="Solve!", command=lambda : sol(),font=(15))
        b5.place(relx=0.4, rely=0.6, anchor=CENTER)

        b7 = Button(self, text="New Problem", command=lambda: newp(),font=(15))
        b7.place(relx=0.6, rely=0.6, anchor=CENTER)

        def sol():
            global sy4, sam4
            pos=float(self.e2.get())
            ln=float(self.e1.get())
            a=np.array([[1,-2],[pos, -1*ln]])
            b= np.array([[-1*sy4], [-1*sam4]])
            print(a,b)
            x=np.linalg.solve(a,b)
            print(x)
            W=float(x[0])
            rb = float(x[1])
            self.An = Label(self,text="""The solution is :\n Max Load = {} N\n Reaction at left end = {} N\n Reaction at right end = {} N
                                      
            \nNOTE: Human takes about 10 mins to solve such problems and computer completed it in about 0.1 secs!""".format(W, rb/2, rb/2),font=(15))
            self.An.place(relx=0.5, rely=0.8, anchor=CENTER)
        def newp():
            global sy4,sam4
            sy4, sam4=0,0
            self.An.destroy()
            self.e1.delete(0, 'end')
            self.e2.delete(0, 'end')
            controller.show_frame(InputPage)
class ADDYst4(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        lo = Label(self, text="MECHwithTECH", font=("Berlin Sans FB", 40 ))
        lo.place(relx=0.5, rely=0.1, anchor=CENTER)

        l1 = Label(self, text="Magnitude:",font=(15))
        l1.place(relx=0.4, rely=0.3, anchor=CENTER)
        self.e1 = Entry(self)
        self.e1.place(relx=0.6, rely=0.3, anchor=CENTER)

        l2 = Label(self, text="Position (from left end):",font=(15))
        l2.place(relx=0.4, rely=0.4, anchor=CENTER)
        self.e2 = Entry(self)
        self.e2.place(relx=0.6, rely=0.4, anchor=CENTER)

        v = DoubleVar()
        l2 = Label(self, text="Direction : ",font=(15))
        l2.place(relx=0.4, rely=0.5, anchor=CENTER)
        self.E2 = Radiobutton(self, text="Upwards", variable=v, value="-1",font=(15))
        self.E2.place(relx=0.55, rely=0.5, anchor=W)
        self.E4 = Radiobutton(self, text="Downwards", variable=v, value="1",font=(15))
        self.E4.place(relx=0.55, rely=0.55, anchor=W)

        b = Button(self, text="Submit", command=lambda :clr(),font=(15))
        b.place(relx=0.5, rely=0.6, anchor=CENTER)

        def clr():
            global sy4
            global sam4
            pos=float(self.e2.get())
            mag=float(self.e1.get())
            self.e2.delete(0,"end")
            self.e1.delete(0, "end")
            sy4+=mag*v.get()
            sam4+=mag*pos*v.get()
            controller.show_frame(ST4)
class ADDUDLst4(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        lo = Label(self, text="MECHwithTECH", font=("Berlin Sans FB", 40 ))
        lo.place(relx=0.5, rely=0.1, anchor=CENTER)

        l1 = Label(self, text="Magnitude:",font=(15))
        l1.place(relx=0.4, rely=0.3, anchor=CENTER)
        self.e1 = Entry(self)
        self.e1.place(relx=0.6, rely=0.3, anchor=CENTER)

        l2 = Label(self, text="Position (Of starting point from left end):",font=(15))
        l2.place(relx=0.4, rely=0.4, anchor=CENTER)
        self.e2 = Entry(self)
        self.e2.place(relx=0.6, rely=0.4, anchor=CENTER)

        l3 = Label(self, text="Length of UDL:",font=(15))
        l3.place(relx=0.4, rely=0.5, anchor=CENTER)
        self.e3 = Entry(self)
        self.e3.place(relx=0.6, rely=0.5, anchor=CENTER)

        v = DoubleVar()
        l2 = Label(self, text="Direction : ",font=(15))
        l2.place(relx=0.4, rely=0.6, anchor=CENTER)
        self.E2 = Radiobutton(self, text="Upwards", variable=v, value="-1",font=(15))
        self.E2.place(relx=0.55, rely=0.6, anchor=W)
        self.E4 = Radiobutton(self, text="Downwards", variable=v, value="1",font=(15))
        self.E4.place(relx=0.55, rely=0.65, anchor=W)

        b = Button(self, text="Submit", command=lambda :clr(),font=(15))
        b.place(relx=0.5, rely=0.7, anchor=CENTER)

        def clr():
            global sam4
            global sy4
            pos=float(self.e2.get())
            mag=float(self.e1.get())
            ln=float(self.e3.get())
            mag*=ln
            pos+=(ln/2)
            self.e2.delete(0,"end")
            self.e1.delete(0, "end")
            sam4=mag*pos*v.get()
            sy4+=mag*v.get()
            controller.show_frame(ST4)
class OvrHng(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        lo = Label(self, text="MECHwithTECH", font=("Berlin Sans FB", 40 ))
        lo.place(relx=0.5, rely=0.1, anchor=CENTER)

        l1=Label(self, text="Position of left support (from left end):",font=(15))
        l1.place(relx=0.4, rely=0.3, anchor=CENTER)
        self.e1=Entry(self)
        self.e1.place(relx=0.6, rely=0.3, anchor=CENTER)

        l2=Label(self, text="Position of right support (from left end):",font=(15))
        l2.place(relx=0.4, rely=0.4, anchor=CENTER)
        self.e2=Entry(self)
        self.e2.place(relx=0.6, rely=0.4, anchor=CENTER)

        l3=Label(self, text="Length of Beam:",font=(15))
        l3.place(relx=0.4, rely=0.5, anchor=CENTER)
        self.e3=Entry(self)
        self.e3.place(relx=0.6, rely=0.5, anchor=CENTER)

        b = Button(self, text="Add Force along Y-axis", command=lambda: controller.show_frame(ADDYovr),font=(15))
        b.place(relx=0.4, rely=0.6, anchor=CENTER)

        b4 = Button(self, text="Add Uniformly Distributed Load", command=lambda: controller.show_frame(ADDUDLovr),font=(15))
        b4.place(relx=0.6, rely=0.6, anchor=CENTER)

        b1=Button(self, text="Solve!", command= lambda : sol(),font=(15))
        b1.place(relx=0.4, rely=0.7, anchor=CENTER)

        b7 = Button(self, text="New Problem", command=lambda: newp(),font=(15))
        b7.place(relx=0.6, rely=0.7, anchor=CENTER)

        def sol():
            global yovr,movr
            la=float(self.e1.get())
            lb=float(self.e2.get())
            a=np.array([[1,1],[la,lb]])
            b=np.array([[yovr],[movr]])
            x=np.linalg.solve(a,b)
            self.An = Label(self, text="""The solution is :\n Reaction at left support = {} N\n Reaction at right support = {} N
                                       
                \nNOTE: Human takes about 10 mins to solve such problems and computer completed it in about 0.1 secs!""".format(x[0][0],x[1][0]),font=(15))
            self.An.place(relx=0.5, rely=0.9, anchor=CENTER)
        def newp():
            global yovr, movr
            yovr, movr=0,0
            self.An.destroy()
            self.e1.delete(0, 'end')
            controller.show_frame(InputPage)
class ADDYovr(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        lo = Label(self, text="MECHwithTECH", font=("Berlin Sans FB", 40 ))
        lo.place(relx=0.5, rely=0.1, anchor=CENTER)

        l1 = Label(self, text="Magnitude:",font=(15))
        l1.place(relx=0.4, rely=0.3, anchor=CENTER)
        self.e1 = Entry(self)
        self.e1.place(relx=0.6, rely=0.3, anchor=CENTER)

        l2 = Label(self, text="Position (from left end):",font=(15))
        l2.place(relx=0.4, rely=0.4, anchor=CENTER)
        self.e2 = Entry(self)
        self.e2.place(relx=0.6, rely=0.4, anchor=CENTER)

        v = DoubleVar()
        l2 = Label(self, text="Direction : ",font=(15))
        l2.place(relx=0.4, rely=0.5, anchor=CENTER)
        self.E2 = Radiobutton(self, text="Upwards", variable=v, value="-1",font=(15))
        self.E2.place(relx=0.55, rely=0.5, anchor=W)
        self.E4 = Radiobutton(self, text="Downwards", variable=v, value="1",font=(15))
        self.E4.place(relx=0.55, rely=0.55, anchor=W)

        b = Button(self, text="Submit", command=lambda :clr(),font=(15))
        b.place(relx=0.5, rely=0.6, anchor=CENTER)

        def clr():
            global yovr
            global movr
            pos=float(self.e2.get())
            mag=float(self.e1.get())
            self.e2.delete(0,"end")
            self.e1.delete(0, "end")
            yovr+=mag*v.get()
            movr+=(mag*pos*v.get())
            controller.show_frame(OvrHng)
class ADDUDLovr(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        lo = Label(self, text="MECHwithTECH", font=("Berlin Sans FB", 40 ))
        lo.place(relx=0.5, rely=0.1, anchor=CENTER)

        l1 = Label(self, text="Magnitude:",font=(15))
        l1.place(relx=0.4, rely=0.3, anchor=CENTER)
        self.e1 = Entry(self)
        self.e1.place(relx=0.6, rely=0.3, anchor=CENTER)

        l2 = Label(self, text="Position (Of starting point from left end):",font=(15))
        l2.place(relx=0.4, rely=0.4, anchor=CENTER)
        self.e2 = Entry(self)
        self.e2.place(relx=0.6, rely=0.4, anchor=CENTER)

        l3 = Label(self, text="Length of UDL:",font=(15))
        l3.place(relx=0.4, rely=0.5, anchor=CENTER)
        self.e3 = Entry(self)
        self.e3.place(relx=0.6, rely=0.5, anchor=CENTER)

        v = DoubleVar()
        l2 = Label(self, text="DIRECTION : ",font=(15))
        l2.place(relx=0.4, rely=0.6, anchor=CENTER)
        self.E2 = Radiobutton(self, text="Upwards", variable=v, value="-1",font=(15))
        self.E2.place(relx=0.55, rely=0.6, anchor=W)
        self.E4 = Radiobutton(self, text="Downwards", variable=v, value="1",font=(15))
        self.E4.place(relx=0.55, rely=0.65, anchor=W)

        b = Button(self, text="Submit", command=lambda :clr(),font=(15))
        b.place(relx=0.5, rely=0.7, anchor=CENTER)

        def clr():
            global yovr,movr
            mag=float(self.e3.get())*float(self.e1.get())
            pos=float(self.e2.get())+float(self.e3.get())/2
            yovr+=mag
            movr+=mag*pos
            self.e1.delete(0,"end")
            self.e2.delete(0, "end")
            self.e3.delete(0, "end")
            controller.show_frame(OvrHng)


class S5(Frame):
 def __init__(self, parent, controller):
  Frame.__init__(self, parent)
  global sgmx, sgmy, sgmm,sy,sm,sy4,sam4,yovr,movr
  sgmx, sgmy, sgmm, sy, sm, sy4, sam4, yovr, movr = 0, 0, 0, 0, 0, 0, 0, 0, 0
  lo = Label(self, text="MECHwithTECH", font=("Berlin Sans FB", 40 ))
  lo.place(relx=0.5, rely=0.1, anchor=CENTER)

  l1=Label(self, text="Choose the beam type:", font=("times",25,"bold"))
  l1.place(relx=0.5, rely=0.3, anchor=CENTER)

  b2=Button(self, text="Inclined Support at left end",font=("times",15), command=lambda: controller.show_frame(ST5))
  b2.place(relx=0.35, rely=0.45, anchor=CENTER)

  b2=Button(self, text="Inclined Support at right end",font=("times",15), command=lambda: controller.show_frame(ST6))
  b2.place(relx=0.65, rely=0.45, anchor=CENTER)

class ST5(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        lo = Label(self, text="MECHwithTECH", font=("Berlin Sans FB", 40 ))
        lo.place(relx=0.5, rely=0.1, anchor=CENTER)

        l1=Label(self,text="Length of Beam:",font=(15))
        l1.place(relx=0.4, rely=0.3, anchor=CENTER)
        self.e1=Entry(self)
        self.e1.place(relx=0.6, rely=0.3, anchor=CENTER)

        l2 = Label(self, text="Inclination of Left support (0-90):",font=(15))
        l2.place(relx=0.4, rely=0.4, anchor=CENTER)
        self.e2 = Entry(self)
        self.e2.place(relx=0.6, rely=0.4, anchor=CENTER)

        b1=Button(self, text="Add Force along Y-axis",width=20, command=lambda :controller.show_frame(ADDYst5),font=(15))
        b1.place(relx=0.4, rely=0.5, anchor=CENTER)

        b2 = Button(self, text="Add Force along X-axis",width=20, command=lambda :controller.show_frame(ADDXst5),font=(15))
        b2.place(relx=0.6, rely=0.5, anchor=CENTER)

        b3 = Button(self, text="Add Oblique Force",width=20, command=lambda :controller.show_frame(ADDOBst5),font=(15))
        b3.place(relx=0.4, rely=0.6, anchor=CENTER)

        b4 = Button(self, text="Add Uniformly Distributed Load", command=lambda :controller.show_frame(ADDUDLst5),font=(15))
        b4.place(relx=0.6, rely=0.6, anchor=CENTER)

        b6=Button(self, text="Solve!", command=lambda : sol(),font=(15))
        b6.place(relx=0.4, rely=0.7, anchor=CENTER)

        b7=Button(self, text="New Problem", command=lambda :newp(),font=(15))
        b7.place(relx=0.6, rely=0.7, anchor=CENTER)

        def sol():
            global x5,y5,m5
            len=float(self.e1.get())
            a=float(self.e2.get())
            a=90-a
            ra=m5/(math.sin(math.radians(a))*len)
            rbx=y5-ra*math.sin(math.radians(a))
            rby=x5+ra*math.cos(math.radians(a))
            if rbx==0:
                rb=rby
                ra=round(ra,2)
                rb=round(rb, 2)
                self.An = Label(self, text="""The solution is :\n Reaction at A={} N\n Reaction at B={} N perpendicularly upwards to Beam
                
                
                \nNOTE: Human takes about 10 mins to solve such problems and computer completed it in about 0.1 secs!""".format(ra,rb),font=(15))
                self.An.place(relx=0.5, rely=0.9, anchor=CENTER)
            else:
                th=90-math.degrees(math.atan(abs(rby)/abs(rbx)))
                rb = math.sqrt(rbx ** 2 + rby ** 2)
                self.An = Label(self, text="""The solution is :\n Reaction at A={} N\n Reaction at B={} N, inclined at {} degrees to +X-axis
                                           
                \nNOTE: Human takes about 10 mins to solve such problems and computer completed it in about 0.1 secs!""".format(ra,rb,th),font=(15))
                self.An.place(relx=0.5, rely=0.9, anchor=CENTER)
        def newp():
            global x5, y5, m5
            x5, y5, m5 = 0, 0, 0
            self.An.destroy()
            self.e1.delete(0, 'end')
            self.e2.delete(0, 'end')
            controller.show_frame(InputPage)
class ADDXst5(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        lo = Label(self, text="MECHwithTECH", font=("Berlin Sans FB", 40 ))
        lo.place(relx=0.5, rely=0.1, anchor=CENTER)

        l1 = Label(self, text="Magnitude:",font=(15))
        l1.place(relx=0.4, rely=0.3, anchor=CENTER)
        self.e1 = Entry(self)
        self.e1.place(relx=0.6, rely=0.3, anchor=CENTER)

        v = DoubleVar()
        l2 = Label(self, text="DIRECTION : ",font=(15))
        l2.place(relx=0.4, rely=0.4, anchor=CENTER)
        self.E2 = Radiobutton(self, text="Towards Left", variable=v, value="-1",font=(15))
        self.E2.place(relx=0.55, rely=0.4, anchor=W)
        self.E4 = Radiobutton(self, text="Towards Right", variable=v, value="1",font=(15))
        self.E4.place(relx=0.55, rely=0.45, anchor=W)

        b = Button(self, text="Submit", command=lambda :clr(),font=(15))
        b.place(relx=0.5, rely=0.6, anchor=CENTER)

        def clr():
            global x5
            mag=float(self.e1.get())
            x5+=mag*v.get()
            self.e1.delete(0, 'end')
            controller.show_frame(ST5)
class ADDYst5(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        lo = Label(self, text="MECHwithTECH", font=("Berlin Sans FB", 40 ))
        lo.place(relx=0.5, rely=0.1, anchor=CENTER)

        l1 = Label(self, text="Magnitude:",font=(15))
        l1.place(relx=0.4, rely=0.3, anchor=CENTER)
        self.e1 = Entry(self)
        self.e1.place(relx=0.6, rely=0.3, anchor=CENTER)

        l2 = Label(self, text="Position (from RIGHT end):",font=(15))
        l2.place(relx=0.4, rely=0.4, anchor=CENTER)
        self.e2 = Entry(self)
        self.e2.place(relx=0.6, rely=0.4, anchor=CENTER)

        v = DoubleVar()
        l2 = Label(self, text="DIRECTION : ",font=(15))
        l2.place(relx=0.4, rely=0.5, anchor=CENTER)
        self.E2 = Radiobutton(self, text="Upwards", variable=v, value="-1",font=(15))
        self.E2.place(relx=0.55, rely=0.5, anchor=W)
        self.E4 = Radiobutton(self, text="Downwards", variable=v, value="1",font=(15))
        self.E4.place(relx=0.55, rely=0.55, anchor=W)

        b = Button(self, text="Submit", command=lambda :clr5(),font=(15))
        b.place(relx=0.5, rely=0.6, anchor=CENTER)

        def clr5():
            global y5,m5
            pos=float(self.e2.get())
            mag=float(self.e1.get())
            self.e2.delete(0,"end")
            self.e1.delete(0, "end")
            y5+=mag*v.get()
            m5+=(mag*pos*v.get())
            controller.show_frame(ST5)
class ADDUDLst5(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        lo = Label(self, text="MECHwithTECH", font=("Berlin Sans FB", 40 ))
        lo.place(relx=0.5, rely=0.1, anchor=CENTER)

        l1 = Label(self, text="Magnitude:", font=(15))
        l1.place(relx=0.4, rely=0.3, anchor=CENTER)
        self.e1 = Entry(self)
        self.e1.place(relx=0.6, rely=0.3, anchor=CENTER)

        l2 = Label(self, text="Position (Of starting point from left end):", font=(15))
        l2.place(relx=0.4, rely=0.4, anchor=CENTER)
        self.e2 = Entry(self)
        self.e2.place(relx=0.6, rely=0.4, anchor=CENTER)

        l3 = Label(self, text="Length of UDL:", font=(15))
        l3.place(relx=0.4, rely=0.5, anchor=CENTER)
        self.e3 = Entry(self)
        self.e3.place(relx=0.6, rely=0.5, anchor=CENTER)

        v = DoubleVar()
        l2 = Label(self, text="DIRECTION : ", font=(15))
        l2.place(relx=0.4, rely=0.6, anchor=CENTER)
        self.E2 = Radiobutton(self, text="Upwards", variable=v, value="-1", font=(15))
        self.E2.place(relx=0.55, rely=0.6, anchor=W)
        self.E4 = Radiobutton(self, text="Downwards", variable=v, value="1", font=(15))
        self.E4.place(relx=0.55, rely=0.65, anchor=W)

        b = Button(self, text="Submit", command=lambda :clr(), font=(15))
        b.place(relx=0.5, rely=0.7, anchor=CENTER)

        def clr():
            global y5,m5
            mag=float(self.e3.get())*float(self.e1.get())*v.get()
            pos=float(self.e2.get())+float(self.e3.get())/2
            y5+=mag
            m5+=(mag*pos)
            self.e1.delete(0,"end")
            self.e2.delete(0, "end")
            self.e3.delete(0, "end")
            controller.show_frame(ST5)
class ADDOBst5(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        lo = Label(self, text="MECHwithTECH", font=("Berlin Sans FB", 40 ))
        lo.place(relx=0.5, rely=0.1, anchor=CENTER)

        l1 = Label(self, text="Magnitude:",font=(15))
        l1.place(relx=0.4, rely=0.3, anchor=CENTER)
        self.e1 = Entry(self)
        self.e1.place(relx=0.6, rely=0.3, anchor=CENTER)

        l2 = Label(self, text="Position:",font=(15))
        l2.place(relx=0.4, rely=0.4, anchor=CENTER)
        self.e2 = Entry(self)
        self.e2.place(relx=0.6, rely=0.4, anchor=CENTER)

        l3 = Label(self, text="Angle with positive X axis (0-360 degrees):",font=(15))
        l3.place(relx=0.4, rely=0.5, anchor=CENTER)
        self.e3 = Entry(self)
        self.e3.place(relx=0.6, rely=0.5, anchor=CENTER)

        b = Button(self, text="Submit", command=lambda :clr(),font=(15))
        b.place(relx=0.5, rely=0.6, anchor=CENTER)
        def clr():
            global x5,y5,m5
            a=float(self.e3.get())
            mag=float(self.e1.get())
            fx, fy=0,0
            if 0<=a<90 or a==360:
                fx=mag*math.cos(math.radians(a))
                fy = mag * math.sin(math.radians(a))
                fy*=(-1)
            elif 90<a<180:
                a%=90
                fx = mag * math.sin(math.radians(a))
                fy = mag * math.cos(math.radians(a))
                fx*=(-1)
                fy *= (-1)
            elif 180<a<270:
                a%=90
                fx = mag*math.cos(math.radians(a))
                fy = mag * math.sin(math.radians(a))
                fx*=(-1)
            elif 270<a<=360:
                a%=90
                fx = mag * math.sin(math.radians(a))
                fy = mag * math.cos(math.radians(a))
            elif a==90:
                fx=0
                fy=(-1*mag)
            elif a==180:
                fx=(-1*mag)
                fy=0
            elif a==270:
                fx=0
                fy=mag
            y5+=fy
            x5+=fx
            m5+=fy*float(self.e2.get())
            controller.show_frame(ST5)

class ST6(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        lo = Label(self, text="MECHwithTECH", font=("Berlin Sans FB", 40 ))
        lo.place(relx=0.5, rely=0.1, anchor=CENTER)

        l1=Label(self,text="Length of Beam:", font=(15))
        l1.place(relx=0.4, rely=0.3, anchor=CENTER)
        self.e1=Entry(self)
        self.e1.place(relx=0.6, rely=0.3, anchor=CENTER)

        l2 = Label(self, text="Inclination of Right support (0-90):", font=(15))
        l2.place(relx=0.4, rely=0.4, anchor=CENTER)
        self.e2 = Entry(self)
        self.e2.place(relx=0.6, rely=0.4, anchor=CENTER)

        b1=Button(self, text="Add Force along Y-axis",width=20, command=lambda :controller.show_frame(ADDYst6), font=(15))
        b1.place(relx=0.4, rely=0.5, anchor=CENTER)

        b2 = Button(self, text="Add Force along X-axis",width=20, command=lambda :controller.show_frame(ADDXst6), font=(15))
        b2.place(relx=0.6, rely=0.5, anchor=CENTER)

        b3 = Button(self, text="Add Oblique Force",width=20, command=lambda :controller.show_frame(ADDOBst6), font=(15))
        b3.place(relx=0.4, rely=0.6, anchor=CENTER)

        b4 = Button(self, text="Add Uniformly Distributed Load", command=lambda :controller.show_frame(ADDUDLst6), font=(15))
        b4.place(relx=0.6, rely=0.6, anchor=CENTER)

        b6=Button(self, text="Solve!", command=lambda : sol(), font=(15))
        b6.place(relx=0.4, rely=0.7, anchor=CENTER)

        b7=Button(self, text="New Problem", command=lambda :newp(), font=(15))
        b7.place(relx=0.6, rely=0.7, anchor=CENTER)

        def sol():
            global x6,y6,m6
            len=float(self.e1.get())
            a=float(self.e2.get())
            a=90-a
            rb=m6/(math.sin(math.radians(a))*len)
            rax=rb*math.cos(math.radians(a))-x6
            ray=y6-rb*math.sin(math.radians(a))
            if rax==0:
                ra=ray
                ra=round(ra,2)
                rb=round(rb, 2)
                self.An = Label(self, text="""The solution is :\n Reaction at A={} N perpendicularly upwards to Beam\n Reaction at B={} N
                
                \nNOTE: Human takes about 10 mins to solve such problems and computer completed it in about 0.1 secs!
                """.format(ra,rb), font=(15))
                self.An.place(relx=0.5, rely=0.9, anchor=CENTER)
            else:
                th=math.degrees(math.atan(abs(ray)/abs(rax)))
                ra = math.sqrt(rax ** 2 + ray ** 2)
                self.An = Label(self, text="""The solution is :\n Reaction at A={} N, inclined at {} degrees to +X-axis\n Reaction at B={} N
                
                \nNOTE: Human takes about 10 mins to solve such problems and computer completed it in about 0.1 secs!""".format(ra,th,rb), font=(15))
                self.An.place(relx=0.5, rely=0.9, anchor=CENTER)
        def newp():
            global x6, y6, m6
            x6, y6, m6 = 0, 0, 0
            self.An.destroy()
            self.e1.delete(0, 'end')
            self.e2.delete(0, 'end')
            controller.show_frame(InputPage)
class ADDXst6(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        lo = Label(self, text="MECHwithTECH", font=("Berlin Sans FB", 40 ))
        lo.place(relx=0.5, rely=0.1, anchor=CENTER)

        l1 = Label(self, text="Magnitude:",font=(15))
        l1.place(relx=0.4, rely=0.3, anchor=CENTER)
        self.e1 = Entry(self)
        self.e1.place(relx=0.6, rely=0.3, anchor=CENTER)

        v = DoubleVar()
        l2 = Label(self, text="DIRECTION : ",font=(15))
        l2.place(relx=0.4, rely=0.4, anchor=CENTER)
        self.E2 = Radiobutton(self, text="Towards Left", variable=v, value="-1",font=(15))
        self.E2.place(relx=0.55, rely=0.4, anchor=W)
        self.E4 = Radiobutton(self, text="Towards Right", variable=v, value="1",font=(15))
        self.E4.place(relx=0.55, rely=0.45, anchor=W)

        b = Button(self, text="Submit", command=lambda :clr(),font=(15))
        b.place(relx=0.5, rely=0.5, anchor=CENTER)

        def clr():
            global x6
            mag=float(self.e1.get())
            x6+=mag*v.get()
            self.e1.delete(0, 'end')
            controller.show_frame(ST6)
class ADDYst6(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        lo = Label(self, text="MECHwithTECH", font=("Berlin Sans FB", 40 ))
        lo.place(relx=0.5, rely=0.1, anchor=CENTER)

        l1 = Label(self, text="Magnitude:",font=(15))
        l1.place(relx=0.4, rely=0.3, anchor=CENTER)
        self.e1 = Entry(self)
        self.e1.place(relx=0.6, rely=0.3, anchor=CENTER)

        l2 = Label(self, text="Position (from left end):",font=(15))
        l2.place(relx=0.4, rely=0.4, anchor=CENTER)
        self.e2 = Entry(self)
        self.e2.place(relx=0.6, rely=0.4, anchor=CENTER)

        v = DoubleVar()
        l2 = Label(self, text="DIRECTION : ",font=(15))
        l2.place(relx=0.4, rely=0.5, anchor=CENTER)
        self.E2 = Radiobutton(self, text="Upwards", variable=v, value="-1",font=(15))
        self.E2.place(relx=0.55, rely=0.5, anchor=W)
        self.E4 = Radiobutton(self, text="Downwards", variable=v, value="1",font=(15))
        self.E4.place(relx=0.55, rely=0.55, anchor=W)

        b = Button(self, text="Submit", command=lambda :clr5(),font=(15))
        b.place(relx=0.5, rely=0.6, anchor=CENTER)

        def clr5():
            global y6,m6
            pos=float(self.e2.get())
            mag=float(self.e1.get())
            self.e2.delete(0,"end")
            self.e1.delete(0, "end")
            y6+=mag*v.get()
            m6+=(mag*pos*v.get())
            controller.show_frame(ST6)
class ADDUDLst6(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        lo = Label(self, text="MECHwithTECH", font=("Berlin Sans FB", 40 ))
        lo.place(relx=0.5, rely=0.1, anchor=CENTER)

        l1 = Label(self, text="Magnitude:",font=(15))
        l1.place(relx=0.4, rely=0.3, anchor=CENTER)
        self.e1 = Entry(self)
        self.e1.place(relx=0.6, rely=0.3, anchor=CENTER)

        l2 = Label(self, text="Position (Of starting point from left end):",font=(15))
        l2.place(relx=0.4, rely=0.4, anchor=CENTER)
        self.e2 = Entry(self)
        self.e2.place(relx=0.6, rely=0.4, anchor=CENTER)

        l3 = Label(self, text="Length of UDL:",font=(15))
        l3.place(relx=0.4, rely=0.5, anchor=CENTER)
        self.e3 = Entry(self)
        self.e3.place(relx=0.6, rely=0.5, anchor=CENTER)

        v = DoubleVar()
        l2 = Label(self, text="DIRECTION : ",font=(15))
        l2.place(relx=0.4, rely=0.6, anchor=CENTER)
        self.E2 = Radiobutton(self, text="Upwards", variable=v, value="-1",font=(15))
        self.E2.place(relx=0.55, rely=0.6, anchor=W)
        self.E4 = Radiobutton(self, text="Downwards", variable=v, value="1",font=(15))
        self.E4.place(relx=0.55, rely=0.65, anchor=W)

        b = Button(self, text="Submit", command=lambda :clr(),font=(15))
        b.place(relx=0.5, rely=0.7, anchor=CENTER)

        def clr():
            global y6,m6
            mag=float(self.e3.get())*float(self.e1.get())*v.get()
            pos=float(self.e2.get())+float(self.e3.get())/2
            y6+=mag
            m6+=(mag*pos)
            self.e1.delete(0,"end")
            self.e2.delete(0, "end")
            self.e3.delete(0, "end")
            controller.show_frame(ST6)
class ADDOBst6(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        lo = Label(self, text="MECHwithTECH", font=("Berlin Sans FB", 40 ))
        lo.place(relx=0.5, rely=0.1, anchor=CENTER)

        l1 = Label(self, text="Magnitude:",font=(15))
        l1.place(relx=0.4, rely=0.3, anchor=CENTER)
        self.e1 = Entry(self)
        self.e1.place(relx=0.6, rely=0.3, anchor=CENTER)

        l2 = Label(self, text="Position:",font=(15))
        l2.place(relx=0.4, rely=0.4, anchor=CENTER)
        self.e2 = Entry(self)
        self.e2.place(relx=0.6, rely=0.4, anchor=CENTER)

        l3 = Label(self, text="Angle with positive X axis (0-360 degrees):",font=(15))
        l3.place(relx=0.4, rely=0.5, anchor=CENTER)
        self.e3 = Entry(self)
        self.e3.place(relx=0.6, rely=0.5, anchor=CENTER)

        b = Button(self, text="Submit", command=lambda :clr(),font=(15))
        b.place(relx=0.5, rely=0.6, anchor=CENTER)
        def clr():
            global x6,y6,m6
            a=float(self.e3.get())
            mag=float(self.e1.get())
            fx, fy=0,0
            if 0<=a<90 or a==360:
                fx=mag*math.cos(math.radians(a))
                fy = mag * math.sin(math.radians(a))
                fy*=(-1)
            elif 90<a<180:
                a%=90
                fx = mag * math.sin(math.radians(a))
                fy = mag * math.cos(math.radians(a))
                fx*=(-1)
                fy *= (-1)
            elif 180<a<270:
                a%=90
                fx = mag*math.cos(math.radians(a))
                fy = mag * math.sin(math.radians(a))
                fx*=(-1)
            elif 270<a<=360:
                a%=90
                fx = mag * math.sin(math.radians(a))
                fy = mag * math.cos(math.radians(a))
            elif a==90:
                fx=0
                fy=(-1*mag)
            elif a==180:
                fx=(-1*mag)
                fy=0
            elif a==270:
                fx=0
                fy=mag
            y6+=fy
            x6+=fx
            m6+=fy*float(self.e2.get())
            controller.show_frame(ST6)

class RDme(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        lo = Label(self, text="MECHwithTECH", font=("Berlin Sans FB", 40 ))
        lo.place(relx=0.5, rely=0.1, anchor=CENTER)

        lo = Label(self, text="""1. ALL FORCES ARE IN NEWTON.\n
2. DISTANCES ARE MEASURED IN METRES.\n
3. ANGLE RANGE : 0-360 w.r.t positive x-axis.\n
4. ALL DISTANCES  ARE MEASURED FROM LEFT SIDE UNLESS SPECIFIED*\n
5. PUSH TYPE OF FORCE MUST BE CONVERTED INTO PULL TYPE FOR CORRECT ANGLE INPUT.\n
   E.g A PUSH-type force is inclined at 30 degrees in the 1st quadrant. Therefore 210 degrees in 3rd quadrant (PULL force)
       this should be the input angle.\n
6. All ANGLES ARE MEASURED IN DEGREES.\n
7. "New Problem" BUTTON WORKS ONLY WHEN ONCE A PROBLEM IS SOLVED.\n""",justify=LEFT)
        lo.place(relx=0.5, rely=0.4, anchor=CENTER)
        
        b = Button(self, text="Back", command=lambda :controller.show_frame(WelcomePage))
        b.place(relx=0.5, rely=0.7, anchor=CENTER)



app=mechproj()
app.wm_state('zoomed')
#app.attributes('-fullscreen', True)
app.mainloop()

