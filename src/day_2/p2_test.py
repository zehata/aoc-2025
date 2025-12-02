from utils.get_file import get_test_input
from day_2.p2 import INVALID_PRODUCT_ID_SUM_INATOR_17_PRO_MAX
from day_2.p2 import get_divisors, get_invalid_ids


def test_correctness():
    input = get_test_input(2)[0]
    assert INVALID_PRODUCT_ID_SUM_INATOR_17_PRO_MAX(input) == 4174379265


def test_get_divisors():
    assert get_divisors(30) == {1, 2, 3, 5, 6, 10, 15}


def test_get_invalid_ids():
    assert get_invalid_ids(88, 99, 1, 2) == {
        88,
        99,
    }

    assert get_invalid_ids(99, 99, 1, 2) == {
        99,
    }

    assert get_invalid_ids(112, 222, 1, 3) == {
        222,
    }

    assert get_invalid_ids(112, 221, 1, 3) == set()

    assert get_invalid_ids(8888, 9999, 2, 2) == {
        8888,
        8989,
        9090,
        9191,
        9292,
        9393,
        9494,
        9595,
        9696,
        9797,
        9898,
        9999,
    }

    assert get_invalid_ids(111111, 222221, 1, 6) == {
        111111,
    }

    assert get_invalid_ids(123123, 123123, 3, 2) == {
        123123,
    }

    assert get_invalid_ids(121212, 121212, 2, 3) == {
        121212,
    }

    assert get_invalid_ids(11111, 22222, 1, 5) == {
        11111,
        22222,
    }

    assert get_invalid_ids(7779, 9998, 1, 4) == {
        8888,
    }

    assert get_invalid_ids(3, 9, 1, 4) == set()
