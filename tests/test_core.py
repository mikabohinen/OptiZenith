import unittest
from optizenith import *

class TestCore(unittest.TestCase):

    def test_variable(self):
        x = Variable("x", 0, 10, "continuous")
        self.assertEqual(x.name, "x")
        self.assertEqual(x.lb, 0)
        self.assertEqual(x.ub, 10)
        self.assertEqual(x.var_type, "continuous")

    def test_linear_expr(self):
        x = Variable("x", 0, 10, "continuous")
        y = Variable("y", 0, 10, "continuous")
        z = Variable("z", 0, 10, "continuous")
        expr = LinearExpr()
        expr.add_term(x, 1)
        expr.add_term(y, 2)
        expr.add_term(z, 3)
        self.assertEqual(expr[x], 1)
        self.assertEqual(expr[y], 2)
        self.assertEqual(expr[z], 3)
        expr2 = LinearExpr()
        expr2.add_term(x, 1)
        expr2.add_term(y, 2)
        expr2.add_term(z, 3)
        expr3 = expr + expr2
        self.assertEqual(expr3[x], 2)
        self.assertEqual(expr3[y], 4)
        self.assertEqual(expr3[z], 6)
        expr3 *= 2
        self.assertEqual(expr3[x], 4)
        self.assertEqual(expr3[y], 8)
        self.assertEqual(expr3[z], 12)
        expr3 += 4
        self.assertEqual(expr3[x], 4)
        self.assertEqual(expr3[y], 8)
        self.assertEqual(expr3[z], 12)
    
    def test_constrain(self):
        x = Variable("x")
        y = Variable("y")
        expr = LinearExpr()
        expr.add_term(x, 1)
        expr.add_term(y, 2)
        constr = Constraint(expr, "<=", 10)
        self.assertEqual(constr.expression, expr)
        self.assertEqual(constr.constrain_type, "<=")
        self.assertEqual(constr.rhs, 10)

    def test_objective(self):
        x = Variable("x")
        y = Variable("y")
        expr = LinearExpr()
        expr.add_term(x, 1)
        expr.add_term(y, 2)
        obj = Objective(expr, "min")
        self.assertEqual(obj.expression, expr)
        self.assertEqual(obj.sense, "min")

    def test_model(self):
        model = Model("test")
        x = model.add_variable("x")
        y = model.add_variable("y", -1, 3, "integer")
        self.assertEqual(model.name, "test")
        self.assertIn(x, model.variables)
        self.assertIn(y, model.variables)

        expr1 = LinearExpr()
        expr1.add_term(x, 1)
        expr1.add_term(y, 2)
        constr1 = model.add_constraint(expr1, "<=", 10)
        self.assertIn(constr1, model.constraints)

        expr2 = LinearExpr()
        expr2.add_term(x, 1)
        expr2.add_term(y, 2)
        model.set_objective(expr2, "max")
        self.assertEqual(model.objective.expression, expr2)
        self.assertEqual(model.objective.sense, "max")

if __name__ == "__main__":
    unittest.main()
