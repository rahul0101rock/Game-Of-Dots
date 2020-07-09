#Made By Rahul Choudhary
import tkinter as tk
from turtle import *
import turtle
from time import *
from operator import itemgetter
import random
from tkinter import messagebox
def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass
print("--------Welcome to the Game 'Dot And Boxes'------- \n-----------------By Rahul choudhary-----------------")
p1_name=input("Enter the name of Player 1: ")
p2_name=input("Enter the name of Player 2: ")
grid=input("Enter The Size Of Grid: ")
sn=["x","P1","P2"]
if p1_name=='':
    p1_name="Player 1"
else:
    sn[1]=(p1_name[0].upper())
if p2_name=='':
    p2_name="Player 2"
else:
    sn[2]=(p2_name[0].upper())
if grid=='':
    grid=6
else:
    grid=int(grid)

title("Dots And Boxes By Rahul Choudhary")
screen = getscreen()
screen.listen()
hideturtle()
turtle.ht()
tracer(0,0)
screen.setworldcoordinates(0,0,(grid * 100 + 100),(grid * 100 + 200))
penup()
screen.bgcolor("#98AFC7")

V = []
H = []
boxes = []
for i in range(grid):
    for i in range(grid-1):
        V.append(0)
for i in range(grid):
    for i in range(grid-1):
        H.append(0)
for i in range(grid-1):
    for i in (range(grid-1)):
        boxes.append(0)
turn = 1

def main():
    printScore()
    goto(100,100)
    for i in range(1,(grid+1)):
        for i in range(1,(grid + 1)):
            dot(10)
            forward(100)
        goto((xcor() - (grid * 100)),(ycor() + 100))
    onscreenclick(click)

    mainloop()
def scorecount():
    p1_score = 0
    p2_score = 0
    for i in range(len(boxes)):
        if boxes[i] == 1:
            p1_score += 1
        elif boxes[i] == 2:
            p2_score += 1
    return [p1_score, p2_score]

def printScore():
    score = scorecount()
    goto(((grid+1) * 20), ((grid * 100) + 20))
    if turn == 1:
        turtle.pencolor("blue")
        write("{}: ".format(p1_name.title()) + str(score[0]), align="center", font=("Arial", 20, "bold"))
        turtle.pencolor("red")
        goto(((grid+1) * 80), ((grid * 100) + 20))
        write("{}: ".format(p2_name.title()) + str(score[1]), align="center", font=("Arial", 20))
    if turn == 2:
        turtle.pencolor("blue")
        write("{}: ".format(p1_name.title()) + str(score[0]), align="center", font=("Arial", 20))
        turtle.pencolor("red")
        goto(((grid+1) * 80), ((grid * 100) + 20))
        write("{}: ".format(p2_name.title()) + str(score[1]), align="center", font=("Arial", 20, "bold"))
    turtle.pencolor("black")
    
def click(x1,y1):
    x = int(x1//1)
    y = int(y1//1)
    for xnum in range(1,(grid + 1)):
        tempx = (xnum % grid) + 1
        for ynum in range(1,(grid)):
            tempy = (ynum % (grid-1)) + 1
            if ((tempx * 100) + 10) >= x >= ((tempx * 100) - 10) and ((tempy * 100) + 90) >= y >= ((tempy * 100) + 10):
                onscreenclick(None)
                updateVariable(tempx, tempy, True)
    for xnum in range(1,(grid)):
        tempx = (xnum % (grid -1)) + 1
        for ynum in range(1,(grid + 1)):
            tempy = (ynum % grid) + 1
            if ((tempx * 100) + 90) >= x >= ((tempx * 100) + 10) and ((tempy * 100) + 10) >= y >= ((tempy * 100) - 10):
                onscreenclick(None)
                updateVariable(tempx, tempy, False)

def updateVariable(x, y, isVertical):
    new = False
    global V
    global H
    if isVertical:
        V[((y - 1) * grid + x)-1] = 1
    else:
        H[((y - 1) * (grid - 1) + x)-1] = 1
    clear()
    for xnum in range(1,(grid+1)): # 4
        for ynum in range(1,grid): # 3
            if V[((ynum - 1) * grid + xnum) - 1] != 0:
                goto((100 * xnum), (100 * ynum))
                pendown()
                goto((100 * xnum), (100 * (ynum + 1)))
                penup()
    for xnum in range(1,grid):
        for ynum in range(1,(grid + 1)):
            if H[((ynum - 1) * (grid-1) + xnum) - 1] != 0:
                goto((100 * xnum), (100 * ynum))
                pendown()
                goto((100 * (xnum + 1)), (100 * ynum))
                penup()
    boxTotal = len(boxes)
    for i in range(0,boxTotal):
        yMulti = 0
        for z in range(grid-1):
            if (i >= z * (grid-1)):
                yMulti += 1
        if (0 not in itemgetter(i,(i + grid - 1))(H)) and (0 not in itemgetter((i + yMulti-1),(i+ yMulti))(V)):
            if boxes[i] == 0:
                boxes[i] = turn
                new = True
    for xnum in range(1,grid):
        for ynum in range(1,grid):
            pos = ((ynum-1) * (grid-1)) + xnum - 1
            if boxes[pos] != 0:
                goto((100 * xnum + 50), (100 * ynum + 20))
                
                if boxes[pos]==1:
                    turtle.pencolor("blue")
                else:
                    turtle.pencolor("red")
                write(sn[boxes[pos]], align="center", font=("Arial", int(150/grid)))
                turtle.pencolor("black")
    if not 0 in boxes:
        clear()
        goto(150,250)
        score = scorecount()
        if score[0] > score[1]:
            message_box("Congrats","  {} wins    ".format(p1_name.title()))
            write("{} wins".format(p1_name.title()), align="center", font=("Arial", 25))
        elif score[0] < score[1]:
            message_box("Congrats","  {} wins    ".format(p2_name.title()))
            write("{} wins".format(p2_name.title()), align="center", font=("Arial", 25))
        else:
            message_box("Play Again","   Tie!!    ")
            write("  Tie!!", align="center", font=("Arial", 25))
        goto(150,100)
        write("Play again", align="center", font=("Arial", 25))
        onscreenclick(reset)
        mainloop()

    finish(new)

def reset(x1, y1):
    global V
    global H
    global boxes
    global turn
    x = int(x1//1)
    y = int(y1//1)
    if 150 >= x >= 50 and 150 >= y >= 50:
        onscreenclick(None)
        V = [0,0,0,0,0,0,0,0,0,0,0,0] 
        H = [0,0,0,0,0,0,0,0,0,0,0,0]
        boxes = [0,0,0,0,0,0,0,0,0]
        turn = 1
        clear()
        finish(True)
    if 450 >= x >= 350 and 150 >= y >= 50:
        raise SystemExit

def finish(again):
    global turn
    if turn == 1 and not again:
        turn = 2
    elif not again:
        turn = 1
    main()
main()

screen._root.mainloop()
