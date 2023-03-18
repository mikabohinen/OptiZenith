from .linear_expr import LinearExpr

class Constraint:
    """
    Represents a constraint in an LP model.

    Attributes:
        expression (LinearExpr): The expression of the constraint.
        constrain_type (str): The type of the constraint ("<=", ">=", "=")
        rhs (float): The right-hand side value of the constraint.
    """

    def __init__(self, expression: LinearExpr, constrain_type: str, rhs: float):
        """
        Initializes a new constraint instance.

        Args:
            expression (LinearExpr): The expression of the constraint.
            constrain_type (str): The type of the constraint ("<=", ">=", "=")
            rhs (float): The right-hand side value of the constraint.
        """
        
        self.expression = expression
        self.constrain_type = constrain_type
        self.rhs = rhs

    def __str__(self) -> str:
        """
        Returns:
            str: A string representation of the constraint.
        """

        constraint_str = f"{self.expression} {self.constrain_type} {self.rhs}"
        return constraint_str
