BACKGROUND_COLOR = "#B1DDC6"

from cgitb import text
import random
from textwrap import fill
from tkinter import *
import pandas

current_card={}
with open("french_words.csv", 'r') as data_file:
    data=pandas.read_csv(data_file)
    list_french= data.to_dict(orient="records")
# ---------------------------- CHANGE WORD ------------------------------- #

def know_word():
    list_french.remove(current_card)
    final_list=pandas.DataFrame(list_french)
    final_list.to_csv("french_words.csv")
    change_word()

def change_word():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image=card_front_img)
    current_card=random.choice(list_french)
    canvas.itemconfig(word_text, text=current_card["French"],fill="black")
    canvas.itemconfig(title_text, text="French",fill="black")
    flip_timer=window.after(3000,flip_card)

# ---------------------------- FLIP CARD ------------------------------- #
def flip_card():
    global current_card
    canvas.itemconfig(title_text, text="English",fill='white')
    canvas.itemconfig(word_text,text=f"{current_card['English']}",fill='white')
    canvas.itemconfig(canvas_image, image=card_back_img)


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.configure(padx=60,pady=60, bg=BACKGROUND_COLOR)
window.title("FLASH_CARDS")


canvas=Canvas(height=520,width=800,highlightthickness=0,bg=BACKGROUND_COLOR)
card_front_img= PhotoImage(file="images/card_front.png")
card_back_img= PhotoImage(file="images/card_back.png")
canvas_image=canvas.create_image(400,260, image=card_front_img)
canvas.grid(row= 0,column=0,columnspan=2,pady=40)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0,command=know_word)
right_button.grid(row=1,column=0)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0,command=change_word)
wrong_button.grid(row=1,column=1)

title_text=canvas.create_text(400, 130, text="French", font=('Arial', 35, "italic"))
word_text=canvas.create_text(400, 280, text="Word", font=('Arial',50, "bold"))
flip_timer=window.after(3000,flip_card)
change_word()
window.mainloop()