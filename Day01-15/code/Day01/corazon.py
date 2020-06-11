"""
用python的turtle模块绘制爱心
"""
import turtle

turtle.bgcolor("black")

turtle.pencolor('red')


turtle.color('pink')


def curve():
    for i in range(200):
        turtle.left(1)
        turtle.forward(1)


turtle.begin_fill()
turtle.left(45)
turtle.forward(150)
curve()
turtle.right(135)
curve()
turtle.forward(150)

turtle.fillcolor("red")
turtle.end_fill()
turtle.mainloop()
turtle.hideturtle()
