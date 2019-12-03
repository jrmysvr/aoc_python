from day_3.solve import (Coordinate,
                         flatten,
                         parse_wire_route,
                         find_intersections)


class CoordinateTests:

    def test_manhattan_distance_between_coordinates_cols(self):
        coor_0 = Coordinate(0, 0)
        coor_1 = Coordinate(0, 1)
        distance = coor_0.distance_between(coor_1)

        assert distance == 1

    def test_manhattan_distance_between_coordinates_row(self):
        coor_0 = Coordinate(0, 0)
        coor_1 = Coordinate(1, 0)
        distance = coor_0.distance_between(coor_1)

        assert distance == 1

    def test_manhattan_distance_between_coordinates_row_and_cols(self):
        coor_0 = Coordinate(0, 0)
        coor_1 = Coordinate(1, 1)
        distance = coor_0.distance_between(coor_1)

        assert distance == 2

    def test_coordinate_moves_row_1(self):
        coor = Coordinate(0, 0)
        coor.move(1, 0)
        assert coor.get_rc() == (1, 0)

    def test_coordinate_moves_col_1(self):
        coor = Coordinate(0, 0)
        coor.move(0, 1)
        assert coor.get_rc() == (0, 1)

    def test_coordinate_moves_row_1_col_1(self):
        coor = Coordinate(0, 0)
        coor.move(1, 1)
        assert coor.get_rc() == (1, 1)

    def test_coordinate_moves_row_1(self):
        coor = Coordinate(1, 1)
        coor.move(-1, 0)
        assert coor.get_rc() == (0, 1)

    def test_coordinate_moves_col_1(self):
        coor = Coordinate(1, 1)
        coor.move(0, -1)
        assert coor.get_rc() == (1, 0)

    def test_coordinate_moves_row_1_col_1(self):
        coor = Coordinate(1, 1)
        coor.move(-1, -1)
        assert coor.get_rc() == (0, 0)


class WireRouteTests:

    def test_wire_route_U1_r1c0(self):
        route = 'U1'
        expected = [(1, 0)]
        assert parse_wire_route(route) == expected

    def test_wire_route_R1_r0c1(self):
        route = 'R1'
        expected = [(0, 1)]
        assert parse_wire_route(route) == expected

    def test_wire_route_D1_rneg1c0(self):
        route = 'D1'
        expected = [(-1, 0)]
        assert parse_wire_route(route) == expected

    def test_wire_route_L1_r0cneg1(self):
        route = 'L1'
        expected = [(0, -1)]
        assert parse_wire_route(route) == expected

    def test_wire_route_U3_multiple_movements(self):
        route = 'U3'
        expected = [(1, 0), (1, 0), (1, 0)]
        assert parse_wire_route(route) == expected

    def test_wire_route_L3_multiple_movements(self):
        route = 'L3'
        expected = [(0, -1), (0, -1), (0, -1)]
        assert parse_wire_route(route) == expected


class FlattenTests:

    def test_case_1(self):
        initial = [1, [2], [3, [4]]]
        expected = [1, 2, 3, 4]
        assert flatten(initial) == expected


class TraceTests:

    def trace_test(self, wire_1, wire_2, expected_distance):
        start = Coordinate(0, 0)
        intersections = find_intersections(wire_1, wire_2)
        distances = [start.distance_between(coordinate)
                     for coordinate in intersections]
        distance = min(distances)
        assert distance == expected_distance

    def test_case_1(self):
        wire_1 = ["R8", "U5", "L5", "D3"]
        wire_2 = ["U7", "R6", "D4", "L4"]
        distance = 6
        self.trace_test(wire_1, wire_2, distance)

    def test_case_2(self):
        wire_1 = ["R75", "D30", "R83", "U83", "L12", "D49",
                  "R71", "U7", "L72"]
        wire_2 = ["U62", "R66", "U55", "R34", "D71", "R55",
                  "D58", "R83"]
        distance = 159
        self.trace_test(wire_1, wire_2, distance)

    def test_case_3(self):
        wire_1 = ["R98", "U47", "R26", "D63", "R33", "U87",
                  "L62", "D20", "R33", "U53", "R51"]
        wire_2 = ["U98", "R91", "D20", "R16", "D67", "R40",
                  "U7", "R15", "U6", "R7"]
        distance = 135
        self.trace_test(wire_1, wire_2, distance)
