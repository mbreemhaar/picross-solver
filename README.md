# Picross Solver

This is a simple Picross solver that uses an iterative algorithm to solve 
Picross puzzles. It is simple to use and can solve any Picross puzzle that 
you throw at it.

## Usage

Using the Picross solver is simple. Just create a new instance of the 
`Puzzle` and pass in the clues for the rows and columns. Then call the
`solve` method to solve the puzzle. To show the solution, simply print the
puzzle instance.

```python
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
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE)
file for details.
