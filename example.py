"""An example of how to use the picross_solver package."""

from picross_solver.puzzle import Puzzle

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

puzzle = Puzzle(row_clues, col_clues)
puzzle.solve()

print(puzzle)
