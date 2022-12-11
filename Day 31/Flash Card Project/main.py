from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
learn_data = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    learn_data = original_data.to_dict(orient="records")
else:
    learn_data = data.to_dict(orient="records")

# -----------------------------------Creating New Cards with french names ------------------------


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(learn_data)
    canvas.itemconfig(card_title, text="French", fill="Black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="Black")
    canvas.itemconfig(background_img, image=front_img)
    flip_timer = window.after(3000, func=flip)


def flip():
    canvas.itemconfig(background_img, image=back_img)
    canvas.itemconfig(card_title, text="English", fill="White")
    canvas.itemconfig(card_word, text=current_card["English"], fill="White")


def known():
    learn_data.remove(current_card)
    data_known = pandas.DataFrame(learn_data)
    data_known.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip)


# ------------------------------------UI-------------------------------------------

canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
background_img = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 40, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right = PhotoImage(file="images/right.png")
right_button = Button(image=right, highlightthickness=0, command=known)
right_button.grid(row=1, column=1)

next_card()
window.mainloop()
