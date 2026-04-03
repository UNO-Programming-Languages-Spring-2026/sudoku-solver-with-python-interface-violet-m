from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        s = ""
        for r in range(1, 10):
            row = []
            for c in range(1, 10):
                row.append(str(self.sudoku[(r,c)]))
                if (c % 3 == 0) and (c != 9):
                    row.append("  ")
                elif c != 9:
                    row.append(" ")
            s = s + "".join(row)
            s = s + "\n"
            if (r % 3 == 0) and (r != 9):
                s = s + "\n"
        return s

    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        return cls(sudoku)

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        sudoku = {}
        for atom in model.symbols(shown=True):
            if (len(atom.arguments) == 3):
                r = int(atom.arguments[0].number)
                c = int(atom.arguments[1].number)
                v = int(atom.arguments[2].number)
                sudoku[(r, c)] = v
        return cls(sudoku)
