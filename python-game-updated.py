# turtle 
import turtle 
import time
import random

delay = 0.1
delay_2 = 0.1

# Score
score = 0
high_score = 0
score_2 = 0
high_score_2 = 0
# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game by @Team 3")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0) # Turns off the screen updates
wn_2 = turtle.Screen()
wn_2.title("Snake Game by @Team 3")
wn_2.bgcolor("green")
wn_2.setup(width=600, height=600)
wn_2.tracer(0) # Turns off the screen updates


# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("turtle")
head.color("black")
head.penup()
head.goto(30,10)
head.direction = "stop"
head_2 = turtle.Turtle()
head_2.speed(0)
head_2.shape("turtle")
head_2.color("yellow")
head_2.penup()
head_2.goto(0,0)
head_2.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)
food_2 = turtle.Turtle()
food_2.speed(0)
food_2.shape("circle")
food_2.color("orange")
food_2.penup()
food_2.goto(0,100)
segments = [] 
segments_2 = []
# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))
pen_2 = turtle.Turtle()
pen_2.speed(0)
pen_2.shape("square")
pen_2.color("white")
pen_2.penup()
pen_2.hideturtle()
pen_2.goto(0, 230)
pen_2.write("Score: 0", align="center", font=("Courier", 24, "normal"))
# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
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
        
def go_up_2():
    if head_2.direction != "down":
        head_2.direction = "up"

def go_down_2():
    if head_2.direction != "up":
        head_2.direction = "down"

def go_left_2():
    if head_2.direction != "right":
        head_2.direction = "left"

def go_right_2():
    if head_2.direction != "left":
        head_2.direction = "right"

def move_2():
    if head_2.direction == "up":
        y_2 = head_2.ycor()
        head_2.sety(y_2 + 20)

    if head_2.direction == "down":
        y_2 = head_2.ycor()
        head_2.sety(y_2 - 20)

    if head_2.direction == "left":
        x_2 = head_2.xcor()
        head_2.setx(x_2 - 20)

    if head_2.direction == "right":
        x_2 = head_2.xcor()
        head_2.setx(x_2 + 20)
# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn_2.listen()
wn_2.onkeypress(go_up_2, "i")
wn_2.onkeypress(go_down_2, "k")
wn_2.onkeypress(go_left_2, "j")
wn_2.onkeypress(go_right_2, "l")

# Main game loop
while True:
    wn.update()
    wn_2.update()

    # Check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(30,10)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal")) 

    if head_2.xcor()>290 or head_2.xcor()<-290 or head_2.ycor()>290 or head_2.ycor()<-290:
        time.sleep(1)
        head_2.goto(0,0)
        head_2.direction = "stop"

        # Hide the segments
        for segment_2 in segments_2:
            segment_2.goto(1000, 1000)
        
        # Clear the segments list
        segments_2.clear()

        # Reset the score
        score_2= 0

        # Reset the delay
        delay_2 = 0.1

        pen_2.clear()
        pen_2.write("Score: {}".format(score_2), align="center", font=("Courier", 24, "normal")) 
    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("turtle")
        new_segment.color("black")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal")) 
    if head_2.distance(food_2) < 20:
        # Move the food to a random spot
        x_2 = random.randint(-290, 290)
        y_2 = random.randint(-290, 290)
        food_2.goto(x_2,y_2)

        # Add a segment
        new_segment_2 = turtle.Turtle()
        new_segment_2.speed(0)
        new_segment_2.shape("turtle")
        new_segment_2.color("magenta")
        new_segment_2.penup()
        segments_2.append(new_segment_2)

        # Shorten the delay
        delay_2 -= 0.001

        # Increase the score
        score_2 += 10

        if score_2 > high_score_2:
            high_score_2 = score_2
        
        pen_2.clear()
        pen_2.write("Score: {}".format(score_2), align="center", font=("Courier", 24, "normal")) 


    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
        
    for index in range(len(segments_2)-1, 0, -1):
        x_2 = segments_2[index-1].xcor()
        y_2 = segments_2[index-1].ycor()
        segments_2[index].goto(x_2, y_2)

    # Move segment 0 to where the head is
    if len(segments_2) > 0:
        x_2 = head_2.xcor()
        y_2 = head_2.ycor()
        segments_2[0].goto(x_2,y_2)

    move()   
    move_2()   

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1
        
            # Update the score display
            pen.clear()
            pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
    
    for segment_2 in segments_2:
        if segment_2.distance(head_2) < 20:
            time.sleep(1)
            head_2.goto(0,0)
            head_2.direction = "stop"
        
            # Hide the segments
            for segment_2 in segments_2:
                segment_2.goto(1000, 1000)
        
            # Clear the segments list
            segments_2.clear()

            # Reset the score
            score_2 = 0

            # Reset the delay
            delay_2 = 0.1
        
            # Update the score display
            pen_2.clear()
            pen_2.write("Score: {} ".format(score_2), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)
    time.sleep(delay_2)
    

wn.mainloop()
