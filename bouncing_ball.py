# -*- coding: utf-8 -*-

import sfml as sf

WIDTH = 640
HEIGHT = 480
TITLE = "Python SFML Bouncing Ball"
SPEED_FACTOR = 60

settings = sf.ContextSettings()
settings.antialiasing_level = 8


class Game:
    def __init__(self):
        self.window = sf.RenderWindow(sf.VideoMode(WIDTH, HEIGHT),
                                      TITLE,
                                      sf.Style.DEFAULT,
                                      settings)
        self.window.framerate_limit = 60

        self.circle = sf.CircleShape(30)
        self.circle.origin = self.circle.radius, self.circle.radius
        self.circle.position = self.window.size / 2
        self.c_vel = sf.Vector2(5, -5)

        self.clock = sf.Clock()

    def run(self):
        while self.window.is_open:
            for event in self.window.events:
                self.event_handler(event)

            elapsed_time = self.clock.restart().seconds

            self.update(elapsed_time)
            self.render()

    def event_handler(self, event):
        if type(event) is sf.CloseEvent:
            self.window.close()

    def update(self, delta):
        if not (self.circle.radius < self.circle.position.y < HEIGHT - self.circle.radius):
            x, y = self.c_vel
            y *= -1.0
            self.c_vel = sf.Vector2(x, y)

        if not self.circle.radius < self.circle.position.x < WIDTH - self.circle.radius:
            x, y = self.c_vel
            x *= -1.0
            self.c_vel = sf.Vector2(x, y)

        self.circle.move(self.c_vel * delta * SPEED_FACTOR)

    def render(self):
        self.window.clear()
        self.window.draw(self.circle)
        self.window.display()


if __name__ == '__main__':
    oyun = Game()
    oyun.run()
    # Game().run()