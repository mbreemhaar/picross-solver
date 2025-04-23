from picross_solver.line import Line


class Picross:
    """A Picross puzzle."""

    def __init__(self, row_clues: list[list[int]], col_clues: list[list[int]]) -> None:
        """Initialize the puzzle with row and column clues."""
        self._row_clues = row_clues
        self._col_clues = col_clues
        self._grid = [[None] * self.col_count for _ in range(self.row_count)]

    @property
    def row_count(self) -> int:
        """Get the number of rows in the puzzle.

        :return: The number of rows in the puzzle.
        """
        return len(self._row_clues)

    @property
    def col_count(self) -> int:
        """Get the number of columns in the puzzle.

        :return: The number of columns in the puzzle.
        """
        return len(self._col_clues)

    @property
    def grid(self) -> list[list[bool | None]]:
        """Get the current state of the grid.

        :return: The current state of the grid.
        """
        return self._grid

    @property
    def is_solved(self) -> bool:
        """Check if the puzzle is solved.

        :return: True if the puzzle is solved, False otherwise.
        """
        return all(all(cell is not None for cell in row) for row in self._grid)

    def update_row(self, row_index: int, cells: list[bool | None]) -> None:
        """Update a row in the grid with the given cells."""
        if row_index < 0 or row_index >= self.row_count:
            e = 'Row index out of range'
            raise IndexError(e)
        if len(cells) != self.col_count:
            e = 'Cells length does not match column count'
            raise ValueError(e)
        self._grid[row_index] = cells

    def update_col(self, col_index: int, cells: list[bool | None]) -> None:
        """Update a column in the grid with the given cells."""
        if col_index < 0 or col_index >= self.col_count:
            e = 'Column index out of range'
            raise IndexError(e)
        if len(cells) != self.row_count:
            e = 'Cells length does not match row count'
            raise ValueError(e)
        for i in range(self.row_count):
            self._grid[i][col_index] = cells[i]

    def solve(self) -> None:
        """Solve the puzzle by iterating through the rows and columns."""
        while not self.is_solved:
            for i in range(self.row_count):
                line = Line(self._grid[i], self._row_clues[i])
                line.refresh_known_cells()
                self.update_row(i, line.cells)

            for i in range(self.col_count):
                line = Line([self._grid[j][i] for j in range(self.row_count)], self._col_clues[i])
                line.refresh_known_cells()
                self.update_col(i, line.cells)

    def __str__(self) -> str:
        """Return a string representation of the puzzle using emojis.

        :return: String representation of the puzzle.
        """
        output = ''
        for row in self._grid:
            output += str(Line(row, [])) + '\n'
        return output
