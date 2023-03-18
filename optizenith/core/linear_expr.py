from typing import Dict, Union
from .variable import Variable

class LinearExpr:
    """
    Represents a linear expression.

    Attributes:
        terms (dict[Variable, float]): The terms of the linear expression.
    """

    def __init__(self, terms: Dict[Variable, float] = None):
        if terms is None:
            self.terms = {}
        else:
            self.terms = terms

    def add_term(self, variable: Variable, coefficient: float) -> None:
        """
        Adds a term to the linear expression.

        Args:
            variable (Variable): The variable of the term.
            coefficient (float): The coefficient of the term.
        """
        if variable in self.terms:
            self.terms[variable] += coefficient
        else:
            self.terms[variable] = coefficient

    def __add__(self, other: "LinearExpr") -> "LinearExpr":
        """
        Adds two linear expressions.

        Args:
            other (LinearExpr): The other linear expression.

        Returns:
            LinearExpr: The sum of the two linear expressions.
        """
        result = LinearExpr(self.terms)

        if isinstance(other, LinearExpr):
            for variable, coefficient in other.terms.items():
                result.add_term(variable, coefficient)
        elif isinstance(other, (int, float)):
            result.add_term(Variable("constant", 0, 0), other)
        else:
            raise TypeError("Unsupported operand type(s) for +: 'LinearExpr' and '{}'".format(type(other)))

        return result

    def __sub__(self, other: "LinearExpr") -> "LinearExpr":
        """
        Subtracts two linear expressions.

        Args:
            other (LinearExpr): The other linear expression.

        Returns:
            LinearExpr: The difference of the two linear expressions.
        """
        return self + (-other)

    def __neg__(self) -> "LinearExpr":
        """
        Negates a linear expression.

        Returns:
            LinearExpr: The negated linear expression.
        """

        result = LinearExpr()
        for variable, coefficient in result.terms.items():
            result.terms[variable] = -coefficient
        return result

    def __mul__(self, scalar: Union[int,float]) -> "LinearExpr":
        """
        Performs scalar multiplication on a linear expression.
        
        Args:
            scalar (int|float): The scalar to multiply the linear expression by.
        """

        if not isinstance(scalar, (int, float)):
            raise TypeError("Scalar multiplication is only supported with int or float values")

        result = LinearExpr()
        for variable, coefficient in self.terms.items():
            result.add_term(variable, coefficient * scalar)
        return result

    def __rmul__(self, scalar: Union[int,float]) -> "LinearExpr":
        return self * scalar

    def __str__(self) -> str:
        return " + ".join([f"{coefficient:.2f} * {variable.name}" for variable, coefficient in self.terms.items()])

