from os import chdir; chdir(r"C:\path\poule_generator")
from math import pi, sin, cos, asin, degrees as deg, radians as rad
from random import uniform as rd, randint
from turtle_functions import forward as f, left as l, right as r, up, down, setangle, setpos, decoder
from processing_ import parse_to_img
from PIL import Image


def main():
    with open('myturtle.txt', 'w') as f:
        f.write(''.join(decoder.instructions))

    # img_table = parse_to_img('myturtle.txt', (image_square_size, image_square_size), pos_init)
    # a = Image.fromarray(img_table, 'RGBA')
    # a.save('image.png')


def my_arc(radius, portion=1., flipped=False, center=False, resolution=100):
    if center:
        r(90)
        up()
        f(radius)
        down()
        l(90)

    n = resolution
    for j in range(int(n*portion)):
        f(2 * pi * radius / n)
        if flipped:
            l(360 - (360 / n))
        else:
            l(360 / n)


def my_circle(radius, resolution=100):
    my_arc(radius, 1, False, True, resolution)


def my_hen(s, pos_init, ratio, randomness=False, arcs_resolution=100):
    #### Geometrical parameters ####
    # body
    body_radius = s / ratio

    if not randomness:
        # legs
        leg_length = body_radius * 1.3
        legs_spread_rel = .1
        foot_length = body_radius * .3
        foot_angle = 45

        # head
        head_radius = body_radius * .5
        eye_x_pos_rel = 1.4
        eye_y_pos_rel = .3
        eye_radius = body_radius * .1

        # beak
        beak_spread_rel = .07
        beak_length = head_radius * 1.6
        beak_angle = 10

        # crest
        crest_spread_rel = .1
        crest_angle = 10
        crest_side_length = body_radius * .4
        crest_number_of_parts = 3

        # tail
        tail_spread_rel = .03
        tail_angle = 20
        tail_side_length = body_radius * .4
        tail_number_of_parts = 2

        # wings
        wings_pos_rel_x = .7
        wings_pos_rel_y = .3
        wings_radius = body_radius * .35

    else:
        # legs
        leg_length = body_radius * rd(1.0, 1.6)
        legs_spread_rel = rd(.05, .15)
        foot_length = body_radius * rd(.1, .60)
        foot_angle = rd(30, 60)

        # head
        head_radius = body_radius * rd(.3, .7)
        eye_x_pos_rel = rd(1.1, 1.7)
        eye_y_pos_rel = rd(.2, .4)
        eye_radius = body_radius * rd(.05, .15)

        # beak
        beak_spread_rel = rd(.02, .11)
        beak_length = head_radius * rd(.8, 2.2)

        # crest
        crest_spread_rel = rd(.05, .15)
        crest_angle = rd(1, 30)
        crest_side_length = body_radius * rd(.2, .7)
        crest_number_of_parts = randint(3, 6)

        # tail
        tail_spread_rel = rd(.02, .04)
        tail_angle = rd(1, 40)
        tail_side_length = body_radius * rd(.2, .6)
        tail_number_of_parts = randint(2, 3)

        # wings
        wings_pos_rel_x = rd(.5, .9)
        wings_pos_rel_y = rd(.15, .45)
        wings_radius = body_radius * rd(.2, .4)

        # other
        arcs_resolution = 20
        weird_circles = arcs_resolution

        # arcs_resolution_range = randint(0, 10)
        # weird_circles = arcs_resolution
        # if arcs_resolution_range >= 4:
        #     arcs_resolution = 100
        # elif arcs_resolution_range >= 2:
        #     arcs_resolution = 10
        # else:
        #     arcs_resolution = 10
        #     weird_circles = arcs_resolution

    ################################

    def make_leg():
        f(leg_length + foot_length)
        l(180)
        up()
        f(foot_length)
        down()
        l(180)

        l(foot_angle)
        f(foot_length)
        l(180)
        up()
        f(foot_length)
        down()
        setangle(-90)
        r(foot_angle)
        f(foot_length)
        l(180)
        up()
        f(foot_length)
        down()
        setangle(-90)

    def make_crest_or_tail(radius, init_angle, spread_rel, angle, side_length, number_of_parts):
        up()
        my_arc(radius, spread_rel, False, False, arcs_resolution)
        down()
        setangle(init_angle + angle)
        f(side_length)
        setangle(init_angle - 90)
        b = side_length * sin(rad(angle))
        c = radius * cos(rad(180 - (90 + spread_rel * 360)))
        crest_horiz_length = 2 * (b+c)
        up()
        f(crest_horiz_length)
        down()
        temp_angle = 180 - (init_angle + angle)
        setangle(temp_angle)
        if temp_angle > 0:
            l(180)
        f(side_length)
        l(180)
        up()
        f(side_length)
        down()
        setangle(init_angle)
        for i in range(number_of_parts):
            my_arc(crest_horiz_length / (2 * number_of_parts), .5, False, False, arcs_resolution)
            setangle(init_angle)

    # body
    my_circle(body_radius, weird_circles)

    # legs
    l(180)
    up()
    my_arc(body_radius, legs_spread_rel, True, False, arcs_resolution)
    down()
    setangle(-90)
    make_leg()
    setpos((pos_init[0], pos_init[1] + body_radius))
    l(90)
    up()
    my_arc(body_radius, legs_spread_rel, False, False, arcs_resolution)
    down()
    setangle(-90)
    make_leg()

    # head
    setpos((pos_init[0], pos_init[1] - body_radius - head_radius))
    my_circle(head_radius, weird_circles)
    l(90)
    up()
    f(head_radius * eye_x_pos_rel)
    l(90)
    f(head_radius * eye_y_pos_rel)
    down()
    my_circle(eye_radius, weird_circles)

    # beak
    setpos((pos_init[0] + head_radius, pos_init[1] - body_radius - head_radius))
    up()
    my_arc(head_radius, beak_spread_rel, False, False, arcs_resolution)
    down()
    beak_angle = deg(asin(head_radius * sin(beak_spread_rel * 2*pi) / beak_length))
    setangle(-beak_angle)
    f(beak_length)
    setangle(beak_angle)
    l(180)
    f(beak_length)

    # crest
    setpos((pos_init[0], pos_init[1] - body_radius - 2*head_radius))
    setangle(180)
    make_crest_or_tail(head_radius, 90, crest_spread_rel, crest_angle, crest_side_length, crest_number_of_parts)

    # tail
    setpos((pos_init[0] - body_radius, pos_init[1]))
    setangle(-90)
    make_crest_or_tail(body_radius, 180, tail_spread_rel, tail_angle, tail_side_length, tail_number_of_parts)

    # wings
    setpos((pos_init[0] + wings_pos_rel_x * body_radius, pos_init[1] - wings_pos_rel_y * body_radius))
    setangle(90)
    my_arc(wings_radius, .5, True, False, arcs_resolution)
    wings_vertical_length = 2 * body_radius * wings_pos_rel_y
    my_shift = wings_radius * .5
    setangle(180)
    f(my_shift)
    setangle()
    for i in range(2):
        setangle()
        my_arc(wings_vertical_length / 4, .5, True, False, arcs_resolution)
    setangle()
    f(my_shift)
    setangle(-90)
    my_arc(wings_radius, .5, True, False, arcs_resolution)


# chdir('')

image_square_size = 100  # Image carrée avec 'image_square_size' pixels de côté
pos_init = (image_square_size/2, image_square_size/2)
ratio = 7
arcs_resolution = 100

# my_hen(image_square_size, pos_init, ratio, True)

# main()
