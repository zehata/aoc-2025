from day_2.p1 import INVALID_PRODUCT_ID_SUM_INATOR
from utils.get_file import get_test_input


def test_correctness():
    input = get_test_input(2)[0]
    sum = INVALID_PRODUCT_ID_SUM_INATOR(input)
    assert sum == 1227775554
