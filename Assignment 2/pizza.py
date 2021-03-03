#combobox / selectbox

from tkinter import *
from tkinter import ttk
from tkinter import messagebox


window = Tk()

#CONFIGURE THE WINDOW
window.title("Hyper-Futuristic Custom Pizza Selection System")
window.geometry('500x500')

#label
label1 = Label(window, text="Please click this button")
label1.grid(column=0, row=2)

total = float

#tupple 
size = ("Choose Pizza Size","Extra-Large","Large","Medium","Small")
select1 = ttk.Combobox(window, value=size, width=20)
select1.current(0)
select1.grid(column=0, row=0)

toppings = ("Chesse", "Mushrooms","Green Peppers","Sausage","Bacon","Pineapple")
select2 = ttk.Combobox(window, value=toppings, width=20)
select2.current(0)
select2.grid(column=1, row=0)

#button function
def hasClicked():
    msg= select1.get()
    msg= select2.get()

    
    if select1.get() == "Extra-Large":
        total = 17.50
    elif select1.get() == "Large":
        total = 15.00
    elif select1.get() == "Medium":
        total = 12.50
    elif select1.get() == "Small":
        total = 9.00

    if select2.get() == "Pineapple":
        total = total + 1
    elif select2.get() == "Mushrooms":
        total = total + 1
    elif select2.get() == "Sausage":
        total = total + 1
    elif select2.get() == "Bacon":
        total = total + 1
    elif select2.get() == "Green Peppers":
        total = total + 1
    elif select2.get() == "Cheese":
        total = total + 1

    msg= "You have selected: " + select1.get() + " Pizza " + "With " + select2.get() + " Your Total is: " + str(total)
    messagebox.showinfo('Results', msg)

    label1.configure(text= msg)


#button
btn = Button(window, text="Submit", command=hasClicked)
btn.grid(column=0, row=3)


#LAUNCH THE WINDOW
window.mainloop()