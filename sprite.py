
# Project imports
import pyglet
from collections import deque

# Library imports
from pygamlet.exceptions import *


class Sprite:

    def __init__(self, image=None, group=None):

        self.rect = None
        self.image = image
        self.sprite = pyglet.sprite.Sprite(self.image)

    def draw(self):
        self.sprite.draw()


class SpriteGroup:

    def __init__(self):
        self._sprites = []

    @property
    def sprites(self):
        return self._sprites.copy()

    def add(self, sprite):
        if sprite not in self._list:
            self._sprites.append(sprite)

    def remove(self, sprite):
        self._sprites.remove(sprite)

    def draw(self):
        for sprite in self._sprites:
            sprite.draw()
