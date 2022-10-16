import time
from turtle import Turtle
import emoji


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.highscore = 0
        with open('score.txt' ,'r') as file:
            self.highscore = int(file.read())
        self.write(f"Score : {self.score}, High Score: {self.highscore}", align='center', font=('Arial', 12, 'normal'))

    def update_score(self):
        self.clear()
        self.score += 10
        self.write(f"Score: {self.score}, High Score: {self.highscore}", align='center', font=('Arial', 12, 'normal'))

    def reset(self):
        self.clear()
        if self.score>self.highscore:
            self.highscore = self.score
            with open('score.txt','w') as file:
                file.write(str(self.highscore))
        self.score = 0
        self.write(f"Score: {self.score}, High Score: {self.highscore}", align='center',
                       font=('Arial', 12, 'normal'))


    def game_over(self):
        game_over = Turtle()
        game_over.color("red")
        game_over.hideturtle()
        game_over.penup()
        game_over.goto(0, 100)
        emoj = emoji.emojize(":weary:", language='alias')
        print(emoj)
        game_over.write("GAME OVER \n " + ' ' * 7 + f"{emoj}", align='center', font=('Arial', 24, 'normal'))
        game_over.clear()
        time.sleep(2)
