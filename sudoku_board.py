from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        s = ""
        # YOUR CODE HERE
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
