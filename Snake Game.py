import os
import turtle
import time
import random

delay = 0.13

# score
score = 0
high_score = 0

# screen
wn = turtle.Screen()
wn.title("Snake game")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)

# head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("blue")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("SCORE: 0  HIGH SCORE: 0", align="center", font=("courier", 24, "normal"))



# functions
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction!= "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# game loop
while True:
    wn.update()

    # collision with border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(0.7)
        head.goto(0, 0)
        head.direction = "stop"

        # hide old segments
        for segment in segments:
            segment.goto(1000, 1000)

        # clear segments
        segments.clear()

        # reset delay
        delay =  0.13

        # reset score
        score = 0

        pen.clear()
        pen.write(f"SCORE:  {score}    HIGH SCORE:  {high_score}", align="center", font=("courier", 24, "normal"))

    # collision check
    if head.distance(food) < 20:
        x = random.randint(-290, 290)       # moving food to random location
        y = random.randint(-290, 290)
        food.goto(x, y)

        # increase length of body
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("light blue")
        new_segment.penup()
        segments.append(new_segment)

        # shorten delay
        delay -= 0.001

        # increase score
        score += 1

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(f"SCORE:  {score}    HIGH SCORE:  {high_score}", align="center", font=("courier", 24, "normal"))

    # move end segment reverse
    for index in range(len(segments)-1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # move segment 0 to head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # self collision check
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(0.7)
            head.goto(0, 0)
            head.direction = "stop"

            # hide old segments
            for segment in segments:
                segment.goto(1000, 1000)

            # clear segments
            segments.clear()

            # reset delay
            delay = 0.13

            # reset score
            score = 0

            pen.clear()
            pen.write(f"SCORE:  {score}    HIGH SCORE:  {high_score}", align="center", font=("courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()



