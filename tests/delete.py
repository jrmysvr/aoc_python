from day_1.solve import (parse_masses)


def test_parse_masses_converts_str_to_list():
    input_str = ""
    output = parse_masses(input_str)
    assert isinstance(output, list)


def test_parse_masses_splits_values_on_newline():
    input_str = "101\n100"
    output = parse_masses(input_str)
    assert len(output) == 2


def test_parse_masses_filters_empty():
    input_str = "101\n100\n"
    output = parse_masses(input_str)
    assert len(output) == 2


def test_parse_masses_returns_list_of_ints():
    input_str = "101\n100\n99\n98"
    output = parse_masses(input_str)
    assert len(output) == 4
    assert all([isinstance(o, int) for o in output])
