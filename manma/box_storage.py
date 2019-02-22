from .box import Box


class BoxStorage(object):
    def __init__(self):  # O(1)
        pass

    def insert_box(self, side, height):  # O(lgn)
        pass

    def remove_box(self, side, height):  # O(lgn)
        pass

    def get_box(self, side, height) -> Box:  # O(lgn)
        """Return the box with minimal volume that answers given criteria."""
        pass

    def check_box(self, side, height) -> bool:  # O(lgn)
        pass

    def get_median_box(self) -> Box:  # O(1)
        """Return the box with the median volume."""
        pass
