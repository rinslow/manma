class Box(object):
    def __init__(self, side, height):
        self._side = side
        self._height = height

    def volume(self):
        return self._side * self._side * self._height

    def __lt__(self, other):
        return self.volume() < other

    def __eq__(self, other):
        return self.volume() == other

    def __gt__(self, other):
        return self.volume() > other

    def __repr__(self):
        return "Box(side=%s, height=%s)" % (self._side, self._height)
