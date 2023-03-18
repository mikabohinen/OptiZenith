from abc import ABC, abstractmethod
from typing import Tuple


class BaseSolver(ABC):
    def __init__(self, model: "Model"):
        self.model = model

    @abstractmethod
    def solve(self) -> Tuple[float, dict]:
        """
        Solve the linear programming problem defined by the model.

        Returns:
            Tuple[float, dict]: A tuple containing the optimal value and the optimal solution.
        """
        pass
