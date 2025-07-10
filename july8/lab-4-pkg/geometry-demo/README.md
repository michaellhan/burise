# geometry-demo

**geometry-demo** is a minimal Python package I built as part of *Lab 4 — Software Packaging & Testing Fundamentals* during the BU RISE Practicum (June 2025). The goal of this lab was to learn how to scaffold a Python package with a clean public API, write and run tests using `pytest`, and install the package locally in editable mode. This project gave me hands-on experience with tools like `setuptools`, Python's `abc` module, and version control with GitHub.

## Features

- Abstract `Shape` base class using Python’s `abc` module  
- Concrete shape classes: `Square` and `Circle`, each with an `area()` method  
- `area_stats` utility function to summarize areas across multiple shapes  
- Clean public API exposed via `__init__.py`  
- Fully tested with `pytest` and designed to be installed in editable mode  

## Installation

Clone the repository and install the package locally:

```bash
git clone https://github.com/<your-username>/geometry-demo.git
cd geometry-demo
pip install -e .
```

Make sure your Python environment includes the necessary dependencies listed in `environment.txt`. If you're using `mamba` or `conda`:

```bash
mamba create -n lab_4 --file environment.txt -y
mamba activate lab_4
```

## Usage

After installation, you can import the package in any script or interactive session:

```python
from geometry import Square, Circle, area_stats

s = Square(3)
c = Circle(1.5)

print(s.area())        # Output: 9.0
print(c.area())        # Output: ~7.0686

print(area_stats(s, c))
# Output:
# {
#     'n': 2,
#     'total': 16.068583470577034,
#     'mean': 8.034291735288517,
#     'min': 7.068583470577034,
#     'max': 9.0
# }
```

## Testing

Run the test suite using `pytest`:

```bash
pytest
```

Tests are written in `tests/test_geometry.py` and cover:

- Normal and edge cases for `Square` and `Circle`  
- Correct structure and values from `area_stats`  
- Error handling when no shapes are provided  

## Project Context

This package was developed as part of a 4-hour lab assignment for BU RISE, where we learned to:

1. Scaffold a minimal Python package with a clean public API  
2. Write a small test suite using `pytest` and run it locally  
3. Install the package in editable mode and confirm importability from another script  

If time allowed, stretch goals included adding new shapes like `Rectangle`, increasing test coverage with `pytest-cov`, setting up GitHub Actions for CI, or publishing to Test PyPI.

## License

This project is for educational use. Feel free to modify and reuse with credit.