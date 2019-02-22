import pytest

from manma.heap import MinHeap, MaxHeap
from manma.rbt import RedBlackTree, Node


def test_min_heap():
    heap = MinHeap()
    heap.insert(2)
    heap.insert(1)
    heap.insert(3)

    assert heap == [1, 2, 3]

    heap.insert(4)

    assert heap == [1, 2, 3, 4]

    assert heap.extract() == 1
    assert heap.extract() == 2
    assert heap.extract() == 3
    assert heap.extract() == 4

    heap = MinHeap.build_from_array([1, 4, 2, 3])

    assert heap.extract() == 1
    assert heap.extract() == 2
    assert heap.extract() == 3
    assert heap.extract() == 4


def test_max_heap():
    heap = MaxHeap()
    heap.insert(2)
    heap.insert(1)
    heap.insert(3)

    assert heap.top() == 3

    heap.insert(4)

    assert heap.top() == 4

    assert heap.extract() == 4
    assert heap.extract() == 3
    assert heap.extract() == 2
    assert heap.extract() == 1

    heap = MaxHeap.build_from_array([1, 4, 2, 3])

    assert heap.extract() == 4
    assert heap.extract() == 3
    assert heap.extract() == 2
    assert heap.extract() == 1


def test_rbt():
    tree = RedBlackTree()
    tree.insert(4)
    tree.insert(5)
    tree.insert(3)

    assert tree.minimum() == 3
    assert tree.maxmium() == 5

    node_of_3 = tree.search(3)

    assert node_of_3 == 3

    tree.delete(node_of_3)

    assert tree.minimum() == 4

    tree.delete(tree.minimum())

    assert tree.minimum() == 5

    tree = RedBlackTree()
    for i in reversed(range(20)):
        tree.insert(i)

    assert list(tree.inorder_walk()) == list(range(20))

    assert RedBlackTree(tree.successor()).predecessor() == tree.root


def test_rbt_delete():
    tree = RedBlackTree()
    for i in range(20):
        tree.insert(i)

    tree.delete(tree.search(5))

    assert tree.search(5) == "nil"

    assert tree.search(6) != "nil"

    tree.delete(tree.search(6))

    assert tree.search(6) == "nil"


def test_rbt_search_successor():
    tree = RedBlackTree()
    for i in range(0, 20):
        tree.insert(i)

    for i in range(22, 44):
        tree.insert(i)

    assert tree.search_successor(0) == 0
    assert tree.search_successor(21) == 22
    assert tree.search_successor(44) == "nil"
