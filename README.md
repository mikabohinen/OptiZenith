Welcome to OptiZenith, a user-friendly linear programming library for
Python. OptiZenith allows you to create and solve linear programming
(LP) models using a simple and intuitive interface.

Installation
============

To install OptiZenith, simply run the following command:
```bash
    pip install optizenith
```

Features
========

OptiZenith provides the following features:

-   Easy-to-understand syntax for creating LP models

-   Support for continuous and integer variables

-   Pre-built solvers: Simplex and Interior Point methods

-   Extensible architecture for adding custom solvers

Example
=======

Here's a simple example to demonstrate how to use OptiZenith to create
and solve an LP model:
```python
    import optizenith

    # Create a new model
    model = optizenith.Model("My LP Model")

    # Add variables
    x1 = model.add_variable("x1", lb=0)
    x2 = model.add_variable("x2", lb=0)

    # Create a linear expression for the objective function
    objective_expr = optizenith.LinearExpr([x1, x2], [3, 2])

    # Set the objective function to minimize the objective expression
    model.set_objective(objective_expr, sense="max")

    # Add constraints
    model.add_constraint(2*x1 + x2, "<=", 4)

    model.add_constraint(3*x1 + 4x2, "<=", 5)

    # Solve the model using the Simplex solver
    result = model.solve(solver="simplex")

    print("Objective Value:", result.obj)
    print("Solution:", result.sol)
```

Documentation
=============

For detailed information on how to use OptiZenith, please refer to the
[OptiZenith Documentation](./docs/optizenith.html).

File Structure
==============

The library's file structure is organized as follows:

-   `docs`: Contains the documentation for the library

-   `optizenith`: Contains the main library code, organized into
    subdirectories:

    -   `core`: Contains the core classes for creating and managing LP
        models (Model, Variable, Constraint, Objective, and LinearExpr)

    -   `solvers`: Contains built-in solvers (Simplex and Interior
        Point) and base\_solver for adding custom solvers

    -   `utils`: Utility functions and classes

-   `tests`: Contains test scripts for the core library and solvers

-   `run_tests.py`: Script to run all tests

-   `setup.py`: Setup script for package installation

Contributing
============

We welcome contributions to improve OptiZenith! If you'd like to
contribute, please feel free to submit a pull request, report a bug, or
suggest new features.

License
=======

OptiZenith is released under the [MIT License](./LICENSE).
