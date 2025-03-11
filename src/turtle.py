import turtle
t = turtle.Turtle()
t.shape("turtle")
t.fillcolor("brown")

t.begin_fill()
t.goto(0,0)
t.goto(0,100)
t.goto(100,100)
t.goto(100,0)
t.end_fill()
t.penup()

t.goto(-200, 200)
t.begin_fill()
t.pendown()
t.goto(0,400)
t.goto(300,200)
t.goto(-200, 200)
t.end_fill()
t.penup()

turtle.done()
