from typing import Dict
from math import lcm

from advent_of_code_2023.helpers.desert_map import (
    follow_map_steps,
    follow_map_steps_criteria,
)


def test_day08_example():
    steps_map_input = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

    lines = steps_map_input.split("\n")
    steps = [0 if s == "L" else 1 for s in lines[0]]
    desert_map = {}
    for path in lines[2:]:
        lhs, rhs = path.split(" = ")
        rhs = rhs.replace("(", "").replace(")", "")
        path0, path1 = rhs.split(", ")
        desert_map[lhs] = [path0, path1]

    steps_needed = follow_map_steps(steps, desert_map, "AAA", "ZZZ")
    print(f"Day 08, Part 01, Example 01: {steps_needed}")

    steps_map_input = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

    lines = steps_map_input.split("\n")
    steps = [0 if s == "L" else 1 for s in lines[0]]
    desert_map: Dict[str, tuple] = {}
    for path in lines[2:]:
        if len(path) > 0:
            lhs, rhs = path.split(" = ")
            rhs = rhs.replace("(", "").replace(")", "")
            path0, path1 = rhs.split(", ")
            desert_map[lhs] = [path0, path1]

    curr_pos = [k for k in desert_map.keys() if k.endswith("A")]
    finished = lambda x: all([pos.endswith("Z") for pos in x])

    num_steps = 0
    ind = 0
    while not finished(curr_pos):
        curr_pos = [desert_map[curr_pos[i]][steps[ind]] for i in range(len(curr_pos))]
        num_steps += 1
        ind += 1
        if ind >= len(steps):
            ind = 0

    print(f"Day 08, Part 02, Example 01: {num_steps}")

    steps_map_input = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

    lines = steps_map_input.split("\n")
    steps = [0 if s == "L" else 1 for s in lines[0]]
    desert_map = {}
    for path in lines[2:]:
        lhs, rhs = path.split(" = ")
        rhs = rhs.replace("(", "").replace(")", "")
        path0, path1 = rhs.split(", ")
        desert_map[lhs] = [path0, path1]

    steps_needed = follow_map_steps(steps, desert_map, "AAA", "ZZZ")
    print(f"Day 08, Part 01, Example 02: {steps_needed}")


def test_day08():
    steps_map_input = open("inputs/input-08.txt").read()

    lines = steps_map_input.split("\n")
    steps = [0 if s == "L" else 1 for s in lines[0]]
    desert_map = {}
    for path in lines[2:]:
        if len(path) > 0:
            lhs, rhs = path.split(" = ")
            rhs = rhs.replace("(", "").replace(")", "")
            path0, path1 = rhs.split(", ")
            desert_map[lhs] = [path0, path1]

    steps_needed = follow_map_steps(steps, desert_map, "AAA", "ZZZ")
    print(f"Day 08, Part 01: {steps_needed}")

    lines = steps_map_input.split("\n")
    steps = [0 if s == "L" else 1 for s in lines[0]]
    desert_map: Dict[str, tuple] = {}
    for path in lines[2:]:
        if len(path) > 0:
            lhs, rhs = path.split(" = ")
            rhs = rhs.replace("(", "").replace(")", "")
            path0, path1 = rhs.split(", ")
            desert_map[lhs] = [path0, path1]

    curr_pos = [k for k in desert_map.keys() if k.endswith("A")]
    print(f"Length of starting positions is: {len(curr_pos)}")
    finished = lambda x: all([pos.endswith("Z") for pos in x])
    on_target = lambda x: len([pos for pos in x if pos.endswith("Z")])
    steps_needed_all = []

    for start in curr_pos:
        # do the each path then LCM
        steps_to_end = follow_map_steps_criteria(steps, desert_map, start, on_target)
        steps_needed_all.append(steps_to_end)

    print(steps_needed_all)
    print(f"LCM of all steps needed is: {lcm(*steps_needed_all)}")

    # num_steps = 0
    # max_found = 0
    # ind = 0
    # while not finished(curr_pos):
    #     curr_pos = [desert_map[curr_pos[i]][steps[ind]] for i in range(len(curr_pos))]
    #     max_found = max(max_found, on_target(curr_pos))
    #     num_steps += 1
    #     ind += 1
    #     if ind >= len(steps):
    #         ind = 0

    #     if num_steps % 5000000 == 0:
    #         print(f"Completed {num_steps} number of steps so far, Max of On Target is {max_found}...")

    # print(f"Day 08, Part 02: {num_steps}")
