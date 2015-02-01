# -*- coding: utf-8 -*-

import sfml as sf
from random import randint

WIDTH = 800
HEIGHT = 600
TITLE = "Python SFML Pong Game"

settings = sf.ContextSettings()
settings.antialiasing_level = 8

FPS = 60
SPEED_FACTOR = 60


class Game:
    def __init__(self):
        self.window = sf.RenderWindow(sf.VideoMode(WIDTH, HEIGHT),
                                      TITLE,
                                      sf.Style.DEFAULT,
                                      settings)
        self.window.framerate_limit = FPS
        self.clock = sf.Clock()

        # Top
        self.ball = sf.CircleShape(30)
        self.ball.origin = self.ball.radius, self.ball.radius
        self.ball.position = self.window.size / 2

        # Sol Çubuk
        self.p_left = sf.RectangleShape((50, 200))
        x = self.p_left.size.x / 2
        y = (HEIGHT - self.p_left.size.y) / 2
        self.p_left.position = sf.Vector2(x, y)

        # Sağ Çubuk
        self.p_right = sf.RectangleShape((50, 200))
        x = WIDTH - (self.p_right.size.x * 1.5)
        y = (HEIGHT - self.p_right.size.y) / 2
        self.p_right.position = sf.Vector2(x, y)

        self.ball_vel = sf.Vector2(randint(-5, 5),
                                   randint(-5, 5))

    def run(self):
        while self.window.is_open:
            for e in self.window.events:
                self.event_handler(e)
            elapsed_time = self.clock.restart().seconds

            self.window.title = "Python SFML Pong Game - %.2f" % \
                                (1.0 / elapsed_time)

            self.update(elapsed_time)
            self.render()

    def event_handler(self, event):
        if type(event) is sf.CloseEvent:
            self.window.close()

    def update(self, delta):
        # Hareket Ettirme
        self.ball.move(self.ball_vel * delta * SPEED_FACTOR)

        if sf.Keyboard.is_key_pressed(sf.Keyboard.W):
            self.p_left.move(sf.Vector2(0, -5) * delta * SPEED_FACTOR)
        if sf.Keyboard.is_key_pressed(sf.Keyboard.S):
            self.p_left.move(sf.Vector2(0, 5) * delta * SPEED_FACTOR)

        if sf.Keyboard.is_key_pressed(sf.Keyboard.UP):
            self.p_right.move(sf.Vector2(0, -5) * delta * SPEED_FACTOR)
        if sf.Keyboard.is_key_pressed(sf.Keyboard.DOWN):
            self.p_right.move(sf.Vector2(0, 5) * delta * SPEED_FACTOR)

        # Çarpışma Tespiti
        if not self.ball.radius < self.ball.position.y < HEIGHT - self.ball.radius:
            x, y = self.ball_vel
            y *= -1.0
            self.ball_vel = sf.Vector2(x, y)

    def render(self):
        self.window.clear()
        self.window.draw(self.ball)
        self.window.draw(self.p_left)
        self.window.draw(self.p_right)
        self.window.display()


if __name__ == '__main__':
    Game().run()