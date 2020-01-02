import sys
import os
utils_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.append(utils_path)
from utils import get_input_text, write_solution


def parse_opcode_parameters(value: int) -> tuple:
    """
    Given a integer value, parse its opcode and parameter values

    Args:
        value (int): integer to parse

    Returns:
        tuple of the opcode and a list of parameters of an opcode (left to right)
    """

    values = list(map(int, str(value)))
    if len(values) == 1:
        return values[0], []

    opcode = values[-2:]  # last two will be the opcode
    opcode = 10 * opcode[0] + opcode[1]
    parameters = values[:-2]
    # provide parsed parameters left to right
    return opcode, parameters[::-1]


def opcode_1(state: list, read_ix: int) -> tuple:
    """
    Opcode 1

    Add values from two read positions and write the result to the write position
    Read positions are state values at read_ix, read_ix + 1
    Write position is state value at read_ix + 2

    Args:
        state (list): list of state values
        read_ix (int): index to start reading from the state

    Returns:
        tuple of False, modified state, and the next value of the instruction pointer
    """
    opcode = state[read_ix]
    read_ix += 1
    _, parameters = parse_opcode_parameters(opcode)
    parameters = parameters + [0] * (3 - len(parameters))

    read_0 = state[read_ix]
    read_1 = state[read_ix + 1]
    write_ix = state[read_ix + 2]
    output = list(state)

    # Update values based on parameters (0 - position, 1 - immediate)
    read_0 = state[read_0] if parameters[0] == 0 else read_0
    read_1 = state[read_1] if parameters[1] == 0 else read_1
    value = read_0 + read_1
    output[write_ix] = value

    return (False, output, read_ix + 3)


def opcode_2(state: list, read_ix: int) -> tuple:
    """
    Opcode 2

    Multiply values from two read positions and write the result to the write position
    Read positions are state values at read_ix, read_ix + 1
    Write position is state value at read_ix + 2

    Args:
        state (list): list of state values
        read_ix (int): index to start reading from the state

    Returns:
        tuple of False, modified state, and the next value of the instruction pointer
    """

    opcode = state[read_ix]
    read_ix += 1
    _, parameters = parse_opcode_parameters(opcode)
    parameters = parameters + [0] * (3 - len(parameters))

    read_0 = state[read_ix]
    read_1 = state[read_ix + 1]
    write_ix = state[read_ix + 2]
    output = list(state)

    # Update values based on parameters (0 - position, 1 - immediate)
    read_0 = state[read_0] if parameters[0] == 0 else read_0
    read_1 = state[read_1] if parameters[1] == 0 else read_1
    value = read_0 * read_1
    output[write_ix] = value

    return (False, output, read_ix + 3)


def opcode_3(state: list, read_ix: int, input_id: int = -1):
    """
    Opcode 3

    Write a value to the state
    An input will be taken and then written to the state address from `read_ix`

    Args:
        state (list): list of state values
        read_ix (int): index to start reading from the state

    Returns:
        tuple of False, modified state, and the next value of the instruction pointer
    """

    opcode = state[read_ix]
    read_ix += 1

    value = (int(input("Input Instruction - Provide an Input ID (Integer):"))
             if input_id < 0
             else input_id)

    write_ix = state[read_ix]
    output = list(state)
    output[write_ix] = value
    return (False, output, read_ix + 1)


def opcode_4(state: list, read_ix: int):
    """
    Opcode 4

    Output the state value at `read_ix`
    Args:
        state (list): list of state values
        read_ix (int): index to start reading from the state

    Returns:
        tuple of False, modified state, and the next value of the instruction pointer
    """

    opcode = state[read_ix]
    read_ix += 1

    read_0 = state[read_ix]
    value = state[read_0]
    sys.stdout.write(str(value) + " ")
    return (False, state, read_ix + 1)


def opcode_5(state: list, read_ix: int):
    """
    Opcode 5

    Update `read_ix` if state parameter 0 is nonzero, otherwise do nothing
    Args:
        state (list): list of state values
        read_ix (int): index to start reading from the state

    Returns:
        tuple of False, modified state, and the next value of the instruction pointer
    """

    opcode = state[read_ix]
    read_ix += 1

    _, parameters = parse_opcode_parameters(opcode)
    parameters = parameters + [0] * (2 - len(parameters))

    read_0 = state[read_ix]
    read_1 = state[read_ix + 1]
    output = list(state)

    # Update values based on parameters (0 - position, 1 - immediate)
    check = state[read_0] if parameters[0] == 0 else read_0
    value = state[read_1] if parameters[1] == 0 else read_1

    new_ix = value if check != 0 else read_ix + 2
    return (False, state, new_ix)


def opcode_6(state: list, read_ix: int):
    """
    Opcode 6

    Update `read_ix` if state parameter 0 is zero, otherwise do nothing
    Args:
        state (list): list of state values
        read_ix (int): index to start reading from the state

    Returns:
        tuple of False, modified state, and the next value of the instruction pointer
    """
    opcode = state[read_ix]
    read_ix += 1

    _, parameters = parse_opcode_parameters(opcode)
    parameters = parameters + [0] * (2 - len(parameters))

    read_0 = state[read_ix]
    read_1 = state[read_ix + 1]
    output = list(state)

    # Update values based on parameters (0 - position, 1 - immediate)
    check = state[read_0] if parameters[0] == 0 else read_0
    value = state[read_1] if parameters[1] == 0 else read_1

    new_ix = value if check == 0 else read_ix + 2
    return (False, state, new_ix)


def opcode_7(state: list, read_ix: int):
    opcode = state[read_ix]
    read_ix += 1
    _, parameters = parse_opcode_parameters(opcode)
    parameters = parameters + [0] * (3 - len(parameters))

    read_0 = state[read_ix]
    read_1 = state[read_ix + 1]
    write_ix = state[read_ix + 2]
    output = list(state)

    # Update values based on parameters (0 - position, 1 - immediate)
    read_0 = state[read_0] if parameters[0] == 0 else read_0
    read_1 = state[read_1] if parameters[1] == 0 else read_1
    output[write_ix] = 1 if read_0 < read_1 else 0

    return (False, output, read_ix + 3)


def opcode_8(state: list, read_ix: int):
    opcode = state[read_ix]
    read_ix += 1
    _, parameters = parse_opcode_parameters(opcode)
    parameters = parameters + [0] * (3 - len(parameters))

    read_0 = state[read_ix]
    read_1 = state[read_ix + 1]
    write_ix = state[read_ix + 2]
    output = list(state)

    # Update values based on parameters (0 - position, 1 - immediate)
    read_0 = state[read_0] if parameters[0] == 0 else read_0
    read_1 = state[read_1] if parameters[1] == 0 else read_1
    output[write_ix] = 1 if read_0 == read_1 else 0

    return (False, output, read_ix + 3)


def opcode_99(state: list, read_ix: int) -> tuple:
    """
    Opcode 99

    Check whether the value at `read_ix` equals 99

    Args:
        state (list): list of state values
        read_ix (int): index to read from state - (read_ix - 1)

    Returns:
        tuple of bool of value at the read position equaling 99, state, and instruction increment
    """

    return state[read_ix] == 99, state, 0


class Input:
    def __init__(self, values):
        self.values = values
        self.ix = 0

    def get_next(self):
        if self.ix < len(self.values):
            value = self.values[self.ix]
            self.ix += 1
            return value
        return None


def run(state: list, user_input):
    """
    run opcodes on state

    Args:
        state (list): list of state values (mutable)

    Returns:
        list of mutated state values
    """

    def _opcode_3(*args):
        return opcode_3(*args, input_id=user_input.get_next())

    # Operational codes and the index increment after opcode is used
    opcodes = {
        1: opcode_1,
        2: opcode_2,
        # Input instruction to be provided directly to opcode 3
        3: _opcode_3,
        4: opcode_4,
        5: opcode_5,
        6: opcode_6,
        7: opcode_7,
        8: opcode_8,
        99: opcode_99,
    }

    ix = 0
    while ix < len(state):
        code = state[ix]
        code, _ = parse_opcode_parameters(code)
        operation = opcodes[code]
        end, state, ix = operation(state, ix)
        if end:
            break

    return state
