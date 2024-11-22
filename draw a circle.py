import turtle #import the turtle module
bob = turtle.Turtle() #create a turtle object
import math

#-----------------
#function that draws a polygon with n number of sides, each has length
#------------------
def polygon(t, n, length):
    for i in range(n):
        bob.fd(length)  #call "forward" method, distance = 100 pixels
        bob.lt(360/n)   #call "left turn" method, angle = 90 degrees

#-----------------
#function that draws a circle with radius r
#------------------
def circle(t, r):
    #will draw circle of radius r by drawing a polygon of 50 sides, each side = circle circumference/50
    circumference = 2*math.pi*r #calculate circumference
    n = 50 #fixed number of side
    length = circumference/n #calculate length of each side
    polygon(t, n, length)
#call square function
circle(bob,300)

#wait for the user to do something
turtle.mainloop() 