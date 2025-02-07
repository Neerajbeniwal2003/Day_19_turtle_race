from turtle import Turtle,Screen
import random

is_race_on=False
screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="make a bet",prompt="who would won:").lower()
colors=["black","red","yellow","pink","medium sea green","peru"]

x=-230
y=-180
all_turtles=[]
for i in colors:
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(i)
    y+=50
    new_turtle.goto(x=x,y=y)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on=True

while is_race_on:
    for i in all_turtles:
        if i.xcor()>230:
            is_race_on=False
            if i.pencolor()==user_bet:
                print(f"you win! {i.pencolor()} is the winner")
            else:
                print(f"you lose! {i.pencolor()} is the winner")
        random_distance=random.randint(0,15)
        i.forward(random_distance)
        
# tim=Turtle(shape="turtle")
# tim.penup()
# tim.goto(x=-230,y=-180)

screen.exitonclick()