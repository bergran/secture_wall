# -*- coding: utf-8 -*-
from unittest import TestCase

from build_a_wall import build_a_wall, NONE_ERROR, LIMITED_EXCEED


class WallTestBuilt(TestCase):

    def test_built_good_5_x_5(self):
        columns = 5
        rows = 5
        self.assertEqual(len(build_a_wall(columns, rows)), 5)

    def test_built_good_10_x_7(self):
        columns = 10
        rows = 7
        self.assertEqual(len(build_a_wall(columns, rows)), 10)

    def test_built_bad_not_integer(self):
        columns = 'eight'
        rows = [3]
        self.assertEqual(build_a_wall(columns, rows), NONE_ERROR)

    def test_built_bad_under_0_value(self):
        columns = 12
        rows = -4
        self.assertEqual(build_a_wall(columns, rows), NONE_ERROR)

    def test_built_bad_limited_exceed(self):
        columns = 123
        rows = 987
        self.assertEqual(build_a_wall(columns, rows), LIMITED_EXCEED)

    def test_built_bad_none_value_pass(self):
        columns = 12
        rows = None
        self.assertEqual(build_a_wall(columns, rows), NONE_ERROR)
