import area


def test_area_square():
    assert area.areaofsquare(2, 3) == 6


def test_area_circle():
    assert area.areaofcircle(2) == 12.5
