from turtle import *
shape("turtle")
# we want to paint a house

#step 1:   draw a square
speed(230)

width(7)
color("red")

forward(200)
right (90)
forward(200)
right(90)
forward(200)
right(90)
forward(200)
begin_fill()
goto(100,100)
goto(200,0)
end_fill()
penup()

#კარები
goto(75,-200)
pendown()
color("brown")
forward(140)
right(90)
forward(50)
right(90)
forward(140)
right(90)
forward(50)

penup()

#ფანჯარა
color("black")
goto(15,-60)
pendown()
left(90)
forward(70)
left(90)
forward(45)
left(90)
forward(70)
left(90)
forward(45)


penup()

#ფანჯარა
color("black")
goto(140,-60)
pendown()
left(90)
forward(70)
left(90)
forward(45)
left(90)
forward(70)
left(90)
forward(45)

exitonclick()