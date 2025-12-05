from time import perf_counter_ns
from utils.get_file import get_input, get_test_input
from intervaltree import IntervalTree


def SPOILED_FOOD_IDENTIFY_INATOR(lines):
    tree = IntervalTree()
    total = 0
    for line in lines:
        if line == "\n":
            continue
        res = line.split("-")
        if len(res) > 1:
            tree.addi(int(res[0]), int(res[1]) + 1)
            continue
        if len(tree[int(res[0][:-1])]):
            total += 1
    return total


def main():
    lines = get_test_input(5)
    start = perf_counter_ns()
    total = SPOILED_FOOD_IDENTIFY_INATOR(lines)
    print(total)
    print(perf_counter_ns() - start)


if __name__ == "__main__":
    main()
