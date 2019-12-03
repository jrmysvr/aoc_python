"""
Solving Day 3, 2019 Advent of Code Challenge
---

The gravity assist was successful, and you're well on your way to the Venus refuelling station.  During the rush back on Earth, the fuel management system wasn't completely installed, so that's next on the priority list.
Opening the front panel reveals a jumble of wires. Specifically, two wires are connected to a central port and extend outward on a grid.  You trace the path each wire takes as it leaves the central port, one wire per line of text (your puzzle input).
The wires twist and turn, but the two wires occasionally cross paths. To fix the circuit, you need to find the intersection point closest to the central port. Because the wires are on a grid, use the Manhattan distance for this measurement. While the wires do technically cross right at the central port where they both start, this point does not count, nor does a wire count as crossing with itself.
For example, if the first wire's path is R8,U5,L5,D3, then starting from the central port (o), it goes right 8, up 5, left 5, and finally down 3:
    ...........
    ...........
    ...........
    ....+----+.
    ....|....|.
    ....|....|.
    ....|....|.
    .........|.
    .o-------+.
    ...........
Then, if the second wire's path is U7,R6,D4,L4, it goes up 7, right 6, down 4, and left 4:
    ...........
    .+-----+...
    .|.....|...
    .|..+--X-+.
    .|..|..|.|.
    .|.-X--+.|.
    .|..|....|.
    .|.......|.
    .o-------+.
    ...........
These wires cross at two locations (marked X), but the lower-left one is closer to the central port: its distance is 3 + 3 = 6.
Here are a few more examples:
What is the Manhattan distance from the central port to the closest intersection?
===

Part 2

It turns out that this circuit is very timing-sensitive; you actually need to minimize the signal delay.

To do this, calculate the number of steps each wire takes to reach each intersection; choose the intersection where the sum of both wires' steps is lowest. If a wire visits a position on the grid multiple times, use the steps value from the first time it visits that position when calculating the total value of a specific intersection.

The number of steps a wire takes is the total number of grid squares the wire has entered to get to that location, including the intersection being considered. Again consider the example from above:

...........
.+-----+...
.|.....|...
.|..+--X-+.
.|..|..|.|.
.|.-X--+.|.
.|..|....|.
.|.......|.
.o-------+.
...........

In the above example, the intersection closest to the central port is reached after 8+5+5+2 = 20 steps by the first wire and 7+6+4+3 = 20 steps by the second wire for a total of 20+20 = 40 steps.

However, the top-right intersection is better: the first wire takes only 8+5+2 = 15 and the second wire takes only 7+6+2 = 15, a total of 15+15 = 30 steps.

Here are the best steps for the extra examples from above:

    R75,D30,R83,U83,L12,D49,R71,U7,L72
    U62,R66,U55,R34,D71,R55,D58,R83 = 610 steps
    R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
    U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = 410 steps

What is the fewest combined steps the wires must take to reach an intersection?

"""

import sys
import os
utils_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.append(utils_path)
from utils import get_input_text, write_solution


class Coordinate:
    """
    Coordinate representation on a grid
    Bottom is 0th row
    Left is 0th column
    """

    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

    def get_rc(self) -> tuple:
        return self.row, self.col

    def distance_between(self, other) -> int:
        """
        Calculate the manhattan distance between two Coordinates

        Args:
            other (Coordinate): coordinate to compare

        Returns:
            int of manhattan to given coordinate
        """
        return abs(self.row - other.row) + abs(self.col - other.col)

    def move(self, dr: int, dc: int):
        """
        Move the coordinate

        Apply movement to coordinate with (row + dr), (col + dc)

        Args:
            dr (int): movement in row
            dc (int): movement in col
        """
        self.row += dr
        self.col += dc

    def __repr__(self):
        return f"({self.row}, {self.col})"

    def __hash__(self):
        return hash((self.row, self.col))

    def __eq__(self, other):
        return (self.row == other.row) and (self.col == other.col)


def parse_wires(input_text: str) -> tuple:
    """
    Get wire routes from input text

    There should be two wire routes separated by a newline
    Wire route data should be comma delimited

    Args:
        input_text (str): text input from challenge

    Returns:
        tuple of two wire routes
    """

    wire_1, wire_2 = input_text.strip("\n").split("\n")
    return wire_1.split(","), wire_2.split(",")


def parse_wire_route(wire_route: str) -> list:
    """
    Parse wire route and convert route to list of movement tuples

    U1 -> up 1 -> (1, 0)
    R2 -> right 2 -> (0, 2)
    D3 -> down 3 -> (-3, 0)
    L4 -> left 4 -> (0, -4)

    Args:
        wire_route (str): description of wire route (U1, D3, R2, L4, ...)

    Returns:
        list of movement tuples - converted route description ((1, 0), (0, 2), (-3, 0), (0, -4)...)
    """
    movements = {
        'U': (1, 0),
        'R': (0, 1),
        'D': (-1, 0),
        'L': (0, -1),
    }

    direction = wire_route[0]
    magnitude = int(wire_route[1:])
    movements = [movements[direction] for _ in range(magnitude)]
    return movements


def flatten(ls: list) -> list:
    """ Flatten a nested list """
    output = []
    for l in ls:
        if isinstance(l, list):
            output += flatten(l)
        else:
            output.append(l)

    return output


def find_intersections(wire_route_0: list, wire_route_1: list) -> list:
    """
    Trace wire movements and find all intersections

    Args:
        wire_route_0 (list): list of route directions of a wire, from challenge input
        wire_route_1 (list): list of route directions of a wire, from challenge input

    Returns:
        list of Coordinates where wires intersect
    """

    trace_0 = Coordinate(0, 0)
    trace_1 = Coordinate(0, 0)

    def Coordinate_at_rc(coor: Coordinate, dr: int, dc: int):
        coor.move(dr, dc)
        return Coordinate(*coor.get_rc())

    parsed_0 = flatten(list(map(parse_wire_route, wire_route_0)))
    parsed_1 = flatten(list(map(parse_wire_route, wire_route_1)))

    wire_coors_0 = set([Coordinate_at_rc(trace_0, *rc) for rc in parsed_0])
    wire_coors_1 = set([Coordinate_at_rc(trace_1, *rc) for rc in parsed_1])

    return list(wire_coors_0.intersection(wire_coors_1))


def distance_to_closest_coordinate(coordinates: list,
                                   common: Coordinate) -> int:
    """
    Given a list of coordinates, find the smallest distance between the
    coordinates and the common coordinate

    Args:
        coordinates (list): list of coordinates
        common (Coordinate): coordinate to compare with the other coordinates

    Return:
        int of the smallest distance between a Coordinate and the common coordinate
    """
    distances = [common.distance_between(coordinate)
                 for coordinate in coordinates]
    return min(distances)


if __name__ == "__main__":
    day = 3
    year = 2019
    input_text = get_input_text(day, year)

    ## Part 1 ##
    wire_1, wire_2 = parse_wires(input_text)
    intersecting_coordinates = find_intersections(wire_1, wire_2)
    closest_distance = distance_to_closest_coordinate(intersecting_coordinates,
                                                      Coordinate(0, 0))
    print(f"Solution Day {day} (Part 1):")
    print("\tThe distance to the closest intersection is", closest_distance)

    write_solution(day, year, str(closest_distance))

    ## Part 2 ##
    #  print(f"Solution Day {day} (Part 2):")

    #  write_solution(day, year,
