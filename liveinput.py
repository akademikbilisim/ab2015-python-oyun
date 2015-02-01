# -*- coding: utf-8 -*-

import sfml as sf

WIDTH = 640
HEIGHT = 480
TITLE = "Python SFML Live Input"

window = sf.RenderWindow(sf.VideoMode(WIDTH, HEIGHT), TITLE)

while window.is_open:
    for event in window.events:
        if type(event) is sf.CloseEvent:
            window.close()

    pos = sf.Mouse.get_position(window)
    # print("Farenin anlık pozisyonu {0}".format(pos))

    if sf.Keyboard.is_key_pressed(sf.Keyboard.SPACE):
        print("SPACE tuşuna basılıyor!")

    if sf.Keyboard.is_key_pressed(sf.Keyboard.M):
        pos = sf.Mouse.get_position()
        print("Farenin ekrandaki pozisyonu {0}".format(pos))

        if sf.Keyboard.is_key_pressed(sf.Keyboard.W):
            print("M ve W birlikte basılıyor!")

    window.clear(sf.Color.BLACK)

    window.display()