"""
Solving Day 1, 2019 Advent of Code Challenge
---
Santa has become stranded at the edge of the Solar System while delivering presents to other planets! To accurately calculate his position in space, safely align his warp drive, and return to Earth in time to save Christmas, he needs you to bring him measurements from fifty stars.

Collect stars by solving puzzles.  Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first.  Each puzzle grants one star. Good luck!


The Elves quickly load you into a spacecraft and prepare to launch.
At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper.  They haven't determined the amount of fuel required yet.
Fuel required to launch a given module is based on its mass.  Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.
For example:
The Fuel Counter-Upper needs to know the total fuel requirement.  To find it, individually calculate the fuel needed for the mass of each module (your puzzle input), then add together all the fuel values.
What is the sum of the fuel requirements for all of the modules on your spacecraft?
===

Part 2
---
During the second Go / No Go poll, the Elf in charge of the Rocket Equation Double-Checker stops the launch sequence.  Apparently, you forgot to include additional fuel for the fuel you just added.
Fuel itself requires fuel just like a module - take its mass, divide by three, round down, and subtract 2.  However, that fuel also requires fuel, and that fuel requires fuel, and so on.  Any mass that would require negative fuel should instead be treated as if it requires zero fuel; the remaining mass, if any, is instead handled by wishing really hard, which has no mass and is outside the scope of this calculation.
So, for each module mass, calculate its fuel and add it to the total.  Then, treat the fuel amount you just calculated as the input mass and repeat the process, continuing until a fuel requirement is zero or negative. For example:
What is the sum of the fuel requirements for all of the modules on your spacecraft when also taking into account the mass of the added fuel? (Calculate the fuel requirements for each module separately, then add them all up at the end.)
Although it hasn't changed, you can still get your puzzle input.
"""

import sys
import os
utils_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.append(utils_path)
from utils import get_input_text, write_solution


def parse_masses(input_str: str) -> list:
    """
    Convert the input string (puzzle input) to a list of
    module masses

    Args:
        input_str (str): input string of the puzzle input

    Returns:
        list of masses ([int])
    """

    output = input_str.strip('\n').split("\n")
    return list(map(int, output)) if any(output) else []


def calculate_fuel(mass: int) -> int:
    """
    Calculate the fuel requirement given a module's `mass`

    Args:
        mass (int): module mass

    Returns:
        int of fuel requirement for the given mass
    """

    return (mass // 3) - 2


def calculate_fuel_recur(mass: int) -> int:
    """
    Calculate the fuel requirement given a module's `mass`
    It is also necessary to account for the fuel required
    for the mass of fuel (in addition to the given `mass`)
    Therefore, continue to calculate fuel requirement while
    the fuel value is non-negative

    Args:
        mass (int): module mass

    Returns:
        int of fuel requirement for the given mass
    """

    fuel = (mass // 3) - 2
    return fuel + calculate_fuel_recur(fuel) if fuel > 0 else 0


if __name__ == "__main__":
    day = 1
    year = 2019
    input_text = get_input_text(day, year)

    ## Part 1 ##
    # Get Mass Values
    masses = parse_masses(input_text)

    # Calculate the Total Fuel Requirement
    total_fuel = sum(list(map(calculate_fuel, masses)))
    print("Solution Day 1 (Part 1):")
    print("\tTotal Fuel Requirement:", total_fuel)

    write_solution(day, year, str(total_fuel))

    ## Part 2 ##
    total_fuel = sum(list(map(calculate_fuel_recur, masses)))
    print("Solution Day 1 (Part 2):")
    print("\tTotal Fuel Requirement:", total_fuel)

    write_solution(day, year, str(total_fuel), part_2=True)
