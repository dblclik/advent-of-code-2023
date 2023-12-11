import re
from math import ceil, floor

from advent_of_code_2023.helpers.quadratic_solver import quadratic_solver

NUMBER_ENTRIES = re.compile(r"\d+")


def test_day06_example():
    print()
    test_input = """Time:      7  15   30
Distance:  9  40  200"""

    times_line, distances_line = test_input.split("\n")
    times = [int(m) for m in NUMBER_ENTRIES.findall(times_line)]
    distances = [int(m) for m in NUMBER_ENTRIES.findall(distances_line)]

    margin_of_error = 1
    for b, c in zip(times, distances):
        lh_zero, rh_zero = quadratic_solver(
            -1, b, -(c + 0.0001)
        )  # add a small delta to c in order to ensure we're >

        print(
            f"For b={b}, c={-c}, the solution range is: {(floor(rh_zero) - ceil(lh_zero) + 1)}"
        )
        margin_of_error *= floor(rh_zero) - ceil(lh_zero) + 1

    print(f"Day 06, Example 01, margin of error is: {margin_of_error}")

    # Some bad kerning for Part 02, so we just need to concat the times and distances to make 2 integers total
    time = int("".join([m for m in NUMBER_ENTRIES.findall(times_line)]))
    distance = int("".join([m for m in NUMBER_ENTRIES.findall(distances_line)]))

    margin_of_error = 1
    lh_zero, rh_zero = quadratic_solver(
        -1, time, -(distance + 0.0001)
    )  # add a small delta to c in order to ensure we're >

    print(
        f"For b={time}, c={-distance}, the solution range is: {(floor(rh_zero) - ceil(lh_zero) + 1)}"
    )
    margin_of_error *= floor(rh_zero) - ceil(lh_zero) + 1

    print(f"Day 06, Example 01, margin of error is: {margin_of_error}")


def test_day06():
    print()
    print()
    test_input = open("inputs/input-06.txt").read()

    times_line, distances_line = test_input.split("\n")[:2]
    times = [int(m) for m in NUMBER_ENTRIES.findall(times_line)]
    distances = [int(m) for m in NUMBER_ENTRIES.findall(distances_line)]

    margin_of_error = 1
    for b, c in zip(times, distances):
        lh_zero, rh_zero = quadratic_solver(
            -1, b, -(c + 0.0001)
        )  # add a small delta to c in order to ensure we're >

        print(
            f"For b={b}, c={-c}, the solution range is: {(floor(rh_zero) - ceil(lh_zero) + 1)}"
        )
        margin_of_error *= floor(rh_zero) - ceil(lh_zero) + 1

    print(f"Day 06, Part 01, margin of error is: {margin_of_error}")

    # Some bad kerning for Part 02, so we just need to concat the times and distances to make 2 integers total
    time = int("".join([m for m in NUMBER_ENTRIES.findall(times_line)]))
    distance = int("".join([m for m in NUMBER_ENTRIES.findall(distances_line)]))

    margin_of_error = 1
    lh_zero, rh_zero = quadratic_solver(
        -1, time, -(distance + 0.0001)
    )  # add a small delta to c in order to ensure we're >

    print(
        f"For b={time}, c={-distance}, the solution range is: {(floor(rh_zero) - ceil(lh_zero) + 1)}"
    )
    margin_of_error *= floor(rh_zero) - ceil(lh_zero) + 1

    print(f"Day 06, Example 02, margin of error is: {margin_of_error}")
