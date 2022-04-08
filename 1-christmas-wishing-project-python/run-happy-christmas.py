import time
import playsound
from turtle import *
from random import randint
from threading import Thread

def play_bg_music():
    playsound.playsound("system-files//bg-sound.mp3")

def finish_music():
    playsound.playsound("system-files//finish-sound.mp3")



thread1 = Thread(target = play_bg_music)
thread1.start()

time.sleep(2)

def create_rectangle(turtle, color, x, y, width, height):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()

    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)

    # fill the above shape
    turtle.end_fill()
    # Reset the orientation of the turtle
    turtle.setheading(0)

def create_circle(turtle, x, y, radius, color):
    turtle_pen.penup()
    turtle_pen.color(color)
    turtle_pen.fillcolor(color)
    turtle_pen.goto(x, y)
    turtle_pen.pendown()
    turtle_pen.begin_fill()
    turtle_pen.circle(radius)
    turtle_pen.end_fill()

BG_COLOR = "#000000"

turtle_pen = Turtle() 			  	# Create turtle object
turtle_pen.speed(10) 			  	# Define turtle speed
screen = turtle_pen.getscreen()   	# Define background-color
screen.bgcolor(BG_COLOR)
screen.title("Merry Christmas")   	# Wishing quotes
screen.setup(width=1.0, height=1.0)	# Set up screen.

y = 0

# Draw tree
width = 340
turtle_pen.speed(50)
while width > 10:
    width = width - 10
    height = 10
    x = 0 - width/2
    create_rectangle(turtle_pen, "green", x, y, width, height)
    y = y + height

# Draw a stars

turtle_pen.speed(5)
turtle_pen.penup()
turtle_pen.color('red')
turtle_pen.goto(-20, y+10)
turtle_pen.begin_fill()
turtle_pen.pendown()
for i in range(5):
    turtle_pen.forward(40)
    turtle_pen.right(144)
turtle_pen.end_fill()


y = -100
create_rectangle(turtle_pen, "brown", -15, y-60, 30, 60)  # Draw tree trunk

# Draw tree
width = 340
turtle_pen.speed(50)

while width > 5:
    width = width - 10
    height = 10
    x = 0 - width/2
    create_rectangle(turtle_pen, "green", x, y, width, height)
    y = y + height

tree_height = y + 40

# Draw yellow color moon
create_circle(turtle_pen, 230, 180, 60, "yellow")
# Slice the full circle to make a crescent desgin
create_circle(turtle_pen, 220, 180, 60, BG_COLOR)


# Draw stars on black background.
turtle_pen.speed(300)
number_of_stars = randint(50,60)
# print(number_of_stars)
for _ in range(0,number_of_stars):
    x_star = randint(-(screen.window_width()//2),screen.window_width()//2)
    y_star = randint(tree_height, screen.window_height()//2)
    size = randint(5,20)
    turtle_pen.penup()
    turtle_pen.color('white')
    turtle_pen.goto(x_star, y_star)
    turtle_pen.begin_fill()
    turtle_pen.pendown()
    for i in range(5):
        turtle_pen.forward(size)
        turtle_pen.right(144)
    turtle_pen.end_fill()

# print greeting message
turtle_pen.speed(5)
turtle_pen.penup()
msg = "Wishing You A Very Merry Christmas ~ Gunarakulan Gunaretnam"
turtle_pen.goto(0, -200)  # y is in minus because tree trunk was below x axis
turtle_pen.color("orange")
turtle_pen.pendown()
turtle_pen.write(msg, move=False, align="center", font=("Arial", 25, "bold"))

finish_music()

turtle_pen.hideturtle()
screen.mainloop()
