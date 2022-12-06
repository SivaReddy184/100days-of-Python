from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)  # used to free out space around it

# Todo Label

my_label = Label(text="My first label", font=("Arial", 24, "bold"))
my_label.grid(row=0, column=0)  # https://docs.python.org/3/library/tkinter.html#the-packer
my_label["text"] = "New Text"  # line 12 and 13 gives same results
# my_label.config(text="New Text")
my_label.config(padx=50, pady=50)  # can also use for separate elements other than using for screen window


# Todo Button


def button_clicked():
    print("I am clicked")
    # my_label.config(text="Button got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(row=1, column=1)  # grid visualises in rows and columns also we cant use pack and grid in same program
# button.place(x=0, y=0)  # place takes x and y values and put the function in certain positions map

# New button
button_2 = Button(text="button 2")
button_2.grid(row=0, column=2)
# Todo Entry

input = Entry(width=10)
input.grid(row=2, column=3)

window.mainloop()
