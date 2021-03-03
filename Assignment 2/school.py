from tkinter import *
from tkinter import messagebox
import numbers 


window = Tk()

#CONFIGURE THE WINDOW
window.title("Your Grade")
window.geometry('250x100')

#label
label1 = Label(window, text="Enter a grade between 0 - 100")

label1.grid(column=0,row=1)

grade = Entry(window, width=10)
grade.grid(column=0,row=0)
grade.focus

        


def hasClicked():
    try:
        if grade.get() == "A":
           msg = "Grade = 85 - 100 " 
        elif grade.get() == "B":
           msg = "Grade = 75 - 84.99 " 
        elif grade.get() == "C":
           msg = "Grade = 60 - 74.99 " 
        elif grade.get() == "F":
           msg = "Grade = 0 - 59.99 "     
        elif int(grade.get()) >= 85 and int(grade.get()) <= 100:
                msg = "A"        
        elif int(grade.get()) >=75 and int(grade.get()) <= 84.99:
                msg = "B"
        elif int(grade.get()) >=60 and int(grade.get()) <= 74.99:
                msg = "C"
        elif int(grade.get()) >=0 and int(grade.get()) <= 59.99:
                msg = "F"
        elif int(grade.get()) >= 100.1 or int(grade.get()) <=-1:
                msg = "Out of Bounds" 
                
        
        
    except ValueError:
            msg = "ERROR: Invalid Input"
        


    label1.configure(text= msg)

btn = Button(window, text="Submit", command=hasClicked)
btn.grid(column=1, row=0)

#LAUNCH THE WINDOW
window.mainloop()