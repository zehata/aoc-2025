import sys
from _io import StringIO
from pathlib import Path
import numpy as np

np.set_printoptions(threshold=sys.maxsize)
np.set_printoptions(linewidth=sys.maxsize)
from scipy import signal
import re

import time


def convolve(df):
    scharr = np.array(
        [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1],
        ]
    )
    return signal.convolve2d(df, scharr, mode="same")


def convert_to_numbers(content):
    content = content.replace("@", "1,").replace(".", "0,").replace(",\n", "\n")
    return content


def convert_to_dataframe(content):
    return np.genfromtxt(StringIO(content), skip_header=False, delimiter=",")


def FORKLIFTABLE_PAPER_ROLL_IDENTIFY_INATOR(content):
    content = convert_to_numbers(content)
    df = convert_to_dataframe(content)
    convolved = convolve(df)
    return (convolved < 4) * df


def count_paper_rolls(paper_rolls):
    uniques, counts = np.unique(paper_rolls, return_counts=True)
    print(*zip(uniques, counts))
    return counts[1]


def main():
    with Path("inputs/day_4/input").open("r") as file:
        content = file.read()
        start = time.perf_counter_ns()
        paper_rolls = FORKLIFTABLE_PAPER_ROLL_IDENTIFY_INATOR(content)
        print((time.perf_counter_ns() - start))
        print(count_paper_rolls(paper_rolls))


def debug():
    with Path("inputs/day_4/test_input").open("r") as file:
        content = file.read()
        paper_rolls = FORKLIFTABLE_PAPER_ROLL_IDENTIFY_INATOR(content)
        print(paper_rolls)
        removed_symbols = re.sub(r"[\[\]. ]", "", np.array_str(paper_rolls))
        removed_ones = re.sub(r"1", "x", removed_symbols)
        removed_zeros = re.sub(r"0", ".", removed_ones)
        paper_rolls_repr = re.sub(r"\d", "@", removed_zeros)
        print(paper_rolls_repr)
        print(len(re.findall(r"x", paper_rolls_repr)))


if __name__ == "__main__":
    main()
