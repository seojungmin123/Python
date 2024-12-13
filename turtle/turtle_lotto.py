import turtle
import random

lotto_num = []
for n in range(1,46):
    lotto_num.append(n)

ball_color = ["red","orange","green","blue","purple","brown"]
random.shuffle(lotto_num)
random.shuffle(ball_color)
count = 0

t = turtle.Turtle()
s = turtle.Screen()
t.speed(0)
t.hideturtle()

s.setup(1200,700)
s.bgcolor("#c3bbdd")
t.pensize(1)
t.penup()
t.goto(0,150)
t.pendown()
t.color("white")
t.write("Random Lotto", align="center",font = ("Impact",100,"bold"))
t.penup()

for i in range(-500,501,200):
    t.penup()
    t.goto(i,-100)
    t.pendown()
    t.begin_fill()
    t.color(ball_color[count])
    t.circle(70,360)
    t.end_fill()

    
    t.penup()
    t.goto(i,-90)
    t.color("white")
    t.pendown()
    t.write(lotto_num[count], align="center",font = ("Impact",70,"bold"))
    count = count+1




turtle.done()




