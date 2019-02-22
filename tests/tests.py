from manma.data_structures import MinHeap, MaxHeap


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
