from .box import Box
from .rbt import RedBlackTree, NIL
from .heap import MaxHeap, MinHeap


class SideNode(object):
    def __init__(self, side):
        self.side = side
        self.heights = RedBlackTree()

    def __lt__(self, other):  # This is like C#s CompareTo
        return self.side < other

    def __eq__(self, other):
        return self.side == other

    def __gt__(self, other):
        return self.side > other


class BoxStorage(object):
    def __init__(self):  # O(1)
        self.sides = RedBlackTree()
        self.boxes_max_heap = MaxHeap()
        self.boxes_min_heap = MinHeap()

    def insert_box(self, side, height):  # O(lgn) + O(lgm) -> O(lgnm)
        # Red Black Trees  # O(lgn) + O(lgm) -> O(lg(nm))
        side_node = self.sides.search(side)

        if side_node == NIL:  # The side we want does not exist
            side_node = SideNode(side)
            side_node.heights.insert(height)
            self.sides.insert(side_node)

        else:
            side_node.key.heights.insert(height)

        # Heaps O(lg(max(n, m)))
        box = Box(side, height)

        if self.boxes_max_heap.size == 0 or box < self.boxes_max_heap.top():
            self.boxes_max_heap.insert(box)

        else:
            self.boxes_min_heap.insert(box)

        if self.boxes_max_heap.size - self.boxes_min_heap.size > 1:
            self.boxes_min_heap.insert(self.boxes_max_heap.extract())

        if self.boxes_min_heap.size - self.boxes_max_heap.size > 1:
            self.boxes_max_heap.insert(self.boxes_min_heap.extract())

    def remove_box(self, side, height):  # O(max(n, m))
        # Red Black Trees: O(lgm) + O(lgn) -> O(lgnm)
        side_node = self.sides.search(side)
        if side_node == NIL:
            raise KeyError("Can't remove box, box does not exist")

        height_node = side_node.key.heights.search(height)
        if height_node == NIL:
            raise KeyError("Can't remove box, box does not exist")

        side_node.key.heights.delete(height_node)

        if side_node.key.heights.root == NIL:
            self.sides.delete(side_node)

        # Heaps: Couldn't find a way to find it that's better than O(max(n, m)
        volume = Box(side, height).volume()

        for index in range(1, len(self.boxes_min_heap.array) + 1):
            item = self.boxes_min_heap.item_at(index)
            if item == volume:
                self.boxes_min_heap.delete_item_at_index(index)
                return

        for index in range(1, len(self.boxes_max_heap.array) + 1):
            item = self.boxes_max_heap.item_at(index)
            if item == volume:
                self.boxes_max_heap.delete_item_at_index(index)
                return

    def get_box(self, side, height) -> Box:  # O(mlgn)
        """Return the box with minimal volume that answers given criteria."""
        all_side_nodes = [side_node
                          for side_node
                          in self.sides.inorder_walk()
                          if side_node.key >= side]

        minimal_volume = float("infinity")
        minimal_volume_side = 0
        minimal_volume_height = 0

        for side_node in all_side_nodes:
            minimal_height = side_node.heights.search_successor(height)
            volume = Box(side_node.key, minimal_height).volume()

            if volume < minimal_volume:
                minimal_volume = volume
                minimal_volume_height = minimal_height
                minimal_volume_side = side_node.key

        if minimal_volume == float("inifinity"):
            raise KeyError("No such box exists")

        return Box(minimal_volume_side, minimal_volume_height)

    def check_box(self, side, height) -> bool:  # O(mlgn)
        all_side_nodes = [side_node
                          for side_node
                          in self.sides.inorder_walk()
                          if side_node.key >= side]

        if len(all_side_nodes) == 0:
            return False

        for side_node in all_side_nodes:
            if side_node.search_successor(height) != "nil":
                return True

        return False

    def get_median_box(self) -> Box:  # O(1)
        """Return the box with the median volume."""
        return self.boxes_max_heap.top()
