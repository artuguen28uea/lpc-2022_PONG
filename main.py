import turtle
import time

screen = turtle.Screen()
screen.title("My Pong")
screen.bgcolor("Black")
screen.setup(width=800, height=600)
screen.tracer(0)

paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("red")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)

paddle_2 = turtle.Turtle()
paddle_2.speed(5)
paddle_2.shape("square")
paddle_2.color("red")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color("blue")
ball.hideturtle()
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1

hud = turtle.Turtle()
hud.speed(0)
hud.shape("square")
hud.color("white")
hud.penup()
hud.hideturtle()
hud.goto(0, 260)
hud.write("0 : 0", align="center", font=("Bodoni MT Black", 24, "normal"))

# Writing "Player 1" on the screen
player1 = turtle.Turtle()
player1.hideturtle()
player1.goto(-240,260)
player1.pencolor("green")
player1.write("Player 1", align="left", font=("Bodoni MT Black", 24, "normal"))

# Writing "Player 2" on the screen
player2 = turtle.Turtle()
player2.hideturtle()
player2.goto(240,260)
player2.pencolor("green")
player2.write(" Player 2", align="right", font=("Bodoni MT Black", 24, "normal"))

start_screen = turtle.Turtle()
start_screen.speed(0)
start_screen.color("white")
start_screen.penup()
start_screen.hideturtle()
start_screen.goto(0, 0)

start_p = False
score_1 = 0
score_2 = 0

def paddle_1_up():
    y = paddle_1.ycor()
    if y < 250:
        y += 30
    else:
        y = 250
    paddle_1.sety(y)

def paddle_1_down():
    y = paddle_1.ycor()
    if y > -250:
        y += -30
    else:
        y = -250
    paddle_1.sety(y)

def paddle_2_up():
    y = paddle_2.ycor()
    if y < 250:
        y += 30
    else:
        y = 250
    paddle_2.sety(y)

def paddle_2_down():
    y = paddle_2.ycor()
    if y > -250:
        y += -30
    else:
        y = -250
    paddle_2.sety(y)

def start_game():
    global start_p
    start_p = True
    print("Evento")


screen.listen()
screen.onkeypress(paddle_1_up, "w")
screen.onkeypress(paddle_1_down, "s")
screen.onkeypress(paddle_2_up, "Up")
screen.onkeypress(paddle_2_down, "Down")
screen.onkeypress(start_game, "space")


while True:
    screen.update()
    
    while not(start_p):
        start_screen.write("Press 'space' to start", align="center", font=("Bodoni MT Black", 24, "normal"))
    ball.showturtle()
    start_screen.clear()

    ball.setx(ball.xcor() + (ball.dx/2))
    ball.sety(ball.ycor() + (ball.dy/2))

    # Colision with the upper wall
    if ball.ycor() > 250:
        #os.system("afplay bounce.wav&")
        ball.sety(250)
        ball.dy *= -1

    # Colision with the lower wall
    if ball.ycor() < -280:
        #os.system("afplay bounce.wav&")
        ball.sety(-280)
        ball.dy *= -1

    # Colision with the paddle 1
    if ball.xcor() < -330 and ball.ycor() < paddle_1.ycor() + 50 and ball.ycor() > paddle_1.ycor() - 50:
        ball.dx *= -1

    # Colision with the paddle 2
    if ball.xcor() > 330 and ball.ycor() < paddle_2.ycor() + 50 and ball.ycor() > paddle_2.ycor() - 50:
        ball.dx *= -1

    # Colision with the left wall
    if ball.xcor() < -390:
        score_2 += 1
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
        # Showing that player 2 won
        if score_2 > 5:
            p2win = turtle.Turtle()  
            p2win.hideturtle()
            p2win.goto(0,0)
            p2win.pencolor("yellow")
            p2win.write("Player 2 wins", align="center", font=("Bodoni MT Black", 35))
            break

    # Colision with the right wall
    if ball.xcor() > 390:
        score_1 += 1
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
        # Showing that player 1 won
        if score_1 > 5:
            p1win = turtle.Turtle()
            p1win.hideturtle()
            p1win.goto(0,0)
            p1win.pencolor("yellow")
            p1win.write("Player 1 wins", align="center", font=("Bodoni MT Black", 35)) 
            break

turtle.done()