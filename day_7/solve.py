"""
Solving Day 7, 2019 Advent of Code Challenge
---
"""

import sys
import os
from itertools import permutations
from io import StringIO

utils_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.append(utils_path)
from utils import get_input_text, write_solution
from intcode_computer import run, Input


def text_to_intcode(input_text):
    return list(map(int, input_text.split(",")))


class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio
        sys.stdout = self._stdout


class Amplifier:

    def __init__(self, name, phase_setting, int_code):
        self.name = name
        self.phase_setting = phase_setting
        self.int_code = list(int_code)  # create a copy
        self.input = None
        self.output = None

    def run(self):
        print(self)
        if self.input is None:
            raise Exception("Set the input value")
        #  https://stackoverflow.com/questions/16571150/how-to-capture-stdout-output-from-a-python-function-call
        output = []
        with Capturing(output) as output:
            run(self.int_code, Input([self.phase_setting, self.input]))

        self.set_output(int(output[0]))

        print(f"\tOutputting: {self.output}")

    def set_output(self, value):
        self.output = value

    def set_input(self, value):
        self.input = value

    def get_output(self):
        return self.output

    def __repr__(self):
        return f"Amplifier {self.name}, input: {self.input}"

    def __str__(self):
        return self.__repr__()


def run_trial(int_code, phase_settings):
    a, b, c, d, e = phase_settings
    amps = [
        Amplifier("A", a, int_code),
        Amplifier("B", b, int_code),
        Amplifier("C", c, int_code),
        Amplifier("D", d, int_code),
        Amplifier("E", e, int_code)
    ]

    amps[0].set_input(0)

    for i in range(len(amps) - 1):
        amps[i].run()
        amps[i + 1].set_input(amps[i].get_output())

    amps[-1].run()
    return amps[-1].get_output()


if __name__ == "__main__":
    day = 7
    year = 2019
    input_text = get_input_text(day, year)

    ## Part 1 ##
    phase_settings = [0, 1, 2, 3, 4]
    int_code = text_to_intcode(input_text)
    highest_thrust = 0
    best_settings = []
    for settings in permutations(phase_settings):
        print("==========================")
        thrust = run_trial(int_code, settings)
        highest_thrust = max(thrust, highest_thrust)
        if thrust == highest_thrust:
            best_settings = settings

    print("\n==========================")
    print(f"Solution Day {day} (Part 1):")
    print(f"The highest thrust was {highest_thrust}")
    print(f"given by the phase settings {best_settings}")
    write_solution(day, year, str(highest_thrust))

    ## Part 2 ##
    #  print(f"Solution Day {day} (Part 2):")

    #  write_solution(day, year,
