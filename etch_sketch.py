from turtle import Turtle,Screen

tim=Turtle()
my_screen=Screen()

def move_forward():
    tim.forward(10)
def turn_right():
    tim.right(15)
def turn_left():
    tim.left(15)
def turn_backward():
    tim.backward(10)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


my_screen.listen()
my_screen.onkeypress(move_forward,"w")
my_screen.onkeypress(turn_right,"d")
my_screen.onkeypress(turn_left,"a")
my_screen.onkeypress(turn_backward,"s")
my_screen.onkey(clear,"c")
my_screen.exitonclick()

