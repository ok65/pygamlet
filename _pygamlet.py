
# Library import
import pyglet

# Project import


class PyGamlet:

    def __init__(self, width=640, height=480, fullscreen=False):
        self.window = pyglet.window.Window(width=width, height=height, fullscreen=fullscreen)

        # Set all the on_something handlers
        for item in dir(self):
            if callable(getattr(self, item)):
                if item.startswith("on_"):
                    self.window.set_handler(item, getattr(self, item))

    def run(self):
        pyglet.app.run()

    def on_draw(self):
        pass


if __name__ == "__main__":

    pyg = PyGamlet()
    pyg.run()