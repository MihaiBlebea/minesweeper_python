from typing import List, Any
import random

DIRECTIONS = (
    (-1, 1),
    (-1, 0),
    (-1, -1),
    (0, 1),
    (0, -1),
    (1, 1),
    (1, 0),
    (1, -1),
)


class SweeperBoard(List):

    count_mines: int = 0

    total_mines: int = 2

    def __init__(self, x: int, y: int):
        assert x > 3, "X must be greater than 3"
        assert y > 3, "Y must be greater than 3"

        cells_count = x * y
        self.total_mines = int(cells_count * 0.3)
        super().__init__(
            [self._create_initial_cell() for _ in range(0, x)] for _ in range(0, y)
        )

    def _should_be_mine(self) -> bool:
        if self.count_mines >= self.total_mines:
            return False

        if random.randint(0, 100) > 50:
            self.count_mines += 1
            return True

        return False

    def _create_initial_cell(self) -> str:
        if self._should_be_mine():
            return "#"

        return "-"

    def _count_total_mines_around(self, x: int, y: int) -> int:
        return len(
            [1 for x_dir, y_dir in DIRECTIONS if self.is_mine(x + x_dir, y + y_dir)]
        )

    def is_mine(self, x: int, y: int) -> bool:
        if x < 0 or y < 0:
            return False

        try:
            return self[y][x] == "#"
        except IndexError:
            return False

    def set_cell_content(self, x: int, y: int, content: Any) -> None:
        assert isinstance(x, int), "X must be an integer"
        assert isinstance(y, int), "Y must be an integer"

        self[y][x] = content

    def process(self) -> None:
        for y, column in enumerate(self):
            for x, cell in enumerate(column):
                if cell == "#":
                    continue

                self.set_cell_content(x, y, self._count_total_mines_around(x, y))


if __name__ == "__main__":
    from pprint import pprint

    m = SweeperBoard(4, 4)

    print("Generating a simple mine sweeper table:")
    pprint(m)

    print("Processig the table...\n")
    m.process()

    print("Result:")
    pprint(m, width=50)