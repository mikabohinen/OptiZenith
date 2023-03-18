from .base_solver import BaseSolver

import numpy as np
from numpy.linalg import solve
from typing import Tuple

class SimplexSolver(BaseSolver):
    """
    The SimplexSolver class implements the Simplex method for solving 
    linear programming problems.
    """

    def __init__(self, model: "Model", **kwargs):
        """
        Initializes a new SimplexSolver instance.

        Args:
            model (Model): The linear programming model to be solved.
            kwargs (dict): A dictionary of keyword arguments.
        """
        super().__init__(model)
        self._max_iterations = kwargs.get("max_iterations", 1000)
        self._tolerance = kwargs.get("tolerance", 1e-6)
        self._verbose = kwargs.get("verbose", False)
        self._max_pivots = kwargs.get("max_pivots", 1000)

    def solve(self) -> Tuple[float, dict]:
        A, b, c, non_basis, basis = self._build_matrices()
        optimal_value, optimal_solution = self._run_simplex(A, b, c, non_basis, basis)
        return optimal_value, optimal_solution

    def _build_matrices(self) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """
        Builds the initial tableau for the Simplex method.

        Returns:
            Tuple[np.ndarray]: The constraint matrix A, the right-hand side vector b,
                               the objective function coefficients c, and the sets of
                               non-basis and basis variables.
        """
        # Assumes that the model is in standard form
        m = len(self.model.constraints)
        n = len(self.model.variables)

        # Set up the matrices
        A = np.zeros((m, m + n))
        c = np.zeros(n + m)
        b = np.zeros((m, 1))

        # Fill in matrix B (basis matrix)
        for i in range(m):
            A[i, i + n] = 1

        # Fill in matrix N (non-basis matrix)
        for i, constraint in enumerate(self.model.constraints):
            for j, coefficient in enumerate(constraint.expression.coefficients):
                A[i, j] = coefficient

        for i, constraint in enumerate(self.model.constraints):
            b[i] = constraint.rhs

        for i, coefficient in enumerate(self.model.objective.expression.coefficients):
            c[i] = coefficient

        non_basis = np.array(list(range(0, n)))
        basis = np.array(list(range(n, n + m)))

        return A, b, c, non_basis, basis

    def _run_simplex(self, A: np.ndarray, b: np.ndarray,
                     c: np.ndarray, non_basis: np.ndarray,
                     basis: np.ndarray) -> Tuple[float, dict]:
        """
        Solves the linear programming problem using the Simplex method.

        Args:
            A (np.ndarray): The constraint matrix.
            b (np.ndarray): The right-hand side vector.
            c (np.ndarray): The objective function coefficients.
            non_basis (np.ndarray): The set of non-basis variables.
            basis (np.ndarray): The set of basis variables.
        Returns:
        Tuple[float, dict]: The optimal value and the optimal solution as a dictionary.
        """

        # Initializing the variables
        n = len(non_basis) + len(basis)
        m = len(basis)
        B = A[:, basis]
        N = A[:, non_basis]
        B_inv = np.linalg.inv(B)
        BN = B_inv @ N
        x_B = B_inv @ b
        z_N = (BN).T @ c[basis] - c[non_basis]
        x = np.zeros((n, 1))
        x[basis] = x_B
        x[non_basis] = 0

        for iteration in range(self._max_iterations):
            # check for optimality
            if np.all(z_N >= self._tolerance):
                break

            # Select the entering variable
            j = np.argmin(z_N)

            delta_x_B = BN[:, j]

            # Check for unboundedness
            if np.all(delta_x_B <= self._tolerance):
                raise ValueError("The problem is unbounded.")

            # Compute primal step length and select leaving variable
            step_lengths = np.array([x_B[i] / delta_x_B[i] if delta_x_B[i] > 0 else np.inf for i in range(m)])
            i = np.argmin(step_lengths)
            t = step_lengths[i]

            # Compute dual step length
            delta_z_N = -(BN).T[:, i]
            s = z_N[j] / delta_z_N[j]

            # Update primal and dual solution
            x[i] = t
            for idx, bi in enumerate(basis):
                x[bi] = x_B[idx] - t * delta_x_B[idx]
            x[non_basis[j]] = 0

            # Update the basis and non-basis sets
            entering_var = non_basis[j]
            leaving_var = basis[i]
            basis[i] = entering_var
            non_basis[j] = leaving_var

            # Update B, N, B_inv, BN, x_B, and z_N for the new basis
            B = A[:, basis]
            N = A[:, non_basis]
            B_inv = np.linalg.inv(B)
            BN = B_inv @ N
            x_B = B_inv @ b
            z_N = (BN).T @ c[basis] - c[non_basis]

        optimal_value = c.T @ x
        optimal_solution = {f"x{i}": x[i, 0] for i in range(n)}
        return float(optimal_value), optimal_solution
