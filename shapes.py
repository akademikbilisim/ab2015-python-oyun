# -*- coding: utf-8 -*-

import sfml as sf

WIDTH = 640
HEIGHT = 480
TITLE = "Python SFML Shapes"

window = sf.RenderWindow(sf.VideoMode(WIDTH, HEIGHT), TITLE)

circle = sf.CircleShape(50)
circle.origin = circle.radius, circle.radius

alpha = 255
circle.fill_color = sf.Color(123, 43, 25, alpha)

rectangle = sf.RectangleShape((100, 100))
rectangle.fill_color = sf.Color.BLUE
rectangle.origin = rectangle.size.x / 2, rectangle.size.y / 2
rectangle.position = 200, 200

while window.is_open:
    for event in window.events:
        if type(event) is sf.CloseEvent:
            window.close()
        if type(event) is sf.MouseWheelEvent:
            alpha += event.delta

            if not 0 <= alpha <= 255:
                print "Bozuk!"
                alpha = 0

            circle.fill_color = sf.Color(123, 43, 25, alpha)

    circle.position = sf.Mouse.get_position(window)

    if sf.Keyboard.is_key_pressed(sf.Keyboard.LEFT):
        rectangle.rotate(-5)
    if sf.Keyboard.is_key_pressed(sf.Keyboard.RIGHT):
        rectangle.rotate(5)

    window.clear()
    window.draw(circle)
    window.draw(rectangle)
    window.display()