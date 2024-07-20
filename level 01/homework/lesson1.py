from turtle import *


#we want to paint a house

#step1:  draw a square
shape("turtle")

speed(4)
width(8)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door
begin_fill()
forward(70)
color("yellow")
left(90)
forward(120)    #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


#drawing a window
left(30)
penup()
forward(120)
left(90)
forward(20)
pendown()
begin_fill()
color("blue")
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward (40)
end_fill()

#drawing 2nd window

penup()
left(90)
forward(125) 
pendown()
begin_fill()
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()



exitonclick()