import turtle

bob = turtle.Turtle()
radius = float(input())
arc = int(input())

def circunference (turtle,radius,arc) :
    length = 2*radius*3.1415
    side = length/360
    for i in range(arc):
        turtle.fd(side)
        turtle.lt(1)

circunference(bob,radius,arc)
