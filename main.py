# import package
import turtle
import time
import random

delay = 0.1

# score
score = 0
hightScore = 0

# screen setup
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor('yellow')
wn.setup(width=600, height=600)
wn.tracer(0)

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# snake food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0, 10)

segments = []

# scoreboards
sc = turtle.Turtle()
sc.speed(0)
sc.shape("square")
sc.color("black")
sc.penup()
sc.hideturtle()
sc.goto(0, 260)
sc.write("Score: 0, High Score: 0", align="center",
         font=("ds-digital", 24, "normal"))

# func


def goUp():
    if head.direction != "down":
        head.direction = "up"


def goDown():
    if head.direction != "up":
        head.direction = "down"


def goRight():
    if head.direction != "left":
        head.direction = "right"


def goLeft():
    if head.direction != "right":
        head.direction = "left"


def move():
    if head.direction != "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction != "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction != "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction != "left":
        x = head.xcor()
        head.setx(x - 20)


# key bindings
wn.listen()
wn.onkeypress(goUp, "w")
wn.onkeypress(goDown, "s")
wn.onkeypress(goRight, "d")
wn.onkeypress(goLeft, "a")

# main loop

while True:
    wn.update()

    # check collision
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

    # hide segmen body
    for segment in segments:
        segment.goto(1000, 1000)  # out of range / keluar jalur
    # clear the segments
    segments.clear()

    # reset
    score = 0
    delay = 0.1
    sc.clear()
    # .format(score, hightScore)
    sc.write("Score: {}, High Score: {}".format(score, hightScore), align="center",
             font=("ds-digital", 24, "normal"))

    # check collision food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # add new segmen to the head
        newSegment = turtle.Turtle()
        newSegment.speed(0)
        newSegment.shape("square")
        newSegment.color("black")
        newSegment.penup()
        segments.append(newSegment)

        # shorten delay
        delay -= 0.001
        # increase score
        score += 10

        if score > hightScore:
            hightScore = score
        sc.clear()
        sc.write("Score: {}, High Score: {}".format(score, hightScore), align="center",
                 font=("ds-digital", 24, "normal"))

# move segment
for index in range(len(segments)-1, 0, -1):
    x = segments[index-1].xcor()
    y = segments[index-1].ycor()
    segments[index].goto(x, y)
# move segment 0 to head
if len(segments) > 0:
    x = head.xcor()
    y = head.ycor()
    segments[0].goto(x, y)

move()

for segment in segments:
    if segment.distance(head) < 20:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1

        sc.clear()
        sc.write("Score: {}, High Score: {}".format(score, hightScore), align="center",
                 font=("ds-digital", 24, "normal"))

    time.sleep(delay)
wn.mainloop()
