# -*- coding: utf-8 -*-

import sfml as sf

WIDTH = 640
HEIGHT = 480
TITLE = "Python SFML Events"

window = sf.RenderWindow(sf.VideoMode(WIDTH, HEIGHT), TITLE)

while window.is_open:
    for event in window.events:
        if type(event) is sf.CloseEvent:
            window.close()
        if type(event) is sf.MouseMoveEvent:
            print("Fare hareket etti! %s" % event.position)

        if type(event) is sf.KeyEvent:
            if event.released and event.code is sf.Keyboard.ESCAPE:
                print("ESC'ye basıldı!")
                window.close()

            if not event.released and event.code is sf.Keyboard.W:
                print("W tuşuna basılıyor!")

    window.clear()

    window.display()