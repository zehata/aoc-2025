from time import perf_counter_ns
from utils.get_file import get_input, get_test_input
from intervaltree import IntervalTree


def SPOILED_FOOD_IDS_TREE_BUILD_INATOR(lines) -> IntervalTree:
    tree = IntervalTree()
    total = 0
    for line in lines:
        if line == "\n":
            tree.merge_overlaps()
            continue
        res = line.split("-")
        if len(res) > 1:
            tree.addi(int(res[0]), int(res[1]) + 1)
            continue
        if len(tree[int(res[0][:-1])]):
            total += 1
    return tree


def VALID_ID_IDENTIFY_INATOR(tree: IntervalTree) -> int:
    interval_total = 0
    for i in tree:
        interval_total += i[1] - i[0]
    return interval_total


def main():
    lines = get_input(5)
    sum_of_valid_ranges = 0
    start = perf_counter_ns()
    for i in range(1000):
        tree = SPOILED_FOOD_IDS_TREE_BUILD_INATOR(lines)
        sum_of_valid_ranges = VALID_ID_IDENTIFY_INATOR(tree)
    print(sum_of_valid_ranges)
    print(
        (perf_counter_ns() - start) / 1000000000
    )  # 8.928885147ms average over 1000 runs


if __name__ == "__main__":
    main()
