## assignment.py
"""Lab July 2 — core functions to implement.

Edit *only* the bodies that contain `raise NotImplementedError()`.
Do **not** rename functions: the autograder expects these names.
"""

from __future__ import annotations
from typing import Iterable, Dict, List
import math

def _validate_numeric(nums: Iterable[float]) -> List[float]:
    """Return a concrete list after validating elements are numeric."""
    nums = list(nums)
    if not nums:
        raise ValueError("Input sequence is empty.")
    for x in nums:
        if not isinstance(x, (int, float)):
            raise TypeError(f"Non‑numeric element detected: {x!r}")
    return nums


def mean_loop(nums: Iterable[float]) -> float:
    """Compute arithmetic mean using an explicit *for* loop.

    Args:
        nums: Sequence of int/float values.
    Returns:
        The mean of the inputs.
    """
    nums = _validate_numeric(nums)
    sum = 0
    for num in nums:
        sum += num

    return sum/len(nums)

def median_loop(nums: Iterable[float]) -> float:
    """Return the median value without using `statistics` or `numpy`."""
    nums = _validate_numeric(nums)
    nums.sort()
    size = len(nums)

    # 0 1 2, size = 3
    # 0 1 2 3, size = 4

    if size % 2 == 0:
        return (nums[size//2-1]+nums[size//2])/2
    return nums[size//2]


def summary_stats(nums: Iterable[float]) -> Dict[str, float]:
    """Return mean, median, min, and max as a dictionary."""

    nums = _validate_numeric(nums)

    d = {}
    d["mean"] = mean_loop(nums)
    d["median"] = median_loop(nums)
    d["min"] = min(nums)
    d["max"] = max(nums)

    return d


def quantile(nums: Iterable[float], q: float) -> float:
    """Compute the *q*‑quantile (0 ≤ q ≤ 1) via linear interpolation."""

    nums = _validate_numeric(nums)
    nums.sort()
    if q == 0: return nums[0]
    if q == 1: return nums[len(nums)-1]


    index = (len(nums)-1)*q
    
    low = nums[math.floor(index)]
    high = nums[math.ceil(index)]
    
    weight = index-math.floor(index)

    return low + (high-low)*weight

# 10 20 0.3

# 10 + 