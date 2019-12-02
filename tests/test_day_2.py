from day_2.solve import (opcode_1,
                         opcode_2,
                         opcode_99,
                         run,
                         format_output)


class OpcodeTests:

    def test_opcode_1_adds_the_read_positions(self):
        read = 1
        write = 3
        state = [1, 1, 2, write]
        result_state, _ = opcode_1(state, read)
        # 1 + 2 == 3
        assert result_state[write] == 3

        read = 1
        write = 3
        state = [1, 0, 0, write]
        result_state, _ = opcode_1(state, read)
        # 1 + 1 == 2
        assert result_state[write] == 2

    def test_opcode_1_writes_to_write_position(self):
        read = 1
        write = 7
        state = [1, 1, 2, write, 0, 0, 0, 0]
        result_state, _ = opcode_1(state, read)
        # 1 + 2 == 3, in last position
        assert result_state[write] == 3

    def test_opcode_2_multiplies_the_read_positions(self):
        read = 1
        write = 3
        state = [1, 2, 2, write]
        result_state, _ = opcode_2(state, read)
        # 2 * 2 == 4
        assert result_state[write] == 4

    def test_opcode_2_writes_to_write_position(self):
        read = 1
        write = 7
        state = [1, 2, 2, write, 0, 0, 0, 1]
        result_state, _ = opcode_2(state, read)
        # 2 * 2 == 4, in last position
        assert result_state[write] == 4

        read = 1
        write = 0
        state = [1, 2, 2, write, 0, 0, 0, 1]
        result_state, _ = opcode_2(state, read)
        # 2 * 2 == 4, in first position
        assert result_state[write] == 4

    def test_opcode_99_reads_from_given_position_minus_1(self):
        state = [99, 0, 0]
        _, result = opcode_99(state, 1)

    def test_opcode_99_returns_true_given_99(self):
        state = [0, 99, 0, 0]
        _, result = opcode_99(state, 2)

        assert result == True

    def test_opcode_99_returns_false_without_99(self):
        state = [0, 99, 0]
        _, result = opcode_99(state, 1)

        assert result == False


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


class OutputTests:

    def test_output_format_100_times_noun_plus_verb(self):
        noun = 12
        verb = 2

        assert format_output(noun, verb) == 1202
