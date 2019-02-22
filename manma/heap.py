import math


def LEFT(index):
    return 2 * index


def RIGHT(index):
    return LEFT(index) + 1


def PARENT(index):
    return math.floor(index / 2)


class __AbstractHeap__(object):
    def __init__(self, array=None):
        self.array = array or []
        self.size = len(self.array)

    @classmethod
    def build_from_array(cls, array):
        heap = cls(array)

        index = math.floor(heap.size / 2)

        while index >= 1:
            heap.heapify(index)
            index -= 1

        return heap

    def item_at(self, index):  # This is because algorithms are 1-based and Python arrays are 0-based
        return self.array[index - 1]

    def set_item(self, index, value):
        if index == len(self.array) + 1:
            self.array.append(value)

        else:
            self.array[index - 1] = value

    def swap(self, index_a, index_b):
        """Swap the content of two indexes."""
        temp = self.item_at(index_a)
        self.set_item(index_a, self.item_at(index_b))
        self.set_item(index_b, temp)

    def heapify(self, index):
        left = LEFT(index)
        right = RIGHT(index)
        if left <= self.size and self.precedes(self.item_at(left),
                                               self.item_at(index)):
            largest = left

        else:
            largest = index

        if right <= self.size and self.precedes(self.item_at(right),
                                                self.item_at(largest)):
            largest = right

        if largest != index:
            self.swap(index, largest)
            self.heapify(largest)

    def top(self):
        return self.item_at(1)

    def extract(self):
        if self.size < 1:
            raise ArithmeticError("heap underflow")

        head = self.item_at(1)
        self.set_item(1, self.item_at(self.size))

        self.size -= 1
        self.array.pop()

        self.heapify(1)
        return head

    def insert(self, key):
        self.size += 1
        self.set_item(self.size, self.border_value())
        self.change_key(self.size, key)

    def change_key(self, index, new_key):
        if self.precedes(self.item_at(index), new_key):
            raise KeyError("New key comes before the current key")

        self.set_item(index, new_key)
        while index > 1 and self.precedes(self.item_at(index),
                                          self.item_at(PARENT(index))):
            self.swap(index, PARENT(index))
            index = PARENT(index)

    def delete_item_at_index(self, index):
        self.set_item(index, self.item_at(self.size))

        self.size -= 1
        self.array.pop()

        self.heapify(index)

    def precedes(self, a, b) -> bool:
        """Returns True if a comes before b in the heap."""
        raise NotImplementedError("__AbstractHeap__ can not compare instances, "
                                  "use either MaxHeap or MinHeap")

    def border_value(self):
        """Returns infinity for minimum heaps, minus infinity for maximum heaps"""
        raise NotImplementedError("__AbstractHeap__ does not define a border value, "
                                  "use either MaxHeap or MinHeap")

    def __repr__(self):
        return repr(list(self))

    def __iter__(self):
        for index in range(self.size):
            yield self.array[index]

    def __eq__(self, other):
        return list(self) == list(other)


class MinHeap(__AbstractHeap__):
    def precedes(self, a, b):
        return min(a, b) == a

    def border_value(self):
        return float("inf")


class MaxHeap(__AbstractHeap__):
    def precedes(self, a, b):
        return max(a, b) == a

    def border_value(self):
        return float("-inf")
