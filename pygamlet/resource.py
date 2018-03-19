
# Library imports
import pyglet

# Project imports
from pygamlet.exceptions import *


class ResourceBundle:

    def __init__(self):

        self.images = _ImageResourceDict()
        self.media = _MediaResourceDict()

    def load(self):
        self.images.load_all()
        self.media.load_all()


class _ResourceDict:
    def __init__(self):
        self._path = dict()
        self._resource = dict()

    def __getitem__(self, key):
        try:
            return self._resource[key]
        except KeyError:
            if key in self._path:
                raise ResourceNotLoaded
            else:
                raise KeyError

    def __delitem__(self, key):
        del self._path[key]
        del self._resource[key]

    def __setitem__(self, key, value):
        self._path[key] = value

    def _load_resource(self, path):
        raise NotImplemented

    def load_all(self):
        for key, path in self._path.items():
            if key not in self._resource.keys():
                self._resource[key] = self._load_resource(path)


class _ImageResourceDict(_ResourceDict):

    def _load_resource(self, path):
        return pyglet.resource.image(path)


class _MediaResourceDict(_ResourceDict):

    def _load_resource(self, path):
        return pyglet.resource.media(path, streaming=False)

