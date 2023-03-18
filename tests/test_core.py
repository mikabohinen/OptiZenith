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
        self.assertEqual(expr.terms[x], 1)
        self.assertEqual(expr.terms[y], 2)
        self.assertEqual(expr.terms[z], 3)
        expr2 = LinearExpr()
        expr2.add_term(x, 1)
        expr2.add_term(y, 2)
        expr2.add_term(z, 3)
        expr3 = expr + expr2
        self.assertEqual(expr3.terms[x], 2)
        self.assertEqual(expr3.terms[y], 4)
        self.assertEqual(expr3.terms[z], 6)
        expr3 *= 2
        self.assertEqual(expr3.terms[x], 4)
        self.assertEqual(expr3.terms[y], 8)
        self.assertEqual(expr3.terms[z], 12)
        expr3 += 4
        self.assertEqual(expr3.terms[x], 4)
        self.assertEqual(expr3.terms[y], 8)
        self.assertEqual(expr3.terms[z], 12)
    
    def test_constrain(self):
        x = Variable("x")
        y = Variable("y")

if __name__ == "__main__":
    unittest.main()
