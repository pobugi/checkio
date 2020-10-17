"""
You are given two lists as coordinates of vertices of each triangle.
You have to return a bool. (The triangles are similar or not)
"""

from typing import List, Tuple
from math import sqrt
Coords = List[Tuple[int, int]]


def similar_triangles(coords_1: Coords, coords_2: Coords) -> bool:
    a1 = sqrt(
        abs(
            (coords_1[1][1] - coords_1[0][1]) ** 2 +
            (coords_1[1][0] - coords_1[0][0]) ** 2
            )
        )
    a2 = sqrt(
        abs(
            (coords_2[1][1] - coords_2[0][1]) ** 2 +
            (coords_2[1][0] - coords_2[0][0]) ** 2
            )
        )
    b1 = sqrt(
        abs(
            (coords_1[1][1] - coords_1[2][1]) ** 2 +
            (coords_1[1][0] - coords_1[2][0]) ** 2
            )
        )
    b2 = sqrt(
        abs(
            (coords_2[1][1] - coords_2[2][1]) ** 2 +
            (coords_2[1][0] - coords_2[2][0]) ** 2
            )
        )
    c1 = sqrt(
        abs(
            (coords_1[2][1] - coords_1[0][1]) ** 2 +
            (coords_1[2][0] - coords_1[0][0]) ** 2
            )
        )
    c2 = sqrt(
        abs(
            (coords_2[2][1] - coords_2[0][1]) ** 2 +
            (coords_2[2][0] - coords_2[0][0]) ** 2
            )
        )

    triangle1 = (a1, b1, c1)
    a1 = max(triangle1)
    c1 = min(triangle1)
    triangle2 = (a2, b2, c2)
    a2 = max(triangle2)
    c2 = min(triangle2)

    return a1 / a2 == c1 / c2


if __name__ == '__main__':
    print("Example:")
    print(similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]))

    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True, 'basic'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False, 'different #1'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]) is True, 'scaling'
    assert similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]) is True, 'reflection'
    assert similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True, 'scaling and reflection'
    assert similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]) is False, 'different #2'
    print("Coding complete? Click 'Check' to earn cool rewards!")
