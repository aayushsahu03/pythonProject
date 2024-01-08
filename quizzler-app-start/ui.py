from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


# noinspection PyTypeChecker
class QuizInterface:

    def __init__(self, quiz_brain:QuizBrain):
        """

        :return:
        """
        self.quiz = quiz_brain # QuizBrain class object
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(padx=20, pady=20,bg=THEME_COLOR)
        self.score_label = Label(text="Score:"+" "*3+"0",fg='white',
                                 bg=THEME_COLOR,
                                 font=("Arial",10,"bold"))
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150,125,
                                                     width =280,
                                                     text="some ques",
                                                     fill=THEME_COLOR,
                                                     font=("Arial",14,"italic"))
        self.canvas.grid(row=1, column=0,
                         columnspan=2,
                         pady=50)
        true_image = PhotoImage(file='./images/true.png')
        self.true_button = Button(image=true_image, highlightthickness=2, command=self.true_pressed)
        self.true_button.grid(row=2,column=0)

        false_image = PhotoImage(file='./images/false.png')
        self.false_button = Button(image=false_image, highlightthickness=2,
                                   highlightcolor= "white", command=self.false_pressed)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg='white')
            self.score_label.config(text="Score:"+" "*3+str(self.quiz.score),font=("Arial",10,"bold"))
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You have reached the end of Quiz!\n\n"
                                                           "Your score is : {}".format(self.quiz.score))
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.canvas.config(bg='white')

    def true_pressed(self):

        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):

        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, right_or_wrong):

        if right_or_wrong:
            self.canvas.config(bg="light green")
        else:
            self.canvas.config(bg="crimson")
        self.window.after(550, self.get_next_question)





