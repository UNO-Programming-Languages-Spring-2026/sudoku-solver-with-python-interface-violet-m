import sys
import clingo
from clingo.application import Application
from sudoku_board import Sudoku

class ClingoApp(clingo.application.Application):
    def main(self, ctrl, files):
        ctrl.load("sudoku.lp")
        for file in files:
            ctrl.load(file)
        ctrl.ground([("base", [])])
        ctrl.solve()
    def print_model(self, model, printer):
        models = model.symbols(shown=True)
        sudoku = Sudoku.from_model(model)
        print(sudoku)
if __name__ == "__main__":
    clingo.clingo_main(ClingoApp(), sys.argv[1:])
