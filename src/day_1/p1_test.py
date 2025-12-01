from day_1.p1 import DOOR_PASSWORD_CRACK_INATOR
from pathlib import Path


def test_correctness():
    with Path("inputs/day_1/test_input").open("r") as file:
        secret_document = file.readlines()
        your_precious_password = DOOR_PASSWORD_CRACK_INATOR(secret_document)

    assert your_precious_password == 3
