from .base_solver import BaseSolver

import numpy as np
from numpy.linalg import solve
from typing import Tuple

class InteriorPointSolver(BaseSolver):
    """
    The InteriorPointSolver class implements the Interior Point method for solving 
    linear programming problems.
    """

    def __init__(self, model: "Model", **kwargs):
        """
        Initializes a new InteriorPointSolver instance.

        Args:
            model (Model): The linear programming model to be solved.
            kwargs (dict): A dictionary of keyword arguments.
        """
        super().__init__(model)
        self._max_iterations = kwargs.get("max_iterations", 100)
        self._tolerance = kwargs.get("tolerance", 1e-6)
        self._mu = kwargs.get("mu", 10)
        self._alpha = kwargs.get("alpha", 0.01)
        self._beta = kwargs.get("beta", 0.5)

    def solve(self) -> Tuple[float, dict]:
        A, b, c, x = self._build_matrices()
        optimal_value, optimal_solution = self._run_interior_point(A, b, c, x)
        return optimal_value, optimal_solution

    def _build_matrices(self) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """
        Builds the initial matrices for the Interior Point method.

        Returns:
            Tuple[np.ndarray]: The constraint matrix A, the right-hand side vector b,
                               the objective function coefficients c, and the initial
                               solution x.
        """
        m = len(self.model.constraints)
        n = len(self.model.variables)

        A = np.zeros((m, n))
        b = np.zeros((m, 1))
        c = np.zeros((n, 1))
        x = np.ones((n, 1))

        for i, constraint in enumerate(self.model.constraints):
            for j, coefficient in enumerate(constraint.expression.coefficients):
                A[i, j] = coefficient
            b[i] = constraint.rhs

        for i, coefficient in enumerate(self.model.objective.expression.coefficients):
            c[i] = coefficient

        return A, b, c, x

    def _run_interior_point(self, A: np.ndarray, b: np.ndarray,
                             c: np.ndarray, x: np.ndarray) -> Tuple[float, dict]:
        """
        Solves the linear programming problem using the Interior Point method.

        Args:
            A (np.ndarray): The constraint matrix.
            b (np.ndarray): The right-hand side vector.
            c (np.ndarray): The objective function coefficients.
            x (np.ndarray): The initial solution.
        Returns:
            Tuple[float, dict]: The optimal value and the optimal solution as a dictionary.
        """
        m, n = A.shape
        e = np.ones((n, 1))

        for iteration in range(self._max_iterations):
            # Calculate the Newton step
            X_inv = np.diag(1 / x.flatten())
            Z = np.diag((x * self._mu / e).flatten())
            M = A @ X_inv @ Z @ A.T
            r_dual = A.T @ Z @ e - c 
            r_cent = -X_inv @ Z @ e - self._mu * e
            delta_y = np.linalg.solve(M, A @ X_inv @ r_cent - r_dual)
            delta_x = X_inv @ (Z @ delta_y - r_cent)

            # Backtracking line search
            t
