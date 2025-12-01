# Copyright Doofenshmirtz Evil Incorporated 2025

from pathlib import Path

INITIAL_POSITION = 50
DIAL_NOTCHES = 100


def DOOR_PASSWORD_CRACK_INATOR(secret_document: list[str]):
    current_position = INITIAL_POSITION
    tally = 0
    for line in secret_document:
        current_position += int(line[1:]) * (-1 if line[0] == "L" else 1)
        current_position %= DIAL_NOTCHES
        if not current_position:
            tally += 1
    return tally


def parse_line(current_position, clicks):
    if clicks < 0:
        temp_position = (100 - current_position) % 100
        temp_position -= clicks
        to_add = temp_position // DIAL_NOTCHES
        temp_position %= DIAL_NOTCHES
        current_position = (100 - temp_position) % 100
    else:
        current_position += clicks
        to_add = abs(current_position // DIAL_NOTCHES)
        current_position %= DIAL_NOTCHES
    return (current_position, to_add)


def test_line(input, expected):
    answer = parse_line(*input)
    print(
        (f"Test for {input}").ljust(22),
        str(answer).ljust(10),
        str(expected).ljust(10),
        answer == expected,
    )


def tests():
    test_line((0, -201), (99, 2))
    test_line((0, -200), (0, 2))
    test_line((0, -101), (99, 1))
    test_line((0, -100), (0, 1))
    print()
    test_line((0, 0), (0, 0))
    test_line((0, 100), (0, 1))
    test_line((0, 101), (1, 1))
    test_line((0, 200), (0, 2))
    test_line((0, 201), (1, 2))
    print()
    test_line((1, -201), (0, 3))
    test_line((1, -200), (1, 2))
    test_line((1, -101), (0, 2))
    test_line((1, -100), (1, 1))
    test_line((1, -1), (0, 1))
    print()
    test_line((1, 99), (0, 1))
    test_line((1, 100), (1, 1))
    test_line((1, 199), (0, 2))
    test_line((1, 200), (1, 2))
    print()
    test_line((40, 20), (60, 0))
    test_line((40, -20), (20, 0))


def DOOR_PASSWORD_CRACK_INATOR_17_ULTRA_PRO_MAX(secret_document: list[str]):
    current_position = INITIAL_POSITION
    tally = 0
    for line in secret_document:
        clicks = int(line[1:]) * (-1 if line[0] == "L" else 1)
        current_position, to_add = parse_line(current_position, clicks)
        tally += to_add
    return tally


with Path("input").open("r") as file:
    secret_document = file.readlines()
    your_precious_password = DOOR_PASSWORD_CRACK_INATOR_17_ULTRA_PRO_MAX(
        secret_document
    )

    print(your_precious_password)
