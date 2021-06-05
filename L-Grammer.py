from tkinter import *
import turtle

root = Tk()
root.title("L-Grammer / copyright©5unghun")
root.geometry("800x600+500+200")

#G = (N, T, S, P)
N = ["D"]
T = ["d", "+", "-"]
S = N[0]
P = ''

def drawTurtle(level):
    global turtle

    #turtle init
    screen.setworldcoordinates(-100, 100, 100, -100)
    turtle.reset()
    turtle.hideturtle()
    turtle.pensize(1)
    turtle.speed(0)

    #turtle screen resize
    if(int(level) >= 1 and int(level) <= 2):
        screen.setworldcoordinates(-300, 300, 300, -300)
        turtle.penup()
        turtle.goto(-240,120)
        turtle.pendown()
    elif(int(level) == 3):
        screen.setworldcoordinates(-800, 800, 800, -800)
        turtle.penup()
        turtle.goto(-700,300)
        turtle.pendown()
    elif(int(level) == 4):
        screen.setworldcoordinates(-2100, 2100, 2100, -2100)
        turtle.penup()
        turtle.goto(-2050,750)
        turtle.pendown()
    else:
        screen.setworldcoordinates(-10000, 10000, 10000, -10000)
        turtle.penup()
        turtle.goto(-8000,4000)
        turtle.pendown()
    
    exp = P
    for _ in range(int(level) - 1):
        exp = exp.replace("D", P)
        exp = exp.replace("+", T[1])
        exp = exp.replace("-", T[2])
    exp = exp.replace("D", T[0])
    print("[ level %s 표현식 ] "%level+exp+"\n\n")
    for comand in exp:  #draw turtle
        if(comand == "+"):
            turtle.left(60)
        elif(comand == "-"):
            turtle.right(60)
        else:
            turtle.forward(50)

#Button click event
def inputText():
    global P
    result1 = pattern.get()
    P = result1
    result2 = level.get()
    drawTurtle(result2)


if(__name__ == "__main__"):
    
    #Create Entry (Pattern)
    pattern = Entry(root)
    pattern.insert(0, "pattern 입력")
    pattern.bind("<FocusIn>", lambda args: pattern.delete('0','end'))
    pattern.place(x=40,y=10, width=600, height=30)
    
    #Create Entry (Level)
    level = Entry(root)
    level.insert(0, "level 입력")
    level.bind("<FocusIn>", lambda args: level.delete('0','end'))
    
    level.place(x=40,y=45, width=600, height=30)
    #Button
    Button(root, text="입력", command=inputText).place(x=650,y=10, width=120, height=70)
    
    #Canvas
    canvas = turtle.ScrolledCanvas(root)
    canvas.place(x=35, y=80, width=740, height=520)

    screen = turtle.TurtleScreen(canvas)
    turtle = turtle.RawTurtle(screen)

    root.mainloop()
