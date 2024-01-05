def koch(l, n):
    if n <= 0 : forward(l)
    
    else:
        koch(l/3, n-1)
        left(60)
        koch(l/3, n-1)
        right(120)
        koch(l/3, n-1)
        left(60)
        koch(l/3, n-1)

def flocon(l, n):
    koch(l, n)
    right(120)
    koch(l, n)
    right(120)
    koch(l, n)
    
def shift_left(l):
    up()
    left(180)
    forward(l)
    left(180)
    down()

##
from turtle import *
speed(0)
l = 200
n = 5
shift_left(150)
flocon(l, n)
done()
##