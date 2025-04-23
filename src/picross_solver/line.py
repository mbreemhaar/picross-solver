import itertools
from collections.abc import Generator


class Line:
    """A line in the Picross puzzle."""

    def __init__(self, cells: list[bool | None], clues: list[int]) -> None:
        """Initialize the line with cells and clues."""
        self._cells = cells
        self._clues = clues

    @property
    def cells(self) -> list[bool | None]:
        """Get the cells for the line."""
        return self._cells

    @property
    def clues(self) -> list[int]:
        """Get the clues for the line."""
        return self._clues

    @property
    def is_solved(self) -> bool:
        """Check if the line is solved.

        :return: True if the line is solved, False otherwise.
        """
        return all(cell is not None for cell in self._cells)

    def __str__(self) -> str:
        """Return a string representation of the line using emojis."""
        output = ''
        for cell in self._cells:
            if cell is None:
                output += '🟨'
            elif cell is True:
                output += '⬛️'
            else:
                output += '⬜️'

        return output + ' '

    def get_all_possible_lines(self) -> Generator[list[bool], None, None]:  # noqa: C901
        """Generate all possible lines that match the clues, considering the known cells."""
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
                    elif current_clue > 0:
                        permutation_clues.append(current_clue)
                        current_clue = 0
                if current_clue > 0:
                    permutation_clues.append(current_clue)

            if self.clues != permutation_clues:
                continue

            # Step 5: Yield the valid lines
            yield permutation

    def refresh_known_cells(self) -> None:
        """Refresh the known cells in the line based on the possible lines."""
        possible_lines = list(self.get_all_possible_lines())

        for i, cell in enumerate(self._cells):
            if cell is not None:
                continue

            if all(line[i] is True for line in possible_lines):
                self._cells[i] = True
            elif all(line[i] is False for line in possible_lines):
                self._cells[i] = False
