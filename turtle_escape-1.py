# Avery Le
# 03/03/2020
# Canvas Assignment - Turtle Escape

import turtle
import random

# Approximate size of turtle objects in pixels when selecting turtle size of 3
BODY_SIZE = 80
# Half of the body size for collision detection with edge of screen
HALF_BODY_SIZE = BODY_SIZE / 2

# if enemies get this close to friend there is a collision
COLLISION_DISTANCE = 5

# Inner boundary within window for reversing the direction of enemies
LOWER_BOUND = -500/2 + HALF_BODY_SIZE
UPPER_BOUND = 500/2 - HALF_BODY_SIZE

win = turtle.Screen()
win.setup(500, 500)  # sets the width and height of the window
win.title("Balls Bounce")  # sets the title for the window


# creates a ball function
def enemy():
    obj = turtle.Turtle()
    obj.shape("circle")
    obj.color("red")
    obj.penup()
    obj.setheading(random.randrange(360))
    return obj


enemies = []
i = 0
# loop to add ball to the list balls
while i < 5:
    e = enemy()
    enemies.append(e)
    i += 1

friend = turtle.Turtle()
friend.shape("turtle")
friend.penup()
friend.setpos(250, -250)


def up():
    friend.setheading(90)
    friend.forward(45)


def down():
    friend.setheading(-90)
    friend.forward(45)


def left():
    friend.setheading(180)
    friend.forward(45)


def right():
    friend.setheading(0)
    friend.forward(45)


win.onkey(up, "Up")
win.onkey(left, "Left")
win.onkey(right, "Right")
win.onkey(down, "Down")

# Tell the program to listen
win.listen()


def check_and_change(obj):
    current_pos = obj.pos()
    if not (-500/2 < current_pos[0]< 500/2) or not (-500/2 < current_pos[1] < 500/2):
        obj.forward(-5)  # [0] and [1] of pos returns the x and y value
        obj.setheading(random.randrange(360))


# detect whether friend has collided with enemies (or vice-versa)
def collision(friend, enemies):
    # initialize is_collision to False
    is_collision = False
    # for all enemies
    for enemy in enemies:
        # how far is this enemy from friend
        how_far = enemy.distance(friend.pos())
        # if how_far is within collision distance
        if how_far < HALF_BODY_SIZE - COLLISION_DISTANCE:
            # set collision to true
            is_collision = True
            break  # break out of loop, one collision is enough
    return is_collision   # return whether collision was detected


# determine whether friend has reached the opposite corner
def reached_opposite_corner(friend):
    # initialize reached corner (opposite corner) to false
    reached_corner = False
    # opposite corner when x < lower bound and y > upper bound
    friend_pos = friend.pos()
    # if friend's x is less than window lower bound
    # and friend's y is greater than window's upper bound
    if friend_pos[0] < LOWER_BOUND and friend_pos[1] > UPPER_BOUND:
        reached_corner = True  # friend has reached corner, set variable to true
    return reached_corner  # return whether friend reached upper left corner


while True and not collision(friend, enemies) and not reached_opposite_corner(friend):
    for enemy in enemies:
        enemy.forward(5)
        check_and_change(enemy)

if collision(friend, enemies) is True:
    print('Game over: Your friend is now turtle soup!')
elif reached_opposite_corner(friend) is True:
    print('Game over: Your friend made it!')
else:
    print('Game over: Unknown reason: Programming error!')

