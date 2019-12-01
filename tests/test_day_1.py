from day_1.solve import (parse_masses,
                         calculate_fuel,
                         calculate_fuel_recur)


class ParseMassTests:
    def test_parse_masses_converts_str_to_list(self):
        input_str = ""
        output = parse_masses(input_str)
        assert isinstance(output, list)

    def test_parse_masses_splits_values_on_newline(self):
        input_str = "101\n100"
        output = parse_masses(input_str)
        assert len(output) == 2

    def test_parse_masses_filters_empty(self):
        input_str = "101\n100\n"
        output = parse_masses(input_str)
        assert len(output) == 2

    def test_parse_masses_returns_list_of_ints(self):
        input_str = "101\n100\n99\n98"
        output = parse_masses(input_str)
        assert len(output) == 4
        assert all([isinstance(o, int) for o in output])


class CalculateFuelTests:
    def test_calculate_fuel_returns_int(self):
        assert isinstance(calculate_fuel(0), int)

    def test_calculate_fuel_given_30_should_return_8(self):
        fuel = calculate_fuel(30)
        assert fuel == 8

    def test_calculate_fuel_given_31_should_return_8(self):
        fuel = calculate_fuel(31)
        assert fuel == 8

    def test_calculate_fuel_given_29_should_return_7(self):
        fuel = calculate_fuel(29)
        assert fuel == 7


class CalculateFuelRecurTests:
    def test_calculate_fuel_returns_int(self):
        assert isinstance(calculate_fuel(0), int)

    def test_calculate_fuel_recur_given_30_should_return_8(self):
        fuel = calculate_fuel_recur(30)
        assert fuel == 8

    def test_calculate_fuel_recur_given_31_should_return_8(self):
        fuel = calculate_fuel_recur(31)
        assert fuel == 8

    def test_calculate_fuel_recur_given_29_should_return_7(self):
        fuel = calculate_fuel_recur(29)
        assert fuel == 7

    def test_calculate_fuel_recur_given_60_should_return_22(self):
        fuel = calculate_fuel_recur(60)
        assert fuel == 22

    def test_calculate_fuel_recur_given_59_should_return_20(self):
        fuel = calculate_fuel_recur(59)
        assert fuel == 20

    def test_calculate_fuel_recur_given_100_should_return_39(self):
        fuel = calculate_fuel_recur(100)
        assert fuel == 39
