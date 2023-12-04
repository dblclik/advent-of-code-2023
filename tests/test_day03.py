from advent_of_code_2023.helpers.grid import NeighborsGrid, number_at_position, is_gear

def test_grid_search():
    test_grid = """467..114..
...*....9.
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


    admit_func = lambda x: x.isnumeric()
    search_chars = []
    grid = [[c for c in r] for r in test_grid.split("\n")]
    for r in grid:
        for c in r:
            if not c.isnumeric() and c != ".":
                search_chars.append(c)

    search_chars = list(set(search_chars))

    ng = NeighborsGrid(grid)
    results = ng.neighbor_search(search_chars, admit_criteria=admit_func)
    test_sum = 0
    seen_cells = {}
    for r in results:
        test_sum += number_at_position(grid, r[0],r[1], seen_cells)

    assert test_sum == 4361

    # This will return the location of all asterisks, we'll then need to determine if it's a gear or not
    results = ng.neighbor_search([str(i) for i in range(10)], admit_criteria=lambda x: x=='*')
    part2_sum = 0
    for r in results:
        gear, ratio = is_gear(ng, r[0], r[1])
        if gear:
            part2_sum += ratio

    assert part2_sum == 467835

def test_day03():
    test_grid = open("inputs/input-03.txt").read()

    admit_func = lambda x: x.isnumeric()
    search_chars = []
    grid = [[c for c in r] for r in test_grid.split("\n") if len(r) > 0]
    for r in grid:
        for c in r:
            if not c.isnumeric() and c != ".":
                search_chars.append(c)

    search_chars = list(set(search_chars))

    ng = NeighborsGrid(grid)
    results = ng.neighbor_search(search_chars, admit_criteria=admit_func)
    part1_sum = 0
    seen_cells = {}
    for r in results:
        part1_sum += number_at_position(grid, r[0],r[1], seen_cells)

    print()
    print(f"Day 03, Part 01: {part1_sum}")

    # This will return the location of all asterisks, we'll then need to determine if it's a gear or not
    results = ng.neighbor_search([str(i) for i in range(10)], admit_criteria=lambda x: x=='*')
    part2_sum = 0
    skipped = []
    for r in results:
        gear, ratio = is_gear(ng, r[0], r[1])
        if gear:
            part2_sum += ratio
        else:
            skipped.append(r)
            

    print()
    print(f"Day 03, Part 02: {part2_sum}")

