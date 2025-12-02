from pathlib import Path
from typing import Optional


def get_input(day_number: int) -> list[str]:
    return get_lines(f"inputs/day_{str(day_number)}/input")


def get_test_input(day_number: int) -> list[str]:
    return get_lines(f"inputs/day_{str(day_number)}/test_input")


def get_lines(path: str) -> list[str]:
    lines: Optional[list[str]] = None
    with Path(path).open("r") as file:
        lines = file.readlines()
    return lines
