# Copyright Doofenshmirtz Evil Incorporated 2025

from pathlib import Path
from day_1.common import INITIAL_POSITION, DIAL_NOTCHES


def parse_line(current_position, clicks):
    if clicks < 0:
        temp_position = (100 - current_position) % 100
        temp_position -= clicks
        to_add = temp_position // DIAL_NOTCHES
        temp_position %= DIAL_NOTCHES
        current_position = (100 - temp_position) % 100
        return (current_position, to_add)

    current_position += clicks
    to_add = current_position // DIAL_NOTCHES
    current_position %= DIAL_NOTCHES
    return (current_position, to_add)


def DOOR_PASSWORD_CRACK_INATOR_17_ULTRA_PRO_MAX(secret_document: list[str]):
    current_position = INITIAL_POSITION
    tally = 0
    for line in secret_document:
        clicks = int(line[1:]) * (-1 if line[0] == "L" else 1)
        current_position, to_add = parse_line(current_position, clicks)
        tally += to_add
    return tally


def main():
    with Path("inputs/day_1/input").open("r") as file:
        secret_document = file.readlines()
        your_precious_password = DOOR_PASSWORD_CRACK_INATOR_17_ULTRA_PRO_MAX(
            secret_document
        )

        print(your_precious_password)


if __name__ == "__main__":
    main()
