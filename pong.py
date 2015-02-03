# -*- coding: utf-8 -*-

import sfml as sf
from random import randint
from forbiddenfruit import curse
import sys


def new_intersects(obj, rectangle):
    l, t, w, h = rectangle
    rectangle = sf.Rectangle((l, t), (w, h))

    left = max(obj.left, rectangle.left)
    top = max(obj.top, rectangle.top)
    right = min(obj.right, rectangle.right)
    bottom = min(obj.bottom, rectangle.bottom)

    if left < right and top < bottom:
        return sf.Rectangle((left, top), (right - left, bottom - top))


curse(sf.Rectangle, 'intersects', new_intersects)

WIDTH = 800
HEIGHT = 600
TITLE = "Python SFML Pong Game"

settings = sf.ContextSettings()
settings.antialiasing_level = 8

FPS = 60
SPEED_FACTOR = 60
MARGIN = 75


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

        x = randint(1, 5)
        y = randint(1, 5)

        if randint(0, 1) % 2 == 0:
            x *= -1.0

        if randint(0, 1) % 2 == 0:
            y *= -1.0

        self.ball_vel = sf.Vector2(x, y)

        self.ball_sound = None

        # Skor Değişkenleri
        self.left_score = 0
        self.right_score = 0

        self.font = None

    def run(self):
        if not self.load_assets():
            sys.exit(-1)

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

        # SOL Çubuk Sınırları
        if self.p_left.position.y < 0:
            x, y = self.p_left.position
            y = 0
            self.p_left.position = sf.Vector2(x, y)

        if self.p_left.position.y > HEIGHT - self.p_left.size.y:
            x, y = self.p_left.position
            y = HEIGHT - self.p_left.size.y
            self.p_left.position = sf.Vector2(x, y)

        # Sağ Çubuk Sınırları
        if self.p_right.position.y < 0:
            x, y = self.p_right.position
            y = 0
            self.p_right.position = sf.Vector2(x, y)

        if self.p_right.position.y > HEIGHT - self.p_right.size.y:
            x, y = self.p_right.position
            y = HEIGHT - self.p_right.size.y
            self.p_right.position = sf.Vector2(x, y)


        # Çarpışma Tespiti
        if not self.ball.radius < self.ball.position.y < HEIGHT - self.ball.radius:
            x, y = self.ball_vel
            y *= -1.0
            self.ball_vel = sf.Vector2(x, y)

        # SOL Çubuk ve Top
        if self.p_left.global_bounds.intersects(self.ball.global_bounds):
            x, y = self.ball_vel
            x *= -1.0 * 1.20
            self.ball_vel = sf.Vector2(x, y)
            self.ball_sound.play()

        # SAĞ Çubuk Top
        if self.p_right.global_bounds.intersects(self.ball.global_bounds):
            x, y = self.ball_vel
            x *= -1.0 * 1.20
            self.ball_vel = sf.Vector2(x, y)
            self.ball_sound.play()

        # Kaleleri kontrol et
        if not self.ball.radius < self.ball.position.x < WIDTH - self.ball.radius:

            # Skor ver
            if self.ball.radius >= self.ball.position.x:
                self.right_score += 1
                x, y = self.p_right.size
                if y > x:
                    y *= 0.95
                self.p_right.size = sf.Vector2(x, y)
            else:
                self.left_score += 1
                x, y = self.p_left.size
                if y > x:
                    y *= 0.95
                self.p_left.size = sf.Vector2(x, y)

            # Sol Çubuk
            x = self.p_left.size.x / 2
            y = (HEIGHT - self.p_left.size.y) / 2
            self.p_left.position = sf.Vector2(x, y)

            # Sağ Çubuk
            x = WIDTH - (self.p_right.size.x * 1.5)
            y = (HEIGHT - self.p_right.size.y) / 2
            self.p_right.position = sf.Vector2(x, y)

            self.ball.position = self.window.size / 2

            # Top hızını sabitliyoruz
            x = randint(1, 5)
            y = randint(1, 5)

            if randint(0, 1) % 2 == 0:
                x *= -1.0

            if randint(0, 1) % 2 == 0:
                y *= -1.0

            self.ball_vel = sf.Vector2(x, y)

    def render(self):
        self.window.clear()
        self.window.draw(self.ball)
        self.window.draw(self.p_left)
        self.window.draw(self.p_right)

        # Fontlar
        scr_lft_text = sf.Text(str(self.left_score))
        scr_lft_text.font = self.font
        scr_lft_text.character_size = 60
        x = (self.window.size.x / 2) - scr_lft_text.global_bounds.width - MARGIN
        y = 50
        scr_lft_text.position = sf.Vector2(x, y)
        scr_lft_text.color = sf.Color.WHITE

        scr_rght_text = sf.Text(str(self.right_score))
        scr_rght_text.font = self.font
        scr_rght_text.character_size = 60
        x = (self.window.size.x / 2) + MARGIN
        y = 50
        scr_rght_text.position = sf.Vector2(x, y)
        scr_rght_text.color = sf.Color.WHITE

        self.window.draw(scr_lft_text)
        self.window.draw(scr_rght_text)

        self.window.display()

    def load_assets(self):
        try:
            buffer = sf.SoundBuffer.from_file(
                'assets/sounds/tone1.ogg'
            )
            self.ball_sound = sf.Sound(buffer)
            self.font = sf.Font.from_file(
                'assets/fonts/kenvector_future_thin.ttf'
            )
        except IOError:
            return False

        return True


if __name__ == '__main__':
    Game().run()