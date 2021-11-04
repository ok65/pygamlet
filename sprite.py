
# Library imports
import pyglet
from collections import deque

# Project imports
from exceptions import *
from signal import SignalBoxClass, SignalDec


class Sprite(SignalBoxClass):

    def __init__(self, image=None, group=None):
        super().__init__()
        self.signals.set("DRAW", "UPDATE")
        self.rect = None
        self.image = image
        self.sprite = pyglet.sprite.Sprite(self.image)

    @SignalDec("DRAW")
    def draw(self):
        self.sprite.draw()

    @SignalDec("UPDATE")
    def update(self):
        pass



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
