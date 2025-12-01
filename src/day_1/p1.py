# Copyright Doofenshmirtz Evil Incorporated 2025

from pathlib import Path
from day_1.common import INITIAL_POSITION, DIAL_NOTCHES


def DOOR_PASSWORD_CRACK_INATOR(secret_document: list[str]):
    current_position = INITIAL_POSITION
    tally = 0
    for line in secret_document:
        current_position += int(line[1:]) * (-1 if line[0] == "L" else 1)
        current_position %= DIAL_NOTCHES
        if not current_position:
            tally += 1
    return tally


def main():
    with Path("inputs/day_1/input").open("r") as file:
        secret_document = file.readlines()
        your_precious_password = DOOR_PASSWORD_CRACK_INATOR(secret_document)

        print(your_precious_password)


if __name__ == "__main__":
    main()
