class Box(object):
    def __init__(self, side, height):
        self._side = side
        self._height = height

    def volume(self):
        return self._side * self._side * self._height
