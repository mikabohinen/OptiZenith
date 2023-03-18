from math import inf

class Variable:
    """
    Represents a decision variable in an LP model.

    attributes:
        name (str): The name of the variable.
        lb (float): The lower bound of the variable.
        ub (float): The upper bound of the variable.
        var_type (str): The type of the variable.
    """

    def __init__(self, name: str, lb: float=0, ub: float=inf, var_type: str="continuous"):
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
