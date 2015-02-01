# -*- coding: utf-8 -*-

import sfml as sf
import sys

WIDTH = 800
HEIGHT = 480
TITLE = "AB2015 Python Oyun - Tappy Plane"
GRAVITY = sf.Vector2(0, 0.1)

video_mode = sf.VideoMode(WIDTH, HEIGHT)

window = sf.RenderWindow(video_mode, TITLE)

try:
    bg_texture = sf.Texture.from_file(
        'assets/images/background.png')

    plane_texture = sf.Texture.from_file(
        'assets/images/planeRed1.png')
    s_buffer = sf.SoundBuffer.from_file(
        'assets/sounds/tone1.ogg')
    music = sf.Music.from_file(
        'assets/sounds/spaceTrash3.ogg')
    font = sf.Font.from_file(
        'assets/fonts/kenvector_future_thin.ttf')
except IOError:
    print("HATA VERDİ!!")
    sys.exit(-1)

background = sf.Sprite(bg_texture)
plane = sf.Sprite(plane_texture)
plane.position = 100, 100

plane_vel = sf.Vector2(0.0, 0.0)
sound = sf.Sound(s_buffer)

yazi = sf.Text("Python Oyun Kurs")
yazi.font = font
yazi.character_size = 25
yazi.position = 100, 100
yazi.color = sf.Color.BLACK

count = 0

while window.is_open:
    for event in window.events:
        if type(event) is sf.CloseEvent:
            window.close()
        if type(event) is sf.KeyEvent:
            if event.released and event.code is sf.Keyboard.SPACE:
                sound.play()

            if event.released and event.code is sf.Keyboard.W:
                count += 1
                yazi.string = "Python Oyun Kurs - {0}".format(count)

    # plane_vel += GRAVITY
    # plane.move(plane_vel)

    window.clear()
    window.draw(background)
    window.draw(plane)
    window.draw(yazi)
    window.display()