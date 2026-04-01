import sys
import clingo
from clingo.application import Application

class ClingoApp(clingo.application.Application):
    def main(self, ctrl, files):
        ctrl.load("sudoku.lp")
        for file in files:
            ctrl.load(file)
        ctrl.ground([("base", [])])
        ctrl.solve()
if __name__ == "__main__":
    clingo.clingo_main(ClingoApp(), sys.argv[1:])
