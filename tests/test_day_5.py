from day_5.solve import *
import io


class OpcodeTests:

    def test_opcode_1_adds_the_read_positions(self):
        write = 3
        state = [1, 1, 2, write]
        _, result_state, _ = opcode_1(state, 0)
        # 1 + 2 == 3
        assert result_state[write] == 3

        write = 3
        state = [1, 0, 0, write]
        _, result_state, _ = opcode_1(state, 0)
        # 1 + 1 == 2
        assert result_state[write] == 2

    def test_opcode_1_writes_to_write_position(self):
        write = 7
        state = [1, 1, 2, write, 0, 0, 0, 0]
        _, result_state, _ = opcode_1(state, 0)
        # 1 + 2 == 3, in last position
        assert result_state[write] == 3

    def test_opcode_1_uses_immediate_mode(self):
        write = 3
        state = [1101, 1, 3, write]
        _, result_state, _ = opcode_1(state, 0)
        # 1 + 3 == 4
        assert result_state[write] == 4

        write = 3
        state = [1101, 3, 3, write]
        _, result_state, _ = opcode_1(state, 0)
        # 3 + 3 == 4
        assert result_state[write] == 6

        write = 1
        state = [1001, 3, 3, write]
        _, result_state, _ = opcode_1(state, 0)
        # 1 + 3 == 4
        assert result_state[write] == 4

    def test_opcode_2_multiplies_the_read_positions(self):
        write = 3
        state = [1, 2, 2, write]
        _, result_state, _ = opcode_2(state, 0)
        # 2 * 2 == 4
        assert result_state[write] == 4

    def test_opcode_2_writes_to_write_position(self):
        write = 7
        state = [1, 2, 2, write, 0, 0, 0, 1]
        _, result_state, _ = opcode_2(state, 0)
        # 2 * 2 == 4, in last position
        assert result_state[write] == 4

        write = 0
        state = [1, 2, 2, write, 0, 0, 0, 1]
        _, result_state, _ = opcode_2(state, 0)
        # 2 * 2 == 4, in first position
        assert result_state[write] == 4

    def test_opcode_2_uses_immediate_mode(self):
        write = 3
        state = [1101, 1, 3, write]
        _, result_state, _ = opcode_2(state, 0)
        # 1 * 3 == 4
        assert result_state[write] == 3

        write = 3
        state = [1101, 3, 3, write]
        _, result_state, _ = opcode_2(state, 0)
        # 3 * 3 == 4
        assert result_state[write] == 9

        write = 1
        state = [1001, 3, 3, write]
        _, result_state, _ = opcode_2(state, 0)
        # 1 * 3 == 3
        assert result_state[write] == 3

    def test_opcode_99_returns_true_given_99(self):
        state = [0, 99, 0, 0]
        result, _, _ = opcode_99(state, 1)

        assert result == True

    def test_opcode_99_returns_false_without_99(self):
        state = [0, 99, 0]
        result, _, _ = opcode_99(state, 0)

        assert result == False

    def test_opcode_3_writes_input_to_state(self, monkeypatch):
        state = [3, 0, 4, 0, 99]
        # expected = [1, 0, 4, 0, 99]
        sys.stdin = input
        monkeypatch.setattr('sys.stdin', io.StringIO('1'))
        _, result_state, _ = opcode_3(state, 0)
        assert result_state[0] == 1

    def test_opcode_4_reads_value_from_state(self, capsys):
        state = [4, 0, 99]
        _ = opcode_4(state, 0)
        captured = capsys.readouterr()
        expected = int(captured.out.strip())
        assert expected == 4

    def test_opcode_5_increments_pointer_if_param_is_nonzero(self):
        # param is nonzero
        state = [5, 4, 3, 99, 2]
        _, state, ix = opcode_5(state, 0)
        assert ix == 99

        # param is zero
        state = [5, 4, 3, 99, 0]
        _, state, ix = opcode_5(state, 0)
        assert ix != 99
        assert ix != 0

    def test_opcode_6_increments_pointer_if_param_is_zero(self):
        state = [6, 4, 3, 2, 0]
        _, state, ix = opcode_6(state, 0)
        assert ix == 2

        state = [6, 4, 3, 2, 99]
        _, state, ix = opcode_6(state, 0)
        assert ix != 0
        assert ix != 2

    def test_opcode_7_stores_1_if_param0_lt_param1_else_0(self):
        state = [7, 1, 2, 4, 99]
        _, state, _ = opcode_7(state, 0)
        assert state == [7, 1, 2, 4, 1]

        state = [7, 1, 3, 0, 99]
        _, state, _ = opcode_7(state, 0)
        assert state == [0, 1, 3, 0, 99]

    def test_opcode_8_stores_1_if_param0_lt_param1_else_0(self):
        state = [8, 1, 4, 3, 1]
        _, state, _ = opcode_8(state, 0)
        assert state == [8, 1, 4, 1, 1]

        state = [8, 1, 3, 0, 99]
        _, state, _ = opcode_8(state, 0)
        assert state == [0, 1, 3, 0, 99]


class ParseParameterTests:

    def test_parse_parameters_1002(self):
        code = 1002
        _, parameters = parse_opcode_parameters(code)
        assert parameters == [0, 1]

    def test_parse_parameters_11002(self):
        code = 11002
        _, parameters = parse_opcode_parameters(code)
        assert parameters == [0, 1, 1]

    def test_parse_parameters_100(self):
        code = 100
        _, parameters = parse_opcode_parameters(code)
        assert parameters == [1]

    def test_parse_parameters_gives_opcode(self):
        code = 11002
        opcode, _ = parse_opcode_parameters(code)
        assert opcode == 2

        code = 99
        opcode, _ = parse_opcode_parameters(code)
        assert opcode == 99

        code = 101
        opcode, _ = parse_opcode_parameters(code)
        assert opcode == 1


class RunTests:

    def run_test(self, state, expected_state):
        end_state = run(state)
        assert end_state == expected_state

    def test_case_1(self):
        state = [1, 0, 0, 0, 99]
        expected = [2, 0, 0, 0, 99]
        self.run_test(state, expected)

    def test_case_2(self):
        state = [2, 3, 0, 3, 99]
        expected = [2, 3, 0, 6, 99]
        self.run_test(state, expected)

    def test_case_3(self):
        state = [2, 4, 4, 5, 99, 0]
        expected = [2, 4, 4, 5, 99, 9801]
        self.run_test(state, expected)

    def test_case_4(self):
        state = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        expected = [30, 1, 1, 4, 2, 5, 6, 0, 99]
        self.run_test(state, expected)

    def test_case_5(self):
        state = [1101, 100, -1, 4, 0]
        expected = [1101, 100, -1, 4, 99]
        self.run_test(state, expected)

    def test_case_6(self):
        state = [1002, 4, 3, 4, 33]
        expected = [1002, 4, 3, 4, 99]
        self.run_test(state, expected)

    def test_case_7(self, capsys, monkeypatch):
        state = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
