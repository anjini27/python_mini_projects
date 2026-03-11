from turtle import Turtle,Screen
import random
is_on_race=False
screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="who will the race?enter the color/turtle number: ")
colors=["red","green","orange","purple","yellow","violet","pink"]
y_positions=[-100,-70,-40,-10,20,50,80]
all_turtles=[]
for turtle_index in range(0,7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_on_race=True
while is_on_race:
     for turtle in all_turtles:
         if turtle.xcor()>230:
             is_on_race=False
             winning_color=turtle.pencolor()
             if winning_color==user_bet:
                 print(f"you've won! The {winning_color} turtle is the win")
             else:
                 print(f"sorry!you lose the game! the winner is {winning_color} turtle")
         rand_distance = random.randint(0, 10)
         turtle.forward(rand_distance)



screen.exitonclick()


# def forwards():
#     tim.forward(20)
# def backwords():
#     tim.backward(20)
#
# def turn_left():
#     new_heading=tim.heading()+20
#     tim.setheading(new_heading)
# def turn_right():
#     new_heading=tim.heading()-20
#     tim.setheading(new_heading)
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
# screen.listen()
# screen.onkey(forwards,"w")
# screen.onkey(backwords,"s")
# screen.onkey(turn_left,"a")
# screen.onkey(turn_right,"d")
# screen.onkey(clear,"c")
# screen.exitonclick()
