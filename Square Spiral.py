import turtle
import math

squareAmount = 100

screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("black")

colors = [
	"red",
	"orange",
	"yellow",
	"green",
	"blue",
	"purple",
	"black"
	]
pattern = turtle.Turtle()
pattern.speed(20)

for i in range (4*squareAmount):
	pattern.forward(i)
	pattern.left(91)
	pattern.pencolor(colors[math.ceil(i/4)%len(colors)])



turtle.done()
