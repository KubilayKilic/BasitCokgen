#turtle module---
import turtle
import math
bob = turtle.Turtle()
print(bob)
'''turtle module provides a function called Trutle
that creates a Turtle object which assinged to
a variable named bob.
Bob refers to an object
with type Turtle as defined in module turtle.'''

'''
draw square inefficient way
bob.fd(100)    #go forward 100 pixels
bob.lt(90)     #look left 90degree tilt from x axis
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
'''

'''
draw square efficiently
for i in range (4):
    bob.fd(100)
    bob.lt(90)
turtle.mainloop()
'''

#ENCAPSULATION

def kare(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)
        
kare(bob)


'''GENERALIZATION
def square(t, length):
    for i in range (4):
        t.fd(length)
        t.lt(90)
        
square(bob, 100)
'''

''' More Generalization
def polygon (t, n, length):
    angle = 360 / n
    for i in range (n):
        t.fd(length)
        t.lt(angle)
polygon(bob, n=8, length=90)
'''
'''
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle /n

    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)
'''

#============================================#

'''
def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) +1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def circle(t, r):
    arc(t, r, 360)

circle(bob, 100) #100 çaplı çember çizer
'''


'''def polyline (t, n ,length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)
polyline(bob, 8, 100, 45)

'''
