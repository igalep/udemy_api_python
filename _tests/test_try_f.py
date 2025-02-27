from dataclasses import dataclass, asdict, astuple

from _src.point import Point

import pytest


class TestClassFirst:
    def add_param(self, a , b):
        return a + b

    @pytest.mark.current
    def test_fixture(self, bootstrap):
        assert bootstrap == Point(1,2)

    @pytest.mark.skip(reason='no need')
    def test_init(self):
        a = Point(4,5)
        b = Point(5,5)

        assert a==b


    def test_getter(self):
        a = Point(4,5)

        assert a.x == 5
        assert a.y == 3

    def test_as_dict(self):
        a = Point(15,4)
        xx = asdict(a)

        assert xx == {"x":1, "y":2}

    @pytest.mark.parametrize(
        'param_a, param_b, result',
        [
            (2,3,5),
            (5,7,12),
            (0,3,3)
        ]
    )
    def test_param(self,param_a, param_b, result):
        res = self.add_param(a=param_a, b=param_b)

        assert res == result


    def p_tuple(p):
        return str(asdict(p))

    @pytest.mark.parametrize(
        'point_a, point_b',
        [
            (Point(1,2), Point(1,2)),
            (Point(2,3), Point(2,3)),
            (Point(3,2), Point(3,2)),
            (Point(1.5, 2), Point(1.5, 2)),
        ], ids=p_tuple
    )
    def test_obj_param(self, point_a, point_b):
        assert point_a == point_b