import itertools
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

class Puzzle:
    def __init__(self, row_clues: list[list[int]], col_clues: list[list[int]]):
        self._grid = [[None] * self.col_count for _ in range(self.row_count)]
        self._row_clues = row_clues
        self._col_clues = col_clues

    @property
    def row_count(self) -> int:
        return len(self._row_clues)

    @property
    def col_count(self) -> int:
        return len(self._col_clues)

    @property
    def grid(self) -> list[list[bool | None]]:
        return self._grid
