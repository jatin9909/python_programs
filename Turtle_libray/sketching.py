import turtle as turtle_module

tim=turtle_module.Turtle()
screen = turtle_module.Screen()

def move_forwards():
	tim.forward(10)

def move_backwards():
	tim.backward(10)

def move_counter_clockwise():
	tim.circle(120,180)

def lef():
	tim.left(45)

def right():
	tim.right(45)

def clear():
	tim.clear()
	tim.penup()
	tim.home()
	tim.clear()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="l", fun=left)
screen.onkey(key="r", fun=right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()