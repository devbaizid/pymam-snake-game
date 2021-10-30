print("Welcome to another Project this project cool Snake Game ")
# Easy
# Best
# About Me Tanvir islam Baizid
# Some   library
from random import randrange
from turtle import *
from freegames import square, vector


# some variables in games

food = vector(0, 0)
snake = [vector(100, 100)]
aim = vector(-10, -10)



# functions

def change(x, y):
    aim.x = x
    aim.y = y


def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 190


def move():

    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 15, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Number:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)


# Execution

setup(800, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 10), 'Right')
onkey(lambda: change(-10, -10), 'Left')
onkey(lambda: change(-10, 10), 'Up')
onkey(lambda: change(10, -10), 'Down')
move()

done()



"""
nice 
cool 
# Python 
# Gui
"""


print("////"*10)

