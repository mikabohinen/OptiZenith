from typing import Dict, Union, Tuple, List

class Variable:
    """
    Represents a decision variable in an LP model.

    Attributes:
        name (str): The name of the variable.
        lb (float): The lower bound of the variable.
        ub (float): The upper bound of the variable.
        var_type (str): The type of the variable.
    """

    def __init__(self, name: str, lb: float=0, ub: float=float("inf"), var_type: str="continuous"):
        """
        Initializes a new Variable instance.

        Args:
            name (str): The name of the variable.
            lb (float): The lower bound of the variable.
            ub (float): The upper bound of the variable.
            var_type (str): The type of the variable. Defaults to "continuous".
        """

        self._name = name
        self._lb = lb
        self._ub = ub
        self._var_type = var_type

    @property
    def lb(self) -> float:
        return self._lb

    @lb.setter
    def lb(self, lb: float) -> None:
        self._lb = lb

    @property
    def ub(self) -> float:
        return self._ub

    @ub.setter
    def ub(self, ub: float) -> None:
        self._ub = ub

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def var_type(self) -> str:
        return self._var_type

    @var_type.setter
    def var_type(self, var_type: str) -> None:
        self._var_type = var_type

    def __str__(self) -> str:
        return f"{self.name} ({self.var_type}): [{self.lb}, {self.ub}]"

    def __repr__(self) -> str:
        return f"Variable({self.name}, {self.lb}, {self.ub}, {self.var_type})"


class LinearExpr:
    """
    Represents a linear expression.

    Attributes:
        terms (dict[Variable, float]): The terms of the linear expression.
    """

    @classmethod
    def from_variable(cls, variable: Variable) -> "LinearExpr":
        """
        Creates a linear expression from a variable.

        Args:
            variable (Variable): The variable to create the linear expression from.
        """

        return cls([variable], [1])

    @classmethod
    def from_constant(cls, constant: float) -> "LinearExpr":
        """
        Creates a linear expression from a constant.

        Args:
            constant (float): The constant to create the linear expression from.
        """

        return cls([Variable("constant", 0, 0)], [constant])

    def __init__(self, variables: List[Variable]=None, coefficients: List[float]=None):
        if variables is None:
            self.variables = []
            self.coefficients = []
        else:
            self.variables = variables
            self.coefficients = coefficients

    def add_term(self, variable: Variable, coefficient: float) -> None:
        """
        Adds a term to the linear expression.

        Args:
            variable (Variable): The variable of the term.
            coefficient (float): The coefficient of the term.
        """
        if variable in self.variables:
            self.coefficients[self.variables.index(variable)] += coefficient
        else:
            self.variables.append(variable)
            self.coefficients.append(coefficient)

    def __add__(self, other: Union["LinearExpr", Variable, int, float]) -> "LinearExpr":
        if isinstance(other, LinearExpr):
            result = LinearExpr(self.variables, self.coefficients)
            for variable, coefficient in zip(other.variables, other.coefficients):
                result.add_term(variable, coefficient)
            return result
        elif isinstance(other, Variable):
            return self + LinearExpr.from_variable(other)
        elif isinstance(other, (int, float)):
            return self + LinearExpr.from_constant(other)
        else:
            raise TypeError("Unsupported operand type(s) for +: 'LinearExpr' and '{}'".format(type(other)))

    def __sub__(self, other: Union["LinearExpr", Variable, int, float]) -> "LinearExpr":
        return self + (-other)

    def __mul__(self, scalar: Union[int,float]) -> "LinearExpr":
        if isinstance(scalar, (int, float)):
            result = LinearExpr()
            for variable, coefficient in zip(self.variables, self.coefficients):
                result.add_term(variable, coefficient * scalar)
            return result
        else:
            raise TypeError("Scalar multiplication is only supported with int or float values")

    def __rmul__(self, scalar: Union[int,float]) -> "LinearExpr":
        return self * scalar

    def __getitem__(self, variable: Variable) -> float:
        return self.coefficients[self.variables.index(variable)]

    def __setitem__(self, variable: Variable, coefficient: float) -> None:
        if variable in self.variables:
            self.coefficients[self.variables.index(variable)] = coefficient
        else:
            self.add_term(variable, coefficient)

    def __str__(self) -> str:
        return " + ".join([f"{coefficient:.2f} * {variable.name}" for variable, coefficient in zip(self.variables, self.coefficients)])


