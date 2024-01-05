#!/usr/bin/env python3
"""takes string k, int or float v and returns tuple"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple"""
    return (k, v * v)
