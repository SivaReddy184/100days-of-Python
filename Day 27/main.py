from tkinter import *

window = Tk()
window.title("Miles to KM")
window.minsize(height=100, width=200)
window.config(padx=20, pady=20)

miles = Entry(width=10)
miles.focus()
miles.grid(row=0, column=1)

label1 = Label(text="Miles")
label1.grid(row=0, column=2)

label2 = Label(text="is equal to")
label2.grid(row=1, column=0)

km_label = Label(text="0")
km_label.grid(row=1, column=1)


def calculate():
    miles_count = miles.get()
    km = round(float(miles_count) * 1.609344)
    km_label.config(text=km)


label3 = Label(text="KM")
label3.grid(row=1, column=2)

button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)

window.mainloop()
