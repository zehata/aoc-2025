from utils.get_file import get_test_input
from day_1.p1 import DOOR_PASSWORD_CRACK_INATOR


def test_correctness():
    lines = get_test_input(1)
    your_precious_password = DOOR_PASSWORD_CRACK_INATOR(lines)
    assert your_precious_password == 3
