# -*- coding: utf-8 -*-

import sfml as sf
from random import randint

WIDTH = 800
HEIGHT = 600
TITLE = "Python SFML Particle Simulation"
FPS = 60
LIFETIME = 100


class ParticleInfo:
    def __init__(self, velocity, lifetime):
        self.velocity = velocity
        self.lifetime = lifetime


class ParticleSystem:
    def __init__(self):
        self.v_array = None
        self.particles = None

    def load(self, size):
        self.v_array = sf.VertexArray(
            sf.PrimitiveType.POINTS,
            size
        )

        p_list = []

        for i in xrange(size):
            x = randint(-100, 100)
            y = randint(-100, 100)

            lifetime = randint(1, LIFETIME)

            p_info = ParticleInfo(sf.Vector2(x, y), lifetime)
            p_list.append(p_info)

        self.particles = dict(
            zip(self.v_array, p_list)
        )

window = sf.RenderWindow(sf.VideoMode(WIDTH, HEIGHT),
                         TITLE)
window.framerate_limit = 60
p_system = ParticleSystem()
p_system.load(1000)

for i in p_system.particles.keys():
    i.position = sf.Mouse.get_position(window)

    i.color = sf.Color(
        randint(0, 255),
        randint(0, 255),
        randint(0, 255),
        randint(0, 255)
    )

clock = sf.Clock()

while window.is_open:
    # Eventler
    for event in window.events:
        if type(event) is sf.CloseEvent:
            window.close()

    elap = clock.restart().seconds

    window.title = "FPS: %.2f - Particles: %d" % (
        (1.0 / elap), len(p_system.particles.keys())
    )

    # Update
    for i, j in p_system.particles.iteritems():
        i.position += j.velocity * elap
        j.lifetime -= 1

        if j.lifetime <= 0:
            j.lifetime = randint(1, LIFETIME)
            i.position = sf.Mouse.get_position(window)

    # Render
    window.clear()

    window.draw(p_system.v_array)

    window.display()