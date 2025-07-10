import pytest
from geometry.shapes import Square, Circle
from geometry.utils import area_stats

def test_square_area_zero_and_positive():
    sq1 = Square(4)
    print(sq1.area())
    assert sq1.area() == 16

    sq2 = Square(0)
    print(sq2.area())
    assert sq2.area() == 0


def test_stats_keys_and_values():
    shapes = [Square(4), Square(2), Circle(5), Circle(2), Circle(2)]
    stats = area_stats(shapes)

    assert type(stats) == dict
    assert list(stats.keys()) == ['n', 'total', 'mean', 'min', 'max']
    for num in stats.values():
        assert type(num) == int or type(num) == float

def test_stats_raises_without_shapes():
    with pytest.raises(ValueError):
        area_stats(None)