from day_1.p2 import DOOR_PASSWORD_CRACK_INATOR_17_ULTRA_PRO_MAX
from pathlib import Path
from day_1.p2 import parse_line


def test_correctness():
    with Path("inputs/day_1/test_input").open("r") as file:
        secret_document = file.readlines()
        your_precious_password = DOOR_PASSWORD_CRACK_INATOR_17_ULTRA_PRO_MAX(
            secret_document
        )

    assert your_precious_password == 6


def test_starting_at_zero():
    assert parse_line(0, -201) == (99, 2)
    assert parse_line(0, -200) == (0, 2)
    assert parse_line(0, -101) == (99, 1)
    assert parse_line(0, -100) == (0, 1)

    assert parse_line(0, 0) == (0, 0)
    assert parse_line(0, 100) == (0, 1)
    assert parse_line(0, 101) == (1, 1)
    assert parse_line(0, 200) == (0, 2)
    assert parse_line(0, 201) == (1, 2)


def test_starting_at_non_zero():
    assert parse_line(1, -201) == (0, 3)
    assert parse_line(1, -200) == (1, 2)
    assert parse_line(1, -101) == (0, 2)
    assert parse_line(1, -100) == (1, 1)
    assert parse_line(1, -1) == (0, 1)
    print()
    assert parse_line(1, 99) == (0, 1)
    assert parse_line(1, 100) == (1, 1)
    assert parse_line(1, 199) == (0, 2)
    assert parse_line(1, 200) == (1, 2)
