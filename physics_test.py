# -*- coding: utf-8 -*-

import sfml as sf
import pymunk # Chipmunk C/C++ # Box2D
import sys

window = sf.RenderWindow(sf.VideoMode(640, 480), "SFML Pymunk")
window.framerate_limit = 60

rad = 14
ball_elasticity = 0.8
friction = 0.8

space = pymunk.Space()
space.gravity = (0.0, -900.0)

circles = []

def create_circle(position):
    mass = 1
    inertia = pymunk.moment_for_circle(mass, 0, rad)
    body = pymunk.Body(mass, inertia)
    body.position = position
    # body.position = position
    shape = pymunk.Circle(body, rad)
    shape.elasticity = ball_elasticity
    shape.friction = friction
    space.add(body, shape)
    return shape

def create_line():
    body = pymunk.Body()
    body.position = (0, 600)
    line_shape = pymunk.Segment(body, (-400, -400), (700, -400), 15)
    line_shape.elasticity = 0.5
    space.add(line_shape)
    return line_shape

line = create_line()

while window.is_open:
    for event in window.events:
        if type(event) is sf.CloseEvent:
            window.close()
        if type(event) is sf.MouseButtonEvent and event.released:
            x, y = event.position
            y = 600 - y
            pos = pymunk.Vec2d(x, y)
            circles.append(create_circle(pos))

    window.clear()

    for c in circles:
        c_draw = sf.CircleShape(c.radius)
        x, y = c.body.position
        y = 600 - y
        c_draw.position = sf.Vector2(x, y)
        window.draw(c_draw)

    line_draw = sf.RectangleShape((640, 15))
    x, y = line.body.position
    y = y - 200
    line_draw.position = x, y
    line_draw.rotation = line.body.angle
    window.draw(line_draw)

    window.display()
    space.step(1/60.0)

sys.exit()