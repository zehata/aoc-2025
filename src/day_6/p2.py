from time import perf_counter_ns
from utils.get_file import get_test_input
from utils.get_file import get_input
from itertools import pairwise
import pandas as pd
import numpy as np


def is_multiply(x):
    return x == "+"


def CHEAT_MATH_HOMEWORK_INATOR(ranges: list[list[int]], last_line: str):
    coefficients = np.array(ranges, dtype=float)
    operations = np.array(last_line.split())
    mask = is_multiply(operations)
    inv = np.logical_not(mask)
    to_multiply = coefficients[~mask]
    to_add = coefficients[~inv]
    return int(np.nansum(np.nanprod(to_multiply, axis=1)) + np.nansum(to_add))


def transform_data(lines: list[str], number_of_spaces: int) -> list[list[int]]:
    data = [list(line[:-1]) for line in lines[0:-1]]

    df = pd.DataFrame(["".join(x) for x in zip(*data)])
    spaces = df.index[df[0] == " " * number_of_spaces]
    spaces = [-1] + list(spaces) + [len(df)]
    nums = df[0].tolist()
    ranges: list[list[int]] = [
        nums[i + 1 : j] + ["NaN"] * (5 - j + i) for i, j in pairwise(spaces)
    ]
    return ranges


def main():
    lines = get_input(6)
    answer = 0
    start = perf_counter_ns()
    for i in range(1000):
        number_of_spaces = len(lines) - 1
        last_line = lines[-1]
        ranges = transform_data(lines, number_of_spaces)
        answer = CHEAT_MATH_HOMEWORK_INATOR(ranges, last_line)
    print((perf_counter_ns() - start) / 1000)
    print(answer)


if __name__ == "__main__":
    main()
