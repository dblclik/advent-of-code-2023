from advent_of_code_2023.helpers.cube_game import CubeGame


def test_day02():
    cg = CubeGame("inputs/input-02.txt", 12, 14, 13)
    part1_sum = 0
    for valid_game_id in cg.valid_game_generator():
        part1_sum += valid_game_id

    print()
    print(f"Day 02, Part 01: {part1_sum}")
    print(f"Day 02, Part 02: {cg.game_power_sum()}")
    print()
