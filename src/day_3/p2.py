from utils.get_file import get_input, get_test_input


def split_number(number):
    number = int(number)
    digits = []
    while number > 0:
        digit = number % 10
        digits.append(digit)
        number //= 10
    return digits


def find_largest_digit_index_in_range(digits, range_min, range_max) -> tuple[int, int]:
    largest_digit = 0
    largest_digit_index = 0
    for digit_index in range(range_max - 1, range_min - 1, -1):
        digit = digits[digit_index]
        if digit == 9:
            return (digit_index, 9)
        if digit > largest_digit:
            largest_digit = digit
            largest_digit_index = digit_index
    return (largest_digit_index, largest_digit)


def ESCALATOR_EMERGENCY_POWER_BATTERY_EXPLODE_INATOR(line):
    digits = split_number(line)
    max_index_to_check = len(digits)
    index = 12
    joltage = 0
    while index > 0:
        joltage *= 10
        index -= 1
        largest_digit_index, largest_digit = find_largest_digit_index_in_range(
            digits, index, max_index_to_check
        )
        max_index_to_check = largest_digit_index
        joltage += largest_digit
    return joltage


def main():
    lines = get_input(3)
    total_joltage = 0
    for line in lines:
        total_joltage += ESCALATOR_EMERGENCY_POWER_BATTERY_EXPLODE_INATOR(line)
    print(total_joltage)


if __name__ == "__main__":
    main()
