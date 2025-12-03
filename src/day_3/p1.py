from utils.get_file import get_test_input, get_input


def ESCALATOR_EMERGENCY_POWER_BATTERY_SELECT_INATOR(number_str: str) -> int:
    number = int(number_str)
    digits = []
    index = 0
    index_of_max_digit = 0
    max_digit = 0

    while number > 0:
        digit = number % 10
        digits.append(digit)
        number //= 10
        if index > 0 and digit >= max_digit:
            max_digit = digit
            index_of_max_digit = index
        index += 1

    index = index_of_max_digit
    max_second_digit = 0
    while index > 0:
        index -= 1
        digit = digits[index]
        if digit >= max_second_digit:
            max_second_digit = digit

    return max_digit * 10 + max_second_digit


def main():
    lines = get_input(3)
    total_power = 0
    for line in lines:
        total_power += ESCALATOR_EMERGENCY_POWER_BATTERY_SELECT_INATOR(line)
    print(total_power)


if __name__ == "__main__":
    main()
