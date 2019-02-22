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
