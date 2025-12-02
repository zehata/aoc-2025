# Copyright Doofenshmirtz Evil Incorporated 2025

from utils.get_file import get_input
from math import ceil, log10


def get_list_of_number_of_digits_to_check(
    no_of_digits_min, no_of_digits_max
) -> list[int]:
    list_of_number_of_digits_to_check: list[int] = []
    i = no_of_digits_min
    while i < no_of_digits_max + 1:
        if not i % 2:
            list_of_number_of_digits_to_check.append(i)
        i += 1

    return list_of_number_of_digits_to_check


def get_range_to_check(no_of_digits) -> tuple[int, int]:
    return (10 ** (no_of_digits - 1), 10**no_of_digits - 1)


def get_no_of_digits(number):
    return ceil(log10(number))


def get_ranges_to_check(min_number: int, max_number: int) -> list[tuple[int, int, int]]:
    no_of_digits_min = get_no_of_digits(min_number)
    no_of_digits_max = get_no_of_digits(max_number)
    list_of_number_of_digits_to_check = get_list_of_number_of_digits_to_check(
        no_of_digits_min, no_of_digits_max
    )
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


def parse_range(min_number: int, max_number: int) -> list[int]:
    ranges_to_check = get_ranges_to_check(min_number, max_number)
    invalid_ids = []
    for range_to_check in ranges_to_check:
        half_of_no_of_digits = int(range_to_check[0] / 2)
        repeated_numbers = get_candidate_numbers(
            half_of_no_of_digits, range_to_check[1], range_to_check[2]
        )
        invalid_ids += [
            repeated_number * (10**half_of_no_of_digits) + repeated_number
            for repeated_number in repeated_numbers
        ]
    return invalid_ids


def INVALID_PRODUCT_ID_SUM_INATOR(input: str):
    ranges = input.split(",")
    grand_total = 0
    for range in ranges:
        invalid_ids = parse_range(*[int(number) for number in range.split("-")])
        grand_total += sum(invalid_ids)
    return grand_total


def main():
    line = get_input(2)[0]
    total = INVALID_PRODUCT_ID_SUM_INATOR(line)
    print(total)


if __name__ == "__main__":
    main()
