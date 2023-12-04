from typing import Optional, List, Callable

class NeighborsGrid:
    def __init__(self, initial_grid: list):
        self.grid = initial_grid
        self.columns = len(initial_grid[0])
        
    @property
    def rows(self):
        return len(self.grid)
    
    def adjacent_neighbors(self, row, col):
        for r in range(max(0,row-1), min(row+2, self.rows)):
            for c in range(max(0, col-1), min(col+2, self.columns)):
                yield self.grid[r][c]

    def adjacent_neighbors_indices(self, row, col):
        for r in range(max(0,row-1), min(row+2, self.rows)):
            for c in range(max(0, col-1), min(col+2, self.columns)):
                if not (r == row and c == col):
                    yield (r, c)

    def neighbor_search(self, search_chars: list, start: Optional[tuple] = None, end: Optional[tuple] = None, admit_criteria: Optional[Callable] = None) -> List[tuple]:
        if start is None:
            start = (0,0)
        if end is None:
            end = (self.rows, len(self.grid))
        if admit_criteria is None:
            admit_criteria = lambda x: True
        search_function = lambda x: x in search_chars
        results = []
        for row in range(start[0], end[0]):
            for column in range(start[1], end[1]):
                if admit_criteria(self.grid[row][column]):
                    if any(map(search_function, self.adjacent_neighbors(row, column))):
                        results.append((row, column))

        return results

def is_gear(ng: NeighborsGrid, row, col):
    numbers_found = []
    seen_cells = {}
    for loc in ng.adjacent_neighbors_indices(row, col):
        number = number_at_position(ng.grid, loc[0], loc[1], seen_cells)
        if number > 0:
            numbers_found.append(number)

    if len(numbers_found) == 2:
        return True, numbers_found[0]*numbers_found[1]
    else:
        return False, 0


def number_at_position(grid: List[List[str]], row, column, seen_cells: dict):
    if not (grid[row][column]).isnumeric():
        return 0
    
    i = -1
    while (column + i >= 0) and (grid[row][column+i].isnumeric()):
        i -= 1

    j = 1
    while (column + j < len(grid[row])) and (grid[row][column+j].isnumeric()):
        j += 1

    for c in range(column + i + 1, column + j):
        cell = f"r{row}c{c}"
        if cell not in seen_cells:
            seen_cells[cell] = 1
        else:
            return 0

    return int("".join(grid[row][column + i + 1: column + j]))
