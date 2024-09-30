from tkinter import *
from tkinter import messagebox
import time
xval = 700
yval = 500
#data
goal1 = open("goal1.py", "r")
goal2 = open("goal2.py", "r")
goal3 = open("goal3.py", "r")
goal4 = open("goal4.py", "r")
goal5 = open("goal5.py", "r")
helping = open("helping.py", "r")

colorpet = open("colourpet.py", "r")

namepet = open("namepet.py", "r")
nameuser = open("nameuser.py", "r")
#data end

def startpro():
    def move():
        global xval
        if xval <= -700:
            def moveframe():
                global yval
                if yval <= 250:
                    print("also end animation")
                    if nameuser.read() == "":
                        def namesave():
                            nameuser = open("nameuser.py", "w")
                            nameusertemp = nameenter.get()
                            if nameusertemp == "":
                                messagebox.showwarning(title="data missing",message="there are some data missing.")
                            else:
                                def petnamesave():
                                    namepet = open("nameuser.py", "w")
                                    colorpet = open("colourpet.py", "w")
                                    colorpettemp = colorenter.get()
                                    namepettemp = anameenter.get()
                                    
                                nameuser.write(nameusertemp)
                                signtext.destroy()
                                nameenter.destroy()
                                namebutton.destroy()
                                asigntext = Label(window, text="You get a penguin when you join!", font=("Arial", 40), bg="white", fg="black")
                                asigntext.pack()
                                asigntext.place(x=0, y=90)
                                asigntext = Label(window, text="The pet's name:", font=("Arial", 20), bg="blue", fg="white")
                                asigntext.pack()
                                asigntext.place(x=0, y=250)
                                colortext = Label(window, text="The pet's color:", font=("Arial", 20), bg="blue", fg="white")
                                colortext.pack()
                                colortext.place(x=0, y=300)
                                acolortext = Label(window, text="colors avalible: green, blue, yellow", font=("Arial", 20), bg="blue", fg="white")
                                acolortext.pack()
                                acolortext.place(x=0, y=330)
                                anameenter = Entry(window, font=("Arial", 20), bg="black", fg="white")
                                anameenter.pack()
                                anameenter.place(x=130, y=260)
                                colorenter = Entry(window, font=("Arial", 20), bg="black", fg="white")
                                colorenter.pack()
                                colorenter.place(x=130, y=300)
                                
                                anamebutton = Button(window, font=("Arial", 30), bg="blue", fg="black", command=petnamesave,text="Confirm")
                                anamebutton.pack()
                                anamebutton.place(x=200, y=300)
                            
                        window.title("Sign up")
                        signtext = Label(window, text="Sign up!", font=("Arial", 90), bg="white", fg="black")
                        signtext.pack()
                        signtext.place(x=0, y=0)
                        signtext = Label(window, text="Your name:", font=("Arial", 20), bg="blue", fg="white")
                        signtext.pack()
                        signtext.place(x=0, y=250)
                        nameenter = Entry(window, font=("Arial", 20), bg="black", fg="white")
                        nameenter.pack()
                        nameenter.place(x=130, y=260)
                        namebutton = Button(window, font=("Arial", 30), bg="blue", fg="black", command=namesave,text="Confirm")
                        namebutton.pack()
                        namebutton.place(x=200, y=300)
                        
                    else:
                        window.title("Pangie")
                        signtext = Label(window, text="Pangie.", font=("Arial", 90), bg="white", fg="black")
                        signtext.pack()
                        signtext.place(x=0, y=0)
                else:
                    yval = yval - 1
                    frame.place(x=0, y=yval)
                    frame.after(1, moveframe)
            print("end animation")
            logo.destroy()
            frame = Frame(window, width=700, height=250, bg="blue")
            frame.pack()
            frame.place(x=0, y=500)
            moveframe()
        else:
            xval = xval - 1
            logo.place(x=xval, y=160)
            logo.after(1, move)
    start.destroy()
    window = Tk()
    window.config(bg="white")
    window.geometry("700x500")
    window.resizable(False, False)
    logo = Label(window, text="willy borgor studio", fg="black", bg="white", font=("Lucida Console", 90))
    logo.pack()
    logo.place(x=-700, y=160)
    move()
    window.mainloop()
def quitpro():
    start.destroy()
start = Tk()
start.geometry("400x200")
start.title("Start program?")
start.config(bg="white")
start.resizable(False, False)
starttext = Label(start, text="Do you want to boot up Pangi?", font=("Arial", 20), fg="black", bg="white")
startbutton = Button(start, command=startpro, text="Boot", font=("Arial", 20), fg="black", bg="blue")
endbutton = Button(start, command=quitpro, text="Quit", font=("Arial", 20), fg="black", bg="white")

starttext.pack()
startbutton.pack()
startbutton.place(x=85, y=100)
endbutton.pack()
endbutton.place(x=250, y=100)

