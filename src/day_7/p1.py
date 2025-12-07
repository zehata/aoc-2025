from utils.get_file import get_input, get_test_input
import numpy as np


def parse_line(tachyon_beams, splitters):
    intercepted = tachyon_beams * splitters
    convolved = np.convolve(intercepted, [1, 0, 1], mode="same")
    output = (tachyon_beams * np.logical_not(intercepted) + convolved) > 0
    return intercepted.sum(), output


def TACHYON_BEAM_SPLITTER_INTERCEPTED_COUNT_INATOR(lines):
    tachyon_beams = None
    total = 0
    for index in range(len(lines)):
        line = lines[index][:-1]

        if index % 2:
            continue

        if not index:
            tachyon_beams = np.array(
                list(line.replace("S", "1").replace(".", "0")), dtype=int
            ).astype(bool)
            continue

        splitters = np.array(
            list(line.replace("^", "1").replace(".", "0")), dtype=int
        ).astype(bool)
        intercepted_beams, tachyon_beams = parse_line(tachyon_beams, splitters)
        total += intercepted_beams
    return total


def main():
    lines = get_input(7)
    print(TACHYON_BEAM_SPLITTER_INTERCEPTED_COUNT_INATOR(lines))


if __name__ == "__main__":
    main()
