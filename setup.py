from setuptools import setup, find_packages

setup(
    name="OptiZenith",
    version="0.1.0",
    description="A Python package for solving linear programming problems.",
    author="Mika Bohinen",
    author_email="mikabo@uio.no",
    url="https://github.com/mikabohinen/OptiZenith",
    packages=[
        "optizenith",
        "optizenith.core",
        "optizenith.utils",
        "optizenith.examples",
        "optizenith.solvers",
        ],
    install_requires=["numpy", "matplotlib"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Students",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        ],
    python_requires=">=3.7",
)
