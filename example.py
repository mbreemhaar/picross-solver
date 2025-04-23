"""An example of how to use the picross_solver package."""

from picross_solver import Picross

row_clues = [
    [4],
    [1, 1],
    [1,1,1,1],
    [1,1,1,1],
    [1,1],
    [1,1,1,1],
    [2,2,2],
    [1,1],
    [4],
]
col_clues = [
    [5],
    [1,2],
    [1,2,1,1],
    [1,1,1],
    [1,1,1],
    [1,2,1,1],
    [1,2],
    [5],
]

puzzle = Picross(row_clues, col_clues)
puzzle.solve()

print(puzzle)
