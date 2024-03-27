BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random

try:
    words_csv = pandas.read_csv("data/words_to_learn.csv")
except:
    words_csv = pandas.read_csv("data/french_words.csv")

words_dict = words_csv.to_dict(orient="records")
current_card = {}

def flip_card():
    canvas.itemconfig(background, image=back_card_img)
    canvas.itemconfig(language, text="English")
    canvas.itemconfig(word, text=current_card["English"])


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_dict)
    canvas.itemconfig(background, image=front_card_img)
    canvas.itemconfig(language, text="French")
    canvas.itemconfig(word, text=current_card["French"])
    flip_timer = window.after(3000, flip_card)

def remove_card():
    words_dict.remove(current_card)
    data = pandas.DataFrame(words_dict)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()

window = Tk()
window.title("Flash Card")
window.config(pady=50, padx=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_img = PhotoImage(file="images/card_front.png")
back_card_img = PhotoImage(file="images/card_back.png")
background = canvas.create_image(400, 263, image=front_card_img)
language = canvas.create_text(400,100,font=("arial",40,"italic"))
word = canvas.create_text(400,263,font=("arial",60,"bold"))
canvas.grid(column=0, row=0, columnspan=2)

img_right = PhotoImage(file="images/right.png")
right_button = Button(image=img_right, highlightthickness=0, command=remove_card)
right_button.grid(column=1, row=1)

img_wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=img_wrong,highlightthickness=0,command=next_card)
wrong_button.grid(column=0, row=1)

next_card()


window.mainloop()