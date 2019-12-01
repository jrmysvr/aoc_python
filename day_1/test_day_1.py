from day_1.solve import (parse_masses)


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
        self.assertEquals(len(output), 4)
        #  all([isinstance(o, int) for o in output])
        for o in output:
            self.assertTrue(isinstance(o, str))
