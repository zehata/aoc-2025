# 100000 - 999999
# 1: 1, 2, 3, ...
# 2: 10, 11, 12, 13, ...
# 3: 100, 101, 102, 103, ...

# 200000 - 999999
# 1: 2, 3, ...
# 2: 20, 21, 22, 23, ...
# 3: 200, 201, 202, 203, ...

# 100000 - 888888
# 1: ..., 7, 8
# 2: ..., 86, 87, 88

# Copyright Doofenshmirtz Evil Incorporated 2025

from functools import cache
from utils.get_file import get_input
from math import ceil, floor, log10
import time


@cache
def get_range_to_check(no_of_digits) -> tuple[int, int]:
    return (10 ** (no_of_digits - 1), 10**no_of_digits - 1)


@cache
def get_no_of_digits(number):
    return ceil(log10(number))


def get_ranges_to_check(min_number: int, max_number: int) -> list[tuple[int, int, int]]:
    no_of_digits_min = get_no_of_digits(min_number)
    no_of_digits_max = get_no_of_digits(max_number)
    list_of_number_of_digits_to_check = range(no_of_digits_min, no_of_digits_max + 1)
    ranges_to_check = [
        (no_of_digits, *get_range_to_check(no_of_digits))
        for no_of_digits in list_of_number_of_digits_to_check
    ]
    if not len(ranges_to_check):
        return []
    ranges_to_check[0] = (
        ranges_to_check[0][0],
        max(ranges_to_check[0][1], min_number),
        ranges_to_check[0][2],
    )
    ranges_to_check[-1] = (
        ranges_to_check[-1][0],
        ranges_to_check[-1][1],
        min(ranges_to_check[-1][2], max_number),
    )
    return ranges_to_check


def get_candidate_numbers(half_of_no_of_digits: int, range_min: int, range_max: int):
    min_number_candidate = int(range_min // 10**half_of_no_of_digits)
    max_number_candidate = int(range_max // 10**half_of_no_of_digits)
    min_number = (
        min_number_candidate + 1
        if range_min % 10**half_of_no_of_digits > min_number_candidate
        else min_number_candidate
    )
    max_number = (
        max_number_candidate
        if range_max % 10**half_of_no_of_digits < max_number_candidate
        else max_number_candidate + 1
    )
    return range(min_number, max_number)


@cache
def get_divisors(number: int) -> set[int]:
    sqrt = floor(number**1 / 2)
    divisors: set[int] = {1}
    for i in range(2, sqrt + 1):
        if number % i == 0:
            divisors.add(i)
            divisors.add(int(number / i))
    return divisors


def repeat_number(number, no_of_digits, repeats):
    total = 0
    for i in range(repeats):
        total += number * (10**no_of_digits) ** i
    return total


def get_invalid_ids(
    min_number: int, max_number: int, no_of_digits: int, repeats: int
) -> set[int]:
    places_to_remove = 10 ** ((repeats - 1) * no_of_digits)
    min_repeatable = min_number // places_to_remove
    max_repeatable = max_number // places_to_remove
    invalid_ids = set()
    for i in range(min_repeatable, max_repeatable + 1):
        number = repeat_number(i, no_of_digits, repeats)
        if number >= min_number and number <= max_number:
            invalid_ids.add(number)
    return invalid_ids


def parse_range(min_number: int, max_number: int) -> set[int]:
    ranges_to_check = get_ranges_to_check(min_number, max_number)
    invalid_ids: set[int] = set()
    for range_to_check in ranges_to_check:
        no_of_digits = range_to_check[0]
        if no_of_digits < 2:
            continue
        divisors = get_divisors(no_of_digits)
        for divisor in divisors:
            invalid_ids = invalid_ids | get_invalid_ids(
                range_to_check[1],
                range_to_check[2],
                divisor,
                int(no_of_digits / divisor),
            )
    return invalid_ids


def INVALID_PRODUCT_ID_SUM_INATOR_17_PRO_MAX(input: str):
    ranges = input.split(",")
    grand_total = 0
    for range in ranges:
        invalid_ids = parse_range(*[int(number) for number in range.split("-")])
        grand_total += sum(invalid_ids)
    return grand_total


def main():
    line = get_input(2)[0]
    start = time.perf_counter_ns()
    total = INVALID_PRODUCT_ID_SUM_INATOR_17_PRO_MAX(line)
    print(time.perf_counter_ns() - start)  # 2E6 ns -> 2 ms (!)
    print(total)


if __name__ == "__main__":
    main()
