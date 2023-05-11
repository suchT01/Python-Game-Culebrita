import turtle
import time
import random

retraso=-1

s=turtle.Screen()
s.setup(650,650)
s.bgcolor("gray")
s.title("Culebrita")

comida=turtle.Turtle()
comida.shape("circle")
comida.speed(0)
comida.color("blue")
comida.penup()

serp=turtle.Turtle()
serp.speed(1)
serp.shape("square")
serp.penup()
serp.goto(0,0)
serp.direction = 'stop'
serp.color("green","green")

cuerpo=[]

def arriba():
    serp.direction='up'

def abajo():
    serp.direction='down'

def derecha():
    serp.direction='right'

def izquierda():
    serp.direction='left'

def movimiento():
    if serp.direction == 'up':
        y=serp.ycor()
        serp.sety(y+20)
    if serp.direction == 'down':
        y=serp.ycor()
        serp.sety(y-20)
    if serp.direction == 'right':
        x=serp.xcor()
        serp.setx(x+20)
    if serp.direction == 'left':
        x=serp.xcor()
        serp.setx(x-20)

s.listen()
s.onkeypress(arriba,"Up")
s.onkeypress(abajo,"Down")
s.onkeypress(derecha,"Right")
s.onkeypress(izquierda,"Left")

while True:
    s.update()
    if serp.xcor() > 300 or serp.xcor() < -300 or serp.ycor() > 300 or serp.ycor()<-300:
        time.sleep(1)
        for i in cuerpo:
            i.clear()
            i.hideturtle()
        serp.home()
        serp.direction = 'Stop'
    if serp.distance(comida) < 20:
        x = random.randint(-250,250)
        y = random.randint(-250,250)
        comida.goto(x,y)
        n_cuerpo=turtle.Turtle()
        n_cuerpo.shape("square")
        n_cuerpo.speed(0)
        n_cuerpo.color("green")
        n_cuerpo.penup()
        cuerpo.append(n_cuerpo)
    
    total = len(cuerpo)
    for i in range(total -1,0,-1):
        x=cuerpo[i-1].xcor()
        y=cuerpo[i-1].ycor()
        cuerpo[i].goto(x,y)
    if total > 0:
        x=serp.xcor()
        y=serp.ycor()
        cuerpo[0].goto(x,y  )
    movimiento()
    for i in cuerpo:
        if i.distance(serp)<20:
            for i in cuerpo:
                i.clear()
                i.hideturtle()
            serp.home()
            cuerpo.clear()
            serp.direction = 'Stop'
turtle.done()