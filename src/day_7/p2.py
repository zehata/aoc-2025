from time import perf_counter_ns
from utils.get_file import get_input, get_test_input
import numpy as np


def parse_line(tachyon_beams, splitters):
    intercepted = tachyon_beams * splitters
    convolved = np.convolve(intercepted, [1, 0, 1], mode="same")
    output = tachyon_beams * np.logical_not(intercepted) + convolved
    return output


def QUANTUM_TACHYON_BEAM_SPLITTER_INTERCEPTED_COUNT_INATOR(lines):
    tachyon_beams = None
    for index in range(len(lines)):
        line = lines[index][:-1]

        if index % 2:
            continue

        if not index:
            tachyon_beams = np.array(
                list(line.replace("S", "1").replace(".", "0")), dtype=int
            )
            continue

        splitters = np.array(list(line.replace("^", "1").replace(".", "0")), dtype=int)
        tachyon_beams = parse_line(tachyon_beams, splitters)
    assert tachyon_beams is not None
    return tachyon_beams.sum()


def main():
    total_timelines = 0
    lines = get_input(7)
    start = perf_counter_ns()
    for i in range(1000):
        total_timelines = QUANTUM_TACHYON_BEAM_SPLITTER_INTERCEPTED_COUNT_INATOR(lines)
    print((perf_counter_ns() - start) / 1000000000)
    print(total_timelines)


if __name__ == "__main__":
    main()
