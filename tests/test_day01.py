from advent_of_code_2023.helpers.calibration_parser import CalibrationParser


def test_day01():
    cp = CalibrationParser("inputs/input-01.txt")
    part1_sum = 0
    part2_sum = 0
    for val in cp.correct_calibration_values():
        part1_sum += val

    for val in cp.correct_calibration_values(string_mapping=True):
        part2_sum += val

    print()
    print(f"Day 01, Part 01: {part1_sum}")
    print(f"Day 01, Part 02: {part2_sum}\n")
