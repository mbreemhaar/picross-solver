from functools import lru_cache
import itertools
from typing import Generator



class Line:
    def __init__(self, cells: list[bool | None], clues: list[int]):
        self._cells = cells
        self._clues = clues

    @property
    def cells(self) -> list[bool | None]:
        return self._cells

    @property
    def clues(self) -> list[int]:
        return self._clues

    @property
    def is_solved(self) -> bool:
        return all(cell is not None for cell in self._cells)

    def __str__(self) -> str:
        output = ''
        for cell in self._cells:
            if cell is None:
                output += '🟨'
            elif cell is True:
                output += '⬛️'
            else:
                output += '⬜️'

        return output + ' '

    @lru_cache
    def get_all_possible_lines(self) -> Generator[list[bool], None, None]:
        """
        Generate all possible lines that match the clues, considering the known cells.
        """
        # 1. Sum the clues to get the total number of filled cells
        # 2. Create all possible permutations of filled and empty cells
        # 3. Filter the permutations to match the known cells
        # 4. Filter the permutations to match the clues
        # 5. Yield the valid lines

        # Step 1: Sum the clues to get the total number of filled cells
        filled_cells_count = sum(self._clues)

        # Step 2: Create all possible permutations of filled and empty cells
        filled_cell_position_combinations = itertools.combinations(range(len(self._cells)), filled_cells_count)

        known_filled_cell_positions = [i for i, cell in enumerate(self._cells) if cell is not None and cell is True]
        known_empty_cell_positions = [i for i, cell in enumerate(self._cells) if cell is not None and cell is False]

        for positions in filled_cell_position_combinations:
            # Step 3: Filter the permutations to match the known cells
            if any(pos in known_empty_cell_positions for pos in positions):
                continue

            if not all(pos in positions for pos in known_filled_cell_positions):
                continue

            permutation = [False] * len(self._cells)
            for pos in positions:
                permutation[pos] = True

            # Step 4: Filter the permutations to match the clues
            permutation_clues = []

            if not any(permutation):
                permutation_clues = [0]
            else:
                current_clue = 0
                for cell in permutation:
                    if cell:
                        current_clue += 1
                    else:
                        if current_clue > 0:
                            permutation_clues.append(current_clue)
                            current_clue = 0
                if current_clue > 0:
                    permutation_clues.append(current_clue)

            if self.clues != permutation_clues:
                continue

            yield permutation

    def refresh_known_cells(self) -> None:
        possible_lines = list(self.get_all_possible_lines())

        for i, cell in enumerate(self._cells):
            if cell is not None:
                continue

            if all(line[i] is True for line in possible_lines):
                self._cells[i] = True
            elif all(line[i] is False for line in possible_lines):
                self._cells[i] = False

class Puzzle:
    def __init__(self, row_clues: list[list[int]], col_clues: list[list[int]]):
        self._row_clues = row_clues
        self._col_clues = col_clues
        self._grid = [[None] * self.col_count for _ in range(self.row_count)]

    @property
    def row_count(self) -> int:
        return len(self._row_clues)

    @property
    def col_count(self) -> int:
        return len(self._col_clues)

    @property
    def grid(self) -> list[list[bool | None]]:
        return self._grid

    @property
    def is_solved(self) -> bool:
        return all(all(cell is not None for cell in row) for row in self._grid)

    def update_row(self, row_index: int, cells: list[bool | None]) -> None:
        if row_index < 0 or row_index >= self.row_count:
            raise IndexError("Row index out of range")
        if len(cells) != self.col_count:
            raise ValueError("Cells length does not match column count")
        self._grid[row_index] = cells

    def update_col(self, col_index: int, cells: list[bool | None]) -> None:
        if col_index < 0 or col_index >= self.col_count:
            raise IndexError("Column index out of range")
        if len(cells) != self.row_count:
            raise ValueError("Cells length does not match row count")
        for i in range(self.row_count):
            self._grid[i][col_index] = cells[i]

    def solve(self):
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
        output = ''
        for row in self._grid:
            output += str(Line(row, [])) + '\n'
        return output
