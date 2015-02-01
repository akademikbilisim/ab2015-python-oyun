# -*- coding: utf-8 -*-

import sfml as sf

WIDTH = 800
HEIGHT = 480
TITLE = "AB2015 Python Oyun Kursu"

pencere = sf.RenderWindow(sf.VideoMode(WIDTH, HEIGHT), TITLE)

cember = sf.CircleShape(150)

cember.fill_color = sf.Color.BLUE
cember.origin = cember.radius, cember.radius
cember.position = 200, 200

dikdortgen = sf.RectangleShape(
    sf.Vector2(150, 250)
)

dikdortgen.fill_color = sf.Color.RED
dikdortgen.outline_thickness = 2
dikdortgen.outline_color = sf.Color.BLUE

dikdortgen.origin = dikdortgen.size.x / 2, dikdortgen.size.y / 2

dikdortgen.rotate(15)

while pencere.is_open:
    for event in pencere.events:

        if type(event) is sf.CloseEvent:
            pencere.close()
        if type(event) is sf.KeyEvent:
            if event.released and event.code is sf.Keyboard.ESCAPE:
                pencere.close()

            if event.released and event.code is sf.Keyboard.W:
                cember.point_count += 1

            if event.released and event.code is sf.Keyboard.S:
                cember.point_count -= 1

    dikdortgen.position = sf.Mouse.get_position(pencere)

    pencere.clear()
    # pencere.draw(cember)
    pencere.draw(dikdortgen)
    pencere.display()