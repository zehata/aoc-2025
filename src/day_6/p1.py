from _io import StringIO
from pathlib import Path
import numpy as np


def is_multiply(x):
    return x == "+"


def CHEAT_MATH_HOMEWORK_INATOR(data: StringIO, last_line: str):
    coefficients = np.genfromtxt(data, unpack=True)
    operations = np.array(last_line.split())
    mask = is_multiply(operations)
    inv = np.logical_not(mask)
    to_multiply = coefficients[~mask]
    to_add = coefficients[~inv]
    return int(to_multiply.prod(axis=1).sum() + to_add.sum())


def main():
    with Path("inputs/day_6/input").open("r") as file:
        content = file.read()
        data, last_line, _ = content.rsplit("\n", 2)
        print(CHEAT_MATH_HOMEWORK_INATOR(StringIO(data), last_line))


if __name__ == "__main__":
    main()
