from queue import LifoQueue
from pydantic import BaseModel
import networkx as nx


class Connection(BaseModel):
    offset: list
    allowed_connections: list


UP = [-1, 0]
DOWN = [1, 0]
RIGHT = [0, 1]
LEFT = [0, -1]


class PipeLoop:
    def __init__(self, grid):
        self.grid = grid
        self.visited = [[0 for _ in range(len(row))] for row in self.grid]
        self.start = self.get_starting_point()
        self.connected_directions = {
            "|": [UP, DOWN],
            "-": [LEFT, RIGHT],
            "L": [UP, RIGHT],
            "J": [UP, LEFT],
            "7": [DOWN, LEFT],
            "F": [DOWN, RIGHT],
            ".": [],
        }
        self.connections = {
            "N": Connection(offset=[-1, 0], allowed_connections=["|", "7", "F"]),
            "W": Connection(offset=[0, -1], allowed_connections=["-", "F", "L"]),
            "E": Connection(offset=[0, 1], allowed_connections=["-", "7", "J"]),
            "S": Connection(offset=[1, 0], allowed_connections=["|", "L", "J"]),
        }
        self.search_queue = LifoQueue()
        self.loop = []

    def get_starting_point(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == "S":
                    return [row, col]

    def in_bounds(self, cell: tuple) -> bool:
        return cell[0] in range(len(self.grid)) and cell[1] in range(
            len(self.grid[cell[0]])
        )

    def has_been_visited(self, cell: tuple):
        return self.visited[cell[0]][cell[1]] == 1

    def connected_cells(self, cell: tuple):
        connected = []
        for k, check in self.connections.items():
            next_cell = [result for result in map(sum, zip(cell, check.offset))]
            if self.in_bounds(next_cell) and not self.has_been_visited(next_cell):
                if self.grid[next_cell[0]][next_cell[1]] in check.allowed_connections:
                    connected.append(next_cell)
        return connected

    def mark(self, cell: tuple):
        self.visited[cell[0]][cell[1]] = 1

    def walk_loop(self):
        starting_neighbors = self.connected_cells(self.start)
        self.mark(self.start)
        curr_cell = starting_neighbors[0]
        moves = 1
        while curr_cell != self.start:
            self.mark(curr_cell)
            possible_moves = [
                cell
                for cell in [
                    [result for result in map(sum, zip(curr_cell, shift))]
                    for shift in self.connected_directions[
                        self.grid[curr_cell[0]][curr_cell[1]]
                    ]
                ]
                if (not self.has_been_visited(cell))
            ]
            if len(possible_moves) == 0:
                return moves + 1
            if len(possible_moves) > 1:
                print(f"Error, more than 1 valid move from cell {curr_cell}!")
                print(f"Possible moves: {possible_moves}")
                return 0
            curr_cell = possible_moves[0]
            moves += 1

        return moves

    def find_loop(self):
        if len(self.loop) > 0:
            print(
                f"Warning, there is a loop of length {len(self.loop)} already in place..."
            )
            return list(self.loop)

        self.search_queue.put(self.start)
        # we know this one won't fail, but hereafter need to wrap in try/except
        next_cell = self.search_queue.get(block=False)

        while next_cell is not None:
            # mark as visited
            if self.visited[next_cell[0]][next_cell[1]] == 0:
                self.mark(next_cell)
                self.loop.append(next_cell)
                next_options = self.connected_cells(next_cell)
                # if len(next_options) == 0:
                #     print(f"Ran out of options at cell: {next_cell}")
                if len(next_options) >= 2:
                    print(
                        f"2 or more options found at: {next_cell} (options: {next_options})"
                    )

                # print(f"Visited {next_cell} (value is {self.grid")
                # try reversing the initial order
                next_options.reverse()
                for cell in next_options:
                    self.search_queue.put(cell)

            try:
                next_cell = self.search_queue.get(block=False)
            except:
                next_cell = None

        return list(self.loop)
