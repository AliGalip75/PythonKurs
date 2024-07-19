import time
import random
from turtle import *

# Ekranı oluştur
draw_board = Screen()
draw_board.title("Catch Turtle")
draw_board.setup(700, 700)
draw_board.bgcolor("cyan")
Font = ("Arial",15,"bold")
# Turtle nesnelerini oluştur
obj1 = Turtle()
obj1.penup()
obj1.hideturtle()
obj1.shape("turtle")
obj1.shapesize(2)

obj2 = Turtle()
obj2.hideturtle()
obj2.shape("blank")
obj2.penup()
obj2.goto(-20, 320)
obj2.pendown()
obj2.write("Time : ", font=Font)

obj3 = Turtle()
obj3.hideturtle()
obj3.shape("blank")
obj3.penup()
obj3.goto(-20, 280)
obj3.pendown()
obj3.write("Score : ", font=Font)

obj4 = Turtle()
obj4.hideturtle()
obj4.shape("blank")
obj4.penup()
obj4.goto(0, 320)
obj4.pendown()

obj5 = Turtle()
obj5.hideturtle()
obj5.shape("blank")
obj5.penup()
obj5.goto(0, 280)
obj5.pendown()

# Başlangıç değerleri
score = 0
time_left = 20
kontrol = score

def show_score():
    global kontrol
    if kontrol != score:
        obj5.clear()
        kontrol = score
    obj5.write("          " + str(score), font=Font)

def click_handler(x, y):
    global score
    score += 1
    show_score()

def show_time():
    obj4.clear()
    obj4.write("       " + str(time_left), font=Font)

def move():
    if time_left > 0:
        random_x = random.randint(-300, 300)
        random_y = random.randint(-300, 300)
        obj1.hideturtle()
        obj1.goto(random_x, random_y)
        obj1.showturtle()
        draw_board.ontimer(move, 500)

def countdown():
    global time_left
    if time_left > 0:
        time_left -= 1
        show_time()
        draw_board.ontimer(countdown, 1000)
    else:
        obj1.hideturtle()  # Oyun bittiğinde kaplumbağayı gizle

# Başlangıçta turtle'ı gizle ve tıklama olayını ayarla
obj1.hideturtle()
obj1.onclick(click_handler)

# Oyunu başlat
show_time()
show_score()
move()
countdown()

draw_board.mainloop()
