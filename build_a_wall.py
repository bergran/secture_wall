# -*- coding: utf-8 -*-
from constants import NONE_ERROR, LIMITED_EXCEED, MORTAR, FULL_BRICK, HALF_BRICK


class Validations:

    @staticmethod
    def validate_not_give(columns, rows):
        if not all([columns, rows]):
            return NONE_ERROR
        return ''

    @staticmethod
    def validate_integers(columns, rows):
        if not isinstance(columns, int) or not isinstance(rows, int):
            return NONE_ERROR
        return ''

    @staticmethod
    def validate_max_bricks(columns, rows, max_bricks=10000):
        if columns * rows >= max_bricks:
            return LIMITED_EXCEED
        return ''

    @staticmethod
    def validate_min_number(columns, rows, min_number=-1):
        if columns <= min_number or rows <= min_number:
            return NONE_ERROR
        return ''


class Wall:

    is_valid_result = False
    is_valid_done = False
    error = None

    def __init__(self, rows=None, columns=None):
        self.rows = rows
        self.columns = columns

    def is_valid(self, validations: list, raise_validation_error=False) -> bool:
        error = []
        index = 0
        while index < len(validations) and not error:
            validation = validations[index]
            error = validation(self.rows, self.columns)
            index += 1

        self.error = error
        self.is_valid_result = not self.error
        self.is_valid_done = True
        return self.is_valid_result

    def build_a_wall(self):
        if self.error:
            return self.error

        rows = self.rows + 1
        wall = []
        for row in range(1, rows):
            is_multiple_2 = row % 2 == 1
            first_brick = '{}'.format('{}{}'.format(HALF_BRICK, MORTAR) if is_multiple_2 else '')
            last_brick = '{}'.format(HALF_BRICK if is_multiple_2 else '')
            columns = self.columns + 1 if is_multiple_2 else self.columns + 2

            wall.append('{}{}{}'.format(first_brick,
                                    '{}|'.format(MORTAR.join(FULL_BRICK for index in range(1, columns - 1))),
                                    last_brick))
        return wall


def build_a_wall(x: int, y: int):
    wall = Wall(x, y)
    wall.is_valid([
        Validations.validate_not_give,
        Validations.validate_integers,
        Validations.validate_min_number,
        Validations.validate_max_bricks
    ], True)
    wall_built = wall.build_a_wall()
    if isinstance(wall_built, list):
        for row in wall_built:
            print(row)
    else:
        print(wall_built)
    return wall_built


if __name__ == '__main__':
    build_a_wall(5, 5)
