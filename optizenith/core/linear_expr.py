from typing import Dict, Union, Tuple, List

class Variable:
    """
    Represents a decision variable in an LP model.

    attributes:
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

    # TODO: Fix the circular import problem.
    # def __add__(self, other) -> LinearExpr:
    #     """
    #     Creates a linear expression with the two variables.

    #     Returns:
    #         LinearExpr: A linear expression with the two variables.
    #     """
    #     
    #     terms = {self: 1, other: 1}
    #     return LinearExpr(terms)

  # # def __mul__(self, scalar) -> LinearExpr:
    #     """
    #     Returns:
    #         LinearExpr: A linear expression with the scalar multiplied by the variable.
    #     """
    #     return LinearExpr({self: scalar})

    # def __rmul__(self, scalar) -> LinearExpr:
        # return self * scalar

    # def __sub__(self, other) -> LinearExpr:
    #     return self + (-1 * other)

    # def __neg__(self) -> LinearExpr:
    #     return -1 * self
    # 
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

    def __add__(self, other: "LinearExpr") -> "LinearExpr":
        """
        Adds two linear expressions.

        Args:
            other (LinearExpr): The other linear expression.

        Returns:
            LinearExpr: The sum of the two linear expressions.
        """
        result = LinearExpr(self.variables, self.coefficients)

        if isinstance(other, LinearExpr):
            for variable, coefficient in zip(self.variables, self.coefficients):
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
        for variable, coefficient in zip(self.variables, self.coefficients):
            result[variable] = -coefficient
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
        for variable, coefficient in zip(self.variables, self.coefficients):
            result.add_term(variable, coefficient * scalar)
        return result

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


