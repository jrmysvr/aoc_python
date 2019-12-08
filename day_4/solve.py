"""
Solving Day 4, 2019 Advent of Code Challenge
---

You arrive at the Venus fuel depot only to discover it's protected by a
password.  The Elves had written the password on a sticky note, but someone
threw it out.
However, they do remember a few key facts about the password:
    It is a six-digit number.
    The value is within the range given in your puzzle input.
    Two adjacent digits are the same (like 22 in 122345).
    Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

Other than the range rule, the following are true:
    111111 meets these criteria (double 11, never decreases).
    223450 does not meet these criteria (decreasing pair of digits 50).
    123789 does not meet these criteria (no double).

How many different passwords within the range given in your puzzle
input meet these criteria?
===

Part 2

The first half of this puzzle is complete! It provides one gold star: *
An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.
Given this additional criterion, but still ignoring the range rule, the following are now true:
How many different passwords within the range given in your puzzle input meet all of the criteria?
"""
import sys
import os
utils_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.append(utils_path)
from utils import get_input_text, write_solution


def parse_range(input_text: str) -> tuple:
    """
    Parse input range values from challenge input text

    Args:
        input_text (str): input text from challenge

    Returns:
        tuple of int values (low, high) of value range
    """

    return tuple(map(int, input_text.split("-")))


def calculate_number_of_passwords(low: int, high: int) -> int:
    """
    Calculate the number of possible passwords within a range [`low`, `high`]

    Args:
        low (int): lowest value (inclusive)
        high (int): highest value (inclusive)

    Returns:
        number (int) of valid passwords within the given range
    """

    return 0


def is_six_digits(num: int) -> bool:
    """ Predicate to check if `num` has 6 digits """
    return len(str(num)) == 6


def is_within_range(num: int, low: int, high: int) -> bool:
    """ Predicate to check if number is between `low` and `high` values (both inclusive) """
    return low <= num <= high


def take_while(ls: list, value):
    output = []
    for i, elem in enumerate(ls):
        if elem != value:
            break
        output.append(elem)

    return output, ls[len(output):]


def has_a_doubled_digit(num) -> bool:
    """
    Predicate to check if a number has two adjacent digits that are the same
    It's also necessary to check if any double digit isn't part of a larger group
    of the same digits
    """
    digits = list(map(int, str(num)))
    groups = []
    while digits:
        taken, digits = take_while(digits, digits[0])
        groups.append(taken)

    return any([len(group) == 2 for group in groups])


def has_no_decreasing_digits(num) -> bool:
    """ Predicate to check that digits of `num` do not decrease """
    digits = list(map(int, str(num)))
    previous = digits[0]
    for current in digits[1:]:
        if not (previous <= current):
            return False
        previous = current

    return True


def is_valid_password(password: int, low: int, high: int) -> bool:
    """ Check password validity based on a series of predicates """

    def is_within_given_range(num):
        return is_within_range(num, low, high)

    predicates = [
        is_six_digits,
        is_within_given_range,
        has_a_doubled_digit,
        has_no_decreasing_digits
    ]

    return all([is_valid(password) for is_valid in predicates])


def count_valid_passwords(low: int, high: int) -> int:
    """ Count valid passwords between `low` and `high` values (both inclusive)"""
    def is_valid(password) -> bool:
        return is_valid_password(password, low, high)

    return len(list(filter(bool, map(is_valid, range(low, high + 1)))))


if __name__ == "__main__":
    day = 4
    year = 2019
    input_text = get_input_text(day, year)

    low, high = parse_range(input_text)
    count = count_valid_passwords(low, high)
    # Part 1 solution had different criteria that was invalidated with Part 2
    #  print(f"Solution Day {day} (Part 1):")
    #  print("\tThe number of valid passwords between"
    #  f" {low} and {high} is {count}")

    # write_solution(day, year, str(count))

    print(f"Solution Day {day} (Part 2):")
    print("\tThe number of valid passwords between"
          f" {low} and {high} is {count}")

    write_solution(day, year, str(count), part_2=True)
