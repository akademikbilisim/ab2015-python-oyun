# -*- coding: utf-8 -*-

import sfml as sf

WIDTH = 800
HEIGHT = 600
TITLE = "Python SFML State Machine Example"
FPS = 60

class State:
    MENU = 0
    SETTINGS = 1
    PAUSED = 2
    PLAYING = 3

window = sf.RenderWindow(sf.VideoMode(WIDTH, HEIGHT),
                         TITLE)
window.framerate_limit = FPS

game_state = State.MENU
last_state = None

color = sf.Color.WHITE


while window.is_open:
    for event in window.events:
        if type(event) is sf.CloseEvent:
            window.close()
        if type(event) is sf.KeyEvent and event.released:
            # Escape Tuşu
            if event.code is sf.Keyboard.ESCAPE:
                if game_state is State.PLAYING:
                    last_state = game_state
                    game_state = State.PAUSED

                elif game_state is State.PAUSED:
                    last_state = game_state
                    game_state = State.PLAYING

            # Settings Tuşu
            if event.code is sf.Keyboard.S:
                if game_state in [State.MENU, State.PAUSED]:
                    last_state = game_state
                    game_state = State.SETTINGS

            # Play tuşu
            if event.code is sf.Keyboard.P:
                if game_state in [State.MENU, State.PAUSED]:
                    last_state = game_state
                    game_state = State.PLAYING

            # Menu tuşu
            if event.code is sf.Keyboard.M:
                if game_state in [State.PAUSED, State.SETTINGS]:
                    last_state = game_state
                    game_state = State.MENU

    if game_state is State.MENU:
        color = sf.Color.BLUE
    elif game_state is State.SETTINGS:
        color = sf.Color.RED
    elif game_state is State.PAUSED:
        color = sf.Color.GREEN
    elif game_state is State.PLAYING:
        color = sf.Color.YELLOW

    window.clear(color)

    window.display()
