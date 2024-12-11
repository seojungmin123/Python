import turtle
import random
turtle.shape("turtle")
'''
a = int(input("몇각형: "))

for i in range(a):
    turtle.forward(1)
    turtle.left(360/a)

turtle_color = ["red", "orange", "yellow", "green", "blue", "purple"]
for j in range(20, 2, -1):
    turtle.color(turtle_color[n-8])
    turtle.begin_fill()
    for i in range(j):
        turtle.forward(50)
        turtle.left(360/j)
    turtle.end_fill()
'''

import random

for j in range(100, 2, -1):
    
    turtle.speed(100000)
    
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.fillcolor(r, g, b)
    
    turtle.begin_fill()
    
    for i in range(j):
        turtle.forward(50)
        turtle.left(360/j)
        
    turtle.end_fill()
        


