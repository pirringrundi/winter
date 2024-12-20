import turtle
screen = turtle.Screen()
screen.screensize(800,800)
screen.bgcolor('lightsteelblue')




t_ground = turtle.Turtle()
t = turtle.Turtle()




t.speed(0)


t_ground.speed(0)
t_ground.pencolor('white')
t_ground.fillcolor("white")
t_ground.penup()
t_ground.goto(-1000,-100)
t_ground.pendown()
t_ground.begin_fill()
t_ground.goto(1000,-100)
t_ground.goto(1000,-1000)
t_ground.goto(1000,-1000)
t_ground.goto(-1000,-1000)
t_ground.end_fill()

t.pencolor('white')
t.fillcolor("white")

t.goto(0,0)
t.penup()

t.goto(-100,-100)


t.pendown()
t.begin_fill()
t.circle(50)
t.end_fill()
t.penup()
t.goto(-100,-10)

t.pendown()
t.begin_fill()
t.circle(35)
t.end_fill()
t.penup()


t.goto(-100,50)
t.begin_fill()
t.pendown()
t.circle(25)
t.end_fill()
t.penup()
t.goto(-100,0)




t.pendown()
t.pencolor('black')
t.fillcolor("black")
t.penup()
t.goto(-90,75)

t.pendown()
t.begin_fill()
t.circle(5)
t.end_fill()
t.penup()
t.goto(-110,75)


t.pendown()
t.begin_fill()
t.circle(5)
t.end_fill()
t.penup()

t.fillcolor('orange')
t.pencolor('orange')
t.pendown()
t.goto(-100,70)
t.begin_fill()
t.circle(5)
t.end_fill()
t.penup()
t.goto(0,70)

t.pencolor('salmon4')
t.fillcolor('salmon4')

t.penup()
t.goto(0,-100)
t.pendown()
t.begin_fill()
t.forward(250)
t.left(90)
t.forward(250)
t.left(90)
t.forward(250)
t.left(90)
t.forward(250)
t.left(90)
t.end_fill()
t.penup()
t.goto(250,250)
t.pendown()
t.end_fill()


t.penup()
t.goto(0,300)
t.pendown()
t.pencolor('green')
t.write("Happy Holidays", font=("arial", 30, "bold"), align="center")
t.pencolor('burlywood4')
t.fillcolor('burlywood3')
t.penup()
t.goto(75,-100)
t.pendown()
t.begin_fill()
t.forward(60)
t.left(90)
t.forward(120)
t.left(90)
t.forward(60)
t.left(90)
t.forward(120)
t.left(90)
t.end_fill()




















#house
enter = input("press enter to begin")
t.showturtle()
t.clear()


screen.bgcolor('lightskyblue2')

t_ground.speed(0)
t_ground.pencolor('black')
t_ground.fillcolor("burlywood3")
t_ground.penup()
t_ground.goto(-1000,-100)
t_ground.pendown()
t_ground.begin_fill()
t_ground.goto(1000,-100)
t_ground.goto(1000,-1000)
t_ground.goto(1000,-1000)
t_ground.goto(-1000,-1000)
t_ground.end_fill()
t.goto(0,0)

t.pencolor('palegreen4')
t.fillcolor("palegreen4")

t.pendown()
t.begin_fill()
t.goto(10,60)
t.goto(-30,20)
t.goto(50,20)
t.goto(10,60)
t.penup()

t.end_fill()
t.penup()
t.goto(10,35)

t.pendown()
t.begin_fill()
t.goto(-50,-15)
t.goto(70,-15)
t.goto(10,35)
t.end_fill()


t.penup()
t.goto(10,10)
t.pendown()
t.begin_fill()
t.goto(-70,-40)
t.goto(90,-40)
t.goto(10,10)
t.end_fill()
t.penup()

t.pencolor('saddlebrown')
t.fillcolor("saddlebrown")
t.goto(20,-100)
t.pendown()
t.begin_fill()
t.goto(0,-100)
t.goto(0,-40)
t.goto(20,-40)
t.goto(20,-100)
t.end_fill()
t.penup()
t.goto(0,0)
t.pendown()


t.pencolor('red')
t.fillcolor("green")

t.penup()
t.goto(50,-100)
t.pendown()
t.begin_fill()
t.forward(25)
t.left(90)
t.forward(25)
t.left(90)
t.forward(25)
t.left(90)
t.forward(25)
t.left(90)
t.end_fill()



t.pencolor('red')
t.fillcolor("green")

t.penup()
t.goto(80,-100)
t.pendown()
t.begin_fill()
t.forward(25)
t.left(90)
t.forward(25)
t.left(90)
t.forward(25)
t.left(90)
t.forward(25)
t.left(90)
t.end_fill()
t.penup()

t.fillcolor('red')
t.pencolor('green')
t.goto(65,-75)
t.pendown()
t.begin_fill()
t.forward(25)
t.left(90)
t.forward(25)
t.left(90)
t.forward(25)
t.left(90)
t.forward(25)
t.left(90)
t.end_fill()


t.penup()

t.goto(20,-20)
t.begin_fill()
t.pendown()
t.circle(5)
t.end_fill()






turtle.done()
