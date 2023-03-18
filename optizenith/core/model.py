from typing import List
from .objective import Objective
from .variable import Variable
from .constraint import Constraint
from .linear_expr import LinearExpr
# from ..solvers.interior_point import InteriorPointSolver
# from ..solvers.simplex import SimplexSolver

class Model:
    """
    Represents a linear programming (LP) model.

    Attributes:
        name (str): The name of the model.
        objective (Objective): The objective function of the model.
        constraints (list[Constraint]): The constraints of the model.
        variables (list[Variable]): The variables of the model.
    """
    
    def __init__(self, name: str = ""):
        """
        Initializes a new model instance.

        Args:
            name (str): The name of the LP model. Defaults to the empty string.
        """
        self.name = name
        self.objective = None
        self.constraints = []
        self.variables = []
    
    def add_constraint(self, expression: LinearExpr, constrain_type: str, rhs: float) -> Constraint:
        """
        Adds a constraint to the model.

        Args:
            expression (LinearExpr): The expression of the constraint.
            constrain_type (str): The type of the constraint.
            rhs (float): The right-hand side value of the constraint.

        Returns:
            Constraint: The constraint that was added to the model.
        """
        constraint = Constraint(expression, constrain_type, rhs)
        self.constraints.append(constraint)
        return constraint

    def add_variable(self, name: str, lb: float, ub: float, var_type: str="continuous") -> Variable:
        """
        Adds a variable to the model.

        Args:
            name (str): The name of the variable.
            lb (float): The lower bound of the variable.
            ub (float): The upper bound of the variable.
            var_type (str): The type of the variable. Defaults to "continuous".

        Returns:
            Variable: The variable that was added to the model.
        """

        variable = Variable(name, lb, ub, var_type)
        self.variables.append(variable)
        return variable
    
    def set_objective(self, expression: LinearExpr, sense: str="minimize") -> None:
        """
        Sets the objective function of the model.

        Args:
            expression (LinearExpr): The expression of the objective function.
            sense (str): The sense of the objective function. Defaults to "minimize".
        """

        self.objective = Objective(expression, sense)

    def solve(self, solver="simplex", **kwargs):
        """
        Solves the model.

        Args:
            solver (str): The solver to use. Defaults to "simplex".
            **kwargs: Additional keyword arguments to pass to the solver.

        Returns:
            Solution: The solution of the model.
        """

        if solver.lower() == "simplex":
            solver_instance = SimplexSolver(self, **kwargs)
        elif solver.lower() == "interior-point":
            solver_instance = InteriorPointSolver(self, **kwargs)
        else:
            raise ValueError(f"Unknown solver: {solver}")

        solution = solver_instance.solve()
        return solution

    def __str__(self) -> str:
        """
        Returns a string representation of the model.

        Returns:
            str: The string representation of the model.
        """

        model_str = f"Model: {self.name}\n"
        model_str += f"Variables:\n"
        for variable in self.variables:
            model_str += f"\t{str(variable)}\n"
        model_str += f"Objective: {str(self.objective)}\n"
        model_str += f"Constraints:\n"
        for constraint in self.constraints:
            model_str += f"\t{str(constraint)}\n"
        return model_str

