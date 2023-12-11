from typing import Callable


def follow_map_steps(steps, desert_map, start, end):
    if start not in desert_map or end not in desert_map:
        return -1

    if start == end:
        return 0

    curr_pos = start
    ind = 0
    steps_needed = 0
    while curr_pos != end:
        curr_pos = desert_map[curr_pos][steps[ind]]
        ind += 1
        steps_needed += 1
        if ind >= len(steps):
            ind = 0

    return steps_needed


def follow_map_steps_criteria(
    steps, desert_map, start, end_criteria: Callable[[str], bool]
):
    curr_pos = start
    ind = 0
    steps_needed = 0
    while not end_criteria(curr_pos):
        curr_pos = desert_map[curr_pos][steps[ind]]
        ind += 1
        steps_needed += 1
        if ind >= len(steps):
            ind = 0

    return steps_needed
