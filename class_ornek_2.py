# -*- coding: utf-8 -*-

import sfml as sf


WIDTH = 640
HEIGHT = 480
TITLE = "Python SFML Class Example 2"

settings = sf.ContextSettings()
settings.depth_bits = 24
settings.antialiasing_level = 1


class Bla:
    # initialize
    def __init__(self):
        self.window = sf.RenderWindow(sf.VideoMode(WIDTH, HEIGHT),
                                      TITLE,
                                      sf.Style.DEFAULT,
                                      settings)

        self.circle = sf.CircleShape(75)

        self.rectangle = sf.RectangleShape((150, 200))
        self.rectangle.position = 200, 100

        self.view = sf.View()
        self.view.reset(
            sf.Rectangle((0, 0), self.window.size)
        )

        self.window.view = self.view

    def run(self):
        while self.window.is_open:
            for event in self.window.events:
                self.event_handler(event)

            self.update()
            self.render()

    def update(self):
        if sf.Keyboard.is_key_pressed(sf.Keyboard.LEFT):
            self.view.move(-5, 0)
        if sf.Keyboard.is_key_pressed(sf.Keyboard.RIGHT):
            self.view.move(5, 0)
        if sf.Keyboard.is_key_pressed(sf.Keyboard.UP):
            self.view.rotate(-5)
        if sf.Keyboard.is_key_pressed(sf.Keyboard.DOWN):
            self.view.rotate(5)

        self.circle.position = sf.Mouse.get_position(self.window)

    def event_handler(self, event):
        if type(event) is sf.CloseEvent:
            self.window.close()
        if type(event) is sf.MouseWheelEvent:
            self.circle.radius += event.delta

    def render(self):
        self.window.clear()
        self.window.draw(self.circle)
        # self.window.draw(self.rectangle)
        self.window.display()


if __name__ == '__main__':
    Bla().run()