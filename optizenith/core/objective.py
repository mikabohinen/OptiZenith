from .linear_expr import LinearExpr

class Objective:
    """
    Represents an objective function of a linear programming model.

    Attributes:
        expression (LinearExpr): The expression of the objective function.
        sense (str): The optimization direction ("minimize" or "maximize").
    """

    def __init__(self, expression: LinearExpr, sense: str = "min"):
        """
        Initializes a new objective function instance.

        Args:
            expression (LinearExpr): The expression of the objective function.
            sense (str): The optimization direction ("min" or "max"). Defaults to "min".
        """
        self.expression = expression
        self.sense = sense

    def __str__(self) -> str:
        """
        Returns:
            str: A string representation of the objective function.
        """

        return f"{self.sense.capitalize()} {self.expression}"
