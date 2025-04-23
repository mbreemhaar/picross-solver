from picross_solver.puzzle import Puzzle

row_clues = [[3,1,1], [1,1,1], [3,2,1], [2,2,1], [6], [1,1], [4], [2], [2,3,1], [1,3,2]]
col_clues = [[2,1],[1,2,2], [1,1], [1,2,1],[4,1,1],[1,3,1,2],[1,1,1,1],[1,1,1],[1,1,1,1], [2,1,1,3]]

puzzle = Puzzle(row_clues, col_clues)
puzzle.solve()

print(puzzle)