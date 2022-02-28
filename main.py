from turtle import Turtle, Screen

pip = Turtle()
screen = Screen()
screen.setup(width=1000, height=800)
pip.penup()
pip.goto(0,200)
pip.pendown()
pip.speed(0)

num = 13
iterations = ["r"]

for i in range(1, num):
    flipped = ""
    for char in iterations[-1][::-1]:
        if char == "r":
            flipped += "l"
        else:
            flipped += "r"
    new_iter = (iterations[-1] + "r") + flipped
    iterations.append(new_iter)

pip.setheading(90)

for itr in iterations:
    for turn in itr:
        if turn == "r":
            pip.right(90)
            pip.forward(2)
        if turn == "l":
            pip.left(90)
            pip.forward(2)

screen.exitonclick()

