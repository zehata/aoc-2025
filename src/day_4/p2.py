import sys
from _io import StringIO
from pathlib import Path
import numpy as np
from scipy import signal
import time
import re

np.set_printoptions(threshold=sys.maxsize)
np.set_printoptions(linewidth=sys.maxsize)


def convolve(df: np.ndarray[tuple[int, int]]) -> np.ndarray[tuple[int, int]]:
    scharr = np.array(
        [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1],
        ]
    )
    return signal.convolve2d(df, scharr, mode="same")


def convert_to_numbers(content: str) -> str:
    content = content.replace("@", "1,").replace(".", "0,").replace(",\n", "\n")
    return content


def convert_to_dataframe(content: str) -> np.ndarray[tuple[int, int]]:
    return np.genfromtxt(StringIO(content), skip_header=False, delimiter=",")


def FORKLIFTABLE_PAPER_ROLL_FORKLIFT_AWAY_INATOR(
    paper_rolls: np.ndarray[tuple[int, int]],
) -> np.ndarray[tuple[int, int]]:
    return paper_rolls // 2


def FORKLIFTABLE_PAPER_ROLL_IDENTIFY_INATOR(
    df: np.ndarray[tuple[int, int]],
) -> np.ndarray[tuple[int, int]]:
    convolved = convolve(df)
    return ((convolved + 1) // 5 + 1) * df


def count_paper_rolls(paper_rolls) -> int:
    uniques: dict[np.float64, int] = dict(
        zip(*np.unique(paper_rolls, return_counts=True))
    )
    if np.float64(1.0) in uniques.keys():
        return uniques[np.float64(1.0)]
    return 0


def REPEATEDLY_REMOVE_PAPER_ROLLS_INATOR(df: np.ndarray[tuple[int, int]]) -> int:
    grand_total = 0
    last_removed = 1
    while last_removed != 0:
        paper_rolls = FORKLIFTABLE_PAPER_ROLL_IDENTIFY_INATOR(df)
        last_removed = count_paper_rolls(paper_rolls)
        grand_total += last_removed
        df = FORKLIFTABLE_PAPER_ROLL_FORKLIFT_AWAY_INATOR(paper_rolls)
    return grand_total


def main():
    with Path("inputs/day_4/input").open("r") as file:
        grand_total = 0
        start = time.perf_counter_ns()
        content = file.read()
        content = convert_to_numbers(content)
        df = convert_to_dataframe(content)
        for i in range(100):
            grand_total = REPEATEDLY_REMOVE_PAPER_ROLLS_INATOR(df)
        print((time.perf_counter_ns() - start))
        print(grand_total)


def debug():
    with Path("inputs/day_4/test_input").open("r") as file:
        content = file.read()
        content = convert_to_numbers(content)
        df = convert_to_dataframe(content)
        paper_rolls = FORKLIFTABLE_PAPER_ROLL_IDENTIFY_INATOR(df)
        paper_rolls_with_symbols_removed = re.sub(
            r"[\[\]. ]", "", np.array_str(paper_rolls)
        )
        paper_rolls_repr = (
            paper_rolls_with_symbols_removed.replace("0", ".")
            .replace("1", "x")
            .replace("2", "@")
        )
        print(paper_rolls_repr)


if __name__ == "__main__":
    main()
