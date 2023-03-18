from optizenith import *
from optizenith.solvers import *

import unittest

class TestSolvers(unittest.TestCase):

    def test_simplex(self):
        model = Model("Simplex Test")
        x = model.add_variable("x")
        y = model.add_variable("y")
        expr = LinearExpr()
        expr.add_term(x, 1)
        expr.add_term(y, 2)
        model.objective = Objective(expr, "max")
        expr = LinearExpr()
        expr.add_term(x, 1)
        expr.add_term(y, 1)
        model.add_constraint(expr, "<=", 10)
        expr = LinearExpr()
        expr.add_term(x, 1)
        expr.add_term(y, 4)
        model.add_constraint(expr, "<=", 20)
        expr = LinearExpr()
        expr.add_term(x, 3)
        expr.add_term(y, 2)
        model.add_constraint(expr, "<=", 30)
        solver = SimplexSolver(model)
        obj, sol = solver.solve()
        self.assertAlmostEqual(obj, 40/3)

if __name__ == "__main__":
    unittest.main()
