import sys
import json
import os

## Setup Filepaths ##
_home = os.path.expanduser("~")
_base = os.path.dirname(os.path.abspath(__file__))
paths = ['.', '..', _home]

config_path = None
for path in paths:
    path = os.path.join(path, 'aoc_config.json')
    if os.path.exists(path):
        config_path = path

if not config_path:
    raise Exception("Config not found")

with open(config_path) as f:
    CONFIG = json.load(f)


def get_input_filepath(day: int, year: int) -> str:
    global CONFIG
    global config_path
    fname = f'input_{year}_{day}.txt'
    config_dir = os.path.dirname(config_path)
    fpath = os.path.join(config_dir,
                         CONFIG['directory'],
                         str(year),
                         fname)

    if not os.path.exists(fpath):
        os.mkdir(fpath)

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
