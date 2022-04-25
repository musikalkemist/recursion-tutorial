import turtle

t = turtle.Turtle()
t.penup()
t.goto((-100, 200))
t.pendown()
t.speed(6)


def draw_spiral(turtle,
                line_length,
                line_offset):
    if line_length / line_offset > 0:
        turtle.forward(line_length)
        turtle.right(90)
        draw_spiral(turtle, line_length - line_offset, line_offset)


if __name__ == "__main__":
    draw_spiral(t, 400, 5)
