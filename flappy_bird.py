# -*- coding: utf-8 -*-

import sfml as sf
import sys
from animation import *

WIDTH = 288
HEIGHT = 505
TITLE = "Python SFML Flappy Bird"
FPS = 60


class Game:
    def __init__(self):
        self.window = sf.RenderWindow(sf.VideoMode(WIDTH, HEIGHT),
                                      TITLE)
        self.window.framerate_limit = FPS

        self.backgrounds = [None, None]
        self.grounds = [None, None]

        self.bird_texture = None
        self.bird_animation = None
        self.bird_sprite = None

        self.clock = sf.Clock()

    def run(self):
        if not self.load_assets():
            sys.exit(-1)

        self.bird_animation = Animation()
        self.bird_animation.texture = self.bird_texture

        self.bird_animation.add_frame(sf.Rectangle((0, 0), (34, 24)))
        self.bird_animation.add_frame(sf.Rectangle((34, 0), (34, 24)))
        self.bird_animation.add_frame(sf.Rectangle((68, 0), (34, 24)))

        self.bird_sprite = AnimatedSprite(sf.seconds(0.2),
                                          False,
                                          True)

        self.bird_sprite.position = sf.Vector2(50, 50)

        while self.window.is_open:
            for e in self.window.events:
                self.event_handler(e)

            elapsed_time = self.clock.restart()

            self.update(elapsed_time)
            self.render()

    def update(self, delta):
        # Backgrounds
        self.backgrounds[0].move(sf.Vector2(-3, 0) * delta.seconds)
        width = self.backgrounds[0].global_bounds.width
        x_coord = self.backgrounds[0].position.x + width

        self.backgrounds[1].position = sf.Vector2(x_coord, 0)

        if self.backgrounds[0].position.x <= -width:
            self.backgrounds[0], self.backgrounds[1] = \
                self.backgrounds[1], self.backgrounds[0]

        # Grounds
        self.grounds[0].move(sf.Vector2(-5, 0) * delta.seconds)
        width = self.grounds[0].global_bounds.width
        x_coord = self.grounds[0].position.x + width
        y_coord = HEIGHT - self.grounds[1].global_bounds.height

        self.grounds[1].position = sf.Vector2(x_coord, y_coord)

        if self.grounds[0].position.x <= -width:
            self.grounds[0], self.grounds[1] = \
                self.grounds[1], self.grounds[0]

        self.bird_sprite.play(self.bird_animation)
        self.bird_sprite.move(sf.Vector2(0, 1))
        self.bird_sprite.update(delta)


    def render(self):
        self.window.clear()

        self.window.draw(self.backgrounds[0])
        self.window.draw(self.backgrounds[1])

        self.window.draw(self.grounds[0])
        self.window.draw(self.grounds[1])

        self.window.draw(self.bird_sprite)

        self.window.display()

    def event_handler(self, event):
        if type(event) is sf.CloseEvent:
            self.window.close()
        if type(event) is sf.KeyEvent and event.released:
            if event.code is sf.Keyboard.SPACE:
                self.bird_sprite.move((0, -15))

    def load_assets(self):
        try:
            bg_texture = sf.Texture.from_file(
                "assets/images/flappy_background.png"
            )

            self.backgrounds[0] = sf.Sprite(bg_texture)
            self.backgrounds[1] = sf.Sprite(bg_texture)

            ground_texture = sf.Texture.from_file(
                "assets/images/ground.png"
            )

            self.grounds[0] = sf.Sprite(ground_texture)
            self.grounds[1] = sf.Sprite(ground_texture)

            y_coord = HEIGHT - self.grounds[0].global_bounds.height
            self.grounds[0].position = sf.Vector2(0, y_coord)
            self.grounds[1].position = sf.Vector2(
                self.grounds[1].global_bounds.width,
                y_coord
            )

            self.bird_texture = sf.Texture.from_file(
                "assets/images/bird.png"
            )
        except IOError:
            print("DOSYALAR YUKLENMEDI")
            return False

        return True


if __name__ == "__main__":
    Game().run()