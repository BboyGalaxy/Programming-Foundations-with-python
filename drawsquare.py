import turtle

def draw_square():
	window = turtle.Screen()
	window.bgcolor("red")

	brad = turtle.Turtle()	
	brad.shape("turtle")
	brad.color("yellow")
	brad.speed(2)
	
	count = 0
	while count < 4:
		brad.forward(100)
		brad.right(90)
		count += 1
	
	angie = turtle.Turtle()
	angie.shape("arrow")
	angie.color("blue")
	angie.circle(100)

	pedro = turtle.Turtle()
	pedro.color("green")
	pedro.forward(100)
	pedro.left(135)
	pedro.forward(75)
	pedro.left(90)
	pedro.forward(75)
	window.exitonclick()

draw_square()