from typing import List, Any
import random
from prettytable import PrettyTable
from src.directions import DIRECTIONS


class SweeperBoard(List):
    count_mines: int = 0

    def __init__(self, x: int, y: int):
        assert x > 3, "X must be greater than 3"
        assert y > 3, "Y must be greater than 3"

        cells_count = x * y
        self.total_mines = int(cells_count * 0.3)
        super().__init__(
            [self._create_initial_cell() for _ in range(0, x)] for _ in range(0, y)
        )

    def __repr__(self):
        return self._draw_board()

    def __str__(self):
        return self._draw_board()

    def _draw_board(self) -> str:
        table = PrettyTable([" "] + [i for i in range(0, len(self))])
        for i, row in enumerate(self):
            table.add_row([i] + row, divider=True)

        return table.get_string()

    def _should_be_mine(self) -> bool:
        if random.randint(0, 100) > 70 and self.count_mines < self.total_mines:
            self.count_mines += 1
            return True

        return False

    def _create_initial_cell(self) -> str:
        return "#" if self._should_be_mine() else "-"

    def _count_total_mines_around(self, x: int, y: int) -> int:
        return len(
            [True for x_dir, y_dir in DIRECTIONS if self.is_mine(x + x_dir, y + y_dir)]
        )

    def is_mine(self, x: int, y: int) -> bool:
        return (
            False
            if x < 0 or y < 0 or y >= len(self) or x >= len(self[y])
            else self[y][x] == "#"
        )

    def set_cell_content(self, x: int, y: int, content: Any) -> None:
        assert isinstance(x, int), "X must be an integer"
        assert isinstance(y, int), "Y must be an integer"

        self[y][x] = content

    def process(self) -> None:
        for y, column in enumerate(self):
            [
                self.set_cell_content(x, y, self._count_total_mines_around(x, y))
                for x, cell in enumerate(column)
                if cell != "#"
            ]
