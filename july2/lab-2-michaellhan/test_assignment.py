"""Autograder tests for Lab 2.

Do not modify this file.  You are welcome to read it to understand
what correctness conditions your functions must satisfy.
"""

import math
import random
import numpy as np
import pytest

from assignment import mean_loop, median_loop, summary_stats, quantile


# ---------- fixtures ---------- #

def random_sample(n: int = 101, seed: int = 0):
    random.seed(seed)
    return [random.uniform(-50, 50) for _ in range(n)]


# ---------- tests: mean_loop ---------- #

def test_mean_basic():
    data = [1, 2, 3, 4]
    assert mean_loop(data) == 2.5


def test_mean_empty():
    with pytest.raises(ValueError):
        mean_loop([])


def test_mean_type():
    with pytest.raises(TypeError):
        mean_loop([1, "two", 3])


# ---------- tests: median_loop ---------- #

def test_median_odd_even():
    assert median_loop([3, 2, 1]) == 2  # odd
    assert median_loop([1, 2, 3, 4]) == 2.5  # even


# ---------- tests: summary_stats ---------- #

def test_summary_keys():
    d = summary_stats([1, 2, 3])
    assert set(d.keys()) == {"mean", "median", "min", "max"}


def test_summary_values():
    d = summary_stats([1, 2, 3])
    assert d["min"] == 1 and d["max"] == 3


# ---------- tests: quantile ---------- #

def test_quantile_bounds():
    data = list(range(11))  # 0..10
    assert quantile(data, 0.0) == 0
    assert quantile(data, 1.0) == 10


def test_quantile_median_equiv():
    sample = random_sample(99, seed=42)
    assert math.isclose(quantile(sample, 0.5), median_loop(sample))


def test_quantile_numpy_alignment():
    sample = random_sample(100, seed=99)
    for q in (0.1, 0.25, 0.9):
        np_q = float(np.quantile(sample, q, method="linear"))
        assert math.isclose(quantile(sample, q), np_q, rel_tol=1e-6)
