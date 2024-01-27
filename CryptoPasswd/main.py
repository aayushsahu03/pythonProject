from tkinter import *
from pathlib import Path
THEME_COLOR = "#FFF"
import sys
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
class PassInterface:

    def __init__(self):
        """

        :return:
        """
        self.window = Tk()
        self.window.title("Cryptic Password Utility")
        self.window.config(padx=20, pady=20)
        self.canvas = Canvas(width=200, height=200, bg='white')
        # self.question_text = self.canvas.create_text(150,125,
        #                                              width =280,
        #                                              text="some ques",
        #                                              fill=THEME_COLOR,
        #                                              font=("Arial",14,"italic"))
        self.canvas.grid(row=0, column=1)                
        true_image = PhotoImage(file=rf'{Path(__file__).parent.resolve()}\logo.png')
        self.canvas.create_image(100,100,image=true_image)

        #Lables
        label1 = Label(text="Website")
        label1.grid(row=1,column=0)
        label2 = Label(text="Username")
        label2.grid(row=2,column=0)
        label3 = Label(text="Paasword")
        label3.grid(row=3,column=0)
        
        #Entries
        website_entry = Entry(width=35)
        website_entry.grid(row=1,column=1)
        user_entry = Entry(width=35)
        user_entry.grid(row=2,column=1)
        passwd_entry = Entry(width=21)
        passwd_entry.grid(row=3,column=1)


        
        self.window.mainloop()


# ---------------------------- SAVE PASSWORD ------------------------------- #
ui = PassInterface()
# ---------------------------- UI SETUP ------------------------------- #