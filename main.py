from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
#---------------------------- READING CSV ----------------------------------#
# data = pandas.read_csv("Day31-FlashCardApp/data/french_words.csv")
data_dict = {}
new_word = {}

# print(random.choice(data_dict)["French"])
# print(data_dict[len(data_dict)-1]["French"])
# Multiple ways of doing this, but teacher recommended the orient way above
# For documentation of above, https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html
# print(data["French"].values)
# print(data["English"].values)

try:
    file = pandas.read_csv("Day31-FlashCardApp/data/words_to_learn.csv")       # if words_to_learn.csv doesn't exist, then it will go to the 'except' code block and make words_to_learn.csv
except FileNotFoundError:
    original = pandas.read_csv("Day31-FlashCardApp/data/japanese_characters.csv")
    data_dict = original.to_dict(orient="records")
    new_word = random.choice(data_dict)
else:
    # this will execute if the all of the 'try' code block succeeds
    data_dict = file.to_dict(orient="records")
    new_word = random.choice(data_dict)
#---------------------------- BUTTONS --------------------------------------#
def incorrect():
    global new_word, flip_timer
    window.after_cancel(flip_timer)
    new_word = random.choice(data_dict)
    canvas.itemconfig(card, image=card_front)
    canvas.itemconfig(language, text="Character", fill="black")
    canvas.itemconfig(word, text=new_word["Character"], fill="black")
    flip_timer = window.after(3000, flip_card)
def correct():
    global new_word, flip_timer
    window.after_cancel(flip_timer)
    new_word = random.choice(data_dict)
    canvas.itemconfig(card, image=card_front)
    canvas.itemconfig(language, text="Character", fill="black")
    canvas.itemconfig(word, text=new_word["Character"], fill="black")
    flip_timer = window.after(3000, flip_card)
    data_dict.remove(new_word)
    data = pandas.DataFrame(data_dict)
    data.to_csv("Day31-FlashCardApp/data/words_to_learn.csv", index=False)

def flip_card():
    canvas.itemconfig(card, image=card_back)
    canvas.itemconfig(language, text="Prounounciation", fill="white")
    canvas.itemconfig(word, text=new_word["Prounounciation"], fill="white")


#---------------------------- UI SETUP -------------------------------------#
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

#### ADDING IMAGES ######
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
wrong_img = PhotoImage(file="Day31-FlashCardApp/images/wrong.png")
right_img = PhotoImage(file="Day31-FlashCardApp/images/right.png")
card_front = PhotoImage(file="Day31-FlashCardApp/images/card_front.png")
card_back = PhotoImage(file="Day31-FlashCardApp/images/card_back.png")
card = canvas.create_image(400, 263, image=card_front)
language = canvas.create_text(400, 150, text="Character", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text=new_word["Character"], font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

#### ADDING IMAGES TO BUTTONS #########
wrong_button = Button(image=wrong_img, highlightthickness=0, command=incorrect)
wrong_button.grid(row=1, column=0)
right_button = Button(image=right_img, highlightthickness=0, command=correct)
right_button.grid(row=1, column=1)


window.mainloop()