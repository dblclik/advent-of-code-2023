import networkx as nx
import pickle
from advent_of_code_2023.helpers.pipe_loop import PipeLoop


def test_day10_example():
    grid = """.....
.S-7.
.|.|.
.L-J.
....."""

    grid = [[c for c in row] for row in grid.split("\n")]
    pipe_loop = PipeLoop(grid=grid)

    assert pipe_loop.start == [1, 1]
    print(pipe_loop.connected_cells(pipe_loop.start))

    loop = pipe_loop.find_loop()

    for pos in loop:
        print(f"Step at {pos}: {grid[pos[0]][pos[1]]}")

    print(len(loop) / 2)

    grid = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""

    grid = [[c for c in row] for row in grid.split("\n")]
    pipe_loop = PipeLoop(grid=grid)

    print(pipe_loop.connected_cells(pipe_loop.start))

    loop = pipe_loop.find_loop()

    for pos in loop:
        print(f"Step at {pos}: {grid[pos[0]][pos[1]]}")

    print(len(loop) / 2)


def test_day10():
    grid = open("inputs/input-10.txt").read()

    grid = [[c for c in row] for row in grid.split("\n")]
    pipe_loop = PipeLoop(grid=grid)
    print(pipe_loop.start)

    # The following worked for some test cases but not for the full input; going to try a Networkx based solution
    print(pipe_loop.connected_cells(pipe_loop.start))

    moves_in_loop = pipe_loop.walk_loop()

    print(moves_in_loop)
