import sys
import json
import os

_base = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(_base, '..', 'aoc_config.json')
with open(config_path) as f:
    CONFIG = json.load(f)


def get_input_filepath(day: int, year: int) -> str:
    global CONFIG
    global config_path
    fname = f'input_{year}_{day}.txt'
    fpath = os.path.join(_base,
                         '..',
                         CONFIG['directory'],
                         str(year),
                         fname)
    return fpath


def get_input_text(day: int, year: int) -> str:
    input_text = ""
    with open(get_input_filepath(day, year)) as f:
        input_text = f.read()

    return input_text


def write_solution(day: int, year: int, solution: str, part_2: bool = False):
    part = "part_2" if part_2 else "part_1"
    fname = f"solution_{year}_{day}_{part}.txt"
    with open(fname, 'w+') as f:
        f.write(solution)
