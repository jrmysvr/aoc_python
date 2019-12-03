# [Advent of Code - 2019](https://adventofcode.com)

**Build**
> python -m pip install -e .

_Additionally, a file called `aoc_config.json` is used to setup filepaths_
_I have the config in a separate module that also uses the config for saving challenge/input text_
_`utils.py` looks for `aoc_config.json` in the current directory_
_The important field to have in the config is `"directory"`_

    {
        ...
        "directory": "challenges",
        ...
    }

Save challenge/input text with the following structure:

    challenges
        2019
            aoc_<year>_<day>.txt
            input_<year>_<day>.txt
            ...

    where <year> is the respective year
    and <day> is the respective day
        `aoc_2019_1.txt`
        `input_2019_1.txt`
**Test**
>pytest

**Run**

>python <day_?>/solve.py
`python day_1/solve.py`

## Solutions
### [Day 1](day_1)
### [Day 2](day_2)

