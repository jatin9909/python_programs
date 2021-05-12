# import turtle
# timmy = turtle.Screen()
# timmy.bgcolor("pink")
# timmy.title("Turtle")

# skk = turtle.Turtle()
# skk.forward(100)

# for i in range(4):
# 	skk.forward(100)
# 	skk.right(100)

# timmy.exitonclick()

import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100 + 1)
    t.forward(x)
    t.left(59)