import turtle

screen = turtle.Screen()
screen.bgcolor("orange")

t = turtle.Turtle()
t.pencolor("white")
t.speed(0)
t.penup()
t.goto((-250, -150))
t.pendown()


def draw_sierpinski(length, levels):
    if levels == 0:
        for i in range(0,3):
            t.fd(length)
            t.left(120)
    else:
        draw_sierpinski(length/2,levels-1)
        t.fd(length/2)
        draw_sierpinski(length/2,levels-1)
        t.bk(length/2)
        t.left(60)
        t.fd(length/2)
        t.right(60)
        draw_sierpinski(length/2,levels-1)
        t.left(60)
        t.bk(length/2)
        t.right(60)


if __name__ == "__main__":
    draw_sierpinski(500, 5)
