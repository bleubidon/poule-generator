from turtle import *
speed(0)
mainloop()
tracer(0, 0)

def go_to_up_left_corner():
    up()
    left(180)
    forward(750)
    right(90)
    forward(370)
    right(90)
    down()


def mycircle():
    sides = 10
    length = 50

    for j in range(sides):
        forward(20*length/sides)
        left(360 / sides)


def my_weird():
    sides = 6
    length = 50
    n = 5

    for i in range(n):
        for j in range(sides):
            f(length)
            l(360//sides)
        length += 20


def my_koch():
    def koch(l, n):
        if n <= 0:
            forward(l)

        else:
            koch(l / 3, n - 1)
            left(60)
            koch(l / 3, n - 1)
            right(120)
            koch(l / 3, n - 1)
            left(60)
            koch(l / 3, n - 1)

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

    speed(0)
    l = 200
    n = 7
    # shift_left(350)
    flocon(l, n)

# mykoch()
# myweird
# forward(200)
mycircle()



update()
done()











