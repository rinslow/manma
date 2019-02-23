from manma.box import Box
from manma.box_storage import BoxStorage


def test_them_all():
    storage = BoxStorage()
    storage.insert_box(4, 4)
    assert len(storage.sides) == 1
    assert storage.get_median_box() == Box(4, 4)

    for _ in range(10):
        storage.insert_box(1, 1)

    assert len(storage.sides) == 2

    assert storage.get_median_box() == Box(1, 1)

    for _ in range(10):
        storage.remove_box(1, 1)

    assert len(storage.sides) == 1

    assert storage.get_median_box() == Box(4, 4)

