import sys
import clingo
from clingo.application import Application
from sudoku_board import Sudoku


class Context:
    def __init__(self, board: Sudoku):
        self.board = board

    def initial(self) -> list[clingo.symbol.Symbol]:
        symbols = []
        for (row, col), val in self.board.sudoku.items():
                symbols.append(clingo.Function("",[clingo.Number(row), clingo.Number(col), clingo.Number(val)]))
        return symbols

class ClingoApp(clingo.application.Application):
    def main(self, ctrl, files):
        if not files:
             return 1
        file_name = files[0]
        bridge = True
        if bridge:
             with open(files[0], 'r') as f:
                content = f.read()
                board = Sudoku.from_str(content)
                context = Context(board)
        else: 
            board = None
            context = None
        ctrl.load("sudoku.lp")
        if bridge:
            ctrl.load("sudoku_py.lp")
        if context:
            ctrl.ground([("base", [])], context=context)
        else:
            ctrl.ground([("base", [])])
        ctrl.solve()
    def print_model(self, model, printer):
        sudoku = Sudoku.from_model(model)
        print(sudoku)
if __name__ == "__main__":
    clingo.clingo_main(ClingoApp(), sys.argv[1:])
