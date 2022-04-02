import turtle

jn = turtle.Screen()
jn.title("PONG!!")
jn.bgcolor("black")
jn.setup(width=800, height=600)
jn.tracer(0)

ponto_a = 0
ponto_b = 0


raquete_a = turtle.Turtle()
raquete_a.speed(0)
raquete_a.shape("square")
raquete_a.color("white")
raquete_a.shapesize(stretch_wid=5, stretch_len=1)
raquete_a.penup()
raquete_a.goto(-350, 0)

raquete_b = turtle.Turtle()
raquete_b.speed(0)
raquete_b.shape("square")
raquete_b.color("white")
raquete_b.shapesize(stretch_wid=5, stretch_len=1)
raquete_b.penup()
raquete_b.goto(350, 0)

bola = turtle.Turtle()
bola.speed(0)
bola.shape("square")
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola.dx = 0.1
bola.dy = - 0.1

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Jogador A: {ponto_a}  Jogador B: {ponto_b}", align="center", font=("Courier", 20, "normal"))


def raquete_a_cima():
    y = raquete_a.ycor()
    y += 20
    raquete_a.sety(y)


def raquete_a_baixo():
    y = raquete_a.ycor()
    y -= 20
    raquete_a.sety(y)


def raquete_b_cima():
    y = raquete_b.ycor()
    y += 20
    raquete_b.sety(y)


def raquete_b_baixo():
    y = raquete_b.ycor()
    y -= 20
    raquete_b.sety(y)


jn.listen()
jn.onkeypress(raquete_a_cima, "w")
jn.onkeypress(raquete_a_baixo, "s")
jn.onkeypress(raquete_b_cima, "8")
jn.onkeypress(raquete_b_baixo, "5")


while True:
    jn.update()
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1

    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1

    if bola.xcor() > 390:
        bola.goto(0, 0)
        bola.dx *= -1
        ponto_a += 1
        pen.clear()
        pen.write(f"Jogador A: {ponto_a}  Jogador B: {ponto_b}", align="center", font=("Courier", 20, "normal"))

    if bola.xcor() < -390:
        bola.goto(0, 0)
        bola.dx *= -1
        ponto_b += 1
        pen.clear()
        pen.write(f"Jogador A: {ponto_a}  Jogador B: {ponto_b}", align="center", font=("Courier", 20, "normal"))

    if ( bola.xcor() > 340 and bola.xcor() < 350) and \
            (bola.ycor() < raquete_b.ycor() + 40 and bola.ycor() > raquete_b.ycor() - 40):
        bola.setx(340)
        bola.dx *= -1

    if (bola.xcor() < -340 and bola.xcor() > -350) and \
            (bola.ycor() < raquete_a.ycor() + 40 and bola.ycor() > raquete_a.ycor() - 40):
        bola.setx(-340)
        bola.dx *= -1
